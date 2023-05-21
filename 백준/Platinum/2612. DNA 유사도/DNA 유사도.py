import sys
sys.setrecursionlimit(10**6)

LEFT = 1
UP = 2
CROSS = 3

MISMATCH = -2 #gap, mismatch
MATCH = 3 #match

def issame(a, b):
    if a == b:
        return MATCH
    else:
        return MISMATCH    

def maxupdate(new, ni, nj, max, maxi, maxj):
    if new >= max:
        return new, ni, nj
    return max, maxi, maxj

def main():
    x_len = int(input())
    x = input()
    y_len = int(input())
    y = input()
 
    maxi = 0
    maxj = 0
    maxval = 0


    c = [[ [0,0] for _ in range(y_len+1) ] for _ in range(x_len+1)]
    #init

    #needleman-Wunsch algorithm
    for i in range(1, x_len+1):
        for j in range(1, y_len+1):
            xi = x[i-1]
            yj = y[j-1]
            cr = issame(xi, yj) + c[i-1][j-1][0]            
            left = MISMATCH + c[i][j-1][0]
            up = MISMATCH + c[i-1][j][0]

            if cr < 0 and left < 0 and up < 0:
                c[i][j][0] = 0
                c[i][j][1] = 0
            elif cr >= left and cr >= up:
                c[i][j][0] = cr
                c[i][j][1] = CROSS
                maxval, maxi, maxj = maxupdate(cr, i, j, maxval, maxi, maxj)
            elif left > up and left > cr:
                c[i][j][0] = left
                c[i][j][1] = LEFT
                maxval, maxi, maxj = maxupdate(left, i, j, maxval, maxi, maxj)
            else:
                c[i][j][0] = up
                c[i][j][1] = UP
                maxval, maxi, maxj = maxupdate(up, i, j, maxval, maxi, maxj)
            
    print(maxval)
    resultx = []
    resulty = []
    while(1):
        arrow = c[maxi][maxj][1]
        if arrow == 0:
            break
        if arrow == CROSS:
            resultx.append(x[maxi-1])
            resulty.append(y[maxj-1])
            maxi -= 1
            maxj -= 1
        elif arrow == LEFT:
            resulty.append(y[maxj-1])
            maxj -= 1
        else:
            resultx.append(x[maxi-1])
            maxi -= 1    

    resultx.reverse()
    resulty.reverse()
    for t in resultx:
        print(t, end='')
    print()
    for t in resulty:
        print(t, end='')
    print()


main()