import random
def main():
    number_to_guess=random.randint(1,100)
    attemps=0
    print("Welcome to the game of gussesing the number")
    print("I have selected a number between 1 and 100")
    print("Can you guess what it is?")
    while True:
        attemps+=1
        try:
            guess=int(input("Enter the number"))
        except ValueError:
            print("Please enter a valid number")
            continue
        if(guess<number_to_guess):
            print("Too low! Try again")
        elif(guess>number_to_guess):
            print("Too high! Try again!")
        else:
            print("Congratulations you won!")
            break
if __name__=='__main__':
    main()