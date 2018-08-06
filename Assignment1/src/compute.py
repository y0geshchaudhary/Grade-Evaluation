'''
Created on 14-May-2018

@author: yogesh
'''
from operator import attrgetter

class Student(object):
    ID = ""#None
    LN = ""#None
    FN = ""#None
    A1 = ""#None
    A2 = ""#None
    PR = ""#None
    T1 = ""#None
    T2 = ""#None
    GR = ""#None
    FL = ""#None
    
    def get_id(self):
        return self.ID


    def get_ln(self):
        return self.LN


    def get_fn(self):
        return self.FN


    def get_a_1(self):
        return self.A1


    def get_a_2(self):
        return self.A2


    def get_pr(self):
        return self.PR


    def get_t_1(self):
        return self.T1


    def get_t_2(self):
        return self.T2


    def get_gr(self):
        return self.GR
    
    
    def get_fl(self):
        return self.FL


    def set_ln(self, value):
        self.LN = value


    def set_id(self, value):
        self.ID = value


    def set_fn(self, value):
        self.FN = value


    def set_a_1(self, value):
        self.A1 = value


    def set_a_2(self, value):
        self.A2 = value


    def set_pr(self, value):
        self.PR = value

    def set_t_1(self, value):
        self.T1 = value


    def set_t_2(self, value):
        self.T2 = value
        
    
    def set_gr(self, value):
        self.GR = value


    def set_fl(self, value):
        self.FL = value


def getIntFromStringForCalc(value):
    if value == None or value == "":
        return 0
    else:
        return int(value)

def getStringFromStringForDisp(value):
    if value == None or value == "":
        return ""
    else:
        return value

def calculateGR(s,examMaxValue,componentContribution):
    a1 = (getIntFromStringForCalc(s.get_a_1())/examMaxValue[0])*componentContribution[0]
    a2 = (getIntFromStringForCalc(s.get_a_2())/examMaxValue[1])*componentContribution[1]
    pr = (getIntFromStringForCalc(s.get_pr())/examMaxValue[2])*componentContribution[2]
    t1 = (getIntFromStringForCalc(s.get_t_1())/examMaxValue[3])*componentContribution[3]
    t2 = (getIntFromStringForCalc(s.get_t_2())/examMaxValue[4])*componentContribution[4]
    gr = a1+a2+pr+t1+t2
    if gr != 0:
        s.set_gr(str(round(gr,2)))
    else:
        s.set_gr("")

def calculateGradeDistribution(passFailPoint):
    fullMarks = 100
    approxBoundary = round((fullMarks-passFailPoint)/7,2)
    gradeDistribution={0:str(fullMarks-approxBoundary)}
    gradeList = [fullMarks-approxBoundary]
    for i in range(1,7):
        gradeList.append(round(gradeList[i-1]-approxBoundary,2))
    
    for i in range(1,7):
        gradeDistribution[i]=str(gradeList[i])
    
    return gradeDistribution
    
def calculateGrade(s, gradeDistribution):
    grades={0:"A+",1:"A",2:"A-",3:"B+",4:"B",5:"B-",6:"C"}
    fl="F"
    for i in range(0,7):
        if s.get_gr()>=gradeDistribution.get(i):
            fl=grades[i]
            break
    s.set_fl(fl)

def displayDetailedRecords(examMaxValue, studentRecords=None, sortedBy="ID", passFailPoint = 50, sortingOrder = False):
    #for spacing
    print()
    componentContribution = [7.5,7.5,25,30,30]
    gradeDistribution = calculateGradeDistribution(passFailPoint)
    
    if studentRecords != None  or len(studentRecords) > 0:
        for s in studentRecords:
            calculateGR(s,examMaxValue,componentContribution)
            calculateGrade(s,gradeDistribution)            
    
    if studentRecords == None  or len(studentRecords) == 0:
        print("Records Empty.") 
    else:
        sortedStudentRecords = sorted(studentRecords, key=attrgetter(sortedBy), reverse=sortingOrder)
        print("{:<7s} {:<9s} {:<9s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s}".format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
        for s in sortedStudentRecords:
            value = {"id":getStringFromStringForDisp(s.get_id()),
                    "ln":getStringFromStringForDisp(s.get_ln()),
                    "fn":getStringFromStringForDisp(s.get_fn()),
                    "a1":getStringFromStringForDisp(s.get_a_1()),
                    "a2":getStringFromStringForDisp(s.get_a_2()),
                    "pr":getStringFromStringForDisp(s.get_pr()),
                    "t1":getStringFromStringForDisp(s.get_t_1()),
                    "t2":getStringFromStringForDisp(s.get_t_2()),
                    "gr":getStringFromStringForDisp(s.get_gr()),
                    "fl":getStringFromStringForDisp(s.get_fl())}
   
            print("{:<7s} {:<9s} {:<9s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s}".format(value["id"],value["ln"],value["fn"],value["a1"],value["a2"],value["pr"],value["t1"],value["t2"],value["gr"],value["fl"]))
            #print("{:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s}".format(s.get_id(),s.get_id(),s.get_fn(),s.get_a_1(),s.get_a_2(),s.get_pr(),s.get_t_1(),s.get_t_2(),s.get_gr(),s.get_fl()))
    
def displayIndividualComponent(studentMap,examMaxValue,option):
    components = {0:"A1",1:"A2",2:"PR",3:"T1",4:"T2"}
    print("\n{} grades ({})".format(components[option-1],examMaxValue[option-1]))
    studentList = sorted(studentMap.values(),key=attrgetter("ID"))
    for i in studentList:
        marks = ""
        if option == 1:
            marks = i.get_a_1()
        elif option == 2:
            marks = i.get_a_2()
        elif option == 3:
            marks = i.get_pr()
        elif option == 4:
            marks = i.get_t_1()
        else:
            marks = i.get_t_2()
        name = i.get_ln()+", "+i.get_fn()
        marks = getStringFromStringForDisp(marks)
        print("{:8s} {:17s} {:8s}".format(i.get_id(),name,marks))
    

def displayComponentAverage(studentMap,examMaxValue,option):
    components = {0:"A1",1:"A2",2:"PR",3:"T1",4:"T2"}
    totalStudents = len(studentMap.values())
    marks = 0
    maxMarks = examMaxValue[option-1]
    for i in studentMap.values():
        if option == 1:
            marks += getIntFromStringForCalc(i.get_a_1())
        elif option == 2:
            marks += getIntFromStringForCalc(i.get_a_2())
        elif option == 3:
            marks += getIntFromStringForCalc(i.get_pr())
        elif option == 4:
            marks += getIntFromStringForCalc(i.get_t_1())
        else:
            marks += getIntFromStringForCalc(i.get_t_2())
    
    compAverage = marks/totalStudents
    print("\n{} average: {:.2f}/{}".format(components[option-1],compAverage,maxMarks))