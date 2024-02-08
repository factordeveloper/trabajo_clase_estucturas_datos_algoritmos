import sys
def contar_frecuencia_palabras(lista_palabras):
    frecuencia = {}
    
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

def main():
    n = int(sys.stdin.readline().strip())
    lista_palabras = [input().strip() for _ in range(n)]

    resultado = contar_frecuencia_palabras(lista_palabras)

    for palabra, frecuencia in resultado.items():
        print(f"{palabra} : {frecuencia}")

main()
