lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

suma_listas = []

for i in range(len(lista1)):
    num1 = lista1[i]
    num2 = lista2[i]
    suma_listas.append(num1 + num2)

print(suma_listas)