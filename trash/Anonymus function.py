num = int(input())
slova = {}
for i in range(num):
    word = str(input())
    tot = 0
    for j in word:
        tot += ord(j.upper()) - ord('A')
    slova[word] = tot
sorted(slova.items())
sorted_slova = dict(sorted(slova.items()))
print(*sorted(sorted_slova, key=lambda x: sorted_slova[x]), sep='\n')
