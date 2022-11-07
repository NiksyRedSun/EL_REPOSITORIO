d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}
result = []
string = str('tvoyamamasha').upper()
for digit in string:
    for key in d.keys():
        if digit in d[key]:
            result.append(key * (int(d[key].index(digit) + 1)))
print(''.join(result))
