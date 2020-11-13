import cards 

# as I said in the previous example, the Deck class is essentially
# a list of Card instances. 

# the Deck class has encoded features that are catered to
# how most real-world card games use decks. you cannot use list
# methods with the Deck class, but INTERNALLY think of the Deck class
# as using a list. 

d = cards.Deck()  # initialization

print(d)

# at first, the deck begins as an enumeration of ace to king in each
# suit. we can shuffle the deck using .shuffle()

d.shuffle()  # (in-place method)

print(d)  # this will scramble the order of cards, as you'd expect

# it can be a bit cumbersome to see all of the cards in one big line,
# so you can instead call the .display() method to view the deck in
# a table.  

d.display()

# we can take a single card from the deck using the .deal() method

c = d.deal()

print(c)  # remember that this is a Card class instance! (refer back to L10-1)
print(c.rank())
print(c.suit())

d.display()

# hopefully you can see that the .deal() method extracts the last card in 
# the deck (internally using the .pop() method!)

# lastly, we can use the len() function on a Deck instance, to check how
# many cards are present in the deck. 

# Since there is typically one of each card in a classic deck (52 cards),
# and we dealt one, we should see that our Deck's length is 51

print(len(d))

# we can check if a deck is empty using .is_empty(), the same as checking if len(d) == 0

print(d.is_empty())