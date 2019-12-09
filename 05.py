data = [ int(x) for x in open('05.txt').read().replace('\n', '').split(',') ]

def solve(INPUT):
    values = [ 0 for x in range(len(data)*2) ] # use an array of arbitrary size (as here) or use a dictionary (todo)
    for i in range(len(data)):
        values[i] = data[i]
    i = 0

    while True:
        cmd = str(values[i]).zfill(5)
        opcode = int(cmd[3:])
        a = values[i + 1] if int(cmd[2]) else values[values[i + 1]]
        b = values[i + 2] if int(cmd[1]) else values[values[i + 2]]

        if opcode == 1:
            values[values[i + 3]] = a + b
            i += 4
        elif opcode == 2:
            values[values[i + 3]] = a * b
            i += 4
        elif opcode == 3:
            values[values[i + 1]] = INPUT
            i += 2
        elif opcode == 4:
            if a != 0:
                return a
            i += 2
        elif opcode == 5:
            i = b if a != 0 else i + 3
        elif opcode == 6:
            i = b if a == 0 else i + 3
        elif opcode == 7:
            values[values[i + 3]] = int(a < b)
            i += 4
        elif opcode == 8:
            values[values[i + 3]] = int(a == b)
            i += 4

print(solve(1))
print(solve(5))