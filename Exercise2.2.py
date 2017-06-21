'''This is a function to calculate the volume of sphere with radius r'''
import math #need to import math to get the PI value

def sphereVolume(r):
# function name is spehreVolume with argument r for the radius
# this function is going to return the volume
    return 4*math.pi*(pow(r,3))/3

'''
following is a test run for the function spehreVolume, with radius 5 volume -
should be ~523.6 (based on google calculator)
'''
print(sphereVolume(5))
