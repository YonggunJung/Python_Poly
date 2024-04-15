nn = []
for i in range(3):
    bn = input("닉네임 입력 : ")
    nn.append(bn)
print(nn, "리스트 크기 : ", len(nn))

bn = input("추가 닉네임 입력 : ")
nn.insert(2, bn)
print("추가 결과", nn, '리스트 크기', len(nn))
nn.sort()
print('정렬 결과', nn)
nn.reverse()
print('역정렬 결과', nn)