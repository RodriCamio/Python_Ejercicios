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

def ingrese(a):
    b = input(f'{white}Ingrese numero {a}: {red}')
    return b



limpiar()
print(f'{white}Ejercicio 4: Matriz de numeros')

fila = ingrese('de filas')
fila = convertir(fila)
columna = ingrese('de columnas')
columna = convertir(columna)
fil = []

for i in range(fila):
    col = []
    for x in range(columna):
        num = ingrese(f'para la matriz[{i}][{x}]')
        col.append(num)
    fil.append(col)
    
print(f'{white}La matriz ingresada es:\n{fil}')
input(f'{white}Ingrese una tela cualquiera para terminar...')