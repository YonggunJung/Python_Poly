# with 블록을 사용해서 파일을 개발하면, 
# 블록을 끝낼 때 자동으로 파일을 폐쇄함 
with open('./data01.txt', 'r') as f1:
    print('='*20)
    txt = f1.read(1)
    while txt !="" :
        print(txt, end = '')
        txt = f1.read(1)
    print('\n'+'='*20)

with open('./memo.txt', 'a', encoding='utf-8') as f1 :
    str1 = '\n\n[2024년 4월 17일 수요일 16시 42분]\n'
    str1 = str1 + '집갈 준비하는 중~'
    f1.write(str1)