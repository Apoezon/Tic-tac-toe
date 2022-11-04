import draw_field


def place_sign(player, player_number, field) -> list:
    size = len(field)
    while True:

        a = input(f"Введите номер строки от 1 до {size}: ")
        while (not a.isdigit() or int(a) <= 0 or int(a) > size):
            print('\033[1A\033[2K', end='')
            a = input(f"Введите номер строки от 1 до {size}: ")

        b = input(f"Введите номер столбца от 1 до {size}: ")
        while (not b.isdigit() or int(b) <= 0 or int(b) > size):
            print('\033[1A\033[2K', end='')
            b = input(f"Введите номер столбца от 1 до {size}: ")

        a = int(a)
        b = int(b)

        if field[a - 1][b - 1] == 0:
            field[a - 1][b - 1] = player_number
            break
        else:
            input("Это поле занято. Нажмите 'Ввод', чтобы ввести еще раз: ")
            print('\033[1A\033[2K\033[1A\033[2K', end='\033[1A\033[2K')
    print('\033[1A\033[2K', end='\033[1A\033[2K')

    # print(f"Строка #{a}, столбец #{b}")
    return field
