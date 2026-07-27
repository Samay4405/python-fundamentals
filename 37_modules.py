# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# import math                                      print(math.pi)
# import math as m                                 print(m.pi)
from math import pi

print(pi)


import gg                                         # from gg import * (it means import everything from gg)

result1 = gg.pi
result2 = gg.square(3)
result3 = gg.cube(3)
result4 = gg.circumference(3)
result5 = gg.area(3)

print(result1, result2, result3, result4, result5)






