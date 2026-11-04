def inter(s1: str, s2: str) -> str:
    res: str = ""
    for i in s1:
        if i in s2 and i not in res:
            res += i
    return res


print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
