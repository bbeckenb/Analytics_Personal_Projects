# seed the pseudorandom number generator
from BlackJack_Function_Def import *

while Game_Control == 'play':
#re-initializes Variables
    Player1_Hand = []
    Player1_Count = 0
    Dealer_Hand = []
    Dealer_Count = 0
    Reason = ''
    End_Game_Flag = 0
    i = 0
    P1_Input = 'w'
#Shuffles Deck before game play
    Shuffle_Deck = Shuffle(Card_Deck)
#Deals 2 cards to Human Player and Dealer then gets an initial count for each
    Deal(2, Player1_Hand, Shuffle_Deck)
    Deal(2, Dealer_Hand, Shuffle_Deck)
    Player1_Count = Hand_Count(Player1_Hand)
    Dealer_Count = Hand_Count(Dealer_Hand)
#Checks for player to pass/ end hit routine and whether or not they 'bust'/ exceed a hand count of 21
#Accounts for player input error
    while P1_Input != 'p' and End_Game_Flag == 0:
        P1_Input = input(f"Current Hand: {Player1_Hand}\n Current Count: {Player1_Count}\n h or p?: ")
        if P1_Input == 'h':
            Deal(1, Player1_Hand, Shuffle_Deck)
            Player1_Count = Hand_Count(Player1_Hand)
        elif P1_Input == 'p':
            break
        else:
            while P1_Input != 'h' and P1_Input != 'p':
                P1_Input = input(f"Wrong Input! Current Hand: {Player1_Hand}\n Current Count: {Player1_Count}\n h or p?: ")
                if P1_Input == 'h':
                    Deal(1, Player1_Hand, Shuffle_Deck)
                    Player1_Count = Hand_Count(Player1_Hand)
                elif P1_Input == 'p':
                    break
                else:
                    pass
        if Player1_Count > 21:
            Reason = 'You Busted!'
            End_Game_Flag = 1
            break
        else:
            pass
#Performs Dealer action automation, ensures dealer hits if their count is less than the player count or 17
#Only enters this routine if the human player has not busted, tie goes to dealer
    if End_Game_Flag == 0:
        while Dealer_Count < Player1_Count:
            Deal(1, Dealer_Hand, Shuffle_Deck)
            Dealer_Count = Hand_Count(Dealer_Hand)
        if Dealer_Count > 21:
            Reason = "Dealer Busted, You Won!"
        elif Dealer_Count >= Player1_Count:
            Reason = "Dealer Scored Higher Than You!"
        else:
            Reason = "You Won!"
    else:
        pass
#End of round routine, displays outcome, hands, hand counts, then asks if player wants to play again
#Accounts for player input error
    while P1_Input != ('y' or 'n'):
        P1_Input = input(f"{Reason}\n, you had {Player1_Count}\n with {Player1_Hand}\n the Dealer had {Dealer_Count}\n with {Dealer_Hand}\n, Play Again? y or n?")
        if P1_Input == 'y':
            break
        elif P1_Input == 'n':
            Game_Control = 'Terminate'
            break
        else:
            while P1_Input != ('y' or 'n'):
                P1_Input = input("Wrong Input! Play Again? y or n?")
                if P1_Input == 'y':
                    break
                elif P1_Input == 'n':
                    Game_Control = 'Terminate'
                    break
            break
