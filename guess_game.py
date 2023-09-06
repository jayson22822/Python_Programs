secret_number = int(input("enter the number to guessed : "))
attempt = int(input("enter no of attempts : "))
no_of_attempts = 0;
while no_of_attempts < attempt:
    guess = int(input("Guess the number : "))
    if guess == secret_number:
        print("You Won!")
        break
    else:
        no_of_attempts = no_of_attempts + 1
        print("Oops! Try again.")
else:
    print("Sorry! You failed.")

