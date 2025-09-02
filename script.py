#Autor: Jose Luis Ramirez
#Codigo correspondiente a los ejercicios planteados del 1 al 30

#Funcion creada para hacer una separacion entre ejercicios que recibe la frase que los separa, es decir el enunciado de estos
def crearSeparacion(frase):
    print("----------------------------------------------------------------------------------")
    print(frase)
    print("----------------------------------------------------------------------------------")
    return 

#1. Ejercicio: Escribir un programa en Python que imprima por pantalla la frase “Hola, ya se imprimir frases”.

def ej1():
    crearSeparacion("1. Ejercicio: Escribir un programa en Python que imprima por pantalla la frase “Hola, ya se imprimir frases")
    print ("Hola, ya se imprimir frases")
    return

#2. Ejercicio: Escribir un programa en Python que imprima por pantalla un número entero, por ejemplo el 273, o el 597.

def ej2():
    crearSeparacion("2. Ejercicio: Escribir un programa en Python que imprima por pantalla un número entero.")
    x=int(3678)
    print(f"el numero entero es: {x}")
    return

#3. Ejercicio:Escribir un programa en Python que imprima por pantalla un número decimal, por ejemplo el 5’3, ó el 7’5.

def ej3():
    crearSeparacion("3. Ejercicio: Escribir un programa en Python que imprima por pantalla un número decimal.")
    x=float(3.14159)
    print(f"el numero decimal es: {x}")
    return

#4. Ejercicio: Escribir un programa en Python que imprima por pantalla la suma de 1234 y 532.

def ej4():
    crearSeparacion("4. Ejercicio: Escribir un programa en Python que imprima por pantalla la suma de 1234 y 532.")
    print(f"la suma de los dos numeros es: {1234+532}")
    return

#5. Ejercicio: Escribir un programa en Python que imprima por pantalla la resta de 1234 y 532.

def ej5():
    crearSeparacion("5. Ejercicio: Escribir un programa en Python que imprima por pantalla la resta de 1234 y 532.")
    print(f"la resta de los dos numeros es: {1234-532}")
    return
#6. Ejercicio: Escribir un programa en Python que imprima por pantalla la multiplicación de 1234 y 532.

def ej6():
    crearSeparacion("5. Ejercicio: Escribir un programa en Python que imprima por pantalla la multiplacion de 1234 y 532.")
    print(f"la multiplicacion de los dos numeros es: {1234*532}")
    return

#7. Ejercicio: Escribir un programa en Python que imprima por pantalla la división de 1234 entre 532.

def ej7():
    crearSeparacion("5. Ejercicio: Escribir un programa en Python que imprima por pantalla la division de 1234 y 532.")
    print(f"la division de los dos numeros es: {1234/532}")
    return

#8. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 3.

def ej8():
    crearSeparacion("8. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 3.")
    for i in range (1,4):
        print (f"{i}\n")

#9. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 9. 

def ej9():
    crearSeparacion("9. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 9.")
    for i in range (1, 10):
        print (f"{i}\n")

#10. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000. Conveniente usar bucles.

def ej10():
    crearSeparacion("10. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000. Conveniente usar bucles.")
    for i in range (1, 99997, 5):
        print (f"{i} {i+1} {i+2} {i+3} {i+4}")

#11. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 5 al 10.

def ej11():
    crearSeparacion("10. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000.")
    for i in range (5, 11, 1):
        print (f"{i}")

#12. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 5 al 15.

def ej12():
    crearSeparacion("10. Ejercicio: Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000.")
    for i in range (5, 11, 1):
        print (f"{i}")

def main():
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()
    ej7()
    ej8()
    ej9()
    ej10()
    ej11()

if __name__ == "__main__":
    main()

