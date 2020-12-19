#
#	PURPOSE       : Text Alignment Hacker Rank Problem 
#	START DATE    : 19-DEC-2020
#	AUTHOR        : Prakash Vel Periyannan
#
#	DATE			DESCRIPTION				AUTHOR							TIME SPENT
#	19-DEC-2020 	Initial File Created.	prakashvel.periyannan@gmail.com   30Mins
#

#REFERENCES
#LINK1:https://www.hackerrank.com/challenges/text-alignment/problem
#LINK2:

#IMPORTS

#FUNCTION

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#print ((thickness%2) > 0)

if ((thickness%2) > 0 and (thickness < 50) ):
    #print ("Debug:thickness:"+str(thickness))
    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
else:
    exit
