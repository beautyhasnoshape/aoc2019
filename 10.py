import math

lines = open('10.txt').readlines()

# part 1 could be simplified similarily to part 2, by creating a dictionary
# for each point and storing lists of points grouped by the angle
w, h = len(lines[0]), len(lines)
points = {}
for y in range(h):
    for x in range(w):
        if lines[y][x] == '#':
            points[(x, y)] = 0

for p in points:
    x, y, count = p[0], p[1], 0
    for p2 in points:
        if p == p2:
            continue

        dx, dy = x - p2[0], y - p2[1]
        if dx == 1 or dy == 1:
            points[(x, y)] += 1
            continue
        elif dx == 0:
            sign = 1 if dy >= 0 else -1
            skip = False
            for i in range(1, abs(dy)):
                if (x, y - sign*i) in points:
                    skip = True
                    break
            if not skip:
                points[(x, y)] += 1
        elif dy == 0:
            sign = 1 if dx >= 0 else -1
            skip = False
            for i in range(1, abs(dx)):
                if (x - sign*i, y) in points:
                    skip = True
                    break
            if not skip:
                points[(x, y)] += 1
        elif dx < 0:
            ratio = dy / abs(dx)
            skip = False
            for i in range(1, abs(dx)):
                if i * ratio == round(i * ratio) and (x + i, y - i * ratio) in points:
                    skip = True
                    break
            if not skip:
                points[(x, y)] += 1
        elif dx > 0:
            ratio = dy / dx
            skip = False
            for i in range(1, dx):
                if i * ratio == round(i * ratio) and (x - i, y - i * ratio) in points:
                    skip = True
                    break
            if not skip:
                points[(x, y)] += 1

idmax, max_count = -1, 0
for id, count in enumerate(points.values()):
    if count > max_count:
        max_count = count
        idmax = id

p = list(points.keys())[idmax]
print(p, '->', max_count)

# part 2
x, y = p[0], p[1]
for p2 in points:
    if p == p2:
        points[p2] = 0.0
        continue
    
    dx, dy = x - p2[0], y - p2[1]
    angle = math.atan2(-dx, dy)
    points[p2] = round(math.degrees(angle if angle >= 0 else 2*math.pi + angle), 2)

pairs = {}
for v, k in [a for a in sorted(points.items(), key=lambda kv: (round(kv[1], 2), (kv[0][0] ** 2 + kv[0][1] ** 2)))]:
    pairs.setdefault(k, []).append(v)
pairs[0].pop()

removed = []
while len(pairs) > 0:
    for angle in [key for key in pairs]:
        items = pairs[angle]
        item = items.pop()
        removed.append(item)
        if len(items) < 1:
            pairs.pop(angle)

print(removed[199], '->', removed[199][0]*100 + removed[199][1])

