# Lab11 - Example Answer (Undocumented)
# Braedyn Lettinga

class Time(object):

    def __init__(self, hours=0, mins=0, secs=0):
        self.hours = hours 
        self.mins = mins 
        self.secs = secs

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def __repr__(self):
        return "Class Time: {:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def from_str(self, time_str):
        time_str = time_str.split(":")

        hours = int(time_str[0])
        mins = int(time_str[1])
        secs = int(time_str[2])

        self.__init__(hours, mins, secs)


A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

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