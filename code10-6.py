# 전역 변수의 값을 함수내에서 변경 불가
# 만약 변경하면 지역변수로 취급
def  g1():
    price = 2000
    value = value+price
    print(price, value)

value = 1000
g1()
print(value)
