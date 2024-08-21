from typing import Set


class ConversionModel:
    def __init__(self):
        self._text : str = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value : str) -> None:
        self._text = value

    # <editor-fold desc="[+] Text Cases">

    @staticmethod
    def to_upper_case(string: str) -> str:
        return string.upper()

    @staticmethod
    def text_lower_case(string: str) -> str:
        return string.lower()

    @staticmethod
    def text_inverse_case(string: str) -> str:
        return "".join([char.lower() if char.isupper() else char.upper() for char in string])

    @staticmethod
    def text_sentence_case(string: str) -> str:
        return string[0].upper()+(string[1:].lower())

    @staticmethod
    def text_capitalized_case(string: str) -> str:
        return string.title()

    @staticmethod
    def text_title_case(string: str, small_words: Set[str] = None) -> str:
        words = string.lower().split()

        titled_words = [words[0].capitalize()]
        titled_words += [word if word in small_words else word.capitalize() for word in words[1:]]

        return ' '.join(titled_words)

    # </editor-fold>




