a = [
    [1,2,2],
    [1,2,1],
    [1,1,1]
]

def noone_won(a:list):
    winner = None
    noone = 0
    for i in a:
        print(set(i))
        if set(i) == {1,2}:
            noone += 1
        else:
            noone += 0
    if noone == len(a):
        winner = 0
    return winner

print(noone_won(a))

