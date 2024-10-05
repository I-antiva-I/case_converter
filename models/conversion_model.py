import string as str_plus

from typing import Set, List


class ConversionModel:
    def __init__(self):
        self._text: str = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value

    # <editor-fold desc="[+] Text Cases">

    @staticmethod
    def to_upper_case(string: str) -> str:
        return string.upper()

    @staticmethod
    def to_lower_case(string: str) -> str:
        return string.lower()

    @staticmethod
    def to_inverse_case(string: str) -> str:
        return "".join([char.lower() if char.isupper() else char.upper() for char in string])

    @staticmethod
    def to_sentence_case(string: str) -> str:
        if len(string) == 0:
            return string

        sentence_breaks = [i for i, char in enumerate(string) if char in ['!', '?', '.']]

        full_string = ""
        original_size = len(string)
        appended_chars_count = 0

        while any(sentence_breaks):
            break_index = sentence_breaks.pop(0)
            string_segment = string[appended_chars_count: break_index + 1]
            segment_size = len(string_segment)

            has_starting_symbol: int = 1 if string_segment[0] in ['\'', '"', "`", " "] else 0

            full_string += (string_segment[0:has_starting_symbol] +
                            string_segment[has_starting_symbol].upper() +
                            string_segment[has_starting_symbol + 1:].lower())

            appended_chars_count += segment_size

        if appended_chars_count < original_size:
            has_starting_symbol: int = 1 if string[appended_chars_count] in ['\'', '"', "`", " "] else 0
            full_string += (string[appended_chars_count:appended_chars_count + has_starting_symbol] +
                            string[appended_chars_count + has_starting_symbol].upper() +
                            string[appended_chars_count + has_starting_symbol + 1:].lower())

        return full_string

    @staticmethod
    def to_capitalized_case(string: str) -> str:
        return string.title()

    @staticmethod
    def to_title_case(string: str, small_words: Set[str] = None) -> str:
        words = string.lower().split()

        if len(words) == 0:
            return string

        titled_words = [words[0].capitalize()]
        titled_words += [word if word.strip(str_plus.punctuation) in small_words
                         else ConversionModel.to_sentence_case(word) for word in words[1:]]

        return ' '.join(titled_words)

    # </editor-fold>
