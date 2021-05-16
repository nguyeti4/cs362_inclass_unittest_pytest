import unittest

#referenced https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

def isPalindrome():
    # Run loop from 0 to len/2
    s = input("Enter a string: ")
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
    
class Test_Palindrome(unittest.TestCase):
    def test_pal(self):
        #Enter "abccba"
        actual = isPalindrome()
        expected = True
        self.assertEqual(actual,expected)
    def test_pal2(self):
        #Enter "kakorot"
        actual = isPalindrome()
        expected = False
        self.assertEqual(actual,expected)
    def test_pal3(self):
        #Enter "ninokuni"
        actual = isPalindrome()
        expected = False
        self.assertEqual(actual,expected)