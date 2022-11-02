def draw_field(field: list) -> None:
    """
    Функция рисует в консоль состояние поля из "двумероного массива" заданного размера
    Пусть: 0 - пустое поле " "
          1 - нолик "O"
          2 - крестик "X"

    Пример пустого поля:
      [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
    В консоли:
    | | | |
    | | | |
    | | | |
    Пример поля:
      [[2, 0, 2],
      [0, 1, 0],
      [0, 0, 1]]
    В консоли:
    |Х| |Х|
    | |O| |
    | | |O|
    :param field:
    :return:
    """
    field_size = len(field)
    range_size = range(field_size)
    # print(f"Размер поля равен {field_size}")
    output_string = ""
    for i in range_size:
        output_string += "|"
        for g in range_size:
            if field[i][g] == 0:
                output_string += " |"
            elif field[i][g] == 1:
                output_string += "O|"
            elif field[i][g] == 2:
                output_string += "X|"
            else:
                print(f"Некорректный ввод в столбце {g + 1} строки {i + 1}")
                return
        output_string += "\n"
    print(output_string)
    return

a = [[2, 0, 2],
     [0, 1, 0],
     [0, 0, 1]]
b = [
    [2, 0, 1, 2],
    [1, 2, 0, 1],
    [2, 2, 0, 0],
    [1, 0, 1, 0]
]
c = [[2, 0, 2],
     [0, 1, 0],
     [3, 0, 1]]

# print(draw_field(a))