fl = [input() for i in range(int(input()))]
sl = [input() for i in range(int(input()))]
fl = [i[:i.index('@')] for i in fl]
num_dict = dict.fromkeys([i.rstrip('0123456789') for i in fl] + sl)
for i in num_dict:
    num_dict[i] = [str(i) for i in range(0, 99)]
for i in fl:
    if i[-1].isdigit():
        if i[-2].isdigit():
            name = i[:-2]
            num = i[-2:]
            num_dict[name].remove(num)
        else:
            name = i[:-1]
            num = i[-1]
            num_dict[name].remove(num)
    else:
        name = i
        num = '0'
        temp_list = num_dict[name]
        num_dict[name].remove(num)
for i in sl:
    if num_dict[i][0] == '0':
        print(f'{i}@beegeek.bzz')
    else:
        print(f'{i}{num_dict[i][0]}@beegeek.bzz')
    del num_dict[i][0]
