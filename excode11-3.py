stu = [] ; n = int(input("학생수: "))

def getGrade(avg) :
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

for i in range(0, n) :
    name = input("[%d]학생이름: " % (i+1)) 
    score1 = int(input("[%d]영어성적:" % (i))) 
    score2 = int(input("[%d]수학성적:" % (i)))
    ele = [name, score1, score2, 0, 0, 0 ] 
    stu.append(ele)

# 총점,평균,학점 계산 및 total, avg, grade 리스트 구성 
for i in range(0, n) : 
    stu[i][3] = stu[i][1] + stu[i][2] 
    stu[i][4] = stu[i][3] / 2 
    stu[i][5] = getGrade(stu[i][4]) 
# 전체 성적표 출력 
printTitle()
for i in range(n) : 
    printRecord(stu[i][0], stu[i][1], stu[i][2], stu[i][4], stu[i][5])
# 최고득점자 조사 및 출력 
max = 0
for i in range(1, n) : 
    if stu[max][3] < stu[i][3] : max = i 
print("\n최고평균 : %6.2f(%s)" % (stu[max][4], stu[max][0])) 
