x = int(input("정수1 : "))
y = int(input("정수2 : "))
max = x
if y >max:
    max = y
print("큰 정수 : ", max)
###############################
a = int(input("정수3 : "))
b = int(input("정수4 : "))
if a>b:
    temp = a
    a = b
    b = temp
print(a, b)
