singer = {}

singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys():
    print( '%s --> %s' % (k, singer[k]))


ss = '파이썬 공부는 즐겁습니다. 물로 모든 공부가 다 재밌지는 않죠. ^^'
print(ss.count('공부'))
print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^'))    
