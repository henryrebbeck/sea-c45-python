#!/usr/bin/env python
"""
code that tests the trigram program defined in trigrams.py

can be run with py.test
"""
from trigrams import next_word, open_file, read_file, rand_word_from_list


def test_open_file():
    bookfilename = "sherlock_med.txt"
    c = open_file(bookfilename)

    assert c.mode == 'r'


def test_read_file():
    bookfilename = "sherlock_oneline.txt"
    file_name = open_file(bookfilename)
    c = read_file(file_name)

    assert c == ('To Sherlock Holmes she is always THE woman. '
                 'To Sherlock Holmes Chloe is always THE kite. '
                 'To Sherlock Holmes Henry is always THE man. '
                 'To Sherlock Holmes Finlay is always THE son.')


def test_next_word():
    # This test checks that the function will take a dictionary
    # and extract either output from the same keyword pair
    # (I am not sure how to test the random nature of this
    # function other than checking it gives either option)
    # perhaps the test would need to call it a number of times and
    # check it gives statistically correct results
    # (ie 50:50 for two words)
    c = next_word('one two',
                  {'one two': ['henry', 'Chloe'],
                   'three four': ['what']}, False)
    assert c == 'henry' or 'Chloe'


def test_rand_word_from_list():
    c = rand_word_from_list(['one', 'two'], False)

    assert c == 'one' or 'two'
