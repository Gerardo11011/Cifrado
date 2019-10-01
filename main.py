#Gerardo Aldair Ponce Gomez
#A00818934
import cesar as chizza
import vinager as vine
import transposition as trans
import mutiplicative as multi


valido = True

while valido:
    print('''
    ¿Cifrado desea realizar?
    c.- Cesar
    v.- Vinager
    t.- Transposition
    m.- Mutiplicative
    ''')

    cifra = input()

    if cifra == 'c' or cifra == 'C':
        chizza.obtenermensaje()
        valido = False
    elif cifra == 'v' or cifra == 'V':
        vine.obtenermensaje()
        valido = False
    elif cifra == 't' or cifra == 'T':
        trans.obtenermensaje()
        valido = False
    elif cifra == 'm' or cifra == 'M':
        multi.obtenermensaje()
        valido = False
    else:
        print('Dato no valido')
