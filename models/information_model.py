from typing import Set, List


class InformationModel:
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
        return sorted(list(self.small_words))

    def add_single_small_word(self, word: str) -> None:
        return self.small_words.add(word)

    def add_multiple_small_words(self, words: List[str]) -> None:
        return self.small_words.update(words)