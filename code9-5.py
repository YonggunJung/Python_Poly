count = 0;
flag = 0;
while flag == 0 and count < 3:
    password = input("패스워드 입력:")
    if password == "Hi!Python":
        flag = 1
    else:
        print("패스워드가 일치하지 않습니다.")
        count += 1

if flag == 1:
    print("로그인 성공")
else:
    print("로그인 실패. 5분후 다시 시도하세요")
