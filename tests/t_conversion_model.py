import pytest

from models.conversion_model import ConversionModel


# <editor-fold desc="[+] Test | to_upper_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("hello world!", "HELLO WORLD!"),
    ("test", "TEST"),
    ("12345", "12345"),
    ("aBcDe", "ABCDE"),
    ("Lorem ipsum dolor sit amet", "LOREM IPSUM DOLOR SIT AMET"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")
])
def test_to_upper_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_upper_case(input_string)
    assert actual_string == expected_string
# </editor-fold>


# <editor-fold desc="[+] Test | to_lower_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("Hello World!", "hello world!"),
    ("TesT", "test"),
    ("12345", "12345"),
    ("aBcDe", "abcde"),
    ("LOREM IPSUM DOLOR SIT AMET", "lorem ipsum dolor sit amet"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")
])
def test_to_lower_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_lower_case(input_string)
    assert actual_string == expected_string
# </editor-fold>


# <editor-fold desc="[+] Test | to_inverse_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("Hello World!", "hELLO wORLD!"),
    ("test", "TEST"),
    ("12345", "12345"),
    ("aBcDe", "AbCdE"),
    ("Lorem ipsum dolor sit amet", "lOREM IPSUM DOLOR SIT AMET"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")
])
def test_to_inverse_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_inverse_case(input_string)
    assert actual_string == expected_string
# </editor-fold>


# <editor-fold desc="[+] Test | to_capitalized_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("hello world!", "Hello World!"),
    ("test", "Test"),
    ("12345", "12345"),
    ("aBcDe", "Abcde"),
    ("Lorem ipsum dolor sit amet", "Lorem Ipsum Dolor Sit Amet"),
    ("Lorem ipsum dolor. sit amet", "Lorem Ipsum Dolor. Sit Amet"),
    ("Lorem ipsum dolor. sit amet?", "Lorem Ipsum Dolor. Sit Amet?"),
    ("Lorem 'ipsum', dolor. sit amet?", "Lorem 'Ipsum', Dolor. Sit Amet?"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")
])
def test_to_capitalized_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_capitalized_case(input_string)
    assert actual_string == expected_string
# </editor-fold>


# <editor-fold desc="[+] Test | to_sentence_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("Hello World!", "Hello world!"),
    ("TesT", "Test"),
    ("12345", "12345"),
    ("aBcDe", "Abcde"),
    ("LOREM IPSUM DOLOR SIT AMET", "Lorem ipsum dolor sit amet"),
    ("Lorem ipsum dolor. sit amet", "Lorem ipsum dolor. Sit amet"),
    ("Lorem ipsum dolor. sit amet?", "Lorem ipsum dolor. Sit amet?"),
    ("Lorem 'ipsum', dolor. sit amet?", "Lorem 'ipsum', dolor. Sit amet?"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")
])
def test_to_sentence_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_sentence_case(input_string)
    assert actual_string == expected_string
# </editor-fold>


# <editor-fold desc="[+] Test | to_title_case">
@pytest.mark.parametrize("input_string, expected_string", [
    ("hello world!", "Hello World!"),
    ("this is test", "This is Test"),
    ("12345", "12345"),
    ("aBcDe", "Abcde"),
    ("Lorem ipsum dolor sit amet", "Lorem Ipsum dolor Sit Amet"),
    ("Lorem ipsum 'dolor' sit amet?", "Lorem Ipsum 'dolor' Sit Amet?"),
    ("Lorem 'ipsum', dolor sit! amet?", "Lorem 'Ipsum', dolor Sit! Amet?"),
    ("", ""),
    ("\t\t  \n\n", "\t\t  \n\n")

])
def test_to_title_case(input_string: str, expected_string: str):
    model: ConversionModel = ConversionModel()
    actual_string: str = model.to_title_case(input_string, {"dolor", "is"})
    assert actual_string == expected_string
# </editor-fold>
