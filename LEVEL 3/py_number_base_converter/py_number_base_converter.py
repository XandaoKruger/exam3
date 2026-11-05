def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    base: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pot: str = ""

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        value: int = int(number, from_base)
    except ValueError:
        return "ERROR"

    if value == 0:
        return "0"

    while value > 0:
        quoc, remain = divmod(value, to_base)
        pot += base[remain]
        value = quoc
    return pot[::-1]




print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))