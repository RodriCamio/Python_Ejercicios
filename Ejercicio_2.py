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
print(f'{white}Ejercicio 2: Lista de nombres')

cantidad = input(f'{white}Ingrese cantidad de nombres: {red}')
cantidad = convertir(cantidad)

nombres = []

for i in range(0,cantidad):
    nombre = input(f'{white}Nombre: {red}')
    nombres.append(nombre)
limpiar()
print(f'{white}Los nombres de la lista son: ')
for i in nombres:
    print('- '+i)
    
input(f'{white}Precione una tecla cualquiera para terminar...')