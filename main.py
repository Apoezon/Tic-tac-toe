import new_field_creation
import draw_field

char_x = "(X)"
char_o = "(O)"

first_player = input("Начнем! Введите первого игрока: ")
second_player = input("Введите второго игрока: ")
field_size = int(input("Введите размер поля: "))
start_field = new_field_creation.new_field_creation(field_size)
draw_field.draw_field(start_field)
input(f"{first_player} {char_x}, Ваш ход:")