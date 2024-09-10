
katok = []

def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
print('------------------------------------------')
def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print ("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    klen = len(katok)

    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

insert_data(2, '솔라')
print(katok)
insert_data(6, '문별')
print(katok)
print('------------------------------------------')
katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났음")
        return

    klen = len(katok)
    katok[position] = None

    for i in range(position + 1, klen):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[klen-1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)
print('------------------------------------------')
select = 0
katok = []
if __name__ == "__main__":
    while(select != 4):
        select = int(input("선택-> 1:추가, 2:삽입, 3:삭제, 4:종료"))
        if(select == 1):
            data = input("추가할 데이터 : ")
            add_data(data)
            print(katok)

        elif(select ==2):
            pos = int(input("삽입할 위치 : "))
            data = input("추가할 데이터 : ")
            insert_data(pos, data)
            print(katok)

        elif(select == 3):
            pos = int(input("삭제할 위치"))
            delete_data(pos)
            print(katok)

        elif(select == 4):
            print(katok)
            exit
        else:
            print("1~4 중 입 하나를 입력하세요")
            continue
        


