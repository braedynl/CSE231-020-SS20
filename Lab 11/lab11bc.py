# Lab11 - Example Answer (Documented)
# Braedyn Lettinga

class Time(object):

    # The constructor wants a number representing
    # hours, minutes and seconds. In order to create an object
    # that holds those things, we create corresponding
    # data members, self.hours, self.mins, self.secs
    def __init__(self, hours=0, mins=0, secs=0):
        self.hours = hours 
        self.mins = mins 
        self.secs = secs

    # Remember that the __str__() methods wants to return a string that's
    # representative of the object. We want to represent the hours, minutes and
    # seconds that the programmer decided on, so we use the data members! 
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    # Similar thing here. __repr__() is more about objectivity rather than fancyness.
    # But it acts just like __str__() -- a visual interpretion of your object
    def __repr__(self):
        return "Class Time: {:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    # This method is used to create an instantiation of a Time() object from a string
    # formatted like "{hours}:{minutes}:{seconds}". So here, I'm splitting by the colon,
    # extracting each number from the list, and then re-constructing the object from
    # those numbers. Importantly, we have to invoke `self` since we're changing the 
    # object that's BEING ACTED UPON by the invocation of .from_str()
    def from_str(self, time_str):
        time_str = time_str.split(":")

        hours = int(time_str[0])
        mins = int(time_str[1])
        secs = int(time_str[2])

        self.__init__(hours, mins, secs)


# Below are Dr. Enbody's tests on your object

A = Time( 12, 25, 30 )

# Remember that print() secretly converts everything to an `str` type.
# So print() will invoke the __str__() method of your class as well as
# the string class constructor, str()

# repr(), a function we haven't talked about at all, really, will invoke
# the __repr__() method. 

print( A )    
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

# We have default arguments set for the constructor to initialize any
# parameter with 0 in the case one isn't supplied. So equivalently, this
# is creating an object with 2 hours, 25 minutes and 0 seconds

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str('03:09:19')

print( D )
print( repr( D ) )
print( str( D ) )