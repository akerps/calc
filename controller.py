import model
import view


def start_string():
    string = view.input_string()
    return string


def math_operation(list, iter, operand):
    if list[iter] == operand:
        list[iter - 1] = model.operators.get(operand)(list[iter - 1], list[iter + 1])
        deleting(list, iter)
        return True
    return False


def deleting(string, i):
    string.pop(i)
    string.pop(i)


def calc_result(list):
    while len(list) > 1:
        if '*' in list or '/' in list:
            for i in range(1, len(list)-1):
                if list[i] == '*':
                    math_operation(list, i, '*')
                    break
                elif list[i] == '/':
                    math_operation(list, i, '/')
                    break
        else:
            if '+' in list or '-' in list:
                for i in range(1, len(list)-1):
                    if list[i] == '+':
                        math_operation(list, i, '+')
                        break
                    elif list[i] == '-':
                        math_operation(list, i, '-')
                        break
    return list[0]


def output_result(string: str):
    string = model.parsing(string)
    string = calc_result(string)
    model.get_result = string
    view.print_result(string)
