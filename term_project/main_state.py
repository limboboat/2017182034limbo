from pico2d import *
import gfw
import gobj
import result
import stage_gen
from tile import Tile

TILE_SPEED = 1000
canvas_width = 400
canvas_height = 600

def enter():
    gfw.world.init(['bg', 'tile'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('메인배경.png', center))

    stage_gen.load(gobj.res('tile.txt'))


def update():
    global speed
    if gfw.world.count_at(gfw.layer.tile) == stage_gen.UNIT_PER_LINE-3:
        stage_gen.clear_lines()
        speed += 300
        stage_gen.load(gobj.res('tile.txt'))
    gfw.world.update()
    dy = -TILE_SPEED * gfw.delta_time
    for obj in gfw.world.objects_at(gfw.layer.tile):
        obj.move(dy)

    stage_gen.update(dy)

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.change(result)

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()