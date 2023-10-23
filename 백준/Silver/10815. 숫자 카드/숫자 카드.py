N = int(input())
Narr = set(map(int,input().split()))
M = int(input())
Marr = list(map(int,input().split()))
for x in Marr:
    if x in Narr:
        print(1, end =' ' )
    else:
        print(0, end = ' ')
     
