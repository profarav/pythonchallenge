import random
import os
import sys
import subprocess
print("This is a black jack game which is you against the dealer")

#This is the printing the firstcard and has all the arrays needed
suit = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
yourcards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
indexfirst = random.randint(0, len(yourcards) - 1)
firstcard = yourcards[indexfirst]
yourcards.pop(indexfirst)
totalamount = firstcard
print(str(firstcard) + str(suit[indexfirst]), "is your first card")
#TESTING CODE print ("printing yourcard remove first card size of deck:",len(yourcards))
#TESTING CODE print ("printing yourcard after removing fist card:",yourcards)

#This is where the dealers deck will be created
dealercards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dealersuit = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
indexdealerfirst = random.randint(0, len(dealercards) - 1)
firstdealer = dealercards[indexdealerfirst]
dealercards.pop(indexdealerfirst)
#This is the second card through fifth card code
indexdealersecond = random.randint(0, len(dealercards) - 1)
seconddealer = dealercards[indexdealersecond]
dealercards.pop(indexdealersecond)
if firstdealer + seconddealer > 15:
    dealeramount = firstdealer + seconddealer
else:
    indexdealerthird = random.randint(0, len(dealercards) - 1)
    thirddealer = dealercards[indexdealerthird]
    dealercards.pop(indexdealerthird)
    if firstdealer + seconddealer + thirddealer > 14:
        dealeramount = firstdealer + seconddealer + thirddealer
    else:
        indexdealerfour = random.randint(0, len(dealercards) - 1)
        fourdealer = dealercards[indexdealerfour]
        dealercards.pop(indexdealerfour)
        if firstdealer + seconddealer + thirddealer + fourdealer > 12:
            dealeramount = firstdealer + seconddealer + thirddealer + fourdealer
        else:
            indexdealerfive = random.randint(0, len(dealercards) - 1)
            fivedealer = dealercards[indexdealerfive]
            dealercards.pop(indexdealerfive)
            if firstdealer + seconddealer + thirddealer + fourdealer + fivedealer < 21:
                dealeramount = firstdealer + seconddealer + thirddealer + fourdealer + fivedealer
            

    #This is where my hitstandendcode works
while True:
    hitstandend = input("Would you like to hit, stand, or, end the game?:").lower()
    if hitstandend == 'hit':
        indexsecond = random.randint(0, len(yourcards) - 1)
        secondcard = yourcards[indexsecond]
        yourcards.pop(indexsecond)
        totalamount = firstcard + secondcard
        #TESTING CODE print ("printing yourcard remove second card size of deck:",len(yourcards))
        #TESTING CODE print ("printing yourcard remove second card:",yourcards)
        print(str(firstcard) + str(suit[indexfirst]), "is your first card")
        print(str(secondcard) + str(suit[indexsecond]), "is your second card")
        if firstcard + secondcard > 21:
            print("Uh Oh! Your cards add up to a total above 21. You have lost.")
            break
        else:
            hitstandend = input("Would you like to hit, stand, or, end the game?:").lower()
            if hitstandend == 'hit':
                indexthird = random.randint(0, len(yourcards) - 1)
                thirdcard = yourcards[indexthird]
                yourcards.pop(indexthird)
                totalamount = firstcard + secondcard + thirdcard
                #TESTING CODE print ("printing yourcard remove second card size of deck:",len(yourcards))
                #TESTING CODE print ("printing yourcard remove second card:",yourcards)
                print(str(firstcard) + str(suit[indexfirst]), "is your first card")
                print(str(secondcard) + str(suit[indexsecond]), "is your second card")
                print(str(thirdcard) + str(suit[indexthird]), "is your third card")
                if firstcard + secondcard + thirdcard > 21:
                    print("Uh Oh! Your cards add up to a total above 21. You have lost.")
                    break
                else:
                    hitstandend = input("Would you like to hit, stand, or, end the game?:").lower()
                    if hitstandend == 'hit':
                        indexfour = random.randint(0, len(yourcards) - 1)
                        fourcard = yourcards[indexfour]
                        yourcards.pop(indexfour)
                        totalamount = firstcard + secondcard + thirdcard + fourcard
                        #TESTING CODE print ("printing yourcard remove second card size of deck:",len(yourcards))
                        #TESTING CODE print ("printing yourcard remove second card:",yourcards)
                        print(str(firstcard) + str(suit[indexfirst]), "is your first card")
                        print(str(secondcard) + str(suit[indexsecond]), "is your second card")
                        print(str(thirdcard) + str(suit[indexthird]), "is your third card")
                        print(str(fourcard) + str(suit[indexfour]), "is your third card")
                        if firstcard + secondcard + thirdcard + fourcard > 21:
                            print("Uh Oh! Your cards add up to a total above 21. You have lost.")
                            break
                    elif hitstandend == 'end':
                        break
                    elif hitstandend == 'stand':
                        if dealeramount > 21:
                            print("Congrats you have won! Yay!!")
                            print(totalamount, dealeramount)
                            break
                        if totalamount > dealeramount and totalamount < 22:
                            print("Congrats you have won! Yay!!")
                            print(totalamount, dealeramount)
                            break
                        else:
                            print(totalamount, " your amount was < than the dealers amount", dealeramount, "Try again next time.")
                            break
            elif hitstandend == 'end':
                break
            elif hitstandend == 'stand':
                if dealeramount > 21:
                    print("Congrats you have won! Yay!!")
                    print(totalamount, dealeramount)
                    break
                if totalamount > dealeramount and totalamount < 22:
                    print("Congrats you have won! Yay!!")
                    print(totalamount, dealeramount)
                    break
                else:
                    print(totalamount, " your amount was < than the dealers amount", dealeramount, "Try again next time.")
                    break
    elif hitstandend == 'end':
        break
    elif hitstandend == 'stand':
        if dealeramount > 21:
            print("Congrats you have won! Yay!!")
            print(totalamount, dealeramount)
            break
        elif totalamount > dealeramount and totalamount < 22:
            print("Congrats you have won! Yay!!")
            print(totalamount, dealeramount)
            break
        else:
            print(totalamount, "was < than", dealeramount, "You lost!")
            break

#restart = input("Would you like to play again? Y/N").lower()
#if restart == 'y':
    #subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])
#else:
print("thanks for playing")



    
    
