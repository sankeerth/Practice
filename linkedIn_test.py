commands = ['G','R','G','L']

def doesCircleExist(commands):
    start_x = 0
    start_y = 0

    x = 0
    y = 0

    dir = 'N'

    for i in range(len(commands)):
        if dir == 'N':
            if commands[i] == 'G':
                y += 1
            elif commands[i] == 'R':
                dir = 'E'
            elif commands[i] == 'L':
                dir = 'W'
        elif dir == 'W':
            if commands[i] == 'G':
                x -= 1
            elif commands[i] == 'R':
                dir = 'N'
            elif commands[i] == 'L':
                dir = 'S'
        elif dir == 'E':
            if commands[i] == 'G':
                x += 1
            elif commands[i] == 'R':
                dir = 'S'
            elif commands[i] == 'L':
                dir = 'N'
        elif dir == 'S':
            if commands[i] == 'G':
                y -= 1
            elif commands[i] == 'R':
                dir = 'W'
            elif commands[i] == 'L':
                dir = 'E'

    if dir == 'N' and ((x-start_x)**2 + (y-start_y)**2) > 0:
        print('NO')
    else:
        print('YES')

doesCircleExist(commands)