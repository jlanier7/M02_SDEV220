"""
------------------------------------------------------------------------------------------------------------------------------------

 Program Name: M02 Lab - GPA Status Calculator

 GitHub Filepath: jlanier7/M02_SDEV220/M02_Lab.py

 Author: Josh Lanier 

 SDEV 220

 11/5/22

 Program Purpose: Given a student's first and last name and GPA, this program calculates whether the student will qualify for the Honor Roll or Dean's List and outputs a message with the 
 results.
  
1. Constants and variables:     
INITIALIZED:  
    - nameLast:     (string)         holds the user input for a student's first name. 
    - nameFirst:    (string)         holds the user input for a student's last name.
    - gpa:          (float)          holds the user input for a student's GPA.
    - DL:           (float CONSTANT) GPA minimum to qualify for Dean's List
    - HR:           (float CONSTANT) GPA minimum to qualify for Honor Roll
    - statusFlag    (string)         flag that changes depending on 'while' loop's initial decision structure evaluation results, and triggers actions in second decision structure in 'while' 
                                     loop depending on its value, initialized as empty string so it will pass through the first decision structure and trigger an evaluation in the second that 
                                     the student does not qualify for either Dean's List or Honor Roll unless explicitly changed by the structure
    - thanks        (string)         message printed after user has entered escape variable    
IN-LINE:
    - messDL:       (string)         message printed if student qualifies for the Dean's List, using f-string insertion of nameLast and nameFirst as it was at the time of messDL last variable 
                                     assignment
    - messHR:       (string)         message printed if student qualifies for the Honor Roll, using f-string insertion of nameLast and nameFirst as it was at the time of messHR last variable 
                                     assignment
    - messNeither:  (string)         message printed if student does not qualify for either Dean's List or Honor Roll, using f-string insertion of nameLast and nameFirst as it was at the time 
                                     of messNeither last variable assignment  
  
2. Inputs

- student's last name  (string)
- student's first name (string)
- student's GPA        (float)

3. Computations (pseudocode)

    initialize variables and constants

    initial priming user input for nameLast

    while nameLast does not equal escape variable ('ZZZ' or 'zzz')

        user input for nameFirst
        user input for gpa

        if gpa is less than or equal to Dean's List GPA minimum
            action flag is assigned Dean's List flag
        else if gpa is less than or equal to Honor Roll GPA minimum
            action flag is assigned Honor Roll flag
        (no if statement for if GPA is less than both minimums, because flag is already set for this scenario. if it is less, it will pass right through both of these, and the first two 'if' 
          evaluations of the next decision structure, and be found True for the 'else' evaluation of that decision strucure)

        message variable declared for what will be printed if student meets Dean's List qualifications
        message variable declared for what will be printed if student meets Honor Roll qualifications
        message variable declared for what will be printed if student does not meet either qualifications

        if action flag is assigned to Dean's List flag
            output the Dean's List message variable
        else if action flag is assigned to Honor Role flag
            output the Honor Roll message variable
        else (only option left is they didn't qualify for either)
            output the 'didn't meet either qualification' message variable

        reset the action flag to the empty string (so it will pass through the first decision structure and trigger an evaluation in the second that the student does not qualify for either 
        Dean's List or Honor Roll unless explicitly changed by the structure)

        user input of nameLast to be evaluated at the beginning of the next iteration of the 'while' loop

    output message thanking user for using the program

4. Outputs   

- inital welcome statement at beginning of program
- message stating whether a student qualifies for either honor, or doesn't meet either of them
- message thanking user for using the program

------------------------------------------------------------------------------------------------------------------------------------
"""

# initializing variables and constants

nameLast = ""
nameFirst = ""
gpa = 0.0
DL = 3.5         # Dean's List (DL) GPA req.
HR = 3.25        # Honor Roll (HR) GPA req.
statusFlag = ""
thanks = "Thanks for using this program!"

print("Lets find out if this student qualifies for the Dean's List or Honor Roll!") # code does not contribute to workflow, simply to be more personable
                                                                                    # to user

# program code

nameLast = str(input("Please enter student's last name or 'ZZZ' to quit: "))   #initial 'nameLast' variable assignment to start 'while' loop testing

while nameLast != ("ZZZ" or "zzz") :

    nameFirst = str(input("Please enter student's first name: "))
    gpa = float(input("Please enter student's GPA: "))

    if gpa >= DL:
        statusFlag = "DL"
    elif gpa >= HR:
        statusFlag = "HR"

    messDL = f"Wow, {nameFirst} {nameLast} has made the Dean's List!"
    messHR = f"Cool, {nameFirst} {nameLast} has made the Honor Roll!"
    messNeither = f"{nameFirst} {nameLast} has not qualified for the Honor Roll or the Dean's List."

    if statusFlag == "DL":
        print(messDL)
    elif statusFlag == "HR":
        print(messHR)
    else:
        print(messNeither)

    print(f'For Testing Purposes: {nameFirst = }, {nameLast = }, {gpa = }, {statusFlag = }')

    statusFlag = ""

    nameLast = str(input("Please enter student's last name or 'ZZZ' to quit: "))

print(f'For Testing Purposes: {nameFirst = }, {nameLast = }, {gpa = }, {statusFlag = }')

print(thanks)