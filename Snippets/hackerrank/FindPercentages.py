#
#PURPOSE: How to Store the Input to Dictionary , using Map , Iterate using without items.Limit Floating Point Value to Two Decimals.
#DATE   : 15-DEC-2020
#
#REFERRENCES: https://www.geeksforgeeks.org/precision-handling-python/
#           : https://www.hackerrank.com/challenges/finding-the-percentage/problem     

if __name__ == '__main__':
    n = int(input())
    
    #Create Empty DICT.
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        print ("DEBUG:name",name)
        print ("DEBUG:line",line)

        scores = list(map(float, line))
        print ("DEBUG:scores",scores)
        #Adding the Student with details
        student_marks[name] = scores
        
    query_name = input()
    
    #DEBUG : Printing the student Scores.
    print ("DEBUG:student_marks:",student_marks)

    #DEBUG : Printing the student Scores.
    print ("DEBUG:Selected Student Name:",query_name)
    
    #DEBUG : Print the value of the data
    selected_student_marks_list = student_marks[query_name]
    print ("DEBUG : selected_student_marks_list:"+str(selected_student_marks_list))
    

    sum = 0
    for i in selected_student_marks_list:
        sum = sum + i     
    avg = float(sum / 3.0)
    print ('%.2f'%avg) 


# 2    
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

#ANSWER: 26.50
