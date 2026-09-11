import string
from enum import StrEnum
from typing import TypedDict

PUNCTUATION = string.punctuation
SENTENCE_ENDINGS = ".!?"


class Sentiment(StrEnum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


class SentimentSummary(TypedDict):
    sentiment: Sentiment
    positive_percentage: float
    negative_percentage: float
    most_positive_sentence: str
    most_negative_sentence: str


class SentimentAnalyzer:
    def __init__(
        self,
        positive_words: list[str],
        negative_words: list[str],
        negations: list[str],
        intensifiers: list[str],
    ):
        """
        Initializes the SentimentAnalyzer with lists of positive words,
        negative words, negations, and intensifiers. 

        Parameters:
            `positive_words`: A list of words considered positive.
            `negative_words`: A list of words considered negative.
            `negations`: A list of negations that can invert sentiment.
            `intensifiers`: A list of intensifiers that can amplify sentiment.
        """
        self.positive_words = {w.lower() for w in positive_words}
        self.negative_words = {w.lower() for w in negative_words}
        self.negations = {w.lower() for w in negations}
        self.intensifiers = {w.lower() for w in intensifiers}

    def _tokenize(self, sentence: str) -> list[str]:
        words: list[str] = []
        for raw in sentence.split():
            start = 0
            end = len(raw)
            while start < end and raw[start] in PUNCTUATION:
                start += 1
            while end > start and raw[end - 1] in PUNCTUATION:
                end -= 1
            if start < end:
                words.append(raw[start:end])
        return words

    def _base_sentiment(self, word: str) -> int:
        is_pos = word in self.positive_words
        is_neg = word in self.negative_words
        if is_pos and not is_neg:
            return 1
        if is_neg and not is_pos:
            return -1
        return 0

    def analyze_sentiment(self, sentence: str) -> int:
        """
        Scores one sentence using the initialized word lists.
            - Words are non-empty strings separated by whitespace and characters
              in `PUNCTUATION`. Comparisons are case-insensitive.
            - Positive and negative words contribute sentiments of +1 and -1,
              respectively. Words that are either both positive and negative or
              neither positive nor negative contribute 0 sentiment.
            - Negations and intensifiers are modifiers that change the
              sentiment of the next non-modifier in the sentence. Negations
              flip the sentiment, while intensifiers double it. Consecutive
              modifiers all apply to the same next non-modifier.

        Parameters:
            `sentence`: The sentence to analyze.

        Returns:
            A sentiment score.
        """
        score = 0
        multiplier = 1

        for raw_word in self._tokenize(sentence):
            word = raw_word.lower()

            if word in self.negations:
                multiplier *= -1
            elif word in self.intensifiers:
                multiplier *= 2
            else:
                score += self._base_sentiment(word) * multiplier
                multiplier = 1

        return score

    def get_sentiment_summary(self, text: str) -> SentimentSummary:
        """
        Returns a `SentimentSummary` for the sentences in `text`.
            - Sentences are non-empty strings separated by characters in
              `SENTENCE_ENDINGS`, with leading and trailing whitespace stripped.
            - Overall sentiment is the sign of the total score, while
              percentages are the fractions of all sentences that are
              individually positive and negative respectively.
            - If multiple sentences are tied for most positive or negative,
              any of them may be returned.
            - For text with no sentences, return NEUTRAL, 0.0 percentages,
              and empty strings for both sentence fields.

        Parameters:
            `text`: The text to summarize.

        Returns:
            A dictionary matching `SentimentSummary`.
        """
        sentences: list[str] = []
        current: list[str] = []
        for ch in text:
            if ch in SENTENCE_ENDINGS:
                sentence = "".join(current).strip()
                if sentence:
                    sentences.append(sentence)
                current = []
            else:
                current.append(ch)
        trailing = "".join(current).strip()
        if trailing:
            sentences.append(trailing)

        if not sentences:
            return {
                "sentiment": Sentiment.NEUTRAL,
                "positive_percentage": 0.0,
                "negative_percentage": 0.0,
                "most_positive_sentence": "",
                "most_negative_sentence": "",
            }

        scores = [self.analyze_sentiment(s) for s in sentences]
        total = sum(scores)
        n = len(sentences)

        if total > 0:
            overall = Sentiment.POSITIVE
        elif total < 0:
            overall = Sentiment.NEGATIVE
        else:
            overall = Sentiment.NEUTRAL

        positive_count = sum(1 for s in scores if s > 0)
        negative_count = sum(1 for s in scores if s < 0)

        most_positive_idx = max(range(n), key=lambda i: scores[i])
        most_negative_idx = min(range(n), key=lambda i: scores[i])

        return {
            "sentiment": overall,
            "positive_percentage": positive_count / n,
            "negative_percentage": negative_count / n,
            "most_positive_sentence": sentences[most_positive_idx],
            "most_negative_sentence": sentences[most_negative_idx],
        }
