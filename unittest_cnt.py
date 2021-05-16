import unittest
import string

#Reference URL: https://www.geeksforgeeks.org/python-program-to-count-words-in-a-sentence/

def word_count():
    test_string = input("Enter a string: ")
    res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])
    return res 
    
class Test_Word_Cnt(unittest.TestCase):
    def test_word_cnt(self):
        #Enter "This is an activity"
        actual = word_count()
        expected = 4
        self.assertEqual(actual,expected)
    def test_word_cnt2(self):
        #Enter "123Hello World"
        actual = word_count()
        expected = 1
        self.assertEqual(actual,expected)
    def test_word_cnt3(self):
        #Enter "Oregon State Uni34"
        actual = word_count()
        expected = 2
        self.assertEqual(actual,expected)
        
    
    