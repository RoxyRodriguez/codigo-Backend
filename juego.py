from  random import randrange
from os import system


aleatorio = randrange(1,4)
salir = 's'

print("======JUEGO DE PIEDRA, PEPEL Y TIJERA======")
print("===========================================\n\n")

while salir == 's':
    system('cls')
    print("OPCIONES")
    print("=============")
    print("1: Piedra")
    print("2: Papel")
    print("3: Tijera")
    print("\n")
    
    opcion = int(input("Ingrese una opción:"))
    
    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Elegiste: ", elijeUsuario)
    
    if aleatorio == 1:
        elijePc = "piedra"
    elif aleatorio == 2:
        elijePc = "papel"
    elif aleatorio == 3:
        elijePc = "tijera"
    
    print("La computadora eligió: ", elijePc,'\n')
    
    if elijePc == "piedra" and elijeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
        
    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("Ganaste, Tijera corta papel")
        
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, Piedra pisa tijera")
        
    if elijePc == "papel" and elijeUsuario == "piedra":
        print("perdiste, papel envuelve a piedra")
        
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("perdiste, Tijera corta papel")
        
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("perdiste, Piedra pisa tijera")
        
    elif elijePc == elijeUsuario:
        print("Empate")

    salir = input("\nDesea Continuar (S/N)? :")