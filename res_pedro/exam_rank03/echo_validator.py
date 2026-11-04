def echo_validator(text: str) -> bool:
    text = text.replace(" ", "").lower()
    return text == text[::-1]


print(echo_validator("racecar"))
print(echo_validator("abbza"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam Im Adam"))
print(echo_validator(""))
