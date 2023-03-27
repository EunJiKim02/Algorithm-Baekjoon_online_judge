
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

INF = 999999999999999999

# MinimumCross 한번 더 생각해보기..
# 분명 다 옴. 5 1 2 3 4 5 케이스가 안됨
# 중간을 분할해서 판단할 수 없음. 이걸 새로 짜야함. 
def MinimumCross(arr, start, mid, end):
    n = end - start
    lstart = mid
    lend = mid
    result = [0,0]
    minn = arr[mid]
    for _ in range(n):
        if lstart <= start: # lend 이동
            lend += 1
            if arr[lend] < minn:
                minn = arr[lend]
            if result[0] * result[1] < minn * (lend - lstart + 1):
                result = (minn , (lend - lstart + 1))
        elif lend >= end: # lstart 이동
            lstart -= 1
            if arr[lstart] < minn:
                minn = arr[lstart]
            if result[0] * result[1] < minn * (lend - lstart + 1):
                result = (minn , (lend - lstart + 1))
        else : # 둘 중에 큰 거로 이동
            if arr[lend +1] > arr[lstart -1]:
                lend += 1
                if arr[lend] < minn:
                    minn = arr[lend]
                if result[0] * result[1] < minn * (lend - lstart + 1):
                    result = (minn , (lend - lstart + 1))
            else:
                lstart -= 1
                if arr[lstart] < minn:
                    minn = arr[lstart]
                if result[0] * result[1] < minn * (lend - lstart + 1):
                    result = (minn , (lend - lstart + 1))

    return result

            
    

def MinimumSquare(arr, start, end):
    if end == start:
        #print(start, end)
        return (arr[start], end - start + 1)
    mid = (start + end) // 2
    leftmax, leftn = MinimumSquare(arr, start, mid)
    rightmax, rightn = MinimumSquare(arr, mid+1, end)
    crossmax, crossn = MinimumCross(arr, start, mid, end)
    #print(start, end , ':', leftmax , leftn, rightmax , rightn, crossmax , crossn)
    if (crossmax * crossn <= rightmax * rightn) and (leftmax * leftn <= rightmax * rightn) :
        return (rightmax , rightn)
    elif (crossmax * crossn <= leftmax * leftn) and (rightmax * rightn <= leftmax * leftn) :
        return (leftmax , leftn)
    else:
        return (crossmax , crossn)
    
    

def main():
    while(True):

        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break
        m, n = MinimumSquare(arr, 1, arr[0])
        print(m * n)


if __name__ == '__main__':
    main()