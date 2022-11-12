import new_field_creation
import draw_field
import your_turn
import who_wins

winner = None
char_x = "(X)"
char_o = "(O)"
charzz = (' ', char_o, char_x)

# Помещаем имена игроков в кортеж players
noone = 'ничья'
first_player = input("Начнем! Введите первого игрока: ")
second_player = input("Введите второго игрока: ")
players = (noone, first_player, second_player)

# Вводим размер поля и рисуем его
field_size = int(input("Введите размер поля: "))
print('\033[2J\033[H', end='')  # стирает все в консоли
field = new_field_creation.new_field_creation(field_size)
draw_field.draw_field(field)

winner = who_wins.who_win(field)

# Начинаем игру:
while winner == None:
    for igrok in [1, 2]:
        print(f"{players[igrok]} {charzz[igrok]}, Ваш ход!")
        field = your_turn.place_sign(players[igrok], igrok, field)
        print('\033[2J\033[H', end='')
        draw_field.draw_field(field)
        winner = who_wins.who_win(field)
        if winner == igrok:
            print(f"{players[igrok]}, поздравляю! Вы победитель!")
            break
        else:
            print("", end='')
        winner = who_wins.noone_won(field)
        if winner == 0:
            print("Победила дружба!")
            break
        else:
            print("", end='')

