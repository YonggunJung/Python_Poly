def writeInfo(name, dept, major2="없음") :
    print("%s님 환영합니다!" % name)
    print("학과 : %s" % dept)
    print("부전공 : %s" % major2)

name = input("이름은? : ")
dept = input("학과는? : ")
answer = input("복수전공 이수 여부(Y/N) : ")

major2 = input("복수전공명: ")
if answer == 'Y' or answer == 'N' :
    writeInfo(name, dept, major2)
else :
    writeInfo(name, dept)
