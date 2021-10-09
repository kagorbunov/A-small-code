import math

my_dict = {
    'Почтовое отделение': {
        'x': 0,
        'y': 2,
    }, 'ул. Грибоедова, 104/25': {
        'x': 2,
        'y': 5,
    }, 'ул. Большая Садовая, 302-бис': {
        'x': 6,
        'y': 6,
    }, 'Вечнозеленая Алея': {
        'x': 3,
        'y': 8,
    }, 'ул. Бейкер-стрит, 2216': {
        'x': 5,
        'y': 2,
    },
}
distance = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
small_way = 10000
all_way = 0
n = 0
finally_list = [0, 0, 0, 0, 0, 0]
for j in range(5):
    for i in range(5):
        interval = math.sqrt((my_dict[list(my_dict.keys())[i]]['x'] - my_dict[list(my_dict.keys())[j]]['x']) ** 2 +
                             (my_dict[list(my_dict.keys())[i]]['y'] - my_dict[list(my_dict.keys())[j]]['y']) ** 2)
        distance[i][j] = interval
for i in range(5):
    if i != 0:
        for j in range(5):
            if j != i and j != 0:
                for k in range(5):
                    if k != j and k != i and k != 0:
                        for l in range(5):
                            if l != k and l != j and l != i and l != 0:
                                all_way = distance[0][i] + distance[i][j] + distance[j][k] + distance[k][l] + \
                                          distance[l][0]
                                n += 1
                                if small_way > all_way:
                                    small_way = all_way
                                    finally_list = [0, i, j, k, l, 0]

text = '(0, 2)'
z = 0
for i in range(1, 6):
    a = '(' + str(my_dict[list(my_dict.keys())[finally_list[i]]]['x']) + ',' + \
        str(my_dict[list(my_dict.keys())[finally_list[i]]]['y']) + ')'
    text += ' -> ' + a + '[' + str(distance[finally_list[z]][finally_list[i]]) + ']'
    z = i
text += ' ' + '=' + ' ' + str(small_way)
print(text)
