def is_palindrome(s):
    # Función auxiliar para verificar si una cadena es palindrómica
    return s == s[::-1]

def longest_palindromic_substring(s):
    max_length = 0
    
    # Itera sobre todas las subcadenas posibles
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
    
    return max_length

if __name__ == "__main__":
    # Leer la entrada desde stdin
    cadena = input().strip()

    # Calcular la longitud de la subcadena palindrómica más larga
    longitud_maxima = longest_palindromic_substring(cadena)

    # Imprimir la longitud de la subcadena palindrómica más larga
    print(longitud_maxima)