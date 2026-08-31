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
        raise NotImplementedError

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
        raise NotImplementedError

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
        raise NotImplementedError
