#
#PURPOSE    : How to Create Multiple Classes in File and use them in base class.
#DATE       : 11-DEC-2020
#AUTHOR     : prakashvel.periyannan@gmail.com
#
#


class apple():
    color1 = "RED"
    color2 = "GREEN"

class orange():
    origin1 = "Nagpur"
    origin2 = "local"


class fruits(apple,orange):
    basket = 10
    print( "Color of the Apple from apple Class in BASE CLASS FRUIT: "+ apple.color1)
    print( "Origin of the Orange from Orange Class in BASE CLASS FRUIT: "+ orange.origin2)
    

fruit_obj = fruits()
print ("Current Fruits in Basket Count: " + str(fruit_obj.basket)) # Do Type Casting while printing else TypeError Can not Concate str to str.