def isPalindrome(string):
    if(string == string[::-1]):
        return "Yes, it is a palindrome"
    else:
        return "No, it is not a palindrom"

word = input()
print(isPalindrome(word))