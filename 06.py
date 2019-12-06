pairs = {}
for k, v in [str(pair).strip('\n').split(sep=')') for pair in open('06.txt', 'r').readlines()]:
    pairs.setdefault(k, []).append(v)

def traverse(node, s, distances):
    distances.append(s)
    if pairs.get(node):
        children = pairs[node]
        for child in children:
            s += 1
            traverse(child, s, distances)
            s -= 1

distances = []
traverse('COM', 0, distances)
print(sum(distances))

def traverse2(node, path, END, result):
    if pairs.get(node):
        children = pairs[node]
        for child in children:
            path.append(child)
            if child == END: # TODO how to simplify the signature and return the path?
                for a in path:
                    result.append(a)
            traverse2(child, path, END, result)
            path.pop(-1)

path1, path2 = [], []
traverse2('COM', [], 'YOU', path1)
traverse2('COM', [], 'SAN', path2)

# union - intersection - YOU - SAN
print(len((set(path1) | set(path2)) - (set(path1) & set(path2))) - 2)
