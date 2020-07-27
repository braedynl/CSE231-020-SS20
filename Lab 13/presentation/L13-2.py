'''
Disclaimer:

I know absolutely nothing about cars. This was just put
together as an example with some surface-level research.
'''

class Car(object):
    
    def __init__(self, owner, model, plate):
        self.owner = owner
        self.model = model
        self.plate = plate
    
    def get_acceleration(self, v0, v1, s):
        '''
        Calculates the Car's acceleration.
        
        Parameters
        ----------
            v0 (float): Initial velocity in km/h.
            v1 (float): Ending velocity in km/h. 
            s (float): Time (in s) required. 
        
        Returns
        -------
            float : Car's acceleration in m/s^2
        '''
        return (((v1 - v0) * 1000) / 3600) / s
    
    def __str__(self):
        return "Car('{}', '{}', '{}')".format(self.owner, self.model, self.plate)


class Ford(Car):

    def __init__(self, owner, model, plate): 
        Car.__init__(self, owner, model, plate)
    
    def __str__(self):  # overriding __str__()
        return "Ford('{}', '{}', '{}')".format(self.owner, self.model, self.plate)
        
    
class Tesla(Car):

    def __str__(self):  # same deal-eo down here
        return "Tesla('{}', '{}', '{}')".format(self.owner, self.model, self.plate)


# when methods are re-defined in child classes, calling that method
# on the child will prioritize the child's definition 

ford = Ford('Jack Stratton', '2020 Ford Focus ST', 'ABC-1234')
print(ford)

tesla = Tesla('Marques Brownlee', 'Model S', 'A12-BCD')
print(tesla)


c = Car('', '', '')

print("Car is instance of Ford:", isinstance(c, Ford))
print("Ford is instance of Car:", isinstance(ford, Car))

# you might want to think about the instance determination like this:
# -> is a Car necessarily a Ford? -> No.
# -> is a Ford necessarily a Car? -> Yes.

# (obviously Ford makes more than just cars, but let's just think about them as a "car-exclusive" manufacturer)

# possibly better example:
# If we have a super class, Fruit, and a sub class, Apple:
# -> is Fruit necessarily an Apple? -> No.
# -> is Apple necessarily a Fruit? -> Yes.