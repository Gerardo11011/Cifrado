#Gerardo Aldair Ponce Gomez
#A00818934

alfabeto = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }


def mensajeInput():
    print('Ingresa tu mensaje:')
    return input()

def claveCifrado():
    clave = ""
    print('Ingresa la llave numerica')
    clave = int(input())
    return clave

#funcion que retorna la letra del alfabeto de acuerdo a su valor en el mismo
def encontrarLLave(aux):
    for key,value in alfabeto.items():
        if  aux == str(value):
            return str(key)


def operacionMensaje(mensaje, clave):
    traduccion = ''
    i = 0
    for letra in mensaje:
        if letra.isalpha():
            #Multiplacion para calcular la posicion de la nueva letra
            aux = str((alfabeto.get(letra) * clave) % 26)
            traduccion += encontrarLLave(aux)
    return traduccion


def obtenermensaje():
    mensaje = mensajeInput()
    clave = claveCifrado()
    print('El mensaje es:')
    print(operacionMensaje(mensaje, clave))
