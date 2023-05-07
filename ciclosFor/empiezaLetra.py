palabras = input("Ingresa una lista de palabras separadas por comas: ").split(",")
letra = input("Ingresa la letra con la que deben empezar las palabras a mostrar: ")

for palabra in palabras:
    if palabra.startswith(letra):
        print(palabra)