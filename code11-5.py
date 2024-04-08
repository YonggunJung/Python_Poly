score = [10, 20, 30, 40, 50, 60, 70, 80, 90]
score[3:6] = [ ]
print("score =", score)             # 이건 잘 지워짐
del(score[1])
print("score =", score)             # 1번 인덱스 요소 삭제


score1 = [10, 20, 30, 40, 50]
score1[3] = []              
print("score =", score1)        # 이건 빈 리스트 삽입됨
score1[3:4] = []
print("score =", score1)        # 3번 인덱스 요소 삭제
