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

s0 = "A man, a plan, a canal: Panama"
s1= "race a car"
s2= "0p"

print(isPalindrome(s0)==True)
print(isPalindrome(s1)==False)
print(isPalindrome(s2)==False)