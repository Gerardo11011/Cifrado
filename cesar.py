CLAVE_MAX = 26


def obtenerModo():
    while True:
        print('''
        ¿Que desea hacer?
        e.- para encriptar
        d.- para desencriptar''')
        modo = input().lower()
        if modo == 'e' or modo == 'd':
            return modo


def mensajeInput():
    print('Ingresa tu mensaje:')
    return input()


def claveCifrado():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (CLAVE_MAX))
        clave = int(input())
        if (clave >= 1 and clave <= CLAVE_MAX):
            return clave

def operacionMensaje(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif simbolo.islower():

                if num > ord('z'):
                    num -= 26

                elif num < ord('a'):
                    num += 26

            traduccion += chr(num)

        else:
            traduccion += simbolo

    return traduccion




def obtenermensaje():
    modo = obtenerModo()
    mensaje = mensajeInput()
    clave = claveCifrado()
    print('El mensaje es:')
    print(operacionMensaje(modo, mensaje, clave))
