from typing import TypedDict
from enum import StrEnum


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
        Initializes the SentimentAnalyzer with lists of positive words, negative words, negations, and intensifiers.

        Parameters:
            positive_words (list[str]): A list of words considered positive.
            negative_words (list[str]): A list of words considered negative.
            negations (list[str]): A list of negation words that can invert sentiment.
            intensifiers (list[str]): A list of intensifier words that can amplify sentiment.
        """

        raise NotImplementedError

    def analyze_sentiment(self, sentence: str) -> int:
        """
        Provide a sentiment score for the given sentence based on the initialized word lists. A word is a modifier if its either a negation or an intensifier.
            - Words in the positive_words list contribute +1 to the score.
            - Words in the negative_words list contribute -1 to the score.
            - Words not in either list contribute 0 to the score.
            - Negation words invert the sentiment of the next non-modifier word.
            - Intensifier words amplify the sentiment of the next non-modifier word by doubling its contribution.
            - Multiple consecutive modifiers apply in sequence to the next non-modifier word.
            - Words are case-insensitive.
            - Punctuation should be ignored and deliminates words

        Parameters:
            sentence (str): The sentence to analyze.

        Returns:
            int: A sentiment score where positive values indicate positive sentiment,
                 negative values indicate negative sentiment, and zero indicates neutral sentiment.
        """
        punctuation = r"!#$%&'()*+,./:;<=>?@[]^_`{|}\~)"

        raise NotImplementedError

    def get_sentiment_summary(self, text: str) -> SentimentSummary:

        raise NotImplementedError
