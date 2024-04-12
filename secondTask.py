#в функции используется списковвое включение. Оно быстрее чем цикл for с точки зрения времени выполнения кода
def list_for_range(min, max):
    result_list = [x for x in range(min, max + 1)]
    return result_list

