palavra = input("Escolha uma das palavras para converter em inglês: maçã, abacaxi, laranja, uva ou morango. ")
palavra = palavra.lower()

traducao = {
    "maçã": "apple",
    "abacaxi": "pineapple",
    "laranja": "orange",
    "uva": "grape",
    "morango": "strawberry"
}

if palavra in traducao:
    print(f"Português: {palavra}")
    print(f"inglês: {traducao[palavra]}")
else:
    print("Essa palavra não está na lista")