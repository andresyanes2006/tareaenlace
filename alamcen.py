def main():
    lista_numeros = []

    while True:
        numero = int(input("Ingrese un número (ingrese un número negativo para terminar el programa): "))
        
        if numero < 0:
            break
        
        lista_numeros.append(numero)

    print("Lista original:", lista_numeros)

    # Eliminar duplicados utilizando un conjunto (set)
    lista_sin_duplicados = list(set(lista_numeros))

    print("Lista sin duplicados:", lista_sin_duplicados)

if __name__ == "__main__":
    main()