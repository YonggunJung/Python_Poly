solar = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
star = "지구"
if star in solar:
    print("우리는 태양계에 살고 있습니다.")

print("우리가 사는 별 :", solar[2])
solar[2] = '푸른별_지구'
print(solar[2])

print(solar)
