
# 한 학생의 점수를 입력받아 점수와 학점을 출력 단 0~100을 벗어나면 오류 메시지 출력
score = int(input("점수 : "))
if 0<=score<=100:
    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("점수 : %d, 학점 : %s" % (score, grade))
else:
    print("정확한 점수를 입력하세요!")

print('='*40)


# 100점 만점의 시험 성적(정수)을 입력 받아 학점 판정후 점수화 학점을 출력


s = int(input("점수 : "))
# 4. if elif else문을 사용
print("4")

if s >= 90:
    g = "A"
elif s >= 80:
    g = "B"
elif s >= 70:
    g = "C"
elif s >= 60:
    g = "D"
else:
    g = "F"
print("점수 : %d, 학점 : %c" % (s, g))
print('='*40)
# 3. 중첩된 if else문 사용
print("3")


if s >= 90:
    g = "A"
else:
    if s >= 80:
        g = "B"
    else:
        if s >= 70:
            g = "C"
        else:
            if s >= 60:
                g = "D"
            else:
                g = "F"
                        
                
print("점수 : %d, 학점 : %c" % (s, g))
print('='*40)

# 2. if문과  if else문만 사용하고 중첩 ㄴㄴ
print("2")
if s >= 60:
    g = "D"
if s >= 70:
    g = "C"
if s >= 80:
    g = "B"
if s >= 90:
    g = "A"
else:
    g = "F"
print("점수 : %d, 학점 : %c" % (s, g))
print('='*40)

# 1. if문만 사용
print("1")
if s < 60:
    g = "F"
if s >= 60:
    g = "D"
if s >= 70:
    g = "C"
if s >= 80:
    g = "B"
if s >= 90:
    g = "A"
print("점수 : %d, 학점 : %c" % (s, g))
print('='*40)



# 문자를 입력받아 소문자이면 대문자로 변환하는 프로그램을 작성
c = input("문자 :")
if c == "a":
    print("A")
if c == "b":
    print("B")
if c == "c":
    print("C")
if c == "d":
    print("D")
if c == "e":
    print("E")
if c == "f":
    print("F")
if c == "g":
    print("G")
if c == "h":
    print("H")
if c == "i":
    print("I")
if c == "j":
    print("J")
if c == "k":
    print("K")
if c == "l":
    print("L")
if c == "m":
    print("M")
if c == "n":
    print("N")
if c == "o":
    print("O")
if c == "p":
    print("P")
if c == "q":
    print("Q")
if c == "r":
    print("R")
if c == "s":
    print("S")
if c == "t":
    print("T")
if c == "u":
    print("U")
if c == "v":
    print("V")
if c == "w":
    print("W")
if c == "x":
    print("X")
if c == "y":
    print("Y")
if c == "z":
    print("Z")
else:
    print(c)
    

print('='*40)



# 정수 3개를 입력받아 크기순으로 정렬하는 프로그램을 if else문으로 작성
a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))

if a > b:
    m = a
    a = b
    b = m
    if b > c: 
        m = b
        b = c
        c = m
if a > b:
    temp = a
    a = b
    b = temp
else:
    pass

print(a, b, c)

print('='*40)
# 홀수 짝수
number = int(input("양의 정수를 입력하세요:"))
if number % 2 !=0:
    print("정수 %d는 홀수입니다." % number)
else:
    print("정수 %d는 짝수입니다." % number)
