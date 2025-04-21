# You are given a 0-indexed string s, a string a, a string b, and an integer k.

# An index i is beautiful if:

# 0 <= i <= s.length - a.length
# s[i..(i + a.length - 1)] == a
# There exists an index j such that:
# 0 <= j <= s.length - b.length
# s[j..(j + b.length - 1)] == b
# |j - i| <= k
# Return the array that contains beautiful indices in sorted order from smallest to largest.


def beautifulIndices(s,a,b,k):
    a_ind,b_ind = [],[]
    end= []
    n = len(s)
    na = n-len(a)+1
    nb = n-len(b)+1
    for i in range(na):
        if(s[i:i+len(a)] == a):
            a_ind.append(i)
    for x in range(nb):
        if(s[x:x+len(b)] == b):
            b_ind.append(x)
    for i in a_ind:
        for j in b_ind:
            if abs(i-j)<=k:
                end.append(i)
                break
    return(end)

print( beautifulIndices("isawsquirrelnearmysquirrelhouseohmy","my","squirrel",15))

def beautifulIndices2(s,a,b,k):
    def prefix(a):
        m = len(a)
        table = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and a[i] != a[j]:
                j = table[j - 1]

            if a[i] == a[j]:
                j += 1

            table[i] = j

        return table

    def kmp_search(text, a):
        n, m = len(text), len(a)
        if m == 0:
            return list(range(n))

        table = prefix(a)
        result = []
        j = 0

        for i in range(n):
            while j > 0 and text[i] != a[j]:
                j = table[j - 1]

            if text[i] == a[j]:
                j += 1

            if j == m:
                result.append(i - m + 1)
                j = table[j - 1]

        return result

    first, second = kmp_search(s, a), kmp_search(s, b)
    i = j = 0
    result = []

    while i < len(first) and j < len(second):
        if abs(first[i] - second[j]) <= k:
            result.append(first[i])
            i += 1
        elif second[j] - first[i] > k:
            i += 1
        else:
            j += 1

    return result

print( beautifulIndices2("isawsquirrelnearmysquirrelhouseohmy","my","squirrel",15))