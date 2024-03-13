a = '123456789'
b = 123456789
c = 'c'
print("%f" %b)      # 실수로 만들기 기본으로 소수점 6자리까지
print("%11.2e" %b)  # +e숫자 형태로 만들어서 숫자1 부분 자릿수로 만들기
print("%5c" %c)     # char 문자 하나
print("%4s" %a)
print("%11s" %a)
print("%-4s" %a)
print("%-11s" %a)
