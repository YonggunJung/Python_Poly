# callFunction()은 전역변수 count를 이용해서
# 자신의 호출횟수를 3의 배수 단위로 재설정함
def call():
    global count
    print("%d 번째 호출" % (count +1))
    if count <2 :
        count += 1
    else:
        count = 0
    return count

count = 0
n = 12
for i in range(n):
    call()
