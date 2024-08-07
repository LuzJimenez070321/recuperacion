# Definir una funcion que calcule la longuitud de una lista o una cadena dada 
def calcular_longitud(lista_o_cadena):
    return len(lista_o_cadena)

# Ejemplos de uso
cadena = "Hola, mundo!"
lista = [1, 2, 3, 4, 5]

longitud_cadena = calcular_longitud(cadena)
print("La longitud de la cadena es:", longitud_cadena)

longitud_lista = calcular_longitud(lista)
print("La longitud de la lista es:", longitud_lista)