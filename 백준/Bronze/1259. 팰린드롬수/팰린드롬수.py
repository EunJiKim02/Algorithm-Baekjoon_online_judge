stack = []

while(True):
    k = True
    stack = list(map(int,input()))
    if(stack[0] == 0):
        break
    length = len(stack) - 1
    cnt = 0
    for i in range(0, len(stack) // 2):
        if(stack[i] != stack[length - i]):
            print('no')
            k = False
            break
        cnt += 1

    if k :
        print('yes')

    stack.clear()
    