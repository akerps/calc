import view

result = 0
string = ''


operators = {'+': (lambda x, y: int(x) + int(y)),
             '-': (lambda x, y: int(x) - int(y)),
             '*': (lambda x, y: int(x) * int(y)),
             '/': (lambda x, y: int(x) / int(y) if int(y) != 0 else view.div_null())}

def parsing(string):
    result = string.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
    parse_list = result.split()
    return parse_list

def get_result():
    global result
    return result