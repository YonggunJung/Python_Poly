f1 = open("file01.txt", "r")
f2 = open("result05.txt", "w", encoding='utf-8-sig')
f2.write("[write() 함수 출력]\n")
for line in f1 :
    f2.write(line)
f1.close()

f1 = open("data01.txt", "r")
f2.write("\n\n[writelines() 함수 출력]\n")
list1 = f1.readlines()
f2.writelines(list1)
f1.close() ; f2.close()
