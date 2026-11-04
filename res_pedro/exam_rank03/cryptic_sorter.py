def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels: set = set("aeiouAEIOU")

    def key(s: str) -> tuple:
        return (len(s), s.lower(), sum(v in vowels for v in s))
    res: list[str] = strings[:]
    for i in range(0, len(res)):
        current = res[i]
        c_key = key(current)
        j = i - 1
        while j >= 0 and key(res[j]) > c_key:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = current
    return res


print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))
