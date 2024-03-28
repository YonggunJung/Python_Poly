# for문 실습과제2 처리조건2, 3번까지

n = int(input("학생수 입력 : "))

topeng = 0; 
boteng = 100; 
topmath = 0; 
botmath = 100;
topavg = 0; 
botavg = 100;
# topname = botname = tengname = bengname = tmathname = bmathname = None
for i in range(1, n+1):
    print("\n%d번째 학생 성적처리" % i)
    name = input("이름: ")
    if name == "":
        break
    eng = input("영어 성적: ")
    if eng == "":
        break
    eng = int(eng)
    math = input("수학 성적: ")
    if math == "":
        break
    math = int(math)
    
    total = eng + math ;  avg = total / 2
    


    
    
                    
                        
    if topavg < avg:
        topavg = avg ; topname = name
    if botavg > avg:
        botavg = avg ; botname = name
    if topeng < eng:
        topeng = eng ; tengname = name
    if boteng > eng:
        boteng = eng ; bengname = name
    if topmath < math:
        topmath = math ; tmathname = name
    if botmath > math:
        botmath = math ; bmathname = name

    if 0<=eng<=100 and 0<= math <=100:
        # 평균 학점 판정
        if avg>=90 :
            grade = '성적우수'
        elif avg>=80 :
            grade = 'B'
        elif avg>=70 :
            grade = 'C'
        elif avg>=80 :
            grade = 'D'
        else:
            grade =  '재이수'

        # 영어 학점
        if eng>=90 :
            eng_grade = 'A'
        elif eng>=80 :
            eng_grade = 'B'
        elif eng>=70 :
            eng_grade = 'C'
        elif eng>=60 :
            eng_grade = 'D'
        else:
            eng_grade =  'F'

        # 수학 학점
        if math>=90 :
            math_grade = 'A'
        elif math>=80 :
            math_grade = 'B'
        elif math>=70 :
            math_grade = 'C'
        elif math>=80 :
            math_grade = 'D'
        else:
            math_grade =  'F'




        
        # 결과 출력
        print("-"*53)
        print(" 이  름\t\t영어\t영어학점\t수학\t수학학점\t총점\t평균\t학점")
        print("-"*53)
        print (" %s\t\t%3d\t%2c\t%3d\t%2c\t%3d\t%.2f\t%s" % (name, eng, eng_grade, math, math_grade, total, avg, grade))
        print("-"*53)
if topavg != 0:        
    print ("\n최고평균 : %6.2f(%s)" % (topavg, topname))
    print ("\n최저평균 : %6.2f(%s)" % (botavg, botname))
    print ("\n최고영어 : %6.2f(%s)" % (topeng, tengname))
    print ("\n최저영어 : %6.2f(%s)" % (boteng, bengname))
    print ("\n최고수학 : %6.2f(%s)" % (topmath, tmathname))
    print ("\n최저수학 : %6.2f(%s)" % (botmath, bmathname))
