import random
number = random.randint(0,100)
guesses = [0]
explicacion = "El programa eligira al azar un numero del 0 al 100, debes adivinar"
explicacion += "el numero lo antes posible."
print(explicacion)

tries = False
while tries == False:
    guess = int(input('Digite su guess: '))
    if guess <1 or guess > 100:
        print("Excediste los limites...")
    if guess == number:
        tries = True
        print("Felicidades, adivinastte el numero, el numero era {}, en un total de {} intentos".format(number,len(guesses)))
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(number - guess) < abs(number-guesses[-2]):
            print("Mas caliente")
        else:
            print("Mas frio")

    else:
        if abs(number-guess) <= 10:
            print("Caliente")
        else:
            print("Frio")
