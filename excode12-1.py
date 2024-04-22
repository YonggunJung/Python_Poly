name, eng, math, total, avg, grade = [], [], [], [], [], []
infile = open("class01.txt", "r", encoding='utf-8-sig')
outfile = open("class01out", "w", encoding='utf-8-sig')
n = int(infile.readline().rstrip('\n'))


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


# n명 학생 이름, 영어 성적, 수학 성적 입력 및 리스트 name, eng, math 구성
for i in  range(0, n) :
    stu = infile.readline().rstrip('\n').split(',')
    name.append(stu[0])
    for j in range(1, len(stu)) :
        if j == 1:
            eng.append(int(stu[j]))
        elif j == 2:
            math.append(int(stu[j]))
    total.append(eng[i] + math[i])
    avg.append(total[i] / 2)
    grade.append(getGrade(avg[i]))

printTitle()
for i in range(n):
    printRecord(name[i], eng[i], math[i], avg[i], grade[i])
    
outfile.write(" 이  름\t\t영어\t수학\t총점\t 평균\t학점\n")
for i in range(len(name)):
    outfile.write(" %s\t\t%3d\t\t%3d\t\t%3d\t\t%.2f\t%c\n" \
                  % (name[i],eng[i],math[i], total[i], avg[i], grade[i]))
infile.close() 
outfile.close() 

max = 0
for i in range(1, n):
    if total[max] < total[i] : max = i
print("\n최고평균 : %6.2f(%s)" % (avg[max], name[max]))

min = 0
for i in range(1, n):
    if total[min] > total[i] : min = i
print("\n최저평균 : %6.2f(%s)" % (avg[min], name[min]))


print('영어 평균: ', sum(eng) / len(eng))
mavg = sum(math) / len(math)
print('수학 평균: ', mavg)
print('학생수 : %d' % n)
print('전체 학급의 평균', sum(avg)/n)



