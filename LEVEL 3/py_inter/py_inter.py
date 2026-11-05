def inter(s1: str, s2: str) -> str:

    recieve: str = ""

    for c in s1:
        if c in s2 and c not in recieve:
            recieve += c

    return recieve



# NORMAL CASES
print(inter("hello", "world")) # lo
print(inter("banana", "band")) # ban
print(inter("abcabc", "bc")) # bc
print(inter("abc", "xyz")) # ""

# EDGE CASES
print(inter("", "abc")) # ""
print(inter("abc", "")) # ""
print(inter("", "")) # ""
print(inter("aaa", "a")) # a
print(inter("a", "aaa")) #  a
print(inter("acb", "cba")) # abc
print(inter("abc", "abc")) # abc
print(inter("aabbcc", "abc")) # acb
print(inter("A", "a")) # ""
print(inter("a b", " ")) # ""
print(inter("a1!b", "!1")) # !1
