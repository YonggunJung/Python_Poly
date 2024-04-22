f1 = open("file01.txt", "r")
txt = f1.read()
print("1. read() 반환값:", txt)
f1.close()

f1 = open("file01.txt", "r")
txt = f1.read(3)
print("2. read(3) 반환값:", txt)
f1.close() 

f1 = open("file01.txt", "r")
txt = f1.readline()
print("3. readline() 반환값:", txt)
f1.close()

f1 = open("file01.txt", "r")
txt = f1.readlines()
print("4. readlines() 반환값:", txt)
f1.close()

print("\nfile01.txt 파일 내용 출력")
for element in txt :
    print(element, end ="" )
