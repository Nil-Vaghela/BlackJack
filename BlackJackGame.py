#BlackJackGame
import random
#Get cards and shuffle them
Cards = ["A",2,3,4,5,6,7,8,9,10,'J',"Q","K"]
random.shuffle(Cards)

#Give Card to Dealer And User

def GiveCards():
    DealersCard = []
    UsersCard = []
    count = 2

    while count != 0:
        randomNumber = random.randint(0,12)
        UsersCard.append(Cards[randomNumber])
        randomNumber = random.randint(0,12)
        DealersCard.append(Cards[randomNumber])
        
        count -= 1

    print(f"Dealer Has {DealersCard[0]}")
    print(f"You have {UsersCard}")
    
    return UsersCard,DealersCard

#if It has A change to 1 or 11
def ChangeA(UserCard,DealersCard):
    for i in range(len(UserCard)):
        if UserCard[i] == 'A':
            UserInputForA = int(input("You have A in your card Will you like to convert it into 11 or 1 ?"))
            UserCard[i] = UserInputForA
    for i in range(len(DealersCard)):
        if DealersCard[i] == 'J' or DealersCard[i] == "Q" or DealersCard[i] == "K":
            DealersCard[i] = 10
        if DealersCard[i] == "A":
            if i == 0:
                if DealersCard[i+1]== "A":
                    DealersCard[i] = 11
                elif DealersCard[i+1] < 8:
                   DealersCard[i] = 11
                else:
                    DealersCard[i] == 1
            elif i == 1:
                if DealersCard[i-1] < 8:
                   DealersCard[i] = 11
                else:
                    DealersCard[i] = 1

    return UserCard, DealersCard



def AskforCard(UserCard,DealersCard):
    AskUser = input("Do you Want card ? : Y or N ")
    UpdatedUserCard = []
    UpdatedDealerCard = []
    SumOfDealerNumber = 0
    for i in DealersCard:
        UpdatedDealerCard.append(i)
    for i in UserCard:
            UpdatedUserCard.append(i)
    while AskUser == "y":
        randomNumber = random.randint(0,12)       
        
        UpdatedUserCard.append(Cards[randomNumber])
        print(UpdatedUserCard)
        ChangeA(UpdatedUserCard,UpdatedDealerCard)
        AskUser = input("Do you Want card ? : Y or N ")
    
    
    for i in UpdatedDealerCard:
        SumOfDealerNumber = SumOfDealerNumber + i
    while SumOfDealerNumber < 17:
        randomNumber = random.randint(0,12)
        if Cards[randomNumber] == "A":
            UpdatedDealerCard.append(1)
        UpdatedDealerCard.append(Cards[randomNumber])
        ChangeA(UpdatedUserCard,UpdatedDealerCard)
        SumOfDealerNumber = 0
        for i in UpdatedDealerCard:
            SumOfDealerNumber = SumOfDealerNumber + i
    for i in range(len(UpdatedUserCard)):
        if UpdatedUserCard[i] == 'J' or UpdatedUserCard[i] == "Q" or UpdatedUserCard[i] == "K":
            UpdatedUserCard[i] = 10
    

    return UpdatedUserCard,UpdatedDealerCard,SumOfDealerNumber

def Result(Usercards,DealerCards,DealerSum):
    Usercardssum = 0
    for i in Usercards:
        Usercardssum = Usercardssum + i
    if Usercardssum > 21:
        print("User Loose",Usercards,DealerCards)
    elif DealerSum > 21:
        print("UserWin",Usercards,DealerCards)
    elif (21-Usercardssum) < (21-DealerSum):
        print("UserWin",Usercards,DealerCards)

    else:
        print("DealerWin",Usercards,DealerCards )


CardGiven = GiveCards()  
Changefunction = ChangeA(UserCard=CardGiven[0],DealersCard=CardGiven[1])
GetFinalCard =AskforCard(UserCard=Changefunction[0],DealersCard=Changefunction[1])

FinalResult = Result(Usercards=GetFinalCard[0],DealerCards=GetFinalCard[1],DealerSum=GetFinalCard[2])