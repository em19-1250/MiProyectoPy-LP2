#Leer un número entero y determinar si es negativo:

numero = int(input("Ingrese un número entero: "))
if numero < 0:
    print("El número es negativo.")
else:
    print("El número no es negativo.")


# Leer un número entero y determinar cuántos dígitos tiene:
numero = int(input("Ingrese un número entero: "))
digitos = len(str(abs(numero)))
print(f"El número tiene {digitos} dígito(s).")

#Leer un número entero y determinar si es primo:

numero = int(input("Ingrese un número entero: "))

if numero > 1:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
else:
    print("El número no es primo.")

#Leer 4 enteros, almacenarlos en una lista y determinar en qué posición está el mayor:

numeros = []
for i in range(4):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

mayor = max(numeros)
posicion = numeros.index(mayor)  # índice inicia en 0

print(f"El mayor número es {mayor} y está en la posición {posicion}.")

#Eliminar duplicados de una lista:

numeros = [1,1,2,3,3,2,5,6,2,7,8,4,3,1]
sin_duplicados = []
for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista sin duplicados (orden original):", sin_duplicados)