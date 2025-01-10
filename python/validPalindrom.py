import re
def isPalindrome(s):
    new = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
    r = True
    j = len(new)-1
    for i in range(len(new)//2):
        if new[i] != new[j]:
            r = False
        j-=1
    return r

stra= "A man, a plan, a canal: Panama"
strb="race a car"
strc= " "
print("is a palindrome?   ", stra, isPalindrome(stra))
print("is b palindrome?   ", strb, isPalindrome(strb))
print("is c palindrome?   ", strc, isPalindrome(strc))