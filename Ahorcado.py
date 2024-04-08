#!usr/bin/env python3

def pedir_letra():
    return input("Introduce una letra: ")
    
def ocultar_palabra(palabra_adivinar):
    palabra_oculta = ""
    for letra in palabra_adivinar:
        palabra_oculta += "_"
    return palabra_oculta
    
def partida(palabra_adivinar ,palabra_oculta, vidas):
    while palabra_adivinar != palabra_oculta and vidas != 0 :
    
        print("TRAZA La palabra a adivinar es:", palabra_adivinar)
        print("TRAZA La palabra con guiones es:", palabra_oculta)
    
        letra = pedir_letra()
        if coincidencia(palabra_adivinar, palabra_oculta, letra) == True:
            palabra_oculta = acierto(palabra_adivinar, palabra_oculta, letra)
            
        else:
            vidas = fallo(letra, vidas)
    print("Has acabado la partida")
        
def coincidencia(palabra_adivinar, palabra_oculta, letra):
    existe = False
    for indice, deletreo in enumerate(palabra_adivinar):
        if deletreo == letra:
            existe = True
    return existe

def acierto(palabra_adivinar, palabra_oculta, letra):
    # Convertir la palabra oculta a lista
    palabra_oculta_lista = list(palabra_oculta)
    
    for indice, deletreo in enumerate(palabra_adivinar):
        if deletreo == letra:
            palabra_oculta_lista[indice] = letra
    
    # Convertir la palabra oculta de nuevo a cadena
    palabra_oculta_actualizada = ''.join(palabra_oculta_lista)
    
    return palabra_oculta_actualizada
    
def fallo(letra, vidas):
    print(f"[!] Has fallado, la letra {letra} no está en la palabra, te quedan {vidas - 1} vidas")
    vidas -= 1
    if vidas == 0:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|   / \\")
        print("|")
    elif vidas == 1:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|   /")
        print("|")
    elif vidas == 2:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|   /|\\")
        print("|")
        print("|")
    elif vidas == 3:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|   /|")
        print("|")
        print("|")
        
    elif vidas == 4:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|    |")
        print("|")
        print("|")
    
    elif vidas == 5:
        print(" ____")
        print("|    |")
        print("|    O")
        print("|")
        print("|")
        print("|")
    
    return vidas
    
           


palabra_adivinar = input("Introduce una palabra para jugar: ")
palabra_oculta = ocultar_palabra(palabra_adivinar)
vidas = 6

partida(palabra_adivinar, palabra_oculta, vidas)
