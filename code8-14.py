score1 = int(input("성적1 :"))
grade1 = "F"
if score1 >= 60:
    grade1 = "D"
if score1 >= 70:
    grade1 = "C"
if score1 >= 80:
    grade1 = "B"
if score1 >= 90:
    grade1 = "A"
print(score1, ":", grade1)


score2 = int(input("성적2 :"))
if score2 >= 90:
    grade2 = "A"
else:
    if score2 >= 80:
        grade2 = "B"
    else:
        if score2 >= 70:
            grade2 = "C"
        else:
            if score2 >= 60:
                grade2 = "D"
            else:
                grade2 = "F"
print(score2, ":", grade2)


score3 = int(input("성적3 :"))
if score3 >= 90:
    grade3 = "A"
elif score3 >= 80:
    grade3 = "B"
elif score3 >= 70:
    grade3 = "C"
elif score3 >= 60:
    grade3 = "D"
else:
    grade3 = "F"
print(score3, ":", grade3)
