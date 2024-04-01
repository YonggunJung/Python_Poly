             

def accumulateSum(num):
    answer = 0
    for i in range(num+1):
        answer += i
    return answer

def evaluateGrade(num):
    if num >= 90 :
        grade = 'A'
    elif num >= 80 :
        grade = 'B'
    elif num >= 70 :
        grade = 'C'
    elif num >= 60 :
        grade = 'D'
    else : grade = 'F'
    return print(grade)

def findMax(num1, num2):
    answer = max(num1, num2)
    return print(answer)

def isPrime(n):
    flag = True
    for i in range(2, n+1):
        if n%i ==0:
            flag = False
    return flag

def printTitle():
    print("-----------------------------------")
    print("성정 처리 결과")
    print("-----------------------------------")


def notifyMessage(score):
    if score >= 80:
        print('축하합니다!')
        print('합격입니다!')
        return
    print('불합격입니다.!')
    print('다시 도전하세요.!')


num = int(input('정수입력 : '))
print(accumulateSum(num))     # 함수 인수값으로 함수호출 
grade = evaluateGrade(num)     # 자료값으로 함수 호출

max = findMax(num, 76)        # 자료값으로 함수 호출

if isPrime(num) :             # 조건식으로 함수 인출 
    print('%d는 소수임' % num)
else : 
    print('%d는 소수 아님' % num) 
printTitle()                  # 함수 단독으로 사용(함수문) 
notifyMessage(num)



def exchange(a, b):
    temp = a
    print("a = ", a, "b = ", b)
    a = b
    b = temp
    print("a = ", a, "b = ", b)
    return a, b

x = 3
y = 5
print("x = ", x, "y = ", y)
exchange(x, y)
print("x = ", x, "y = ", y)
        
