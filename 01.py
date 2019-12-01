import math

f = open("01.txt", "r")

s = 0
for l in f.readlines():
    a = math.floor((int(l) / 3) - 2)
    s += a

print(s)

f = open("01.txt", "r")

s = 0
for l in f.readlines():
    a = math.floor((int(l) / 3) - 2)
    s += a
    while True:
        a = math.floor((int(a) / 3) - 2)
        if a < 0:
            break
        s += a

print(s)
