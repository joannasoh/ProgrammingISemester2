from Box import Box
length = input("Please enter length of a box: ")
breadth = input("Please enter breadth of a box: ")
height = input("Please enter height of a box: ")

makeBox = Box(length,breadth,height)

sArea()

getVolume()

from Sphere import Sphere
diameter = input("Please enter diameter of a sphere: ")
radius = input("Please enter radius of a sphere: ")

makeSphere = Sphere(diameter, radius, pi)

sArea()

getVolume()


from Pyramid import Pyramid
length = input("Please enter length of a pyramid: ")
breadth = input("Please enter breadth of a pyramid: ")
height = input("Please enter height of a pyramid: ")
base = input("Please enter height of a pyramid: ")

makePyramid = Pyramid(length,breadth,height, base)

getVolume()
