Lloyd = {
    "name":"Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }

students = [ Lloyd, Alice, Tyler]

for x in students:
    print x['name']
    print x['homework']
    print x['quizzes'] 
    print str(x['tests']) + "\n"


def average(name,test):
    ave = sum(name[test])/len(name[test])
    return ave

def getAverage(student):
    homework = average(student,"homework")
    quiz = average(student,"quizzes")
    test = average(student,"tests")
    weighted_average = (homework * .1) + (quiz * .3) + (test * .6)
    return weighted_average

def getLetterGrade(score):
    score = round(score)
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60:
        return "F"

def getClassAverage():
    total = 0
    number_stud = len(students)
    for x in students:
        total += getAverage(x)
    class_ave = (total/number_stud)
    return class_ave

print "Class Average is: " + str(getClassAverage())+"%" + "\n"      
for x in students:              
    print str(x["name"])+ "\n" + "Grade:" + getLetterGrade(getAverage(x)) + "\n" + str(getAverage(x))+"%" + "\n"