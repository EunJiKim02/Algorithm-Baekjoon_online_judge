from collections import deque

repeat = int(input())

#queue
q = deque()

for _ in range(repeat):
    n, m = map(int, input().split())
    s = list(map(int,input().split()))
    cnt = 0
    #append data to queue
    for i, x in enumerate(s):
      q.append((x, i))
    while(True):
        if(len(q) == 0):
            print(cnt)
            break
        max_q = max(q)


        x = q.popleft()
        if int(x[0]) < max_q[0]:
            q.append(x)
        else:
            cnt += 1    
            if(int(x[1]) == (m)):
                print(cnt)
                break


    q.clear()       
    
    