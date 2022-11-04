
def matrix_trans(a:list):
    # создаем новую матрицу
    b = range(len(a))
    c = range(len(a[0]))
    a_trans = []
    for d in c:
        a_trans.append([])
    for e in c:
        for d in b:
            a_trans[e].append('')
    # заменяем строку q, элемент r элементом из матрицы а
    for q in c:
        for r in b:
            a_trans[q][r] = a[r][q]
    return a_trans

def make_diags(a:list):
    """
    Функция помещает две диагонали поля в лист для проверки фукнцией check_row()
    :param a:
    :return:
    """
    a_diag = [[],[]]
    b = range(len(a))
    c = len(a)
    for i in b:
        a_diag[0].append(a[i][i])
        a_diag[1].append(a[-i-1][i])
    return a_diag

def check_row(a:list):
    """
    Фукция проверяет горизонтальные элементы поля на предмет
    :param a:
    :return:
    """
    for i in a:
        # print(f" Set(i) = {set(i)}")
        if set(i) == {1}:
            winner = 1
            break
        elif set(i) == {2}:
            winner = 2
            break
        else:
            winner = None
    return winner

def check_column(a:list):
  b = matrix_trans(a)
  winner = check_row(b)
  return winner

def check_diagonal(a:list):
  winner = 0
  b = make_diags(a)
  winner = check_row(b)
  return winner

def who_win(a:list):
    # print('Получили матрицу на вход who-win', a, sep="\n")
    winner = check_row(a)
    # print('checked_row(a)', a, sep="\n")
    if winner == None:
        winner = check_column(a)
        # print('checked_column(a)', a, sep="\n")
    if winner == None:
        winner = check_diagonal(a)
        # print('checked_diagonal', a, sep="\n")
    return winner
def noone_won(a:list):
    winner = None
    noone = 0
    for i in a:
        if set(i) == {1,2}:
            noone += 1
        else:
            noone += 0
    if noone == len(a):
        winner = 0
    return winner
#
# a=[
#   [1,1,1],
#   [0,0,0],
#   [2,0,2]
# ]
# b = [1,1,1]
# c = [2,2,2]
# d=[
#   [2,2,2],
#   [0,1,0],
#   [1,0,1]
# ]
# e=[
#   [2,2,1],
#   [0,1,0],
#   [1,0,1]
# ]
# f=[
#   [2,2,1],
#   [0,2,1],
#   [1,0,1]
# ]
# g = [
#   [2,2,1],
#   [0,2,1],
#   [1,0,2]
# ]
# h = [
#   [2,2,1],
#   [0,0,1],
#   [1,0,2]
# ]
#
# i = [a, d, e, f, g, h]
#
# print(f"Победитель в a равен {who_win(a)}, a должен быть 1")
# print(f"Победитель в d равен {who_win(d)}, a должен быть 2")
# print(f"Победитель в e равен {who_win(e)}, a должен быть 1")
# print(f"Победитель в f равен {who_win(f)}, a должен быть 1")
# print(f"Победитель в g равен {who_win(g)}, a должен быть 2")
# print(f"Победитель в h равен {who_win(h)}, a должен быть None")
#
# for item in i:
#   print(who_win(item))