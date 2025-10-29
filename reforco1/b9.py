l1 = int(input("Digite o lado do triângulo: "))
l2 = int(input("Digite o lado do triângulo: "))
l3 = int(input("Digite o lado do triângulo: "))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print("De acordo com o teorema da desigualdade triangular, um triângulo com esses valores não pode ser formado")
elif l1 == l2 == l3:
    print("O triângulo é equilátero")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("O triângulo é escaleno")
else:
    print("O triângulo é isósceles")