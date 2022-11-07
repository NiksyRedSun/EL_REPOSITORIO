def time():
    return '16:20'

def season():
    return 'Early autumn'

def diagnosis():
    return 'F 20.0'

functions_dict = {'time':time(), 'season':season(), 'diagnosis':diagnosis(),}
functions_keys = 'Try this: /'
for i in functions_dict:
    functions_keys += i + '/'
functions_keys += 'dice/date (ex: sitename/function_name)'






