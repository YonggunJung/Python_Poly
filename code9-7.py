n1 = int(input("첫 번재 정수를 입력하세요"))
n2 = int(input("두 번재 정수를 입력하세요"))
if n1 <= n2:
    min = n1
    max = n2
else:
    min = n2
    max = n1

while max % min != 0:
    temp = min
    min = max % min
    max = temp
gcd = min
print("%d, %d의 최대공약수 : %d\n" %(n1, n2, gcd))
