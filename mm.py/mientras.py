import os
isActive = True
rta = 0
menu = "1.sumar\n2. restar\n0. salir"
while (isActive):
    try:
        rta = int(input(menu))
    except ValueError:
        print ("error en el dato")
    else:
        if (rta == 1):
            print("sumando")
        elif (rta == 2):
            print("restando")
        elif (rta == 0):
            print("ok chao")
            isActive = False
        else:
            print("la opcion que ingreso es invalida..")
            os.system("pause")
        os.system("pause") 