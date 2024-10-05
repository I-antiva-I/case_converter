from typing import Set, List


class InformationModel:
    """
    The `InformationModel` class to manages
    the `small words` (words that should be excluded during title case conversion)

    Properties:

    * small_words : Set[str] - A set of small words such as "and", "or", "the".
    """

    def __init__(self):
        self._small_words: Set[str] = {
            "and", "or", "but", "a", "an", "the", "as", "at",
            "by", "for", "in", "of", "on", "to", "with", "is"
        }

    @property
    def small_words(self) -> Set[str]:
        return self._small_words

    @small_words.setter
    def small_words(self, value: Set[str]) -> None:
        self._small_words = value

    @property
    def sorted_small_words(self) -> List[str]:
        """
        Returns the small words as a sorted list.
        """
        return sorted(list(self.small_words))

    def add_single_small_word(self, word: str) -> None:
        """
        Adds a single word to the set of small words.
        :param word: A word.
        """
        return self.small_words.add(word)

    def add_multiple_small_words(self, words: List[str]) -> None:
        """
        Adds multiple words to the set of small words.
        :param words: A list of words.
        """
        return self.small_words.update(words)