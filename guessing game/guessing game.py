# guessing game

# method 1
# secret = "amin"
# guess = ""
# guess_count = 0
# guess_limit = 5

# while guess!=secret:
#     guess_count +=1
#     guess = input("enter your guess")
#     if (guess == secret):
#         print("you win")
#     elif(guess_count == guess_limit):
#         print("you are out of guesses")
#         break

# method 2
import random

def playAgain():
    secret = str(random.randint(0,1000))
    res = [int(x) for x in str(secret)]
    # print(secret)
    if len(res) == 1:
        print("clue: your random generated number has " + str(len(res)) + " digit")
    else:
        print("clue: your random generated number has " + str(len(res)) + " digits starting with the number " + str(res[0]))

    guess_count = 0
    guess_limit = int(input("enter how many trys you get"))
    out_of_guesses = False
    guess = 0
    while guess!=secret and not(out_of_guesses):
        if (guess_count < guess_limit ):
            guess_count+=1
            guess=input("enter your guess")
            if not(guess.isdigit()):
                print("you didnt enter a digit, PLAY AGAIN")
                break

        else:
            out_of_guesses=True

    if out_of_guesses:
        print("you are out of guesses. Your random number was " + secret)
        playAgain()
    elif guess==secret:
        print("you win")
        playAgain()
        
playAgain()
        




# array = [[1,2,3],[4,5,6]]

# for every in array:
#     for column in every:
#         print(column)