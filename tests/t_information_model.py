from typing import Set, List

import pytest

from models.information_model import InformationModel


@pytest.mark.parametrize("input_word, input_set, expected_set", [
    ("hello", {"yes", "no", "maybe"}, {"yes", "no", "maybe", "hello"}),
    ("world", {"yes", "no", "maybe"}, {"yes", "no", "maybe", "world"}),
    ("yes", {"yes", "no", "maybe"}, {"yes", "no", "maybe"}),
    ("no", {"yes", "no", "maybe"}, {"yes", "no", "maybe"}),
])
def test_add_single_small_word(input_word: str, input_set: Set[str], expected_set: Set[str]):
    model: InformationModel = InformationModel()
    model.small_words = input_set
    model.add_single_small_word(input_word)
    actual_set: Set[str] = model.small_words
    assert actual_set == expected_set


@pytest.mark.parametrize("input_word_list, input_set, expected_set", [
    (["hello"], {"yes", "no", "maybe"}, {"yes", "no", "maybe", "hello"}),
    (["hello", "world"], {"yes", "no", "maybe"}, {"yes", "no", "maybe", "hello", "world"}),
    (["yes", "no", "maybe"], {"yes", "no", "maybe"}, {"yes", "no", "maybe"}),
    (["no", "none"], {"yes", "no", "maybe"}, {"yes", "no", "maybe", "none"}),
])
def test_add_multiple_small_words(input_word_list: List[str], input_set: Set[str], expected_set: Set[str]):
    model: InformationModel = InformationModel()
    model.small_words = input_set
    model.add_multiple_small_words(input_word_list)
    actual_set: Set[str] = model.small_words
    assert actual_set == expected_set
