f1 = open('./memo.txt', 'w', encoding='utf-8')
str1 = '[2024년 3월 4일 월요일]\n'
str1 = str1 + '폴리텍 하이테크 과정 시작 \n\n'
f1.write(str1)
f1.close()

f1 = open('./memo.txt', 'a', encoding='utf-8')
str1 = '[2024년 4월 17일 수요일]\n'
str1 = str1 + '매우 열심히 공부 중~'
f1.write(str1)
f1.close()