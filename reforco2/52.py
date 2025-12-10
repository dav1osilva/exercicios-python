quantidade_espacos = 4
while quantidade_espacos >= 1:
    quantidade_asteriscos = 1
    while quantidade_asteriscos <= 5:
        print(quantidade_espacos * " ", quantidade_asteriscos * "*")
        quantidade_asteriscos += 1
        quantidade_espacos -= 1