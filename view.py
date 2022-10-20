def input_string():
    string = input("Введите математическое выражение без скобок: ")
    return string


def div_null():
    print("Делить на ноль нельзя!")
    exit()


def print_result(result):
    print(f'Результат операции = {result}')