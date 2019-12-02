numbers = [int(n) for n in open("02.txt", "r").read().split(sep=',')]
numbers[1], numbers[2] = 12, 2
idx = 0

while idx < len(numbers) and numbers[idx] != 99:
    op, idx1, idx2, out = numbers[idx], numbers[idx+1], numbers[idx+2], numbers[idx+3]
    if op == 1:
        numbers[out] = numbers[idx1] + numbers[idx2]
    elif op == 2:
        numbers[out] = numbers[idx1] * numbers[idx2]    
    idx += 4

print(numbers[0])

stop = False
for i in range(99):
    for j in range(99):
        numbers = [int(n) for n in open("02.txt", "r").read().split(sep=',')]
        numbers[1], numbers[2] = i, j
        idx = 0

        while idx < len(numbers) and numbers[idx] != 99:
            op, idx1, idx2, out = numbers[idx], numbers[idx+1], numbers[idx+2], numbers[idx+3]
            if op == 1:
                numbers[out] = numbers[idx1] + numbers[idx2]
            elif op == 2:
                numbers[out] = numbers[idx1] * numbers[idx2]    
            idx += 4
        
        if numbers[0] == 19690720:
            print(100 * numbers[1] + numbers[2])
            stop = True
            break
    if stop:
        break


