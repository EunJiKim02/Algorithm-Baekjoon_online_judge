
n = int(input())

image = []
for _ in range(n):
    image.append(list(map(int, input())))


def quadtree(image, x, y, n):
    out = False
    check = image[x][y]
    i = 0
    j = 0

    for i in range(n):
        for j in range(n):
            if(check != image[x + i][y + j]):
                print('(', end = '')
                quadtree(image, x, y, n//2)
                quadtree(image, x, y + n//2, n//2)
                quadtree(image, x + n//2, y , n//2)
                quadtree(image, x + n//2 , y + n//2, n//2)
                print(')', end='')
                out = True
                break
        if out:
            break
        
    if(i == n-1 and j == n-1 and not out):
        if(check == 0):
            print(0, end = '')
            return
        else:
            print(1, end = '')
            return
    else:
        return 
            

quadtree(image, 0, 0, n)