a = 200
if a <100:
    print("100보다 작군요.")
else:
    print("100보다 크네요.")

for i in range(0, 3, 1):
    print("안녕하세요 ? for문을 공부중입니다. ^^")

def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = 0
hap = plus(100, 200)
print("100과 200의 plus()함수 결과는 %d" % hap)

def func1():
    a = 10
    print("func1()에서 a 값 %d" %a)

def func2():
    print("func2()에서 a 값 %d" %a)

a = 20
func1()
func2()

def func3():
    global b
    b = 10
    print("func3()에서 b 값 %d" %b)

def func4():
    print("func4()에서 b 값 %d" %b)

b = 20
func3()
func4()

aa = [10, 20, 30, 40]
print(aa[0])
aa[1] = 200
print(aa)
print("1================================")
aa = []
for i in range(0, 4):
    aa.append(0)
hap = 0
print(aa)
for i in range(0, 4):
    aa[i] = int(input(str(i+1) +"번째 숫자 : "))

hap = 0
for i in range(0, 4):
    hap = hap + aa[i]

print ("합계 ==> %d" % hap)
print(aa)






