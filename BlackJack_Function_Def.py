from random import seed
from random import randint

# define cards
Card_Deck = ['two of hearts', 'two of clubs', 'two of diamonds', 'two of spades',
'three of hearts', 'three of clubs', 'three of diamonds', 'three of spades',
'four of hearts', 'four of clubs', 'four of diamonds', 'four of spades',
'five of hearts', 'five of clubs', 'five of diamonds', 'five of spades',
'six of hearts', 'six of clubs', 'six of diamonds', 'six of spades',
'seven of hearts', 'seven of clubs', 'seven of diamonds', 'seven of spades',
'eight of hearts', 'eight of clubs', 'eight of diamonds', 'eight of spades',
'nine of hearts', 'nine of clubs', 'nine of diamonds', 'nine of spades',
'ten of hearts', 'ten of clubs', 'ten of diamonds', 'ten of spades',
'jack of hearts', 'jack of clubs', 'jack of diamonds', 'jack of spades',
'queen of hearts', 'queen of clubs', 'queen of diamonds', 'queen of spades',
'king of hearts', 'king of clubs', 'king of diamonds', 'king of spades',
'Ace of hearts', 'Ace of clubs', 'Ace of diamonds', 'Ace of spades']

# define global variables
Shuffle_Deck = []
Player1_Hand = []
Player1_Count = 0
Dealer_Hand = []
Dealer_Count = 0
i = 0
P1_Input = 'w'
End_Game_Flag = 0
Game_Control = 'play'

def Shuffle(cards):
    "Creates a temporary array of integer 0s, equal to the length of the input array, randomly fills the Temporary array with elements from the inputted array as long as it finds an integer zero in a spot"
    x = y = len(cards) - 1
    Temp_Array = []

    while x >= 0:
        Temp_Array.append(0)
        x -= 1

    x = y
    while x >= 0:
        z = randint(0, y)
        if Temp_Array[z] == 0:
            Temp_Array[z] = cards[x]
            x -= 1
        else:
            while Temp_Array[z] != 0:
                z = randint(0, y)
            Temp_Array[z] = cards[x]
            x -= 1
    return Temp_Array

def Deal(x, hand, Shuffle_Deck_Pass):
    "deals x number of cards from the stack to a chosen hand"
    while x > 0:
        L = len(Shuffle_Deck_Pass)
        hand.append(Shuffle_Deck_Pass[L-1])
        Shuffle_Deck_Pass.pop(L-1)
        x -= 1
    return hand, Shuffle_Deck_Pass

def Hand_Count(hand):
    "counts points for player hands"
    x = L = len(hand) - 1
    Ace_Count = count = 0
    while L >= 0:
        if 'two' in hand[L]:
            count += 2
        elif 'three' in hand[L]:
            count += 3
        elif 'four' in hand[L]:
            count += 4
        elif 'five' in hand[L]:
            count += 5
        elif 'six' in hand[L]:
            count += 6
        elif 'seven' in hand[L]:
            count += 7
        elif 'eight' in hand[L]:
            count += 8
        elif 'nine' in hand[L]:
            count += 9
        elif 'ten' in hand[L]:
            count += 10
        elif 'jack' in hand[L]:
            count += 10
        elif 'queen' in hand[L]:
            count += 10
        elif 'king' in hand[L]:
            count += 10
        elif 'Ace' in hand[L]:
            Ace_Count += 1
        L -= 1

    if Ace_Count > 0:
        Eleven_Count = int((21 - count) / 11)
        if (Eleven_Count > 0 and (count + 11 + Ace_Count - 1) <= 21):
            count += 11
            Ace_Count -= 1
            count += Ace_Count
        else:
            count += Ace_Count

    return count

'''def Start_Game():
    "Initializes or re-initializes all global variables, deals 2 random cards to P1 and Dealer"
    Shuffle_Deck = []
    Player1_Hand = []
    Player1_Count = 0
    Dealer_Hand = []
    Dealer_Count = 0
    Deck_Holder = []
    i = 0
    P1_Input = 'w'
    Game_Control = 'play'
    return'''

'''def Restart_Game(event):
    P1_Input = input(f"{event}\n, you had {Player1_Count}\n the Dealer had {Dealer_Count}\n with {Dealer_Hand}\n, Play Again? y or n?")
    if P1_Input == 'y':
        pass
    elif P1_Input == 'n':
        Game_Control = 'Terminate'
    return'''
