# 가변인수(arbitrary argument list) : 함수를 호출할 때 실인수들을 가변적으로 전달하는 것
#  함수의 가변인수 정의 :  형식인수 앞에 *를 붙임 
# def  functionName(*arg) : 
    # 함수에서는 arg를 튜플로 생각하고 원소들을 참조하면 됨 
    # 즉, 함수에서 arg는 크기 len(arg)인 튜플임 
# 요건 몰랐던 거임
def  getAverage(*num) :
     total = 0
     for i in num :
         total = total + i
     avg = total / len(num)
     return avg
print(getAverage(10, 20, 30))
print(getAverage(10, 20, 30, 40, 50))
print(getAverage(10, 20, 30, 40, 50, 60, 70, 80))
# a = (10, 20, 30)
# print(getAverage(a)) 이건 안됨 에러남 