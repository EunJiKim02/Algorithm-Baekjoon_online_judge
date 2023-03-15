a, b, c = map(int, input().split())

if(a == b):
    if( b == c): #3개 모두 동일한 경우
        print(10000 + a * 1000)
    else:
        print(1000 + a * 100)
else: # a != b
    if( b == c):
        print(1000 + b * 100)
    elif(a == c):
        print(1000 + a * 100) 
    else:
        k = max(a, max(b, c))
        print(100 * k)
        