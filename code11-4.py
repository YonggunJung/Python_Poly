score = [10, 20, 30, 40, 50]
score[2:3] = [33, 35, 37]
print("score=", score)
print("score 원소 개수=", len(score))
score = [10, 20, 30, 40, 50]
score[2:2] = [33, 35, 37]
print("score=", score)          # 이렇게도 가능 하구나
print("score 원소 개수=", len(score))
score = [10, 20, 30, 40, 50]
score[2:4] = [90]
print("score=", score)          # 이렇게 넣으면 두개가 하나로 줄어들고
print("score 원소 개수=", len(score))
score = [10, 20, 30, 40, 50]
score[2:4] = [90, 91]           # 이렇게 넣으면 바뀌고
print("score=", score)
print("score 원소 개수=", len(score))
score = [10, 20, 30, 40, 50]
score[2:4] = 90                 # 이건 에러 남
print("score=", score)
print("score 원소 개수=", len(score))