import string as str_plus

from typing import Set


class ConversionModel:
    """

    The `ConversionModel` manages text conversion, providing various static methods for text transformation.

    Properties:

    * text : str - A property to get or set the current text stored in the model.
    """

    def __init__(self):
        self._text: str = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value

    # <editor-fold desc="[+] Text cases">

    @staticmethod
    def to_upper_case(string: str) -> str:
        """
        Converts input string to upper case.
        :param string: Input string.
        :return: Converted string in upper case.
        """

        return string.upper()

    @staticmethod
    def to_lower_case(string: str) -> str:
        """
        Converts input string to lower case.
        :param string: Input string.
        :return: Converted string in lower case.
        """

        return string.lower()

    @staticmethod
    def to_inverse_case(string: str) -> str:
        """
        Inverts case of input string, converting uppercase characters to lowercase and vice versa.
        :param string: Input string.
        :return: Converted string in inverse case.
        """

        return "".join([char.lower() if char.isupper() else char.upper() for char in string])

    @staticmethod
    def to_sentence_case(string: str) -> str:
        """
        Converts input string to sentence case, capitalizing the first letter after
        sentence breaks ('.', '?', '!', ...).
        :param string: Input string.
        :return: Converted string in sentence case.
        """

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
        """
        Converts input string to capitalized case, where the first letter of each word is capitalized.

        :param string: Input string.
        :return: Converted string in capitalized case.
        """

        return string.title()

    @staticmethod
    def to_title_case(string: str, small_words: Set[str] = None) -> str:
        """
        Converts input string to title case, capitalizing the first word and any word,
        excluding `small words` (if provided).

        :param string: Input string.
        :param small_words: Set of `small words`.
        :return: Converted string in title case.
        """

        words = string.lower().split()

        if len(words) == 0:
            return string

        titled_words = [words[0].capitalize()]
        titled_words += [word if word.strip(str_plus.punctuation) in small_words
                         else ConversionModel.to_sentence_case(word) for word in words[1:]]

        return ' '.join(titled_words)

    # </editor-fold>
