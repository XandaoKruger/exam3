# py_string_permutation_checker.py

>[!NOTE]
> Write a function that determines if two strings are permutations of each other.
> Case sensitive. Whitespace and punctuation count as regular characters.
> Empty strings are permutations of each other.

### Function signature

	def string_permutation_checker(s1: str, s2: str) -> bool:

### Examples

| Input | Output |
| :---: | :---: |
| `string_permutation_checker("abc", "bca")` | `True` |
| `string_permutation_checker("abc", "def")` | `False` |
| `string_permutation_checker("listen", "silent")` | `True` |
| `string_permutation_checker("hello", "bello")` | `False` |
| `string_permutation_checker("", "")` | `True` |
| `string_permutation_checker("a", "")` | `False` |
| `string_permutation_checker("Abc", "abc")` | `False` |
| `string_permutation_checker("a gentleman","elegant man")` | `True` |

### Lib __rich__ mport

>[!NOTE]
> Rich library used to replace the built-in print with the library's print, which has numerous functions. Here used to color 'TRUE & FALSE' automatically just by making this import.
>
> To install use -> pip install rich
>
> Otherwise, just comment the line with '#' and everything will be normal.