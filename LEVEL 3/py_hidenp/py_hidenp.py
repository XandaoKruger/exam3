from rich import print
# pip install rich -> True's and False's now have collors

def hidenp(small: str, big: str) -> bool:

    y: int = 0

    for c in big:
        if y < len(small) and small[y] == c:
            y += 1
        

    return y == len(small)



# NORMAL CASES
print(hidenp("abc", "a1b2c3")) # True
print(hidenp("ace", "abcde")) # True
print(hidenp("aec", "abcde")) # False
print(hidenp("", "abc")) # True
print(hidenp("abc", "ab")) # False
print(hidenp("aaaa", "aaa")) # False
print(hidenp("sing","subsequence testing")) # True

# EDGE CASES
print(hidenp("","")) # True
print(hidenp("a","")) # False
print(hidenp("A","a")) # False
