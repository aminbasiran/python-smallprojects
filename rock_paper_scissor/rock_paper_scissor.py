import random
handSigns = ["rock","paper","scissor"]



number = input("Play how many consecutive wins?")

def playGame(howManyWins):
    
    playerOne = ""
    playerTwo = ""
    scoreA = 0
    scoreB = 0
    while scoreA != int(howManyWins) and scoreB != int(howManyWins): 
        
        playerOne = handSigns[int(random.randint(0,2))]
        playerTwo = handSigns[int(random.randint(0,2))]
        if playerOne==playerTwo:
            print("you picked the same signs. No points for both of you")
        elif playerOne == handSigns[0]:
            if playerTwo == handSigns[2]:
                print("playerOne gets a point")
                scoreA = scoreA + 1
            else:
                print("playerTwo gets a point")
                scoreB = scoreB+ 1

        elif playerOne == handSigns[1]:
            if playerTwo == handSigns[0]:
                print("playerOne gets a point")
                scoreA = scoreA +1
            else:
                print("playerTwo gets a point")
                scoreB = scoreB + 1

        elif playerOne == handSigns[2]:
            if playerTwo == handSigns[1]:
                print("playerOne gets a point")
                scoreA = scoreA +1
            else:
                print("playerTwo gets a point")
                scoreB = scoreB + 1
    if scoreA == int(howManyWins):
        print("playerOne wins")
    else:
        print("playerTwo wins")


playGame(number)

        





   

























# # # elif number == 5:
# #     playerOne = handSigns[int(random.randint(0,2))]
# #     print(playerOne)
# #     playerTwo = handSigns[int(random.randint(0,2))]
# #     print(playerTwo)
# #     if playerOne==playerTwo:
#         print("its a draw")
#         # playGame()
#     else:
#         print("this isnt a draw")
#         # playGam

# else:
#     print("please input valid number")
