with open('files.txt', 'r', encoding='utf-8') as ffile:
    files = sorted([i.split() for i in ffile.readlines()])
    exts = sorted(list(set([i[0].split('.')[1] for i in files])))
    res_dict = {}
    for ext in exts:
        temp_list, temp_list_B, temp_list_KB, temp_list_MB, temp_list_GB = [[] for i in range(5)]
        for file in files:
            if file[0].split('.')[1] == ext:
                temp_list.append(file[0])
                if file[2] == 'B':
                    temp_list_B.append(int(file[1]))
                if file[2] == 'KB':
                    temp_list_KB.append(int(file[1]))
                if file[2] == 'MB':
                    temp_list_MB.append(int(file[1]))
                if file[2] == 'GB':
                    temp_list_GB.append(int(file[1]))
        idt_dict = dict.fromkeys(['names', 'B', 'KB', 'MB', 'GB'])
        idt_dict['names'], idt_dict['B'], idt_dict['KB'], idt_dict['MB'], idt_dict['GB'] = temp_list, temp_list_B, temp_list_KB, temp_list_MB, temp_list_GB
        res_dict[ext] = idt_dict

def result_info(dict):
    summary = sum(dict['B']) + sum(dict['KB']) * 1024 + sum(dict['MB']) * 1024 ** 2 + sum(dict['GB']) * 1024 ** 3
    unit = 'B'
    if summary/1024 >= 1:
        summary = round(summary/1024)
        unit = 'KB'
    if summary/1024 >= 1:
        summary = round(summary/1024)
        unit = 'MB'
    if summary/1024 >= 1:
        summary = round(summary/1024)
        unit = 'GB'
    print(*dict['names'], sep='\n')
    print('----------')
    print(f'Summary: {summary} {unit}')


for i in res_dict:
    result_info(res_dict[i])
    print()





