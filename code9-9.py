month = int(input("월의 날짜 수(28~31)? : "))
start = int(input("월의 첫 번째 요일(일:0 ~ 토:6)? : "))
print("-"*40)
print("일\t월\t화\t수\t목\t금\t토")
         
i = 0
while i < start:
    print("\t"*(start-1), end = "\t")
    i += 1
n = 1
day = start
while n <= month:
    if day % 7 == 0:
        day = 0
        print("\n")
        
    print("%2d" % n, end = "\t")
    day += 1
    n += 1
print("\n--------------------------------")
