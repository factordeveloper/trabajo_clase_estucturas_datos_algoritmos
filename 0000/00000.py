import sys

def ordenar_par_impar(numeros):
    # Separa la lista en números pares e impares
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    pares.sort()
    impares.sort()

    array_ordenado = pares + impares
    print(*array_ordenado)

def main():
    while True:
        linea = sys.stdin.readline().strip()
        if not linea:
            break

        n = int(linea)

        if n == 0:
            break
        
        array = list(map(int, sys.stdin.readline().strip().split()))
        ordenar_par_impar(array)

main()
