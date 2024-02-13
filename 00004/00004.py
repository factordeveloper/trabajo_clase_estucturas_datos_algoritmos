import sys

def sumar_subarrays(arr):
    max_suma = float('-inf')

    # Itera sobre todos los posibles subarreglos contiguos
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_suma = sum(arr[i:j+1])
            max_suma = max(max_suma, current_suma)

    return max_suma

def main():
    # Lee la entrada de la consola estándar
    for line in sys.stdin:
        # Convierte la línea en una lista de números enteros
        numbers = list(map(int, line.split()))

        # Obtiene el tamaño de la lista de números
        n = numbers[0]

        # Calcula la suma máxima del subarreglo contiguo y la imprime
        max_suma = sumar_subarrays(numbers[1:])
        print(max_suma)


main()
