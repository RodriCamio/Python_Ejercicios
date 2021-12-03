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
print(f'{white}Ejercicio 3: encontrar un nombre en la lista')

cantidad = input(f'{white}Ingrese cantidad de nombres: {red}')
cantidad = convertir(cantidad)

nombres = []

for i in range(0,cantidad):
    nombre = input(f'{white}Nombre: {red}')
    nombres.append(nombre)
contador = 0
limpiar()
comparar = input(f'{white}Ingrese un nombre para saber si se encuentra en la lista y cuantas veces: ')
if comparar in nombres:
    for i in nombres:
        if comparar == i:
            contador += 1 
        else:
            pass
    if contador == 1:
        print(f'{white}"{comparar}" se encuentra en la lista {contador} vez')
    else:
        print(f'{white}"{comparar}" se encuentra en la lista {contador} veces')
    
else:
    print(f'{red}"{comparar}" no se encuentra en la lista{white}')
    
input(f'{white}Presione una tecla cualquiera para terminar...')