# Lab11 - Example Answer (Undocumented)
# Braedyn Lettinga

class PetError( ValueError ):
    pass

class Pet( object ):

    def __init__( self, species=None, name="" ):
        SPECIES = ["dog", "cat", "horse", "gerbil", "hamster", "ferret"]

        if species in SPECIES:
            self.species_str = species.title()
            self.name_str = name.title()
        else:
            raise PetError()
            
    def __str__( self ):
        if self.name_str:
            return "Species of {:s}, named {}".format(self.species_str, self.name_str)
        else:
            return "Species of {:s}, unnamed".format(self.species_str)


class Dog( Pet ):
    
    def __init__(self, name="", chases="Cats"):
        Pet.__init__(self, "Dog", name)
        self.chases = chases

    def __str__(self):
        if self.name_str:
            return "Species of: Dog, named {}, chases {}".format(self.name_str, self.chases)
        else:
            return "Species of: Dog, unnamed, chases {}".format(self.chases)
        

class Cat( Pet ):
    
    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, "Cat", name)
        self.hates = hates

    def __str__(self):
        if self.name_str:
            return "Species of: Cat, named {}, hates {}".format(self.name_str, self.hates)
        else:
            return "Species of: Cat, unnamed, hates {}".format(self.hates)
