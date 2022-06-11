import random

x = random.randint(1,100)
ans = 0

while x != ans:
    ans = int(input())
    if x == ans:
        print("Win")
    elif x > ans:
        print("Need more")
    elif x < ans:
        print("Need less")
    else:
        print("Need number")
