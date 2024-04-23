
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
cont_par = 0
cont_impar = 0
for i in range(n1, n2 + 1):
    print(i, end=' ')
    if i % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1


print(f"\n\nEntre {n1} e {n2} existem {cont_par} pares e {cont_impar} impares")

# Alteração feita para o pix
