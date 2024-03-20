
# 8. 영어와 수학이 모두 80점 이상이면 합격, 모두 미만이면 불합격,
    # 한 과목만 80이상이면 재시험 기회제공 메세지 출력
eng = int(input("영어시험 점수를 입력하세요 :"))
math = int(input('수학시험 점수를 입력하세요 :'))
if eng >= 80 and math >= 80:
    pa = "합격"
elif eng <80 and math < 80:
    pa = "불합격"
else:
    pa = "재시험 기회제공"
print(pa)



# 7. 나이를 입력받아 입장료를 계산
#    10세 이하 입장료는 1000원 65세는 무료 기본은 2000원
age = int(input("나이 : "))
if age <= 10:
    fee = 1000
elif age >= 65:
    fee = 0
else:
    fee = 2000
print("입장료는 %d입니다." %fee)
    



# 6. 아이디를 입력 받아 아이디가 admin이면 모든 콘텐츠 이용 가능을 출력
#  아니면 회원 레벨을 입력 받아 2~7이면 일부 콘텐츠 이용 가능
#  그것도 아니면 콘텐츠 이용 불가
ids = input("아이디를 입력하세요 : ")
level = int(input("회원 레벨을 입력해주세요 : "))
if ids == "admin":
    l = "모든 콘텐츠 이용 가능"
elif ids != "admin" and 2<= level <=7:
    l = "일부 콘텐츠 이용 가능"
else:
    l = "콘텐츠 이용 불가"
print(l)


# 5. 물의 섭씨 또는 화씨 온도를 입력 받아 섭씨온도와 물의 생태를 판별
#       단 화씨 온도가 입력될 경우에는 섭씨 온도로 변경
unit = int(input("1:섭씨, 2:화씨 :"))
tem = int(input("온도를 입력하세요 :"))

if unit == 2:
    tem = (tem-32)*5/9
if unit == 1:
    u = "섭씨"
else:
    u = "화씨"
print("물의 %s 온도 : %.2f, 상태 : 액체" %(u, tem))


# 4. if 문으로 만 나이 계산하기
py = int(input("현재년을 입력해 주세요 : "))
pm = int(input("현재월을 입력해 주세요 : "))
pd = int(input("현재일을 입력해 주세요 : "))
by = int(input("출생년을 입력해 주세요 : "))
bm = int(input("출생월을 입력해 주세요 : "))
bd = int(input("출생일을 입력해 주세요 : "))
print("-"*40)
print("오늘 날짜 : %d년 %d월 %d일" % (py, pm, pd))
print("생년 월일 : %d년 %d월 %d일" % (by, bm, bd))
print("-"*40)

if pm < bm:
    age = py - by -1
if pm == bm and pd < bd:
    age = py - by -1
if pm >= bm and pd >= bd:
    age = py - by



print("만 나이 : %d세" % age)

# 3. 고객 만족도에 따른 팁 계산하기
print("서비스 만족도 : \n1 : 매우만족\n2: 만족\n3: 불만족")
res = int(input("서비스 만족도를 입력해주세요 : "))
food = int(input("음식 값을 입력해주세요 : "))
if res == 1:
    tip = food * 0.2
    r = "매우 만족"
elif res == 2:
    tip = food * 0.1
    r = "만족"
else:
    tip = food * 0.05
    r = "불만족"
print("t\서비스 만족도 : %s, 팁 : %d" %(r, tip))


# 2. 세수중 가장 큰 값 찾는 프로그램
a = int(input("첫 번째 정수를 입력하세요 : "))
b = int(input("두 번째 정수를 입력하세요 : "))
c = int(input("세 번째 정수를 입력하세요 : "))
if a < b and b > c:
    m = b
elif a > b and a > c:
    m = a
else:
    m = c
print("입력된 세 수 %d %d %d 중에서 가장 큰수는 %d 입니다." %(a, b, c, m))





# 1. 할인율 계산하기
price = int(input("물건 구매가를 입력하세요 :"))
if 10000<=price<50000:
    price1 = price * 0.95
    discount = 5
elif 50000<=price<300000:
    price1 = price * 0.925
    discount = 7.5
else:
    price1 = price * 0.9
    discount = 10
    


print("구매가 :", price, '원')
print("할인율 :", discount, "%")
print("할인 금액 :", int(price * discount), "원")
print("지불 금액 :", int(price1), "원")
