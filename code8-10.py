print("2차 방정식 계수 a, b, c를 입력하세요!")
a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
d = b**2 - 4*a*c
if a ==0:
    print("ERROR : divide by zero\n")
else:
    if d >=0:
        rootd = d**(1/2)
        x1 = (-1*b + rootd) / (2*a)
        x2 = (-1*b - rootd) / (2*a)
        print("x1 = %5.2f, x2 = %5.2f" %(x1, x2))

    else:
        print("근 없음!\n")
