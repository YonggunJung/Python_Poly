# 학생수(n)와 각 학생의 이름, 영어, 수학 성적을 입력받아
# 학생별로 총점, 평균과 전체 평균에 대한 학점을 계산해서 출력하고,
# 학급의 전체 평균도 계산해서 출력하는 것으로,
# while 문을 이용하여 8장의 [실습코드 8-1]을 입력된 학생 수만큼 반복한다.
# 만약 학생수를 입력하지 않는 다면??
count = 1
ctotal = 0
eng = 0
print("모든 학생의 점수입력이 끝나면 영어 점수에 -1을 입력하세")
while 0 <=eng <= 100:
    print("\n%d번째 학생 성적 처리" % count)
    eng = int(input("영어 점수 : "))
    if eng == -1:
        count -= 1
        break
    math = int(input("수학 점수 : "))
    if eng >= 90:
        eg = "A"
    elif eng >= 80:
        eg = "B"
    elif eng >= 70:
        eg = "C"
    elif eng >= 60:
        eg = "D"
    else:
        eg = "F"
        
    if math >= 90:
        mg = "A"
    elif math >= 80:
        mg = "B"
    elif math >= 70:
        mg = "C"
    elif math >= 60:
        mg = "D"
    else:
        mg = "F"

    total = eng+ math
    avg = total / 2

    if avg >= 90:
        avgg = "A"
    elif avg >= 80:
        avgg = "B"
    elif avg >= 70:
        avgg = "C"
    elif avg >= 60:
        avgg = "D"
    else:
        avgg = "F"
        
    
    
    print("\n%d번째 학생 영어 점수(학점) : %d(%c) , 수학 점수(학점) : %d(%c)," \
          "총점 : %d, 평균 : %d, 총 학점 : %c" \
          % (count, eng, eg, math, mg, total, avg, avgg))
    

    ctotal += total
    count += 1
    
cavg = ctotal / (count*2)
print("\n학생수 : %d, 전체평균 : %6.2f\n" %(count, cavg))
