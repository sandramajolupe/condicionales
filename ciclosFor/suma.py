def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista(numeros)
print("La suma de la lista es:", resultado)