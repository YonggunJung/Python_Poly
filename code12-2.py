# 이렇게 파일을 열면 꼭 닫아 줘야함
f1 = open("data01.txt", "r")
print('='*20)
txt = f1.read(2)   # read(n)은 n byte씩 읽어라는 뜻 영문은 한 글자 1바이트 한글은 2바이트
print(txt)
while txt != '':
    print(txt, end = '')
    txt = f1.read(2)
print('\n'+'='*20)
f1.close()