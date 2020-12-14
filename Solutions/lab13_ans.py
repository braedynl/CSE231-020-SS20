'''
CSE231 - Introduction to Programming I
Lab 13
Example Solution

Author: Braedyn Lettinga
'''

class PetError(ValueError):
    pass

class Pet:
    
    # here, we're creating a parent class, "Pet",
    # to inherit from later.

    def __init__(self, species:str=None, name:str=''):

        # we only accept a certain set of species names
        ACCEPTABLE = ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']
        
        # if species isn't its default of None, and the species
        # name is one of the acceptable ones
        if species != None and species.lower() in ACCEPTABLE:
            self.species_str = species.title()  # we assign to our attributes
            self.name_str = name.title()
        else:
            raise PetError()  # ... and raise a custom "PetError" otherwise
            
    def __str__(self) -> str:

        # we consider an empty name_str "unnamed", since that's
        # the default to the constructor
        if self.name_str == '':
            return "Species of: {}, unnamed".format(self.species_str)
        
        # otherwise, if the name_str isn't empty, we return a string
        # that contains its name
        return "Species of: {}, named {}".format(self.species_str, self.name_str)        

class Dog(Pet):  # Dog child class to the Pet parent class

    def __init__(self, name:str='', chases:str='Cats'):
        
        # unbound call to the Pet constructor. We pass
        # species='Dog' and name=name. The Dog's constructor
        # is sort of like a layer on top of the Pet constructor
        Pet.__init__(self, "Dog", name)

        # we also create a new attribute, unique to the Dog class,
        # "chases", which is something that the Dog instance chases
        self.chases = chases

    def __str__(self) -> str:

        # similar to the Pet class, a name_str that's empty is considered unnamed.
        # we also use "Dog" in the place of the species, since a Dog instance will
        # ALWAYS be a species of "Dog" 
        if self.name_str == '':
            return "Species of: Dog, unnamed, chases {}".format(self.chases)
        return "Species of: Dog, named {}, chases {}".format(self.name_str, self.chases)

class Cat(Pet):  # Cat child class to the Pet parent class

    # near-identical to the Dog class, with some swaps here and there

    def __init__(self, name:str='', hates:str='Dogs'):
        Pet.__init__(self, "Cat", name)
        self.hates = hates
    
    def __str__(self) -> str:
        if self.name_str == '':
            return "Species of: Cat, unnamed, hates {}".format(self.hates)
        return "Species of: Cat, named {}, hates {}".format(self.name_str, self.hates)


# Testing our classes

try:
    # Pet with species="hamster", name='' (default)
    A = Pet( "hamster" )
    print( A )
            
    # Dog named Fido who chases Cats
    B = Dog( "Fido" )
    print( B )

    # Cat named Fluffy who hates everything
    C = Cat( "Fluffy", "everything" )
    print( C )

    # we expect a PetError here, since "pig"
    # is not within the acceptable species list
    D = Pet( "pig" )
    print( D )
    
except PetError:
    print( "Got a pet error." )