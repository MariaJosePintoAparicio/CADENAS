import os

print("""
============Bienvenido Al Ahorcado============
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                ==========


Tiene tres intentos para intentar adivinar la palabra
\n""")

palabra =input("Ingrese la palabra a adivinar: ").lower()
os.system("cls")
letra = ""
vidas = 3
palabraVacia = palabra
palabraComparacion = palabra
for item in palabraVacia:
    palabraVacia = palabraVacia.replace(item,"_")

while vidas > 0 and palabraVacia != palabraComparacion:


    for j,caracter in enumerate(palabraComparacion):
        if palabraVacia[j] == caracter:
            print(palabra[j],end=" ")
        else:
            print(palabraVacia[j],end=" ")


    print(f"\nVidas = {vidas}")
    letra = input("Ingrese la letra: ").lower()
    if len(letra) == 1:
        if letra in palabra:

            for j, caracter in enumerate(palabra):

                if caracter == letra:
                    palabraComparacion = palabraComparacion.replace(letra,"_")
        else:
            vidas -= 1
        os.system("cls")
    else:
        print("\nIngrese solo una letra")
if  vidas == 0:
    print(f"     Game over\nla palabra era: {palabra}")
else:
    print("Ganaste :D")