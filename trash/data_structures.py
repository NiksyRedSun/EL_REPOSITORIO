n = int(input())
parrents = [int(i) for i in input().split()]
top = parrents.index(-1)

def Height(top):
    height = 1
    for children in [i for i in range(len(parrents)) if parrents[i]==top]:
        height = max(height, 1+Height(children))
    return height

print(Height(top)+1)