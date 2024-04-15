name, eng, math, total, avg, grade = [], [], [], [], [], []
n = int(input("학생수 : "))
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



for i in range(n):
    print("\n%d번재 학생 자료" % (i+1))
    name.append(input("이름 : "))
    eng.append(int(input("영어 : ")))
    math.append(int(input("수학 : ")))

for i in range(n):
    total.append(eng[i] + math[i])
    avg.append(total[i] / 2)
    grade.append(getGrade(avg[i]))

printTitle()
for i in range(n):
    printRecord(name[i], eng[i], math[i], avg[i], grade[i])

max = 0
for i in range(1, n):
    if total[max] < total[i] : max = i
print("\n최고평균 : %6.2f(%s)" % (avg[max], name[max]))

print('영어 평균: ', sum(eng) / len(eng))
mavg = sum(math) / len(math)
print('수학 평균: ', mavg)
print('전체 학급의 평균', sum(avg)/n)
stotal = sorted(total)
idx = total.index(stotal[1])
print("2등 %s  %d" % (name[idx], total[idx]))
for i in range(n):
    if math[i] >= mavg:
        print(name[i])

