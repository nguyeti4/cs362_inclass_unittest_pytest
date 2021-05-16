import pytest

#referenced https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

def isPalindrome():
    # Run loop from 0 to len/2
    s = input("Enter a string: ")
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
    
def test_pal():
    #Enter "abccba"
    assert isPalindrome() == True
def test_pal2():
    #Enter "kakorot"
    assert isPalindrome() == False
def test_pal3():
    #Enter "ninokuni"
    assert isPalindrome() == False