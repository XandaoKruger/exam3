# py_anagram.py

>[!NOTE]
> Write a function that checks if two strings are anagrams.
> They must contain exactly the same letters with the same quantity,
> ignoring case and spaces.

### Function signature

	def anagram(s1: str, s2: str) -> bool:

### Examples

| Input | Output |
| :---: | :---: |
| `anagram("listen", "silent")` | `True` |
| `anagram("Triangle", "Integral")` | `True` |
| `anagram("Dormitory", "Dirty Room")` | `True` |
| `anagram("hello", "world")` | `False` |
| `anagram("", "")` | `True` |
| `anagram("abc", "abcc")` | `False` |

### Lib __rich__ mport

>[!NOTE]
> Rich library used to replace the built-in print with the library's print, which has numerous functions. Here used to color 'TRUE & FALSE' automatically just by making this import.
>
> To install use -> pip install rich
>
> Otherwise, just comment the line with '#' and everything will be normal.