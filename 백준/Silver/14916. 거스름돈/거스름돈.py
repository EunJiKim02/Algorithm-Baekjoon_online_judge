n = int(input())

COIN5 = 5
COIN2 = 2

n5 = n // COIN5
r5 = n % COIN5
n2 = 0
while(1):
    if(r5 % COIN2 == 0):
        n2 = r5 // COIN2
        break
    r5 = r5 + COIN5
    n5 = n5 - 1
    
if(n5 < 0 or n2 < 0):
    print(-1)
else:
    print(n5 + n2)

    