import random as r 
random_value = r.randint(2,9)

guesses = 0 #user haven't made any guess yet!
value = 0 

user_name = input('Howdy?May I know your name? ').strip().capitalize()
print("Hello,"+"{}!".format(user_name))
ques_choice = input('Are you ready to guess?[Y/N]:').strip()

if ques_choice == 'y':
    print('Hello,'+"{}".format(user_name))
    print("I am thinking of a number between 1 to 10!")
elif ques_choice == 'n':
    print("We're sorry, Will meet you later!")
    exit()
else:
    print("Wrong input!")
    exit()

while not (random_value == value):
    number = int(input('Enter your guess here: '))
    guesses = guesses+1
    if number == random_value:
        print("Brilliant!")
        print("You guessed it correctly,the correct number is {}".format(random_value))
        if guesses == 1:
            print("It took you {}".format(guesses)+" try in total!")
        else:
            print("It took you {}".format(guesses)+" tries in total!")

        exit()
    elif number < random_value:
        print("Guess higher")
    else:
        print("Guess lower")     



