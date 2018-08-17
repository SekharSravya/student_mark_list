students_marks = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))

subjects_faculty = []
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        subjects_faculty.append(tuple(columns))

print('Select an option to perform an action on data')
print('*********************************************')
print('''1. Find the faculty with highest student count who got more than 90%. 
2. Find the faculty with highest pass percentage (> 40%)  
3. Find the faculty with least pass percentage (<= 40%)  
4. Who is the top student with maximum total? 
5. Find the student with least numbers total?
6. Who is the best student in Mathematics?
7. What is the average mark for each subject, (ignore failures)? ''')

choice = int(input("Enter your choice(1-7) : "))
##taking the input

####code for choice 1




if choice == 1:
    subject_count = {}
    for students,subject,marks in students_marks:
        if subject not in subject_count and marks >= 90:
            subject_count[subject] = 1
            
        elif marks >= 90:
            subject_count[subject] += 1
            
    max_subject = max(subject_count.items(), key = lambda x:x[1])

    for subject, faculty in subjects_faculty:
        if max_subject[0] == subject:
            print(faculty)

            
#print(subject_count)
            
    
 ###code for coice 2

elif choice == 2:
    subject_count = {}
    for students, subject, marks in students_marks:
        if subject not in subject_count and marks >= 40:
            subject_count[subject] = 1
            
        elif marks >= 40:
            subject_count[subject] += 1 


    max_subject = max(subject_count.items(), key = lambda x:x[1])
    
    for subject, faculty in subjects_faculty:
        if max_subject[0] == subject:
            print(faculty)
    
    print(subject_count)
    

###code for choice 3

    
elif choice == 3:
    subject_count = {}
    for students, subject, marks in students_marks:
        if subject not in subject_count and marks >= 40:
            subject_count[subject] = 1
            
        elif marks >= 40:
            subject_count[subject] += 1 


    min_subject = min(subject_count.items(), key = lambda x:x[1])
    
    for subject, faculty in subjects_faculty:
        if min_subject[0] == subject:
            print(faculty)
    
    print(subject_count)



##code for choice 4         
        
elif choice == 4:
    student_total = {}
    for students, subject, marks in students_marks:
        if students not in student_total:
            student_total[students] = marks
        else:
            student_total[students] += marks                
    
    topper = max(student_total.items(), key = lambda x:x[1])
    
    print(topper)


##code for choice 5

elif choice == 5:
    student_total = {}
    for students, subject, marks in students_marks:
        if students not in student_total:
            student_total[students] = marks
        else:
            student_total[students] += marks                
    
    challenger = min(student_total.items(), key = lambda x:x[1])
    
    print(challenger)



#code for choice 6
    
elif choice == 6:
    maths_score = {}
    for students, subject, marks in students_marks:
        if students not in maths_score and subject == "Mathematics" :
            maths_score[students] = marks
            
    maths_topper = (max(maths_score.items(), key = lambda x:x[1]),)
    
    print(maths_topper)
    
    
#code for choice 7
    
elif choice == 7:
    subject_total = {}
    for students, subject, marks in students_marks:
        if subject not in subject_total:
            subject_total[subject] = marks
            
        else:
            subject_total[subject] += marks
            
    
    n = 0
    for students,subject, marks  in students_marks :
        
        if subject == "Mathematics":
            n += 1
        
        
    for subject, total in subject_total.items() :
        
        total = total/n


        print(subject,total)
    
        
else:
	print("Your choice: {} is not a valid option.".format(choice))            


