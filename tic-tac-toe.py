def draw(regionCode):
    if count % 2 == 0:  # even
        shape = 'x'
        shapeDraw(shape, regionCode)
    if count % 2 == 1:  # odd
        shape = 'o'
        shapeDraw(shape, regionCode)
    if count == 9:
        time.sleep(1.5)
        new()


def shapeDraw(shape, regionCode):
    if shape == 'x':
        row = regionCode[0]
        col = regionCode[1]
        matrix[row][col] = shape
        # print(matrix)

        # draw
        turtle.pu()
        turtle.color('Blue')
        turtle.setposition(-200 + col * 160, 110 - row * 160)
        turtle.left(45)
        turtle.pd()
        turtle.forward(120)
        turtle.right(45)
        turtle.pu()
        turtle.setposition(-115 + col * 160, 110 - row * 160)
        turtle.left(135)
        turtle.pd()
        turtle.forward(120)
        turtle.pu()
        turtle.right(135)
        turtle.color('Black')

        matrixCheck()

    elif shape == 'o':
        row = regionCode[0]
        col = regionCode[1]

        matrix[row][col] = shape
        # print(matrix)

        # draw
        turtle.pu()
        turtle.color('Red')
        turtle.setposition(-160 + col * 160, 110 - row * 160)
        turtle.pd()
        turtle.circle(42.5)
        turtle.color('Black')
        turtle.pu()

        matrixCheck()


def matrixCheck():
    flag = 0
    possibleWin = []

    # rows
    possibleWin.append([matrix[0][0], matrix[0][1], matrix[0][2]])
    possibleWin.append([matrix[1][0], matrix[1][1], matrix[1][2]])
    possibleWin.append([matrix[2][0], matrix[2][1], matrix[2][2]])

    # cols
    col1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    col2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    col3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
    possibleWin.append(col1)
    possibleWin.append(col2)
    possibleWin.append(col3)

    # diagonal
    diagonal1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diagonal2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
    possibleWin.append(diagonal1)
    possibleWin.append(diagonal2)

    for i in possibleWin:
        if i == ['o', 'o', 'o'] or i == ['x', 'x', 'x']:
            # print('game_over')
            index = possibleWin.index(i)
            flag = 1

    # processing index
    if flag == 1:
        if index == 0:
            x1, y1, x2, y2 = 0, 0, 2, 0
            drawLine(x1, y1, x2, y2, index)

        elif index == 1:
            x1, y1, x2, y2 = 0, 1, 2, 1
            drawLine(x1, y1, x2, y2, index)

        elif index == 2:
            x1, y1, x2, y2 = 0, 2, 2, 2
            drawLine(x1, y1, x2, y2, index)

        elif index == 3:
            x1, y1, x2, y2 = 0, 0, 0, 2
            drawLine(x1, y1, x2, y2, index)

        elif index == 4:
            x1, y1, x2, y2 = 1, 0, 1, 2
            drawLine(x1, y1, x2, y2, index)

        elif index == 5:
            x1, y1, x2, y2 = 2, 0, 2, 2
            drawLine(x1, y1, x2, y2, index)

        elif index == 6:
            x1, y1, x2, y2 = 0, 0, 3, 3
            drawLine(x1, y1, x2, y2, index)

        elif index == 7:
            x1, y1, x2, y2 = 3, 0, 0, 3
            drawLine(x1, y1, x2, y2, index)


def drawLine(x1, y1, x2, y2, index):
    turtle.pencolor('black')
    turtle.pensize(10)
    if index < 3:  # rows
        turtle.pu()
        turtle.setposition(-230 + x1 * 160, 160 - y1 * 160)
        turtle.pd()
        turtle.setposition(-250 + (x2 + 1) * 160, 160 - y2 * 160)
        time.sleep(2)
    elif 2 < index < 6:  # cols
        turtle.pu()
        turtle.setposition(-160 + x1 * 160, 220 - y1 * 160)
        turtle.pd()
        turtle.setposition(-160 + x2 * 160, 260 - (y2 + 1) * 160)
        time.sleep(2)
    elif 5 < index < 8:  # diagonals
        turtle.pu()
        turtle.setposition(-230 + x1 * 150, 230 - y1 * 160)
        turtle.pd()
        if index == 6:
            turtle.setposition(-260 + x2 * 160, 260 - y2 * 160)
        elif index == 7:
            turtle.setposition(-220 ,-220)
        time.sleep(2)
    new()


def buttonClick(x, y):
    # print(x, y)
    global count

    if state == 'notRunning':
        if -130 < x < -30 and -20 < y < 20:
            start()

    elif state == 'running':
        if 86 <= y <= 235:
            if -234 <= x <= -85:
                regionCode = [0, 0]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif -76 <= x <= 75:
                regionCode = [0, 1]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif 84 <= x <= 234:
                regionCode = [0, 2]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
        elif -74 <= y <= 77:
            if -234 <= x <= -85:
                regionCode = [1, 0]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif -76 <= x <= 75:
                regionCode = [1, 1]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif 84 <= x <= 234:
                regionCode = [1, 2]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
        elif -231 <= y <= -85:
            if -234 <= x <= -85:
                regionCode = [2, 0]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif -76 <= x <= 75:
                regionCode = [2, 1]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)
            elif 84 <= x <= 234:
                regionCode = [2, 2]
                if regionCode not in checkCountList:
                    checkCountList.append(regionCode)
                    count += 1
                    draw(regionCode)

        # print(checkCountList)

    if state == 'notRunning':
        if 20 < x < 120 and -20 < y < 20:
            turtle.clear()
            turtle.bye()


def start():
    turtle.setup(500, 500)
    turtle.pensize(10)
    turtle.hideturtle()

    turtle.clear()
    turtle.color("white")
    global state
    state = 'running'

    global count
    count = 0

    global matrix
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    global checkCountList
    checkCountList = []

    turtle.speed(0)
    for i in range(1, 3):
        turtle.pu()
        turtle.setposition(-230, 240 - 160 * i)
        turtle.pd()
        turtle.forward(460)
        turtle.pu()
    turtle.right(90)
    for i in range(2):
        turtle.penup()
        turtle.setposition(-80 + 160 * i, 230)
        turtle.pendown()
        turtle.forward(460)
    turtle.left(90)

    turtle.speed(0)
    turtle.onscreenclick(buttonClick, 1)
    turtle.listen()


def new():
    turtle.setup(500, 500)
    turtle.speed(0)
    turtle.pensize(5)
    turtle.hideturtle()

    turtle.clear()
    turtle.color('black')
    turtle.pu()
    turtle.setposition(-130, 20)
    turtle.pd()

    choices = ['PLAY', 'QUIT']
    choice_color = ["Green", "Red"]
    for j in range(2):
        turtle.begin_fill()
        turtle.fillcolor(choice_color[j])
        for i in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(90)
        turtle.pu()
        turtle.end_fill()
        turtle.setposition(-100 + 175 * j, -10)
        turtle.pd()
        turtle.color("White")
        turtle.write(choices[j], font=("Arial", 14, "bold"))
        turtle.color("Black")
        turtle.pu()
        turtle.setposition(-100, 20)
        turtle.forward(150)
        turtle.pd()

    global state
    state = 'notRunning'

    turtle.onscreenclick(buttonClick, 1)


if __name__ == '__main__':
    import turtle
    import time
    turtle.title("Tic Tac Toe")
    turtle.Screen().bgpic("C:\\Users\\Lenovo\\Desktop\\wall\\tile.gif")

    new()
    turtle.mainloop()
