1) lado = 8


raiz_3 = 1.732


area = (3 * raiz_3 / 2) * (lado ** 2)


area_arredondada = round(area, 2)


print("Área do hexágono =",area_arredondada, "cm²")


2) numeros = (2, 5, 8, 9, 12, 15, 18)


print("Números menores de 15:")

for n in numeros:

    if n <= 15:

        print(n, end=' ')

print()  


contagem = 0

for n in numeros:

    if n <= 15 and n % 2 == 0:

        contagem += 1


print("Quantidade de números pares =", contagem)


3) lista = (1, 2)


def soma_lista(lista):

    total = 0

    for num in lista:

        total += num

    return total


print(soma_lista(lista))


4) nomes = ('alice', 'bob', 'lucas')


nomes_maiusculo = tuple(nome.upper() for nome in nomes)


print(nomes_maiusculo)



5) for i in range(5):

print(i)


