n = int(input())

cycle = 1
x = (n//10 + n%10) %10 + (n%10)*10
while x != n:
    x = (x//10 + x%10) %10 + (x%10)*10
    cycle += 1
print(cycle)

