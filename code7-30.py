name = input("이름:")
eng = int(input("영어 성적 :"))
math= int(input("수학 성적 :"))
kor= int(input("국어 성적 :"))
sci= int(input("과학 성적 :"))
total = eng + math + kor + sci;
avg = total / 4;
print("-"*45)
print(" 이름\t\t영어\t수학\t국어\t과학\t총점\t평균")
print("-"*45)
print(" %s\t\t%3d\t%3d\t%3d\t%3d\t%3d\t%.2f" % (name, eng, math, kor, sci, total, avg))
print("-"*45)
