import sys
sys.setrecursionlimit(10**6)
MOD = 1000000007
# nCr = n! / r!(n-r)!
# (a % b) % m = ((a % m) * (b^m-2 % m)) %m
# -> a = n!, b = r!(n-r)!

def power(x, y):
    if(y == 1):
        return x
    tmp = power(x , y//2)
    if(y % 2 == 0):
        return tmp * tmp
    else:
        return tmp * tmp * x % MOD 

def factorial(n):

    ans = 1
    for i in range(1, n+1):
        ans = (ans * i)%MOD
    return ans

def main():
    n, k = map(int, input().split())
    ans = (factorial(n) % MOD * power((factorial(k)%MOD * factorial(n - k)%MOD ) % MOD, MOD-2) % MOD) %MOD
    print(ans)



if __name__ == "__main__":
    main()