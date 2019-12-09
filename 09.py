data = [ int(x) for x in open('09.txt').read().replace('\n', '').split(',') ]

def solve(INPUT):
    values = [ 0 for x in range(len(data)*2) ] # use an array of arbitrary size (as here) or use a dictionary (todo)
    for i in range(len(data)):
        values[i] = data[i]
    i, offset = 0, 0

    while True:
        cmd = str(values[i]).zfill(5)
        opcode = int(cmd[3:])
        a = values[i+1] if int(cmd[2]) == 0 else (i+1 if int(cmd[2]) == 1 else values[i+1]+offset)
        b = values[i+2] if int(cmd[1]) == 0 else (i+2 if int(cmd[1]) == 1 else values[i+2]+offset)
        c = values[i+3] if int(cmd[0]) == 0 else (i+3 if int(cmd[0]) == 1 else values[i+3]+offset)

        if opcode == 1:
            values[c] = values[a] + values[b]
            i += 4
        elif opcode == 2:
            values[c] = values[a] * values[b]
            i += 4
        elif opcode == 3:
            values[a] = INPUT
            i += 2
        elif opcode == 4:
            return values[a]
        elif opcode == 5:
            i = values[b] if values[a] != 0 else i + 3
        elif opcode == 6:
            i = values[b] if values[a] == 0 else i + 3
        elif opcode == 7:
            values[c] = int(values[a] < values[b])
            i += 4
        elif opcode == 8:
            values[c] = int(values[a] == values[b])
            i += 4
        elif opcode == 9:
            offset += values[a]
            i += 2

print(solve(1))
print(solve(2))
