from random import shuffle

vasos = ['O',' ',' ']

def shufflevasos(vasos):
    shuffle(vasos)
    return vasos

def user_guess():
    guess = int(input('Donde esta la pelota? '))
    guess -= 1
    while guess > 2:
        print('El numero esta afuera de la cantidad de vasos que hay') 
        guess = int(input('Por favor, ingresa un número entre 1 y 3: '))
        guess -= 1
    return guess

def logica(vasos, guess):
    correcto = False
    while correcto == False:
        if vasos[guess] == 'O':
            print('Felicidades adivinaste donde estaba la bola!')
            correcto = True
        else:
            print('No estaba ahi! jajaja')
            print('Estaba aqui: {}'.format(vasos))
            vasos = shufflevasos(vasos)
            guess = user_guess()
            logica(vasos,guess)
            return False

print('Aqui esta la bola, siguela')
print(vasos)
print('*mixing* *mixing*')
print('Espero que la hayas seguido bien!')
shufflevasos(vasos)
guess = user_guess()
logica(vasos,guess)

