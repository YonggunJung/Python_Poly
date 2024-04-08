def  hanoiTower(n, a, b, t) :
    if n>=1 :
        hanoiTower(n-1, a, t, b)
        print(n, '-1',a, t, b)
        print(" %d-원반 이동  : %c->%c \n" % (n, a, b))
        hanoiTower(n-1, t, b, a)
        print(n, '-2',t, a, b)
    else :
        pass
    return

n = int(input("[하노이 타워 문제] 원반 개수: "))
hanoiTower(n, 'A', 'B', 'T')
