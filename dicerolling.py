import random
def roll_dice():
    return random.randint(1,6)
def main():
    print("Start Rolling a dice")
    while True:
        choice=input("Press 's' to start and 'q' to quit the game").lower()
        
        if choice=="s":
            num=roll_dice()
            print(f"The number that apperared in the dice is  {num}")
        elif choice=="q": 
            print("Quit the rolling game")
            break
        else:
            print("You entered an Invalid input")

if __name__=='__main__':
    main()


