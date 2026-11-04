def pattern_tracker(text: str) -> int:
    pairs: int = 0
    for i in range(0, len(text)):
        if text[i].isdigit() and text[i - 1].isdigit():
            if int(text[i]) - int(text[i - 1]) == 1:
                pairs += 1
    return pairs


print(pattern_tracker("123"))
print(pattern_tracker("12a34"))
print(pattern_tracker("987654321"))
print(pattern_tracker("01234567"))
print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
