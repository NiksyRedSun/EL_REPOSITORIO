import random

def time():
    return '16:20'

def season():
    return 'Early autumn'

def diagnosis():
    return 'F 20.0'

def dice():
    return str(random.randint(1, 6))

functions_dict = {'time':time(), 'season':season(), 'diagnosis':diagnosis(), 'dice':dice()}
functions_keys = 'Try this: /'
for i in functions_dict:
    functions_keys += i + '/'
functions_keys += ' (ex: sitename/function_name)'






