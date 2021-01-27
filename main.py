import os
class Student:
    def __init__(self,firstName,lastName,studentID):
        self.firstName=firstName
        self.lastName=lastName
        self.studentId(studentID)
    
    def studentId(self,studentID):
        if studentID.isdigit()==True: # if studentID<=0 and studentID>=9: I used this but It didn't work properly.
            if len(studentID)!=6:
                print('ID must be 6 digits. Please try again.')
            else:
                self.__studentID=studentID
        else:
            print('ID must be digits.')

    def getName(self):
        return self.firstName
    def getSurname(self):
        return self.lastName        
    def getID(self):
        return self.__studentID
    def __str__(self):
       return self.firstName +' '+ self.lastName +' '+str(self.__studentID)

class University:
    def __init__(self, universityID, universityNameandDepName, universityPoint, universityCapacity):
        wordList=universityNameandDepName.split(' ') #I did that because I want to see university name and department name separated.
        index=0
        name=''
        department=''
        for word in wordList:
            index=index+1
            if word=='Üniversitesi':
                name=name+word
                break
            name = name + word + ' '
        for i in range(index, len(wordList)):
            if i==len(wordList)-1:
                department=department+wordList[i]
                break
            department=department+wordList[i] + ' '
        self.universityName=name
        self.depName=department
        self.universityID=universityID
        self.universityPoint=universityPoint
        self.universityCapacity=universityCapacity
        self.freeSlot=universityCapacity #5 #6
        self.placed_students = []

    def place_student(self,student):
        self.placed_students.append(student)
        self.freeSlot = int(self.freeSlot) - 1
    
    def get_placed_students(self):
        return self.placed_students

    def get_university_and_department_name(self):
        return f"{self.universityName} {self.depName}"

    def getUniversityName(self):
        return self.universityName
    def getDepName(self):
        return self.depName
    def getUniversityID(self):
        return self.universityID
    def getUniversityPoint(self):
        return self.universityPoint
    def getUniversityCapacity(self):
        return self.universityCapacity

    def get_free_slot(self):
        return self.freeSlot
    def __str__(self):
        return self.universityID +' '+ self.universityName +' '+ self.depName +' '+ self.universityPoint +' '+ self.universityCapacity
    def display(self):
        return self.universityName +' '+ self.depName +' '+ self.universityPoint

class Answer:
    def __init__(self, idOfAnswer, bookType, answers, preference1, preference2):
        self.idOfAnswer=idOfAnswer
        self.bookType=bookType
        self.answers=answers
        self.preference1=preference1
        self.preference2=preference2

class Result:
    def __init__(self, idofStudent, nameSurname, bookType, correctAnswers, wrongAnswers, blankAnswers, score, finalScore, preferenceName1, preferenceName2):
        self.idofStudent=idofStudent
        self.nameSurname=nameSurname
        self.bookType=bookType
        self.correctAnswers=correctAnswers
        self.wrongAnswers=wrongAnswers
        self.blankAnswers=blankAnswers
        self.score=score
        self.finalScore=finalScore
        self.preferenceName1=preferenceName1
        self.preferenceName2=preferenceName2

def studentList() ->list: #the list of the students
    studentFile=open('inputs/student.txt','r',encoding="utf-8")
    studentRecords=[]
    for line in studentFile:
        line=line.rstrip().split(' ') #for deleting \n part and then I splitted them because I want to save them as Student.
        student = Student(line[1], line[2], line[0])
        studentRecords.append(student)
    studentFile.close()
    return studentRecords

def fromIDtoStudent(ID): #1
    studentRecords=studentList()
    for everystudent in studentRecords:
         if everystudent.getID()==ID:
            return(f'{everystudent.getName()} {everystudent.getSurname()}') #I did this because otherwise, there was , or + etc.
    return ID
  
def universityandDepartmentList()->list: #2 #7
    universityFile=open('inputs/university.txt','r',encoding="utf-8")
    universityRecords=[]
    for line in universityFile:
        line=line.rstrip().split(',') #for deleting \n part and I am splitting them with ','
        university = University(line[0], line[1], line[2], line[3])
        universityRecords.append(university)
    universityFile.close()
    for j in range(len(universityRecords)-1):
        for i in range(len(universityRecords)-1):
            if universityRecords[i].getUniversityPoint()<universityRecords[i+1].getUniversityPoint():
                temp=universityRecords[i]
                universityRecords[i]=universityRecords[i+1]
                universityRecords[i+1]=temp
    return universityRecords

