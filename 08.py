count, size = 0, 25*6 # image size: 25 x 6
pixels = [int(a) for a in open('08.txt', 'r').read().strip('\n')]

layers = {}
for i in range(len(pixels) // size):
    layer = pixels[i*size:i*size+size]
    layers[layer.count(0)] = (layer.count(1), layer.count(2))

result = layers[min(layers.keys())]
print(result[0] * result[1])

for idx in range(size):
    if pixels[idx] < 2:
        continue
    for i in range(len(pixels) // size):
        if pixels[i*size+idx] < 2:
            pixels[idx] = pixels[i*size+idx]
            break

row = ''
for i in range(len(pixels[0:size])):
    row += ' ' if pixels[i] == 0 else 'X'
    if i != 0 and (i+1) % 25 == 0:
        print(row)
        row = ''
