class1 = [ 
          [88, 75, 96, 74, 82],
          [72, 82, 63, 88, 76],
          [92, 84, 82, 96, 76]
         ]
classSum = 0
cavg = 0
m = len(class1)
n = len(class1[0])
for i in range(m):
    sum = 0
    for j in range(n) :
        sum = sum + class1[i][j]
    avg = sum / n
    print ("%d번 학생 : 총점=%d, 평균=%6.2f" % (i, sum, avg))
    cavg = cavg + avg
avgClass = cavg / (m)
print("전체 평균 = %6.2f" % (avgClass))
