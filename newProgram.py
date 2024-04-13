# Start of a new Python program
from os.path import exists

if exists('spider.txt' and 'snake.txt'):
    endLoop = True
    print("\nHello, are you scared of spiders or snakes? \n")
    while(endLoop):
        userAnswer = input("Please answer Spider or Snake: ")
        answer = userAnswer.lower()


        if answer == "spider":
            with open('spider.txt', 'r') as file:
                print('\n'+file.read())
        elif answer=="snake":
            with open('snake.txt', 'r') as file:
             print('\n'+file.read()) 

        stillScared = input("Are you still scared? Please enter Yes or No: ")
        checkStillScared = stillScared.lower()
        if checkStillScared != "yes":
            endLoop=False  
    
    print("Thanks for playing!")

    
else:
    print("Sorry no file")