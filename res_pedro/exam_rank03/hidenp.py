def hidenp(small: str, big: str) -> bool:
    s: str = ""
    j: int = 0
    for x in range(0, len(big)):
        if j < len(small) and big[x] == small[j]:
            s += big[x]
            j += 1
    return s == small


print(hidenp("abc", "a1b2c3"))
print(hidenp("ace", "abcde"))
print(hidenp("aec", "abcde"))
print(hidenp("", "abc"))
print(hidenp("abc", "ab"))
print(hidenp("aaaa", "aaa"))
print(hidenp("sing", "subsequence testing"))
