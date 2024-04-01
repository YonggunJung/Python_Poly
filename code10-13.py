def checkPassword(pw):
    global count
    count += 1
    if pw == 'python':
        return 1
    return 0

count = 0
pw = input("패스워드 입력:")
state = checkPassword(pw)
while count <3:
    if state == 1:
        break
    pw = input("패스워드 재입력:")
    state = checkPassword(pw)

if count < 3:
    print("로그-인 성공!")
else:
    print("부정사용자임(3회 패스워드 오류)")