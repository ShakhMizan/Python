from statistics import mean as m

admins = {'Mizan':'pass123','user2':'pass2'}
studentDict = {'Adnan':[78,80,86],
               'Habib':[45,65,45],
               'Misbah':[45,67,54]
               }

def enterGrades():
    nameToEnter = input('Students Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding grades.......')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('student does not exist')
    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to remove? ')
    if nameToRemove in studentDict:
        print('student removing..........')
        del studentDict[nameToRemove]

    else:
        print('name does not exist in the studentDict')
    print(studentDict)

def studentAverages():
    for eachStudent in studentDict:
        gradelist = studentDict[eachStudent]
        averageGrades = m(gradelist)
        print(eachStudent,'has an average of grade is: ',averageGrades)

def main():
    print("""
    Welcome to Grade Central
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Students Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (input a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAverages()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given,try again')


login = input('Username: ')
passwd = input('password: ')

if login in admins:
    if admins[login] == passwd:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid password, will denote in 5 seconds!')

else:
    print('Invalid Username,calling the FBI to report this')