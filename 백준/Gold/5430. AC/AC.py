from collections import deque

p = int(input())
deq = deque()
result = deque()

for _ in range(p):
    deq.clear()

    fun = input()
    n = int(input())
    
    if(n == 0):
        hh = input()
        inp = []
    else:
        inp = list(map(int, input().strip('[').strip(']').split(',')))
    deq = deque(inp)


    #0은 왼쪽, 1은 오른쪽
    direction = 0
    for i in fun:
        match i:
            case 'R':
                if(n == 0):
                    direction = 5
                if(direction == 1):
                    direction = 0
                else:
                    direction = 1
            case 'D':
                if(n == 0):
                    print('error')
                    direction = 2
                    break
                if(len(deq) == 0):
                    print('error')
                    direction = 2
                    break
                if(direction == 1):
                    deq.pop()
                else:
                    deq.popleft()
    if direction == 2:
        continue
    elif direction == 5:
        print('[]')
        continue
    print('[', end='')
    while(True):
        if(len(deq) == 0):
            break
        if(direction == 1):
            print(deq.pop(), end='')
        else:
            print(deq.popleft(), end='')
        if(len(deq) != 0):
            print(',', end='')
        else:
            break
    print(']')