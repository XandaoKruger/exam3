# py_string_sculptor.py

>[!NOTE]
> Write a function that transforms a string by alternating the case of
> alphabetic characters only.
> Non-alphabetic characters remain unchanged and are NOT counted in the
> alternation index.
> The first alphabetic character should be lowercase, the second uppercase, etc.

### Function signature

	def string_sculptor(text: str) -> str:

### Examples

| Input | Output |
| :---: | :---: |
| `string_sculptor("hello")` | `"hElLo"` |
| `string_sculptor("Hello World")` | `"hElLo WoRlD"` |
| `string_sculptor(" hello ")` | `" hElLo "` |
| `string_sculptor("abc123def")` | `"aBc123DeF"` |
| `string_sculptor("Python3.9!")` | `"pYtHoN3.9!"` |
| `string_sculptor("")` | `""` |
