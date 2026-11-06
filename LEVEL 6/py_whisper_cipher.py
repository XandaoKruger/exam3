def whisper_cipher(text: str, shift: int) -> str:

    result: list = []

    for c in text:
        if "a" <= c <= "z":
            base = ord("a")
        elif "A" <= c <= "Z":
            base = ord("A")
        else:
            result.append(c)
            continue
        result.append(chr((ord(c) - base + shift) % 26 + base))
    return "".join(result)


print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 5))
print(whisper_cipher("", 10))
print(whisper_cipher("abc", -3))