def fromIDtoUniversity(ID): #3 Last Part
    universityRecords=universityandDepartmentList()
    for university in universityRecords:
         if university.getUniversityID()==ID:
            return(f'{university.getUniversityName()} {university.getDepName()}') #I did this because otherwise, there was , or + etc.
    return "Couldn't find the record."

def creatingAnswerClass()->list: #3 First Part
    studentAnswers=open('inputs/answer.txt','r', encoding="utf-8")
    answerList=[]
    for line in studentAnswers:
        line=line.rstrip().split(' ')
        answer=Answer(line[0], line[1], line[2], line[3], line[4])
        answerList.append(answer)
    return answerList

def creatingResultTxt(): #3 Second Part
    studentResults=open('inputs/result.txt','w', encoding="utf-8")
    theKey=open('inputs/key.txt','r')
    answerList=creatingAnswerClass()
    keyA=theKey.readline().rstrip() #It was affecting the keyB so, I used rstrip()
    keyB=theKey.readline()
    correctCounter=0
    blankCounter=0
    for answer in answerList:
        correctCounter=0
        blankCounter=0 
        if answer.bookType=='A':
            for i in range(len(answer.answers)-1):
                if answer.answers[i]==keyA[i]: #It will compare the answer of student and answer key.
                    correctCounter+=1
                elif answer.answers[i]=='*':
                    blankCounter+=1
            wrongCounter=len(answer.answers)-correctCounter-blankCounter #It is meaningless to count incorrect answers so this is why I used this.
            studentResults.writelines(f'{answer.idOfAnswer}, {fromIDtoStudent(answer.idOfAnswer)}, {answer.bookType}, {correctCounter}, {wrongCounter}, {blankCounter}, {correctCounter-1*1/4*wrongCounter}, {15*(correctCounter-1*1/4*wrongCounter)}, {fromIDtoUniversity(answer.preference1)}, {fromIDtoUniversity(answer.preference2)}\n')
        else:
            correctCounter=0
            blankCounter=0
            for i in range(len(answer.answers)-1):
                if answer.answers[i]==keyB[i]:
                    correctCounter+=1
                elif answer.answers[i]=='*':
                    blankCounter+=1
            wrongCounter=len(answer.answers)-correctCounter-blankCounter
            studentResults.writelines(f'{answer.idOfAnswer}, {fromIDtoStudent(answer.idOfAnswer)}, {answer.bookType}, {correctCounter}, {wrongCounter}, {blankCounter}, {correctCounter-1*1/4*wrongCounter}, {15*(correctCounter-1*1/4*wrongCounter)}, {fromIDtoUniversity(answer.preference1)}, {fromIDtoUniversity(answer.preference2)}\n')
    studentResults.close()

def sortGrades()->list: #4
    creatingResultTxt()
    resultFile=open('inputs/result.txt', 'r', encoding="utf-8")
    resultList=[]
    for line in resultFile:
        line=line.rstrip().split(', ')
        result=Result(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
        resultList.append(result)
    resultFile.close()
    for j in range(len(resultList)-1):
        for i in range(len(resultList)-1):
            if float(resultList[i].finalScore) < float(resultList[i+1].finalScore): #I used float(), otherwise It thought them as if they weren't digits.
                temp=resultList[i]
                resultList[i]=resultList[i+1]
                resultList[i+1]=temp
    return resultList

def takingAplaceatUniversity()->list: #5
    creatingResultTxt()
    toaccesspreferences=creatingAnswerClass()
    sorted_students=sortGrades()
    sorted_universities=universityandDepartmentList()
    for sorted_student in sorted_students:
        for university in sorted_universities:
            if float(sorted_student.finalScore) > float(university.getUniversityPoint()) and int(university.get_free_slot())>=0 and (university.get_university_and_department_name() == sorted_student.preferenceName1 or university.get_university_and_department_name() == sorted_student.preferenceName2):
                university.place_student(sorted_student)
                #print(sorted_student.nameSurname)
                break
    
    for university in sorted_universities:
        print(university.getUniversityName() + " :")
        for student in university.get_placed_students():
            print(student.nameSurname)
        print("")
                
                

takingAplaceatUniversity()