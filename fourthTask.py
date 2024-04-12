#Сортировка по убыванию
def sort_asc_order(args):
    args.sort(key=len)
    return args

#Сортировка по возрастанию
def sort_desc_order(args):
    args.sort(key=len, reverse=True)
    return args


if __name__ == '__main__':
    input_user = input("Введите значения через пробел: ").split()
    print(f'Сортировка по возрастанию {sort_asc_order(input_user)}')
    print(f'Сортировка по убыванию {sort_desc_order(input_user)}')