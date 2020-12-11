#
#PURPOSE    : How to Pass Multiple Values in a Python Program.
#DATE       : 09-DEC-2020
#AUTHOR     : prakashvel.periyannan@gmail.com
#
#REFERENCE  :https://www.geeksforgeeks.org/args-kwargs-python/#:~:text=The%20special%20syntax%20*args%20in,%2C%20variable%2Dlength%20argument%20list.&text=What%20*args%20allows%20you%20to,arguments%20that%20you%20previously%20defined.

def multi_add(*args):
    result = 0 #Intialized the Variable with zero
    for items in args:
        print ("Arguments Passed to the Functions are :"+str(items))  # Type Casting to Strings, Else we will get Type Error.
        result = result + items
    return result

final_result = multi_add(5,6,7) # Add the Sample Arguments 5,6,7
print ("Final Result:"+str(final_result))
#Answer Should be 18