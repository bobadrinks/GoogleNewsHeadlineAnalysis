"""A collection of functions for my project."""

import requests
from bs4 import BeautifulSoup
import string
from collections import Counter
import re
import os
import sys


def get_headlines(url):
    """Retrieves headlines from Google News website.

    Parses all headlines currently on Google News site and
    creates a list of headlines (where each headline is a string).

    Parameters:
    url (str): The URL of the Google News website.

    Returns:
    list: a list of strings (headlines)
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Google News headlines have class Dy5T1d
    headlines = soup.find_all(class_='DY5T1d')
    # Parse headline text from:
    # <a class="DY5T1d" href=...>headline text here</a>
    for i, headline in enumerate(headlines):
        headlines[i] = headline.text
    return headlines


def print_headlines(headlines):
    """Prints headlines.

    Given a list of headlines, prints each one on a line.

    Parameters:
    headlines (list): List of strings.

    Returns:
    None.
    """
    for i, headline in enumerate(headlines):
        print("({}.) {}".format(i, headline))


def text_to_word_bag(text):
    """Convert a string to a list of individual words.

    Given some text, strips punctuation and filler words,
    and creates a list of words.

    Parameters:
    text (str): A string of headlines separated by spaces.

    Returns:
    list: A list of words.
    """
    # strip punctuation and standalone numbers
    for bad_char in '''!"#$%&\()*+—–-,./:;<=>?@[\\]^_`{|}~''':
        # needs to be escaped
        if bad_char in ['[', ']', '.', '(', ')', '\\', '^']:
            text = re.sub(r'^\{}'.format(bad_char), ' ', text)
            text = re.sub(r'\{}$'.format(bad_char), ' ', text)
            text = re.sub(r' \{}'.format(bad_char), ' ', text)
            text = re.sub(r'\{} '.format(bad_char), ' ', text)
        else:
            text = re.sub(r'^[{}]'.format(bad_char), ' ', text)
            text = re.sub(r'[{}]$'.format(bad_char), ' ', text)
            text = re.sub(r' [{}]'.format(bad_char), ' ', text)
            text = re.sub(r'[{}] '.format(bad_char), ' ', text)
    text = re.sub(r' [0-9] ', '', text)
    text = re.sub(r'  ', ' ', text)

    words_to_remove = []
    # add words to remove (prepositions, etc.) to blacklist
    path_to_file = os.path.join(os.getcwd(), 'words_to_remove.txt')
    f = open(path_to_file, "r")
    for line in f.readlines():
        words_to_remove.append(line.strip())
    text = [w for w in text.split(' ') if w.lower() not in words_to_remove]
    return text


def count_occurrences(word, search_text):
    """Counts occurrences of words given a string.

    Given some text, searches for occurrences of a specific
    word in that text.

    Parameters:
    word (str): A single word (or string) to search for.
    search_text (str): A string of headlines separated by spaces.

    Returns:
    int: The number of occurrences of word in search_text.
    """
    all_words = text_to_word_bag(search_text)
    return all_words.count(word)


def most_common_words(num, search_text):
    """Finds most common num words in search_text.

    Given some text, finds the [num] most common words and
    returns a list of tuples [(word, count), (word, count) ...]

    Parameters:
    num (int): The number of (most common) words to find.
    search_text (str): A string of headlines separated by spaces.

    Returns:
    list: List of tuples [(word, count), (word, count) ...]
    """
    all_words = text_to_word_bag(search_text)
    ctr = Counter(all_words)
    return ctr.most_common(num)
