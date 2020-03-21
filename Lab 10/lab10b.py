# Lab10b - Example Answer (Undocumented)
# Braedyn Lettinga

import cards

# Create the deck of cards
the_deck = cards.Deck()

hand1 = []
hand2 = []

def battle(hand1_list:list, hand2_list:list):
    top1 = hand1_list.pop(0)
    top2 = hand2_list.pop(0)

    if top1.rank() == 1 and top2.rank() <= 13:
        won = 1
    elif top2.rank() == 1 and top1.rank() <= 13:
        won = 2

    elif top1.rank() > top2.rank():
        won = 1
    elif top2.rank() > top1.rank():
        won = 2

    print("Battle was 1: {}, 2: {}. Player {} wins battle.".format(top1, top2, won))
    
    if won == 1:
        hand1_list.extend( [top1, top2] )
    else:
        hand2_list.extend( [top2, top1] )


def main():
    for _ in range(5):
        hand1.append(the_deck.deal())
        hand2.append(the_deck.deal())

    print("Starting Hands")
    print("Hand1:", hand1)
    print("Hand2:", hand2)
    print()

    while True:
        battle(hand1, hand2)

        print("hand1:", hand1)
        print("hand2:", hand2)

        if hand1 == []:
            print("Player 2 wins!!!")
            break   
        elif hand2 == []:
            print("Player 1 wins!!!")
            break
        
        prompt = input("Keep Going: (Nn) to stop:").lower()
        if prompt == "y":
            continue
        else:
            if len(hand1) > len(hand2):
                print("Player 1 wins!!!")
            elif len(hand2) > len(hand1):
                print("Player 2 wins!!!")
            break

if __name__ == "__main__":
    main()