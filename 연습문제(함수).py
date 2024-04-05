
# 6. 10자리 이상, 영문대문자 반드시 포함하는 유효한 비밀번호 만들기

def password():
    flag = False
    up = True
    while flag == False:
        pw = input("비밀번호 : ")
        pwc = input("비밀번호 확인 : ")
        for c in pw:
            if c.isupper():
                flag = True
        if flag == False:
            print("대문자를 입력하세요")
        if pw != pwc:
            print("비밀번호가 일치하지 않습니다.")
            continue
        elif len(pw) < 10:
            print('10자리 이상 입력해주세요')
            continue

                
        
        
        
    print("유효한 비밀번호입니다~~")
password()







# 5. 두 수의 최소 공배수 구하기
a = int(input('첫 번째 수 : '))
b = int(input('두 번째 수 : '))
def lcm(a,  b):
    answer = 0
    max = b
    if a > b :
        max = a
    for i in range(max, (a*b)+1):
        if i % a == 0 and i % b == 0:
            answer = i
            break
    return answer
print(lcm(a, b))


# 4. 입력받은 문자열 역순으로 출력
str1 = input('문자열 입력 : ')
def reverse(str1):
    answer = str1[::-1]
    return answer
print(reverse(str1))


# 3. 2~n까지의 정수 중에서 소수 찾기
n = int(input('n값 : '))
def sosu(n):
    answer = []
    for i in range(2, n):
        flag = 0
        for j in range(2, i):
            if i%j ==0:
                flag = 1

        if flag ==0:
            answer.append(i)
    print('2~%d까지의 정수중 소수 : ' % n, end = '')
    for k in range(len(answer)):
        print(answer[k], end = " ")
sosu(n)
        
        
                



# 2-1. 3개의 정수 중 가장 큰 수 찾기
def maxTwo(i, j):
    if i > j:
        return i
    return j

def maxThree(x, y, z):
    max1 = maxTwo(x, y)
    max2 = maxTwo(y, z)
    answer = maxTwo(max1, max2)
    return answer

a = int(input('첫 번째 수 : '))
b = int(input('두 번째 수 : '))
c = int(input('세 번째 수 : '))

max_num = maxThree(a, b, c)
print('%d, %d, %d 중 가장 큰  수 : %d' %(a, b, c, max_num))


# 2. 최대공약수 구하기
def computeMaxGong(num1, num2):
    answer = 0
    if  num1 <= num2 : 
        min = num1  
        max = num2
    else : 
        min = num2   
        max = num1

    while max%min != 0:
        temp = min
        min = max % min
        max = temp
    answer = min
    return answer

num1 = int(input('첫 번째 수 : '))
num2 = int(input('두 번째 수 : '))

max_gong = computeMaxGong(num1, num2)
print(max_gong)


# 1. 배수의 합계
def sum_besu(start, end, besu):
    sum = 0
    for i in range(start, end+1):
        if i % besu == 0:
            sum += i

    return sum

start = int(input('시작 수 입력 : '))
end = int(input('끝 수 입력 : '))
besu = int(input('배수 입력 : '))


print('%d ~ %d의 정수 중 %d의 배수의 합 : %d' % (start, end, besu, sum_besu(start, end, besu)))
