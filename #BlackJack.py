#BlackJack
import random

carddict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
def card_creation():
    card = random.choice(list(carddict))
    return card


def gameplay():
    balance = 2500
    print('Your balance is ${}'.format(balance))
    
    print("------------------")
    playerlst = []
    cpulst = []
    while True:

        while True:
            bet = int(input("Insert Bet amount: "))
            if bet > balance:
                print("Isufficient Credits.")
            else:
                break
         
        print("------------------")
        playercard1 = card_creation()
        playercard2 = card_creation()
        cpucard1 = card_creation()
        cpucard2 = card_creation()
        firststandp = carddict[playercard1] + carddict[playercard2]
        if firststandp > 21:
            print("Bust!")
            for num in playerlst:
                print("You have a {}.".format(num))
            balance -= bet 
            print("New Balance is ${}".format(balance))
        if firststandp == 21:
            print("You win!")
            balance += bet 
            print("New Balance is ${}".format(balance))
            continue
        playerlst.append(carddict[playercard1])
        playerlst.append(carddict[playercard2])
        firststandc = carddict[cpucard1] + carddict[cpucard2]
        cpulst.append(carddict[cpucard1])
        cpulst.append(carddict[cpucard2])

        while True:
            for num in playerlst:
                print("You have a {}.".format(num))
            print("({})".format(firststandp))
            print("------------------")
            print("Dealer has a {}.".format(cpulst[0]))
    
            print("------------------")
            hit_or_stand = input("Hit or Stand? ") 
            print("------------------")
            hit_or_stand = hit_or_stand.lower()
            while firststandc < 17:
                cpulst.append(card_creation())
                firststandc += carddict[cpulst[-1]]

            if hit_or_stand == 'hit':
                newcard = card_creation()
                playerlst.append(newcard)
                firststandp += carddict[newcard]    
                #print(playerlst)
                #print(firststandp)
                if firststandp > 21:
                    print("Bust!")
                    balance -= bet 
                    print("New Balance is ${}".format(balance))
                    break
                if firststandp == 21:
                    print("You win!")
                    for num in playerlst:
                        print("You have a {}.".format(num))
                    balance += bet 
                    print("New Balance is ${}".format(balance))
                    break
               

            if hit_or_stand == 'stand':
                break



        newcpulst = []
        for num in cpulst:
            newcpulst.append(str(num))
        cpunumbers = ', '.join(newcpulst)
        
            

        if hit_or_stand == 'stand':
            if firststandp <= 21 and firststandc < firststandp:
                print("You win! The dealers cards were " + cpunumbers)
                
                balance += bet 
                print("New Balance is ${}".format(balance))
            elif firststandp <= 21 and firststandc > 21:
                print("You win! The dealers cards were " + cpunumbers)
                
                balance += bet 
                print("New Balance is ${}".format(balance))
            elif firststandp == firststandc:
                print("Push! The dealers cards were " + cpunumbers)
                
            else:
                print("You Lose! The dealers cards were " + cpunumbers)
                
                balance -= bet 
                print("New Balance is ${}".format(balance))


   
        playagain = input("Play again? ").lower()
        print("------------------")
        if playagain == 'no':
            break
        elif playagain == 'yes':
            playerlst.clear()
            cpulst.clear()
        else:
            print("Not an option!")
        


ask = input("Welcome to Blackjack! Would you like to get started? \n")
if (ask.lower() == "yes"):
    gameplay()
    

