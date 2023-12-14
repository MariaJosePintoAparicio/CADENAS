import os
os.system('cls')
mensaje = "fundamentos "
contadorConsonantes = int(0)
vocales=int(0)
lstvocales= "aeiou"
for  caracter in mensaje:
    if caracter.upper() in lstvocales:
        vocales+=1
    elif caracter.isalpha():
        contadorConsonantes+=1



print (f"el total de vocales es = {vocales}")
print(f"el total de consonantes es ={contadorConsonantes}") 
for item in range (1,5,2):
    print(item)



for i,item in enumerate (mensaje):
    print(f"pos{i} - {item}") 
    mensaje = mensaje.replace (item,"-",i)
    print (mensaje)
    os.system("pause")






