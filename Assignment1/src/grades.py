'''
Created on 14-May-2018

@author: yogesh
'''
from compute import Student, displayDetailedRecords, displayIndividualComponent, displayComponentAverage, calculateGradeDistribution

if __name__ == '__main__':
    pass
#Menu for 1> Display individual component
def displayIndividualComponentMenu(studentMap,examMaxValue):
    #for spacing
    print()
    print("1> A1")
    print("2> A2")
    print("3> PR")
    print("4> T1")
    print("5> T2")
    option = input("Enter option number.")    
    if option == "1":
        displayIndividualComponent(studentMap,examMaxValue,int(option))
        
    elif option == "2":
        displayIndividualComponent(studentMap,examMaxValue,int(option))
        
    elif option == "3":
        displayIndividualComponent(studentMap,examMaxValue,int(option))
        
    elif option == "4":
        displayIndividualComponent(studentMap,examMaxValue,int(option))
        
    elif option == "5":
        displayIndividualComponent(studentMap,examMaxValue,int(option))
        
    else:
        print("choose valid option.")
        displayIndividualComponentMenu(studentMap,examMaxValue)

#Menu for 2> Display component average
def displayComponentAverageMenu(studentMap,examMaxValue):
    #for spacing
    print()
    print("1> A1")
    print("2> A2")
    print("3> PR")
    print("4> T1")
    print("5> T2")
    option = input("Enter option number.")    
    if option == "1":
        displayComponentAverage(studentMap,examMaxValue,int(option))
        
    elif option == "2":
        displayComponentAverage(studentMap,examMaxValue,int(option))
        
    elif option == "3":
        displayComponentAverage(studentMap,examMaxValue,int(option))
        
    elif option == "4":
        displayComponentAverage(studentMap,examMaxValue,int(option))
        
    elif option == "5":
        displayComponentAverage(studentMap,examMaxValue,int(option))
        
    else:
        print("choose valid option.")
        displayComponentAverageMenu(studentMap,examMaxValue)

#Menu for 4> Sort by alternate column
def displaySortByColumnMenu(studentMap,examMaxValue):
    #for spacing
    print()
    print("1> By LN (last name).")
    print("2> By GR (numeric grade).")
    option = input("Choose option number.")    
    if option == "1":
        displayDetailedRecords(examMaxValue, studentRecords=studentMap.values(), sortedBy="LN", passFailPoint = 50, sortingOrder = False)
        
    elif option == "2":
        displayDetailedRecords(examMaxValue, studentRecords=studentMap.values(), sortedBy="GR", passFailPoint = 50, sortingOrder = True)

    else:
        print("Choose valid option.")
        displaySortByColumnMenu(studentMap,examMaxValue)

#Menu for 5> Change Pass/Fail point
def displayPassFailMenu(studentMap,examMaxValue):
    #for spacing
    print()
    pFPoint = int(input("Enter new P/F point."))
    displayDetailedRecords(examMaxValue, studentRecords=studentMap.values(), sortedBy="ID", passFailPoint = pFPoint, sortingOrder = False)

def displayMainMenu(studentMap,examMaxValue):
    print("Main Menu:")
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit")
    option = input("Enter option number.")    
    if option == "1":
        displayIndividualComponentMenu(studentMap,examMaxValue)
        print("\n")
        displayMainMenu(studentMap, examMaxValue)
    
    elif option == "2":
        displayComponentAverageMenu(studentMap,examMaxValue)
        print("\n")
        displayMainMenu(studentMap, examMaxValue)
    
    elif option == "3":
        displayDetailedRecords(examMaxValue, studentRecords=studentMap.values(), sortedBy="ID", passFailPoint = 50, sortingOrder = False)
        print("\n")
        displayMainMenu(studentMap, examMaxValue)
    
    elif option == "4":
        displaySortByColumnMenu(studentMap, examMaxValue)
        print("\n")
        displayMainMenu(studentMap, examMaxValue)
    
    elif option == "5":
        displayPassFailMenu(studentMap, examMaxValue)
        print("\n")
        displayMainMenu(studentMap, examMaxValue)
    
    elif option == "6":
        print("Good Bye.")
        exit()
    else:
        print("choose valid option.\n")
        displayMainMenu(studentMap,examMaxValue)


def readDataFromFile():
    studentMap = {}
    s = None
    #reading class file
    classFile  = open("class.txt","r")
    for line in classFile:
        #print(line)
        record = line.split("|")
        s = Student()
        s.set_id(record[0].lstrip().rstrip())
        s.set_fn(record[1].lstrip().rstrip())
        s.set_ln(record[2].lstrip().rstrip())
        studentMap[record[0].lstrip().rstrip()] = s
    classFile.close()

    #reading a1 file    
    a1File = open("a1.txt","r")
    a1Max = a1File.readline()
    for line in a1File:
        record = line.split("|")
        s = studentMap.get(record[0].lstrip().rstrip())
        #print(record[1])
        s.set_a_1(record[1].lstrip().rstrip())
    a1File.close()

    #reading a2 file    
    a2File = open("a2.txt","r")
    a2Max = a2File.readline()
    for line in a2File:
        record = line.split("|")
        s = studentMap.get(record[0].lstrip().rstrip())
        s.set_a_2(record[1].lstrip().rstrip())
    a2File.close()

    #reading project file    
    projectFile = open("project.txt","r")
    projectMax = projectFile.readline()
    for line in projectFile:
        record = line.split("|")
        s = studentMap.get(record[0].lstrip().rstrip())
        s.set_pr(record[1].lstrip().rstrip())
    projectFile.close()

    #reading t1 file    
    t1File = open("test1.txt","r")
    t1Max = t1File.readline()
    for line in t1File:
        record = line.split("|")
        s = studentMap.get(record[0].lstrip().rstrip())
        s.set_t_1(record[1].lstrip().rstrip())
    t1File.close()

    #reading t2 file    
    t2File = open("test2.txt","r")
    t2Max = t2File.readline()
    for line in t2File:
        record = line.split("|")
        s = studentMap.get(record[0].lstrip().rstrip())
        s.set_t_2(record[1].lstrip().rstrip())
    t2File.close()

    #list for examMaxValue
    examMaxValue = [int(a1Max.lstrip().rstrip()),int(a2Max.lstrip().rstrip()),int(projectMax.lstrip().rstrip()),int(t1Max.lstrip().rstrip()),int(t2Max.lstrip().rstrip())]
    
    dataTuple = studentMap,examMaxValue
    return dataTuple


dataTuple = readDataFromFile()
studentMap = dataTuple[0]
examMaxValue = dataTuple[1]
displayMainMenu(studentMap,examMaxValue)