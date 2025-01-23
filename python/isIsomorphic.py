def isIsomorphic(s,t):
    if len(s)!= len(t):
        return False
    indexS={}
    indexS[ord(s[0])]=1
    indexT={}
    indexT[ord(t[0])] =1
    for i in range(len(s)):
        if indexS.get(ord(s[i])) != indexT.get(ord(t[i])):
            return False
        indexS[ord(s[i])] = i + 1
        indexT[ord(t[i])] = i + 1
    return True

s0="egg"

t0="add"

s1="foo"

t1="bar"

print(isIsomorphic(s0,t0))
print(isIsomorphic(s1,t1))