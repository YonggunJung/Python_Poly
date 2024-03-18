name = input("이름: ")
eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
total = eng + math ;  avg = total / 2

if 0<=eng<=100 and 0<= math <=100:
    # 평균 학점 판정
    if avg>=50 :
        grade = '재이수'
    if avg>=60 :
        grade = 'D'
    if avg>=70 :
        grade = 'C'
    if avg>=80 :
        grade = 'B'
    if avg>=90:
        grade =  '성적우수'

    # 영어 학점
    if eng>=50 :
        eng_grade = 'A'
    if eng>=60 :
        eng_grade = 'B'
    if eng>=70 :
        eng_grade = 'C'
    if eng>=80 :
        eng_grade = 'D'
    if eng>=90:
        eng_grade =  'F'

    # 수학 학점
    if math>=50 :
        math_grade = 'F'
    if math>=60 :
        math_grade = 'D'
    if math>=70 :
        math_grade = 'C'
    if math>=80 :
        math_grade = 'B'
    if math>=90:
        math_grade =  'A'




    
    # 결과 출력
    print("-"*53)
    print(" 이  름\t\t영어\t영어학점\t수학\t수학학점\t총점\t평균\t학점")
    print("-"*53)
    print (" %s\t\t%3d\t%2c\t%3d\t%2c\t%3d\t%.2f\t%s" % (name, eng, eng_grade, math, math_grade, total, avg, grade))
    print("-"*53)
