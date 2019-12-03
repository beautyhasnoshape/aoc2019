lines = open('03.txt', 'r').readlines()

x_array, y_array = [], []

def create_grid(line):
    grid = {} # use dictionary as list with append() will be much too slow! use arrays or tuples (x, y) as keys, and summarized distance from start as value
    commands = [(a[0], int(a[1:])) for a in line.split(sep=',')]
    x, y, distance = 0, 0, 0
    for command in commands:
        d, l = command[0], command[1]
        for _ in range(l):
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'L':
                x -= 1
            elif d == 'R':
                x += 1

            distance += 1
            if (x, y) not in grid:
                grid[(x, y)] = distance

    return grid

wire_a = create_grid(lines[0])
wire_b = create_grid(lines[1])

intersections = wire_a.keys() & wire_b.keys()
print(min([abs(x) + abs(y) for (x, y) in intersections]))

# for part b find the shortest distances travelled to an intersection
print(min([wire_a[intersection] + wire_b[intersection] for intersection in intersections]))