'''
                            HOW I NOTATE THINGS
                            ===================

A "->" represents a variable changing its value on a subsequent iteration. Example:

# i: 0 -> 1 -> 2 -> 3 -> 4
for i in range(5):
    print(i)

On first iteration, i will hold 0, then 1 on next iteration, then 2 on next iteration, etc.

A "..." represents a variate amount of implied values that would be too cumbersome to fit
into a single-line comment. Example:

# i: 0 -> 1 -> 2 -> ... -> 98 -> 99
for i in range(100):
    print(i)

There are too many numbers to list here. Given the pattern of the iteration, you should be
able to deduce what would follow 2, and come before 98.
'''

#########################################################################################
                    ### ITERATING THROUGH A SUB-DICTIONARY ###
#########################################################################################

subD = {
    'Western Europe': {
        'Switzerland': ((1, 7.587), (1.39651, 0.41978), (1.34951, 0.94143, 0.66557)), 
        'Iceland': ((2, 7.561), (1.30232, 0.14145), (1.40223, 0.94784, 0.62877)), 
        'Denmark': ((3, 7.527), (1.32548, 0.48357), (1.36058, 0.87464, 0.64938)), 
        'Norway': ((4, 7.522), (1.459, 0.36503), (1.33095, 0.88521, 0.66973)), 
        'Finland': ((6, 7.406), (1.29025, 0.41372), (1.31826, 0.88911, 0.64169)), 
        'Netherlands': ((7, 7.378), (1.32944, 0.31814), (1.28017, 0.89284, 0.61576)), 
        'Sweden': ((8, 7.364), (1.33171, 0.43844), (1.28907, 0.91087, 0.6598)), 
        'France': ((29, 6.575), (1.27778, 0.20646), (1.26038, 0.94579, 0.55011))
    }, 
    'North America': {
        'Canada': ((5, 7.427), (1.32629, 0.32957), (1.32261, 0.90563, 0.63297)), 
        'United States': ((15, 7.119), (1.39451, 0.1589), (1.24711, 0.86179, 0.54604))
    }, 
    'Latin America and Caribbean': {
        'Costa Rica': ((12, 7.226), (0.95578, 0.10583), (1.23788, 0.86027, 0.63376)), 
        'Mexico': ((14, 7.187), (1.02054, 0.21312), (0.91451, 0.81444, 0.48181)), 
        'Brazil': ((16, 6.983), (0.98124, 0.17521), (1.23287, 0.69702, 0.49049)), 
        'Venezuela': ((23, 6.81), (1.04424, 0.11069), (1.25596, 0.72052, 0.42908)), 
        'Panama': ((25, 6.786), (1.06353, 0.0927), (1.1985, 0.79661, 0.5421)), 
        'Chile': ((27, 6.67), (1.10715, 0.12869), (1.12447, 0.85857, 0.44132)), 
        'Argentina': ((30, 6.574), (1.05351, 0.08484), (1.24823, 0.78723, 0.44974)), 
        'Uruguay': ((32, 6.485), (1.06166, 0.24558), (1.2089, 0.8116, 0.60362)), 
        'Colombia': ((33, 6.477), (0.91861, 0.0512), (1.24018, 0.69077, 0.53466))
    }
}

# every region, every country in each region, and every tuple for each country

header = "ITERATING THROUGH A SUB-DICTIONARY"
print(header)
print('-' * len(header))

# region: 'Western Europe' -> 'North America' -> 'Latin America and Caribbean'
# country_dict: {'Switzerland': ((...), (...), (...)), ...} -> {'Canada': ((...), (...), (...)), ...} -> {'Costa Rica': ((...), (...), (...)), ...}
for region, country_dict in subD.items():

    # country: 'Switzerland' -> ... -> 'Canada' -> ... 'Costa Rica' -> ...
    # data: (switzerland's data) -> ... -> (canada's data) -> ... -> (costa rica's data) -> ...
    for country, data in country_dict.items():
        
        print("{:<29}{:<15}{:<}".format(region, country, str(data)))

        # data: ((happiness_rank, happiness_score), (economy, trust), (family, health, freedom))
        happiness_rank = data[0][0]   # 0th nested tuple, 0th item
        happiness_score = data[0][1]  # 0th nested tuple, 1st item
        economy = data[1][0]          # 1st nested tuple, 0th item
        trust = data[1][1]            # 1st nested tuple, 1st item
        family = data[2][0]           # 2nd nested tuple, 0th item
        health = data[2][1]           # 2nd nested tuple, 1st item
        freedom = data[2][2]          # 2nd nested tuple, 2nd item

print()

#########################################################################################
                    ### ITERATING THROUGH A SUPER-DICTIONARY ###
#########################################################################################

