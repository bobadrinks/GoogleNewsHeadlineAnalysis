"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import get_headlines, print_headlines, \
                                text_to_word_bag, count_occurrences, \
                                most_common_words

##
##


def test_get_headlines():
    assert callable(get_headlines)
    assert isinstance(get_headlines('https://www.news.google.com'), list)


def test_print_headlines():
    assert callable(print_headlines)
    headlines = ["Headline 1", "Headline 2", "Headline 3"]
    assert print_headlines(headlines) is None


def test_text_to_word_bag():
    assert callable(text_to_word_bag)
    text = "blah blah hello yes no"
    assert isinstance(text_to_word_bag(text), list)


def test_count_occurrences():
    assert callable(print_headlines)
    text = "blah blah hello yes no"
    assert (count_occurrences("blah", text)) == 2
    assert isinstance(count_occurrences("blah", text), int)


def test_most_common_words():
    assert callable(most_common_words)
    text = "blah blah hello yes no"
    assert isinstance(most_common_words(1, text), list)
    assert most_common_words(1, text) == [('blah', 2)]
