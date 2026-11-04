def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    res: str = ""
    s: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    try:
        c = int(number, from_base)
    except ValueError:
        return "ERROR"
    while c > 0:
        res += s[c % to_base]
        c //= to_base
    return res[::-1]


print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))
