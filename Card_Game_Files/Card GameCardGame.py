#Player 1 Login

playerOneAuthorised = False
playerOneLoginDetails = open("PlayerOneLoginDetails.txt","r")
playerOneValidUsername = playerOneLoginDetails.readline().strip()
playerOneValidPassword = playerOneLoginDetails.readline().strip()

while playerOneAuthorised == False:
    playerOneUsernameInput = input("Enter Player 1's username:")
    playerOnePasswordInput = input("Enter Player 1's password:")

    if playerOneUsernameInput == "" or playerOnePasswordInput == "":
        print("Login unsuccessful. Player 1 Username/Password field has been left blank. Please try again.")
    elif playerOneUsernameInput == playerOneValidUsername and playerOnePasswordInput == playerOneValidPassword:
        print("Player 1 login successful.")
        print("-----------------------------------------------------------------------------------------------")
        playerOneLoginDetails.close()
        break
    else:
        print("The username/password that player 1 has entered is incorrect. Please try again.")

#Player 2 Login

playerTwoAuthorised = False
playerTwoLoginDetails = open("PlayerTwoLoginDetails.txt","r")
playerTwoValidUsername = playerTwoLoginDetails.readline().strip()
playerTwoValidPassword = playerTwoLoginDetails.readline().strip()

while playerTwoAuthorised == False:
    playerTwoUsernameInput = input("Enter Player 2's username:")
    playerTwoPasswordInput = input("Enter player 2's password:")

    if playerTwoUsernameInput == "" or playerTwoUsernameInput == "":
        print("Login unsuccessful. Player 2 Username/Password field has been left blank. Please try again.")
    elif playerTwoUsernameInput == playerTwoValidUsername and playerTwoPasswordInput == playerTwoValidPassword:
        print("Player 2 login successful.")
        print("-----------------------------------------------------------------------------------------------")
        playerTwoLoginDetails.close()
        break
    else:
        print("The username/password that player 2 has entered is incorrect. Please try again.")

#Main Game

# Since beats red beats black and black beats yellow and yellow beats red and the same colours cancel each other out,
# by ending the values on the cards with a hidden decimal it will make it easier to identify when cards of the same
# colour have been chosen. Also it makes it easier to see which cards has one in the case of different colours. So
# for example, in the case of a yellow card and a red card comparing the cards will make yellow win as even if the
# numbers are the same yellow will still win because of the hidden decimal on the end. The only exception to this
# rule is in the case of red and black. In this case a hidden 0.3 will be added to the chosen red card so the logic
# can continue. 

import random

cardsLeftInDeck = 30
redCards = [1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1]
yellowCards = [1.2,2.2,3.2,4.2,5.2,6.2,7.2,8.2,9.2,10.2]
blackCards = [1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3]
random.shuffle(redCards)
random.shuffle(yellowCards)
random.shuffle(blackCards)

fullDeck = redCards + yellowCards + blackCards
random.shuffle(fullDeck)
print("")
print("The deck has been shuffled")
print("")
#Runs for 15 rounds. 

#print(playerOneHand)
    #playerOneHand.append(fullDeck[0])
    #fullDeck.pop(0)
    #print(playerOneHand)
    #print(fullDeck)
    #print("Done")


import math

playerOneHand = []
playerTwoHand = []
roundNumber = 1
print(fullDeck)
while len(fullDeck) > 0 and roundNumber != 16:
    print("")
    print("Round",roundNumber)
    print("-----------------------------------------------------------------------------------------------")
    roundNumber = roundNumber + 1
    playerOneCardTakenRealNumber = fullDeck[0]
    playerTwoCardTakenRealNumber = fullDeck[1]
    playerOneCardTaken = math.trunc(playerOneCardTakenRealNumber)
    playerTwoCardTaken = math.trunc(playerTwoCardTakenRealNumber)
    print("Player 1 got a",playerOneCardTaken)
    print("Player 1 got a",playerTwoCardTaken)
    print("")
    stringPlayerOneCardTakenRealNumber = str(playerOneCardTakenRealNumber)
    stringPlayerTwoCardTakenRealNumber = str(playerTwoCardTakenRealNumber)
    if stringPlayerOneCardTakenRealNumber.endswith("1") or stringPlayerTwoCardTakenRealNumber.endswith("1") == True:
        print("True")
    else:
        print("False")
    print("Test")
    test = str(playerOneCardTakenRealNumber)
    print(test)
    
    
    
    

    
    
    
  
    


        
        
    
    
    
