# Lab11 - Example Answer (Documented)
# Braedyn Lettinga

class PetError( ValueError ):
    '''
    A custom error that inherits from ValueError
    '''
    pass

class Pet( object ):

    def __init__( self, species=None, name="" ):
        SPECIES = ["dog", "cat", "horse", "gerbil", "hamster", "ferret"]

        # If the species is one of ^ the following, then we accept
        # it as a Pet() object, else raise PetError
        if species in SPECIES:
            self.species_str = species.title()    # It gets a species attribute
            self.name_str = name.title()    # and a name attribute
        else:
            raise PetError()
            
    def __str__( self ):
        if self.name_str:    # If the Pet() has a name, we print it off in the string representation
            return "Species of {:s}, named {}".format(self.species_str, self.name_str)
        else:    # Else, we say that it's unnamed
            return "Species of {:s}, unnamed".format(self.species_str)


class Dog( Pet ):
    
    def __init__(self, name="", chases="Cats"):
        # Here, we're inheriting from the Pet() class to reduce the
        # amount of copy-paste, since we're considering a Dog() to
        # have similar features to the Pet() parent class
        Pet.__init__(self, "Dog", name)

        self.chases = chases    # We're adding one more attribute, however

    def __str__(self):
        if self.name_str:    # Like the Pet() class, we print its name and what it chases now
            return "Species of: Dog, named {}, chases {}".format(self.name_str, self.chases)
        else:
            return "Species of: Dog, unnamed, chases {}".format(self.chases)
        

class Cat( Pet ):
    
    def __init__(self, name="", hates="Dogs"):

        # Almost identical to the Dog() class, but now we have
        # self.hates
        Pet.__init__(self, "Cat", name)
        self.hates = hates

    def __str__(self):
        if self.name_str:    # Same deal
            return "Species of: Cat, named {}, hates {}".format(self.name_str, self.hates)
        else:
            return "Species of: Cat, unnamed, hates {}".format(self.hates)
