# format()함수는 형식
# format(출력값, '출력서식)  이런 식으로 한다

# >는 오른쪽 정렬
print( format("Hello!", ">10") )
# <는 왼쪽 정렬
print( format("Hello!", "<10") )
# ^는 가운데 정렬
print( format("Hello!", "^10") )
# 수치값의 콤머표현
print( format(1234557, ",") )
# 정수 5자리 출력 우측정렬
print( format(365, "5d") )
# 소수점이하 세자리 반올림 출력
print( format(93.25678, "6.2f") )  # 6은 전체를 6자리로 만들고 .2는 소수 둘째자리 까지

print( format(93.25678, "7.2f") ) # 전체 7자릿수에, 소수 2번째 짜리 까지 만올림하여 우측 정렬

# %숫자d : 숫자 만큼의 자릿수로 정수 우측정렬
# %-숫자d : 숫자 만큼의 자릿수로 정수 좌측정렬
# %숫자f : 숫자 만큼의 자릿수로 실수 우측정렬
# %숫자1.숫자2d : 숫자 1만큼의 자릿수로, 숫자2의 소수점 자리까지 반올림하여 실수 우측정렬

# 별 피라미드

print(format("*", "^13"))
print(format("*"*3, "^13"))
print(format("*"*5, "^13"))
print(format("*"*7, "^13"))
print(format("*"*9, "^13"))
print(format("*"*11, "^13"))
print(format("*"*13, "^13"))


name = "김철수" ; eng = 66 ; math = 88
total = eng + math ; avg = total / 2
print("*"*20)
print(" 이름", format(name, "^9"), sep="\t|")
print("*"*20)
print(" 영어", format(eng, "6d"), sep="\t|")
print(" 수학", format(math, "6d"), sep="\t|")
print("-"*20)
print(" 총점", format(total, "6d"), sep="\t|")
print(" 평균", format(avg, "9.2f"), sep="\t|")
print("*"*20) 
print( format("123456789", "^9") )
