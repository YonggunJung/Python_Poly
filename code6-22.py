state1 =  0 and "abc"   # 0은 거짓, "abc"는 참
state2 =  3 and "abc"  # 3, "abc"는 참. 이 경우는 맨 뒤 값이 나온다.
print('0 and "abc" :', state1)
print('3 and "abc" :', state2)
state3 = not 0 ; state4 = not 1
print("not 0 :", state3) ;  print("not 1 :", state4)
state5 = not "" ; state6 = not "abc"
print('"" : ', state5) ;  print('"abc" : ', state6)
