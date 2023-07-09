def hanoi(n, start, end, support):
    if n == 1:
        print(start, '->', end)
        print('sub',start, end, support)
        return
    
    hanoi(n-1, start, support, end)

    print(start, '->', end)
    print('start',n-1,start,support,end)

    hanoi(n-1, support, end, start)
    

n = int(input('원판의 개수는? (10미만) : '))

hanoi(n, 1, 3, 2)