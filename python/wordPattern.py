def wordPattern(pattern, s):
    dictt = {}
    words = s.split()
    if len(set(pattern)) != len(set(words)): return False 
    if len(words) != len(pattern): return False 
    for i in range(len(pattern)):
        if pattern[i] not in dictt.keys() and words[i] not in dictt.values():
            dictt[pattern[i]]= words[i]
        else:
            if dictt[pattern[i]] !=words[i]:
                return False
    return True

print(wordPattern("abba","dog cat cat dog")) #true
print(wordPattern("abba","dog cat cat fish")) #false
print(wordPattern("abba","dog cat cat")) #false
print(wordPattern("abba","dog dog cat")) #false