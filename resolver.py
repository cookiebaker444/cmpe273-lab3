import json
students = []
classes = []
def getStudents(_, info, id):
    try:
        for student in students:
            if student['id'] == id:
                return student
    except TypeError:
        return "No such student found"

def getClasses(_, info, id):
    try:
        for clas in classes:
            if clas['id'] == id:
                return clas
    except TypeError:
        return "No such class"

def addStudent(_, info, name):
    if len(students) == 0:
        sId = 0
    else:
        sId = students[-1]['id'] + 1
    student = {
        'id' : sId,
        'name' : name
    }
    students.append(student)
    return student
        
def addClass(_, info, name):
    if len(classes) == 0:
        cId = 0
    else:
        cId = classes[-1]['id'] + 1
    newClass = {
        'id' : cId,
        'name' : name,
        'students' : []
    }
    classes.append(newClass)
    return newClass

def updateClass(_, info, cId, sId):
    s = {}
    try:
        for student in students:
            if student['id'] == sId:
                s = student
                for clas in classes:
                    if clas['id'] == cId:
                        sList = clas['students']
                        sList.append(s)
                        break
    except TypeError:
        return "Please add student first"
    return clas




