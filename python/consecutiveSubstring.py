def containsString(s,t):
    boo = False
    for i in range(len(t)):
        if t[i] == s[0]:
            for x in range(len(s)):
                curr = 0
                if t[i+x] == s[x]:
                    curr+=1
            if curr == len(s):
                boo = True
    return boo