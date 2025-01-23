def isSubsequence(s,t):  
    k = 0
    if s == "":
        return True
    for i in t:
        if i == s[k]:            
            k+=1
        if k == len(s) and k>0:
            return True  
    return False      
s0="acb"
t0="ahbgdc"
s1="abc"
t1="ahbgdc"


print(isSubsequence(s0,t0))
print(isSubsequence(s1,t1))