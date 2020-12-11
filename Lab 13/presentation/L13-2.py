'''
Disclaimer:

I know absolutely nothing about cars. This was just put
together as an example with some surface-level research.
'''

class Car(object):
    
    def __init__(self, owner:str, model:str, plate:str):
        self.owner = owner
        self.model = model
        self.plate = plate

    def __str__(self) -> str:
        return "Car('{}', '{}', '{}')".format(self.owner, self.model, self.plate)
    
    def __repr__(self) -> str:
        return self.__str__()

    def get_acceleration(self, v0:float, v1:float, s:float) -> float:
        '''
        Given a starting velocity, v0, and an ending velocity, v1,
        calculates the acceleration in m/s^2 in s amount of seconds.

        Parameters
        ----------
        v0
            Initial velocity in km/h
        v1
            Ending velocity in km/h
        s
            Time (in seconds) required to get from v0 to v1

        Returns
        -------
            float : Car's acceleration in m/s^2
        '''

        # formula derivation:
        # -> a = dv/dt
        # -> a = (v1 - v0) / (t1 - t0)
        dv = ((v1 - v0) * 1000) / 3600  # 1 km = 1000 m, 1 h = 3600 s
        dt = s
        return dv / dt


class Ford(Car):

    def __init__(self, owner, model, plate): 
        Car.__init__(self, owner, model, plate)
    
    def __str__(self):  # overriding __str__()
        return "Ford('{}', '{}', '{}')".format(self.owner, self.model, self.plate)
        
    
class Tesla(Car):

    def __str__(self):  # same deal-eo down here
        return "Tesla('{}', '{}', '{}')".format(self.owner, self.model, self.plate)


# when methods are re-defined in child classes, calling that method
# on an instance of the child will prioritize the child's definition 

ford = Ford('Jack Stratton', '2020 Ford Focus ST', 'ABC-1234')
print(ford)
print(repr(ford))  # what happens when the parent has the only method definition, but is calling an overwritten method?

tesla = Tesla('Marques Brownlee', 'Model S', 'A13-BIO')
print(tesla)
print(repr(tesla))

car = Car('Hasan Piker', 'Toyota Camry LE', 'ABC-DEF')

print("Variable `car` is an instance of Ford:", isinstance(car, Ford))    # False
print("Variable `ford` is an instance of Car:", isinstance(ford, Car))    # True
print("Variable `tesla` is an instance of Car:", isinstance(tesla, Car))  # True

# you might want to think about the instance determination like this:
# -> is a Car necessarily a Ford? -> No.
# -> is a Ford necessarily a Car? -> Yes.

# (obviously Ford makes more than just cars, but let's just think about them as a "car-exclusive" manufacturer)

# possibly better example:
# If we have a super class, Fruit, and a sub class, Apple:
# -> is Fruit necessarily an Apple? -> No.
# -> is Apple necessarily a Fruit? -> Yes.

my_bool = True
my_int = 1

print("Variable `my_int` is an instance of bool:", isinstance(my_int, bool))  # False
print("Variable `my_bool` is an instance of int:", isinstance(my_bool, int))  # True

# from these two ^ tests alone, we can find who is a sub-class of who.

# if an int is not an instance of bool, but a bool is an instance of int,
# then that must mean int is the super class, and bool is the sub class! 
