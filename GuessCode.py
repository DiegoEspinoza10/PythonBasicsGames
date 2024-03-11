from random import randrange

class Code:
    def __init__(self,number):
        self.number = number

    def generate_code(self):
        code = 0
        if self.number == 4:
            code = randrange(1000,9999)
        else:
            code = randrange(100000,999999)
        return code

def check_rights(password, guess):
    password_digits = [int(digit) for digit in str(password)]
    guess_digits = [int(digit) for digit in str(guess)]
    
    right_position = 0
    wrong_position = 0
    
    for i in range(len(password_digits)):
        if password_digits[i] == guess_digits[i]:
            right_position += 1
        elif guess_digits[i] in password_digits:
            wrong_position += 1
    
    if right_position == 4:
        return "You won!"
    else:
        return f'Numbers in the right position: {right_position}, wrong position: {wrong_position}'


keep_playing = True  
while keep_playing:
    number_length = int(input("Select a length for the number 4 or 6: "))
    if number_length == 4 or number_length == 6:
        code = Code(4)
        password_code = code.generate_code()
        correct = False
        print(password_code)
        while correct != True:
            guess = int(input("Type the number: "))
            result = check_rights(password_code, guess)
            print(result)
            if result == "You won!":
                break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "no":
            keep_playing = False
    else:
        print("Select 4 or 6")

