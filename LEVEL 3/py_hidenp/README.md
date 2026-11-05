# py_hidenp

> [!NOTE]
> Write a function that checks if the string 'small' is a subsequence
> of 'big'. A subsequence means all characters of 'small' appear in 'big'
> in the same order, but not necessarily consecutively.
> Function is case-sensitive.

### Function signature

	def hidenp(small: str, big: str) -> bool:

### Examples

| Input | Output |
| :---: | :---: |
| `hidenp("abc", "a1b2c3")` | `True` |
| `hidenp("ace", "abcde")` | `True` |
| `hidenp("aec", "abcde")` | `False` |
| `hidenp("", "abc")` | `True` |
| `hidenp("abc", "ab")` | `False` |
| `hidenp("aaaa", "aaa")` | `False` |
| `hidenp("sing","subsequence testing")` | `True` |

### Lib __rich__ mport

>[!NOTE]
> Rich library used to replace the built-in print with the library's print, which has numerous functions. Here used to color 'TRUE & FALSE' automatically just by making this import.
>
> To install use -> pip install rich
>
> Otherwise, just comment the line with '#' and everything will be normal.