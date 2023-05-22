import random

computer_choice_number = random.randint(1, 100)

guessed = False
user_try = 6
while True:
    if user_try == 0:
        break
    user_number = int(input(f"Guess a number between 1 to 100 within {user_try} try: ...\n"))
    user_try -= 1

    if user_number == computer_choice_number:
        guessed = True
        break
    if user_number < computer_choice_number:
        if computer_choice_number-user_number <= 10:
            print(f"You are very close , but low . Try again , you have {user_try} try left")
        else:
            print(f"You are low . Try again , you have {user_try} try left")
    elif user_number > computer_choice_number:
        if user_number-computer_choice_number <= 10:
            print(f"You are very close , but high . Try again , you have {user_try} try left")
        else:
            print(f"You are high . Try again , you have {user_try} try left")
if guessed:
    print("You WIN !")
else:
    print(f"You lose ... the number was {computer_choice_number}")