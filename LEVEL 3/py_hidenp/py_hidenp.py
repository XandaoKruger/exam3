def hidenp(small: str, big: str) -> bool:

    # verify: bool = False

    # for x in range(0, len(big)):
    #     if y < len(small) and small[y] == big[x]:
    #         verify = True
    # return verify




print(hidenp("abc", "a1b2c3"))
print(hidenp("ace", "abcde"))
print(hidenp("aec", "abcde"))
print(hidenp("", "abc"))
print(hidenp("abc", "ab"))
print(hidenp("aaaa", "aaa"))
print(hidenp("sing","subsequence testing"))