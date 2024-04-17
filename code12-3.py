f2 = open('./result01.txt', 'w', encoding= 'utf-8')
txt = input('메세지를 남기세요.\n')
for i in range(3):
    f2.write(txt + '\n')
    txt = input()
f2.close()