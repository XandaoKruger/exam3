# py_inter.py

> Write a function that returns a string with the characters that appear
> in both strings, without repetitions. Characters are added in the order
> they appear in the first string.

### Function signature

	def inter(s1: str, s2: str) -> str:

### Examples

| Input | Output |
| :---: | :---: |
| `inter("hello", "world")` | `"lo"` |
| `inter("banana", "band")` | `"ban"` |
| `inter("abcabc", "bc")` | `"bc"` |
| `inter("abc", "xyz")` | `""` |
| `inter("", "abc")` | `""` |