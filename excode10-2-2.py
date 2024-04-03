name=eng=math=topAvg=topName=None
def readData() :
    global name, eng, math
    name = input("이름: ")

    eng = int(input("영어 성적: ")) 
    math = int(input("수학 성적: "))

def getAvg(eng, math, n) :
    return (eng+math) / n

def getGrade(score) :
    global avg, grade
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

def processOne():
    global avg, grade
    readData()
    avg = getAvg(eng, math, 2)
    grade = getGrade(avg)
    printTitle()
    printRecord(name, eng, math, avg, grade)

print('\n프로그램 시작')

topAvg = 0
topName = ""
botAvg = 101
botName = ""
topeng = 0
tename = ""
boteng = 101
bename = ""
topmath = 0
tmname = ""
botmath = 101
bmname = ""
i= 0
while True:
    i += 1
    print('\n%d번째 학생 성적 처리' % i)
    processOne()
    
    if name == '' or math < 0 or eng < 0:
        break 
    
    if topAvg < avg :
        topAvg = avg
        topName = name
    if botAvg > avg :
        botAvg = avg
        botName = name
    if topeng < eng:
        topeng = eng
        tename = name
    if topmath < math:
        topmath = math
        tmname = name
    if boteng > eng:
        boteng = eng
        bename = name
    if botmath > math:
        botmath = math
        bmname = name


print('\n최고 평균 : %6.2f(%s)\n최저 평균 : %6.2f(%s)\n최고 영어 : %d(%s)\t최저 영어 : %d(%s)\n최고 수학 : %d(%s)\t최저 수학 : %d(%s)' \
      % (topAvg, topName, botAvg, botName, topeng, tename, boteng, bename, topmath, tmname, botmath, bmname))
print('\n프로그램 종료')
