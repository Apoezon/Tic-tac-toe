def new_field_creation(field_size: int):
    """
    Функция создает пустое игровое поле размера field_size.
    На входе получает значение размера поля и выводит "двумерный массив" для отображения поля функцией draw_field
    :param field_size:
    :return:
    """
    new_field = []
    range_size = range(field_size)
    for i in range_size:
        line_array = []
        for g in range_size:
            line_array.append(0)
        new_field.append(line_array)
    # print(new_field)
    return new_field
# print(new_field_creation(3))