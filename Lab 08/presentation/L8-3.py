from operator import itemgetter

populations = {
    "Houston": 2325502,
    "New York": 8398748,
    "Chicago": 2705994,
    "Los Angeles": 3990456,
    "Pheonix": 1660272,
    "Grand Rapids": 200217,    # Best city in Michigan, fight me
    "Detroit": 672662
}

keys = list(populations.keys())
values = list(populations.values())

li_tup = list(populations.items())

# We've been working with lists of tuples/lists
# for a while, and so we can just apply what we've
# learned about sorting them to .items() since
# .items() gives you a list of tuples

sorted_dict = sorted(populations.items())

sorted_dict = sorted(populations.items(), key=itemgetter(1), reverse=True)
# Equivalent way of doing this^ in raw Python:
# sorted_dict = sorted(populations.items(), key=lambda tup: tup[1], reverse=True)

# Remember that we can cast a list of tuples back into a
# dictionary with the dict() cast function

populations = dict(sorted_dict)