superD = {
    2015: {
        'Western Europe': {
            'Switzerland': ((1, 7.587), (1.39651, 0.41978), (1.34951, 0.94143, 0.66557)), 
            'Iceland': ((2, 7.561), (1.30232, 0.14145), (1.40223, 0.94784, 0.62877)), 
            'Denmark': ((3, 7.527), (1.32548, 0.48357), (1.36058, 0.87464, 0.64938)), 
            'Norway': ((4, 7.522), (1.459, 0.36503), (1.33095, 0.88521, 0.66973)), 
            'Finland': ((6, 7.406), (1.29025, 0.41372), (1.31826, 0.88911, 0.64169)), 
            'Netherlands': ((7, 7.378), (1.32944, 0.31814), (1.28017, 0.89284, 0.61576)), 
            'Sweden': ((8, 7.364), (1.33171, 0.43844), (1.28907, 0.91087, 0.6598)), 
            'France': ((29, 6.575), (1.27778, 0.20646), (1.26038, 0.94579, 0.55011))
        }, 
        'North America': {
            'Canada': ((5, 7.427), (1.32629, 0.32957), (1.32261, 0.90563, 0.63297)), 
            'United States': ((15, 7.119), (1.39451, 0.1589), (1.24711, 0.86179, 0.54604))
        }, 
        'Latin America and Caribbean': {
            'Costa Rica': ((12, 7.226), (0.95578, 0.10583), (1.23788, 0.86027, 0.63376)), 
            'Mexico': ((14, 7.187), (1.02054, 0.21312), (0.91451, 0.81444, 0.48181)), 
            'Brazil': ((16, 6.983), (0.98124, 0.17521), (1.23287, 0.69702, 0.49049)), 
            'Venezuela': ((23, 6.81), (1.04424, 0.11069), (1.25596, 0.72052, 0.42908)), 
            'Panama': ((25, 6.786), (1.06353, 0.0927), (1.1985, 0.79661, 0.5421)), 
            'Chile': ((27, 6.67), (1.10715, 0.12869), (1.12447, 0.85857, 0.44132)), 
            'Argentina': ((30, 6.574), (1.05351, 0.08484), (1.24823, 0.78723, 0.44974)), 
            'Uruguay': ((32, 6.485), (1.06166, 0.24558), (1.2089, 0.8116, 0.60362)), 
            'Colombia': ((33, 6.477), (0.91861, 0.0512), (1.24018, 0.69077, 0.53466))
        }
    }, 
    2016: {
        'Western Europe': {
            'Denmark': ((1, 7.526), (7.592, 0.57941), (1.44178, 1.16374, 0.79504)), 
            'Switzerland': ((2, 7.509), (7.59, 0.58557), (1.52733, 1.14524, 0.86303)), 
            'Iceland': ((3, 7.501), (7.669, 0.56624), (1.42666, 1.18326, 0.86733)), 
            'Norway': ((4, 7.498), (7.575, 0.59609), (1.57744, 1.1269, 0.79579)), 
            'Finland': ((5, 7.413), (7.475, 0.57104), (1.40598, 1.13464, 0.81091)), 
            'Netherlands': ((7, 7.339), (7.394, 0.55211), (1.46468, 1.02912, 0.81231)), 
            'Sweden': ((10, 7.291), (7.355, 0.58218), (1.45181, 1.08764, 0.83121)), 
            'France': ((32, 6.478), (6.559, 0.46562), (1.39488, 1.00508, 0.83795))
        }, 
        'North America': {
            'Canada': ((6, 7.404), (7.473, 0.5737), (1.44015, 1.0961, 0.8276)), 
            'United States': ((13, 7.104), (7.188, 0.48163), (1.50796, 1.04782, 0.779))
        }, 
        'Latin America and Caribbean': {
            'Costa Rica': ((14, 7.087), (7.175, 0.55225), (1.06879, 1.02152, 0.76146)), 
            'Brazil': ((17, 6.952), (7.029, 0.40425), (1.08754, 1.03938, 0.61415)), 
            'Mexico': ((21, 6.778), (6.876, 0.37709), (1.11508, 0.7146, 0.71143)), 
            'Chile': ((24, 6.705), (6.795, 0.37789), (1.2167, 0.90587, 0.81883)), 
            'Panama': ((25, 6.701), (6.801, 0.48927), (1.18306, 0.98912, 0.70835)), 
            'Argentina': ((26, 6.65), (6.74, 0.42284), (1.15137, 1.06612, 0.69711)), 
            'Uruguay': ((29, 6.545), (6.634, 0.54388), (1.18157, 1.03143, 0.72183)), 
            'Colombia': ((31, 6.481), (6.578, 0.44735), (1.03032, 1.02169, 0.59659)), 
            'Venezuela': ((44, 6.084), (6.195, 0.19847), (1.13367, 1.03302, 0.61904))
        }
    }
}

# every year, every region for each year, every country in each region, and every tuple for each country

# the sub-dictionaries are assigned as values to particular years. it's the same thing, but nested one
# layer deeper to go through every year

header = "ITERATING THROUGH A SUPER-DICTIONARY"
print(header)
print('-' * len(header))

# year: 2015 -> 2016
# subD: {'Western Europe': {...}, 'North America': {...}, 'Latin America and Caribbean': {...}}
for year, subD in superD.items():

    # region: 'Western Europe' -> 'North America' -> 'Latin America and Caribbean'
    # country_dict: {'Switzerland': ((...), (...), (...)), ...} -> {'Canada': ((...), (...), (...)), ...} -> {'Costa Rica': ((...), (...), (...)), ...}
    for region, country_dict in subD.items():

        # country: 'Switzerland' -> ... -> 'Canada' -> ... 'Costa Rica' -> ...
        # data: (switzerland's data) -> ... -> (canada's data) -> ... -> (costa rica's data) -> ...
        for country, data in country_dict.items():
            
            print("{:<6}{:<29}{:<15}{:<}".format(str(year), region, country, str(data)))

            # data: ((happiness_rank, happiness_score), (economy, trust), (family, health, freedom))
            happiness_rank = data[0][0]   # 0th nested tuple, 0th item
            happiness_score = data[0][1]  # 0th nested tuple, 1st item
            economy = data[1][0]          # 1st nested tuple, 0th item
            trust = data[1][1]            # 1st nested tuple, 1st item
            family = data[2][0]           # 2nd nested tuple, 0th item
            health = data[2][1]           # 2nd nested tuple, 1st item
            freedom = data[2][2]          # 2nd nested tuple, 2nd item
