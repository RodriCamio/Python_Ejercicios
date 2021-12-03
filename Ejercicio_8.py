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

def multiplos(a):
    inicio = 1
    multi = []
    while inicio <= a:
        if inicio%3 == 0 or inicio%5 == 0:
            multi.append(inicio)
            inicio += 1
        else:
            inicio += 1 
    return multi
limpiar()
print(f'{white}Ejercicio 8: Multiplos de 3 y de 5 hasta...')

num1 = input(f'{white}Ingrese el limite: ')
num1 = convertir(num1)
limpiar()
lista = multiplos(num1)
print(f'{white}Los multiplos de 3 y de 5 hasta {num1} son:\n {red} {lista}')
input(f'{white}Presione una tecla cualquiera para terminar...')