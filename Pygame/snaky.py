import pygame as pg
import random as rnd

pg.init()
pg.display.set_caption("Snaky") # rubriken på fönstret

display_width = 800
display_height = 600
snaky_block = 10

blue = (0,0,233)
white = (220,220,220)
red = (233,0,0)

delta_x = delta_y = 0
x = display_width/2
y = display_height/2

display = pg.display.set_mode((display_width, display_height))

pg.display.update()

clock = pg.time.Clock()
game_over = False

food_x = rnd.randint(0,display_width-snaky_block)
food_y = rnd.randint(0,display_height-snaky_block)

snaky_list = []
snaky_length = 1

# snaky
# snaky_list: [[1,5], [2,1], [30,43]]
def draw_snaky(snaky_block, snaky_list):
    for x in snaky_list:
        pg.draw.rect(display, blue, [x[0], x[1], snaky_block, snaky_block])


# game loop
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                delta_x = -2.5
                delta_y = 0
            elif event.key == pg.K_d:
                delta_x = 2.5
                delta_y = 0
            elif event.key == pg.K_w:
                delta_x = 0
                delta_y = -2.5
            elif event.key == pg.K_s:
                delta_x = 0
                delta_y = 2.5

    # snaky dör när den träffar kanten
#    if x >= display_width or x < 0 or y >= display_height or y < 0:
#        game_over = True
    if x >= display_width:
        x = 0
    elif x < 0:
        x = display_width
    elif y >= display_height:
        y = 0
    elif y < 0:
        y = display_height

    # uppdaterar x- och y-koordinat mha delta_x och delta_y
    x += delta_x
    y += delta_y
    
    display.fill(white)
    # ritar maten
    pg.draw.rect(display, red, [food_x, food_y, snaky_block, snaky_block])

    snaky_head = [x,y]
    snaky_list.append(snaky_head)

    # slänga gamla koordinaten, e.g. "slänger sin svans"
    if len(snaky_list) > snaky_length:
        del snaky_list[0]

    # ritar ormen
    draw_snaky(snaky_block, snaky_list)

    # krockar sin egen kropp med huvudet
    for coordinate in snaky_list[:-1]:
        if coordinate == snaky_head:
            game_over = True


    # käkar matend
    if food_x-7 < x < food_x+7 and food_y-7 < y < food_y+7:
        snaky_length += 2
        food_x = rnd.randint(0, display_width-snaky_block)
        food_y = rnd.randint(0, display_height-snaky_block)

    pg.display.update()

    clock.tick(100)