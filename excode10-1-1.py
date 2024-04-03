
# 전역변수를 사용하지 않는 함수들만 사용한다.
def readData() :
    name = input("이름: ") 
    eng = int(input("영어 성적: ")) 
    math = int(input("수학 성적: "))
    return name, eng, math

def getAvg(eng, math, n) :
    return (eng+math / n)

def getGrade(score) :
    if avg>=90 :  return 'A'
    elif avg>=80 :  return 'B'
    elif avg>=70 :  return 'C'
    elif avg>=60 :  return 'D'
    else :  return 'F'


def printTitle():
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)

def printRecord(name, subj1, subj2, mean, level) :
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name,subj1,subj2, subj1+subj2, mean, level))
    print("-"*53)

names, engs, maths = readData()
avg = getAvg(engs, maths, 2)
grade = getGrade(avg)
printTitle()
printRecord(names, engs, maths, avg, grade)