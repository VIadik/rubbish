from collections import deque


def make_wave():
    global field, HIGHT, WIDE, x_start, y_start, y_finish, x_finish
    queue_of_cell = deque()
    field[y_start][x_start] = 1
    delta_x = [0, 0, 1, -1]
    delta_y = [1, -1, 0, 0]
    for i in range(4):
        y_temporary = y_start + delta_y[i]
        x_temporary = x_start + delta_x[i]
        if field[y_temporary][x_temporary] == 0:
            queue_of_cell.append([y_temporary, x_temporary])
            field[y_temporary][x_temporary] = 2
    while len(queue_of_cell) != 0:
        y, x = queue_of_cell.popleft()
        for i in range(4):
            y_temporary = y + delta_y[i]
            x_temporary = x + delta_x[i]
            if field[y_temporary][x_temporary] == 0:
                queue_of_cell.append([y_temporary, x_temporary])
                field[y_temporary][x_temporary] = field[y][x] + 1
    for i in range(len(field)):
        print(*field[i])
    print("-------------------------------")


def find_way():
    global field, x_start, y_start, x_finish, y_finish, INF
    y_temporary = y_finish
    x_temporary = x_finish
    delta_x = [0, 0, 1, -1]
    delta_y = [1, -1, 0, 0]
    if field[y_finish][x_finish] == 0:
        return False
    lenth = field[y_finish][x_finish]
    print(lenth)
    while lenth > 0:
        lenth -= 1
        print(x_temporary, y_temporary)
        for i in range(4):
            x_temporary_in_for = x_temporary + delta_x[i]
            y_temporary_in_for = y_temporary + delta_y[i]
            if field[y_temporary_in_for][x_temporary_in_for] == lenth:
                x_temporary = x_temporary_in_for
                y_temporary = y_temporary_in_for
                field[y_temporary][x_temporary] = INF
    for i in range(len(field)):
        print(*field[i],  sep=" ")
    return True


field = [[-1, -1, -1, -1, -1],
         [-1, 0, 0, 0, -1],
         [-1, 0, 0, 0, -1],
         [-1, 0, 0, 0, -1],
         [-1, 0, 0, 0, -1],
         [-1, 0, 0, 0, -1],
         [-1, -1, -1, -1, -1]]

HIGHT = 7
WIDE = 5
INF = 1000
x_start = 1
y_start = 2
x_finish = 3
y_finish = 5
make_wave()
print(find_way())
