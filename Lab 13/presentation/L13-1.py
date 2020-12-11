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
        Car.__init__(self, owner, model, plate)  # or: super().__init__(owner, model, plate)
    
class Tesla(Car):
    pass

    # if you want the exact same constructor as the parent class, you can disregard it entirely.
    # though, it can make your code a bit vague. I'd recommend doing the method above ^


ford = Ford('Jack Stratton', '2020 Ford Focus ST', 'ABC-1234')

print(ford.owner)  # has all the attributes from its parent class
print(ford.model)
print(ford.plate)

# ...and all of the method functions from its parent class
print(ford)
print(ford.get_acceleration(0, 100, 5.7))  # "0-100 km/h in 5.7 seconds", source=www.motor1.com


# same deal
tesla = Tesla('Marques Brownlee', 'Model S', 'A12-BCD')

print(tesla.owner)  # inherited attributes
print(tesla.model)
print(tesla.plate)

print(tesla)  # inherited methods
print(tesla.get_acceleration(0, 60*1.609, 2.7))  # "0 to 60 mph in 2.7 seconds", source=cars.usnews.com