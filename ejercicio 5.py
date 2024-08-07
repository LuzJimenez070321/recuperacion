# Escribir una funcion sum y una funcion multip que sumen y multiplliquen respectivamente todos los numeros de una lista 
def suma(*numeros):
    return sum(numeros)

def multip(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

# Ejemplos de uso
resultado_suma = suma(1, 2, 3, 4)
resultado_multip = multip(1, 2, 3, 4)

print("La suma de los números es:", resultado_suma)
print("El producto de los números es:", resultado_multip)