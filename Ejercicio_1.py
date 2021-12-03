import os
import colorama

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

limpiar()
print(f'{white}Ejercicio 1: Solo numeros enteros')

num1 = input(f'{white}Ingrese un numero entero: ')
num1 = convertir(num1)
limpiar()
print(f'{white}El numero ingresado es: {num1}')
input(f'{white}Presione una tecla cualquiera para terminar...')