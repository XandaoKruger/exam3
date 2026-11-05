
# py_bracket_validator

> [!NOTE]
> Write a function that checks if the brackets in a string are valid.
>
> A string is valid if every opening bracket has a matching closing bracket
> in the correct order.
>
> Allowed brackets: (), [], {}

### Function signature

	def bracket_validator(s: str) -> bool:


### Examples

| Input | Output |
| :---: | :---: |
| `bracket_validator("()")` | `True` |
| `bracket_validator("()[]{}")` | `True` |
| `bracket_validator("(]")` | `False` |
| `bracket_validator("([)]")` | `False` |
| `bracket_validator("{[]}")` | `True` |
| `bracket_validator("hello(world)")` | `True` |
| `bracket_validator("((())")` | `False` |
| `bracket_validator("")` | `True` |