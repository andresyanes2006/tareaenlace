import random

def generaraleatorios(cantidad):
    numeros = [random.randint(1, 100) for i in range(cantidad)]
    return numeros

def main():
    cantidad = 15
    naleatorios = generaraleatorios(cantidad)
    
    print("Números generados aleatoriamente:")
    print(naleatorios)
    
    nordenados = sorted(naleatorios)
    
    print("\nNúmeros ordenados:")
    print(nordenados)

if __name__ == "__main__":
    main()
