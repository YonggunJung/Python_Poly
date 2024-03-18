print("  ...\n (메시지 A)  \n  ...\n")
print("[임의의 키를 누르세요]\n")
input()
print("  ...\n (메시지 B)  \n  ...\n")

# 홀수, 짝수
num = int(input("정수입력:"))
prime = (num%2) == 0;
print(num, "이건 짝수다:", prime)

# 시간 계산
t = 8976
h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60

time = input("시간을 초 단위로 입력하세요 : ")

print(time, "초는", h, "시간", m, "분",  s, "초 입니다.")
