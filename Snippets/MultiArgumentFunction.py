#
#PURPOSE    : How to Pass Multiple Values in a Python Program.
#DATE       : 09-DEC-2020
#AUTHOR     : prakashvel.periyannan@gmail.com
#


def multi_add(*args):
    result = 0 #Intialized the Variable with zero
    for items in args:
        print ("Arguments Passed to the Functions are :"+str(items))  # Type Casting to Strings, Else we will get Type Error.
        result = result + items
    return result

final_result = multi_add(5,6,7) # Add the Sample Arguments 5,6,7
print ("Final Result:"+str(final_result))
#Answer Should be 18