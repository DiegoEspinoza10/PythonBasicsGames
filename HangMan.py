from random import shuffle

#Conjunto de palabras que pueden salir
words = ['pantera', 'oso','profesor','Argentina','Doctor','Ganadero','Lionel']

#mezclamos lista de palabras y elijimos una al azar
def chooseword(words):
    shuffle(words)
    eleccion = words[1]
    return eleccion


def user_guess(palabra):
    lives = 6
    guess = ['_'] * len(palabra)
    while lives > 0:
        print('\nTe quedan {} vidas'.format(lives))
        print(' '.join(guess)) 
        respuesta = int(input('\nQuiere adivinar toda la palabra? 1.Si 2.No'))
        if respuesta == 1:
            word = input('Digite la palabra: ')
            if(word == palabra):
                print('Correcto!')
                exit()
            else:
                print('Incorrecto!')
                lives = lives - 1
        else:
            letter = input('Digite una letra: ')
            if letter in palabra:
                print('{} si esta en la palabra'.format(letter))
                for i in range(len(palabra)):
                    if palabra[i] == letter:
                        guess[i] = letter
                if '_' not in guess:
                    print('¡Correcto! La palabra era:', palabra)
                    exit()
            else:
                print('No esta en las palabras')
                lives = lives - 1
    print('-----------------------------------------------')
    print('| Se acabaron las vidas. La palabra era:', palabra + '|')
    print('-----------------------------------------------')



palabra = chooseword(words)
palabra.split()
user_guess(palabra)
