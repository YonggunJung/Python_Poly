day = input("오늘은 무슨 요일인가요?")
if day == "월" or day == "화":
    do = "파이썬 과제하기"
elif day == "수":
    do = "전공 과제하기"
elif day == "목" or day == "금":
    do = "어학 공부하기"
else:
    do = "취미 활동하기"
print("오늘의 할 일 :", do)
