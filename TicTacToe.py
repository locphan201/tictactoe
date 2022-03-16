import pygame as pg

pg.init()
window = pg.display.set_mode((290, 290))
pg.display.set_caption('Tic Tac Toe')
icon = pg.image.load('thumb.png')
pg.display.set_icon(icon)

def setup():
    box = [[None, None, None], [None, None, None], [None, None, None]]
    return box

def draw_grid(window, size):
    window.fill((0, 0, 0))
    for i in range(2):
        pg.draw.line(window, (255, 255, 255), (10+size*(i+1), 10), (10+size*(i+1), 10+size*3), 2)
        pg.draw.line(window, (255, 255, 255), (10, 10+size*(i+1)), (10+size*3, 10+size*(i+1)), 2)

def draw_xo(window, box, size):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == True:
                pg.draw.circle(window, RED, (10+(i+0.5)*size, 10+(j+0.5)*size), size/2-10, 4)
            elif box[i][j] == False:
                pg.draw.line(window, GREEN, (20+i*size, 20+j*size), ((i+1)*size, (j+1)*size), 4)
                pg.draw.line(window, GREEN, (20+i*size, (j+1)*size), ((i+1)*size, 20+j*size), 4)

def check(window, box, size):
    for i in range(3):
        col = box[i]
        if col[0] == False or col[0] == True:
            if col[0] == col[1] == col[2]:
                pg.draw.line(window, (0, 255, 255), (10+(i+0.5)*size, 10+0.5*size), (10+(i+0.5)*size, 280-0.5*size), 2)
                return True

    for i in range(3):
        row = [box[0][i], box[1][i], box[2][i]]
        if row[0] == False or row[0] == True:
            if row[0] == row[1] == row[2]:
                pg.draw.line(window, (0, 255, 255), (10+0.5*size, 10+(i+0.5)*size), (280-0.5*size, 10+(i+0.5)*size), 2)
                return True

    hori1 = [box[0][0], box[1][1], box[2][2]]
    if hori1[0] == False or hori1[0] == True:
        if hori1[0] == hori1[1] == hori1[2]:
            pg.draw.line(window, (0, 255, 255), (10+0.5*size, 10+0.5*size), (280-0.5*size, 280-0.5*size), 2)
            return True

    hori2 = [box[2][0], box[1][1], box[0][2]]
    if hori2[0] == False or hori2[0] == True:
        if hori2[0] == hori2[1] == hori2[2]:
            pg.draw.line(window, (0, 255, 255), (10+0.5*size, 280-0.5*size), (280-0.5*size, 10+0.5*size), 2)
            return True
    return False

def win_announce(window, turn):
    rect = pg.Rect(50, 95, 190, 100)
    pg.draw.rect(window, (150, 150, 255), rect)
    font = pg.font.SysFont('Arial', 30)
    text_surface = font.render('WINS!', True, (0, 0, 0))
    if turn == 0:
        pg.draw.circle(window, (255, 0, 0), (95, 145), 25, 4)
    else:
        pg.draw.line(window, (0, 255, 0), (70, 120), (120, 170), 4)
        pg.draw.line(window, (0, 255, 0), (70, 170), (120, 120), 4)
    window.blit(text_surface, (135, 130))

def main(window):
    running = True
    clock = pg.time.Clock()
    fps = 60
    size = 90
    turn = True
    box = setup()
    win = False

    while running:
        clock.tick(fps)
        x, y = pg.mouse.get_pos()
        draw_grid(window, size)
        draw_xo(window, box, size)
        win = check(window, box, size)
        if win:
            win_announce(window, turn)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                ind_x = (x-10)//size
                ind_y = (y-10)//size
                if win == False and box[ind_x][ind_y] == None:
                    box[ind_x][ind_y] = turn
                    turn = not turn
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if win:
                        win == False
                        box = [[None, None, None], [None, None, None], [None, None, None]]

        pg.display.update()   

if __name__ == '__main__':
    main(window)