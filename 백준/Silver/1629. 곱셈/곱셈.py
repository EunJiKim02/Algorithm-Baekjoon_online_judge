import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin.readline

#a를 b번 곱할 거임

def mul(x, y):
    return x * y

def square(x, n, c):
    if(n == 1):
        return x % c
    k = square(x, n//2, c)
    if(n % 2 == 0):
        return mul(k %c, k %c)%c
    else:
        return mul(mul(k%c, k%c), x)%c


def main():
    a, b, c = map(int, input().split())
    result = square(a, b, c)
    print(result % c)


if __name__ == "__main__":
    main()