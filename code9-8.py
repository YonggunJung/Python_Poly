print("최소 정수/최대 정수/평균 구하기(-1 : 입력 종료)")
num = int(input("정수 입력 :"))
if num != -1 :
    n = 1;
    sum = num
    max = min = num
    num = int(input("정수 입력 :"))
    while num != -1:
        n += 1
        sum += num
        if num < min:
            min = num
        elif num > max:
            max = num
        num = int(input("정수 입력 :"))
    avg = sum / n
    print("정수 개수: %d" % n)
    print("최소 정수 : %d, 최대 정수 : %d" %(min, max))
    print("입력된 정수 평균 : %.2f" % avg)
print("프로그램 종")
