def key(s: str) -> tuple:
    vogais: str = "aeiou"
    criterio: tuple = (len(s), s.lower(), sum(x in vogais for x in s.lower()))

    return criterio


def cryptic_sorter(strings: list[str]) -> list[str]:
    copia: list[str] = strings.copy()

    for i in range(1, len(copia)):
        
        atual = copia[i]
        nota_atual = key(atual)
        j = i - 1
        
        while j >= 0 and key(copia[j]) > nota_atual:
            
            copia[j + 1] = copia[j]
            j -= 1

        copia[j + 1] = atual

    return copia

# print(key("bb"))
# print(key("AAaa"))
# print(key("AA"))
# print(key("aie"))
# print(key("to escrevendo QUALQUER coisa por vias de teste"))

print(cryptic_sorter(["aaAAbbBB", "testando", "TestAndo", "cachorro", "dOg", "DoGUInho"]))
