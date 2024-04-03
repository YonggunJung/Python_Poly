# 
#  단 2개의 함수만 사용한다면, 어떤 함수들을 사용할지 생각해서 프로그램을 다시 작성하라. 
def readData() :
    name = input("이름: ") 
    eng = int(input("영어 성적: ")) 
    math = int(input("수학 성적: "))
    avg = (eng+math) /2 
    if avg>=90 :  grade =  'A'
    elif avg>=80 :  grade = 'B'
    elif avg>=70 :  grade = 'C'
    elif avg>=60 :  grade = 'D'
    else :  grade = 'F'

    return name, eng, math, grade
    
def printRecord(name, subj1, subj2, level) :
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name,subj1,subj2, subj1+subj2, (subj1+subj2) / 2, level))
    print("-"*53)

names, engs, maths, grades = readData()

printRecord(names, engs, maths, grades)