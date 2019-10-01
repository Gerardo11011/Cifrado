import math
import numpy as np

def mensajeInput():
    print('Ingresa tu mensaje:')
    return input()

def obtenerModo():
    while True:
        print('''
        ¿Que desea hacer?
        e.- para encriptar
        d.- para desencriptar''')
        modo = input().lower()
        if modo == 'e' or modo == 'd':
            return modo

def claveCifrado():
    clave = ""
    while True:
        print('Ingresa la palabra clave')
        clave = str(input())
        return len(clave)

def operacionMensaje(mensaje, modo, clave):
    traduccion = ''
    sinespacio = mensaje.replace(' ', '')
    tama = len(sinespacio)
    k = 0
    #genera la matriz en caso de que se desee encriptar
    if modo[0] == 'e':
        row = math.ceil(tama / clave)
        columns = clave
        #se llena la matriz de forma normal
        matriz = [['' for x in range(columns)] for y in range(row)]

    #genera la matriz en caso de que se desee desencriptar
    elif modo[0] == 'd':
        row = clave
        columns = math.ceil(tama / clave)
        #se invierten el orden de llenado para la matriz
        matriz = [['' for x in range(columns)] for y in range(row)]

    #Rellena la matriz con el mensaje
    for i in range (row):
        for j in range (columns):
            if k < tama:
                if sinespacio[k].isalpha():
                    matriz[i][j] = sinespacio[k]
                    k += 1

    #se imprime la matriz con el mensaje
    for i in range (columns):
        for j in range (row):
            if matriz[j][i].isalpha():
                traduccion += matriz[j][i]

    return traduccion




def obtenermensaje():
    modo = obtenerModo()
    mensaje = mensajeInput()
    clave = claveCifrado()
    print('El mensaje es:')
    print(operacionMensaje(mensaje, modo, clave))
