import pytest
import string

#Reference URL: https://www.geeksforgeeks.org/python-program-to-count-words-in-a-sentence/

def word_count():
    test_string = input("Enter a string: ")
    res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])
    return res 
    
def test_word_cnt():
    #Enter "This is an activity"
    assert word_count() == 4
def test_word_cnt2():
    #Enter "123Hello World"
    assert word_count() == 1
def test_word_cnt3():
    #Enter "Oregon State Uni34"
    assert word_count() == 2