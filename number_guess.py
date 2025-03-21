import random

while True:
    
    guess = random.randint(1,100)
    attempt = 0

    while True:
        user_input = int(input("Enter a number between 1 to 100: "))
        attempt+=1
        if guess < user_input:
            print("Number is to high")
        elif guess > user_input:
            print("Number is to low")
        else:
            print(f"Correct! You guessed in {attempt} attempt!")
            break
        if attempt == 3:
            if guess % 2 == 0:
                print("Hint: Number is Even")
            else:
                print(" Hint: Number is Odd")
               
    again = ("You want to play a game again!")
    response = input("Enter a 'Yes' or 'No': ").lower()
    if response != "yes":
        print("Thanks For Playing a game!")
        break
