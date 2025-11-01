palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

vogais = {
    "a": 0,
    "i": 0,
    "o": 0,
    "u": 0,
    "e": 0,
}

for letra in palavra:
    if letra in vogais:
        vogais[letra] += 1

print(vogais)