import cards  # 'cards', here, is in reference to the name of the file, 'cards.py'

# you could also do: `from cards import Card, Deck`
# this would allow you to call the Card and Deck classes directly, instead of having
# to do `cards.Card()` or `cards.Deck()`

# the Deck class can be thought of as a list of Card classes. to start out, however,
# we'll take a look at a Card class instance

c = cards.Card(1, 4)

# the Card constructor takes two optional parameters:
#                 Card(rank=0, suit=0)
# `rank` is an int (1-13), where aces are 1 and kings are 13 
# (Enumeration: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
#               1  2  3  4  5  6  7  8  9  10  11 12 13
# `suit` is an int (1-4), where 1 is clubs, 2 is diamonds, 3 is hearts, and 4 is spades.

# so, we can deduce that the initialization we're creating above is an ace of spades. 

print(c)  

# when unicode characters aren't available, (e.g. the club, diamond, heart and spade symbols), the
# class will use 'c', 'd', 'h', and 's' to represent the different suits respectively (you'll see
# this happen on Mimir).

print(c.rank())  # you can call the .rank() method to find a Card instance's rank
print(c.suit())  # and the .suit() method to find a Card instance's suit

# both return ints, where the mapping of each is as shown in the constructor description above

# so, you can check for a particular card rank like this:
if c.rank() == 1:
    print('The card is an ace!')
else:
    print('The card is not an ace!')

c2 = cards.Card(1, 4)  # if I make another ace of spades...

print(c == c2)  # you can see if two cards have the same rank and suit using the `==` operator
