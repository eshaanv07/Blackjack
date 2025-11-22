import random

suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks=['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck=[(rank, suit) for suit in suits for rank in ranks]

random.shuffle(deck)

def value(hand):
    total = 0
    aces = 0

    for card in hand:
        rank=card[0]
        if rank in ['Jack', 'Queen', 'King']:
            total+=10
        elif rank == 'Ace':
            aces+=1
            total+=11
        else:
            total+=int(rank)

    while total > 21 and aces > 0:
        total-=10
        aces-=1
    return total


player_cards=[deck.pop(),deck.pop()]
dealer_cards=[deck.pop(),deck.pop()]

while True:
    player_score=value(player_cards)
    dealer_score=value(dealer_cards)

    print("Player Cards:",player_cards)
    print("Player Score:",player_score)
    print()

    if player_score > 21:
        print("Player LOSES! Dealer WINS!!.")
        exit()

    choice = input('Hit or Stand? ("h" for hit, "s" for stand): ').lower()

    if choice == "h":
        player_cards.append(deck.pop())
    elif choice == "s":
        break
    else:
        print("Invalid choice. Choose again.")

print("\nDealer reveals:")
print("Dealer Cards:",dealer_cards)
print("Dealer Score:",dealer_score)
print()

while value(dealer_cards) < 17:
    new = deck.pop()
    dealer_cards.append(new)
    print("Dealer draws:",new)
    print("Dealer Cards:",dealer_cards)
    print("Dealer Score:",value(dealer_cards))
    print()

    if value(dealer_cards) > 21:
        dealer_score = value(dealer_cards)
        player_score = value(player_cards)
        print("\nFINAL RESULTS")
        print("Player Cards:",player_cards)
        print("Player Score:",player_score)
        print("Dealer Cards:",dealer_cards)
        print("Dealer Score:",dealer_score)
        print()
        print("Dealer busts! Player WINS!.")
        exit()

dealer_score=value(dealer_cards)
player_score=value(player_cards)

print("\nFINAL RESULTS")
print("Player Cards:",player_cards)
print("Player Score:",player_score)
print("Dealer Cards:",dealer_cards)
print("Dealer Score:",dealer_score)
print()

if dealer_score > 21:
    print("Dealer busts! Player WINS!.")
elif player_score > dealer_score:
    print("Player WINS!")
elif dealer_score > player_score:
    print("Dealer WINS!")
else:
    print("It's a tie (Push).")
