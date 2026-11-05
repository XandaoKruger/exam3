# py_echo_validator

> [!NOTE]
> Write a function that checks if a string is a palindrome,
> ignoring spaces and case, only consider alphabetic characters
> for the comparison.

### Function signature

	def echo_validator(text: str) -> bool:

### Examples

| Input | Output |
| :---: | :---: |
| `echo_validator("racecar")` | `True` |
| `echo_validator("A man a plan a canal Panama")` | `True` |
| `echo_validator("race a car")` | `False` |
| `echo_validator("Was it a car or a cat I saw")` | `True` |
| `echo_validator("hello")` | `False` |
| `echo_validator("Madam Im Adam")` | `True` |
| `echo_validator("madam")` | `True` |
| `echo_validator("Able was I ere I saw Elba")` | `True` |
| `echo_validator("")` | `False` |