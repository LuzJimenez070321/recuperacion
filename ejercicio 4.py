# Escribir una funcion que tome un caracter y devuelva true si es una vocal, de lo contrario devuelva false
def es_vocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u']
    return caracter.lower() in vocales

# Ejemplo de uso
caracter = 'a'
resultado = es_vocal(caracter)

if resultado:
    print(f"El carácter '{caracter}' es una vocal.")
else:
    print(f"El carácter '{caracter}' no es una vocal.")