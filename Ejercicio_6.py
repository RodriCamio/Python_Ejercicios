import os
import colorama
from math import factorial

colorama.init()
white = "\x1b[1;37;40m" 
red = "\x1b[1;31;222m"

def limpiar():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
        
def convertir(valor): #función para verificar y convertir un número ingresado por teclado
    while valor == "" or valor.isdecimal() == False:
            limpiar()
            print(f"{white}Error")
            print(f"{white}Ingrese nuevamente:")
            valor = input(f">>>{red} ")
    valor = int(valor)
    return valor
def fact(a):
    a = factorial(a)
    return a
limpiar()
print(f'{white}Ejercicio 6: Factorial de un numero')

num1 = input(f'{white}Ingrese un numero para factorizar: ')
num1 = convertir(num1)
num1 = fact(num1)

limpiar()
print(f'{white}El factorial del numero ingresado es: {red} {num1}')
input(f'{white}Presione una tecla cualquiera para terminar...')