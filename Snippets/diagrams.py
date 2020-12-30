#
#	PURPOSE       : To Test the PyDOT language for Creating the Graphs.
#	START DATE    : 26-DEC-2020
#	AUTHOR        : Prakash Vel Periyannan
#
#	DATE			DESCRIPTION				AUTHOR							TIME SPENT
#	26-DEC-2020 	Initial File Created.	prakashvel.periyannan@gmail.com     15Mins
#   29-DEC-2020     Convert List of Dict    prakashvel.periyannan@gmail.com     30Mins
#   29-DEC-2020     Clean Dict              prakashvel.periyannan@gmail.com      30Mins

#REFERENCES
#LINK1:https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29
#LINK2:https://stackoverflow.com/questions/5316206/converting-dot-to-png-in-python
#LINK3:https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
#LINK4:https://stackoverflow.com/questions/48541444/pandas-filtering-for-multiple-substrings-in-series
#LINK5:https://regex101.com/ 
#LINK6:https://stackoverflow.com/questions/23265301/remove-tab-chars-from-the-string/23265395 
#LINK7:https://stackoverflow.com/questions/38194403/list-to-dictionary-even-items-as-keys-odd-items-as-values 
#LINK8:https://realpython.com/iterate-through-dictionary-python/ 

#IMPORTS
import os
import re





LTSSM =[
	"No Command","apple","Pass","Fail"	 
]

#print ("DEBUG LTSSM STATES:"+str(len(LTSSM)))

def fileRead():
    debug_file = open(r"Sample.txt",mode="r")
    debug_file_content = debug_file.readlines()
    return debug_file_content
 

debug_file_content_return = fileRead() 

# entry = re.compile("Entry : ")
# ltssm = re.compile("\tPASS :")

combined = re.compile('Entry : |\tPASS :')

#for value in debug_file_content_return:
#newlist = list(filter(entry.match, debug_file_content_return))
newlist = list(filter(combined.match, debug_file_content_return)) # Read Note
#print (newlist)
#print(len(newlist))

cleanlist1 = []
cleanlist2 = []
#
for items in newlist:
    #print(items.replace("\t",""))
    cleanlist1.append(items.replace("\t",""))

for items in cleanlist1:
    #print(items.replace("\n",""))
    cleanlist2.append(items.replace("\n",""))

#print(compare_listcomp(LTSSM, debug_file_content_return)) # displays [5]

# print ("CLEAN LIST:"+str(cleanlist2))

finalDict = dict(zip(cleanlist2[::2], cleanlist2[1::2]))

# print("finalDict:"+str(finalDict))
# print(finalDict["Entry : 1 : 2020-12-07 18:17:34.121"])

update_ltssm = open("sample_out.txt", mode="w")
update_ltssm.write('@startuml\nbox "STATE" #LightGrey\n\n')

value_zero = ""
ltssm_state_changes = []
ltssm_entry_packets = []

for key, value in finalDict.items():
    #print (key,value)
    if value_zero != value:
        #Handle No Command
        temp_value = value.split(":")[1]
        if temp_value == ' Sample':
            temp_wo_space = temp_value.replace(" ","")
            print (temp_wo_space,key)
            ltssm_state_changes.append(temp_wo_space)
            ltssm_entry_packets.append(key)
            #update_ltssm.write(temp_value,key)
        else:    
            short_ltssm_state = ("_".join((temp_value).split("_")[4:]))
            print (short_ltssm_state,key)
            ltssm_state_changes.append(short_ltssm_state)
            ltssm_entry_packets.append(key)
            #update_ltssm.write(temp_value,key)
    else :
        pass
    value_zero = value

print ("STATE_CHANGE" +str(ltssm_state_changes))
print ("ENTRY_PACKET" +str(ltssm_entry_packets))

#Going 1 Less than the Size as we are incrementing current and Next State
for i in  range(0,(len(ltssm_state_changes)-1)):
    Label = " : "+ltssm_entry_packets[i+1]
    ltssm_statement = ltssm_state_changes[i] +" -> " +ltssm_state_changes[i+1]+Label+"\n\n"
    print (ltssm_statement)
    update_ltssm.write(ltssm_statement)



update_ltssm.write('\n\n@enduml')
update_ltssm.close()

#Converts the .txt to UML Sequential Diagram
os.system("python -m plantuml state.txt")
