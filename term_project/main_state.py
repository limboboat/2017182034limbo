from pico2d import *
import gfw
import gobj
import result
import stage_gen
from tile import Tile

TILE_SPEED = 600
canvas_width = 400
canvas_height = 600
sound_time=0
tile_switch=False
sound = None
END = False
check_start = False
play_sound_time = 0
play_speed = 17
def enter():
    global sound, check_start
    gfw.world.init(['bg', 'tile', 'ui'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('메인배경.png', center))
    gfw.world.add(gfw.layer.ui, gobj.ImageObject('시작 제목.png', (200,100)))
    stage_gen.load(gobj.res('tile.txt'))
    sound = load_music(gobj.res('반짝반짝작은별.mp3'))
    evts = get_events()
    for e in evts:
        handle_event(e)

def update():
    global speed, sound, END, check_start, play_speed
    if Tile.start:
        if check_start == False:
            gfw.world.clear_at(gfw.layer.ui)
            sound.play()
            check_start = True

    if END:
        sound.stop()
        gfw.change(result)
    else:
        if gfw.world.count_at(gfw.layer.tile) == stage_gen.UNIT_PER_LINE-3:
            stage_gen.clear_lines()
            speed += 300
            stage_gen.load(gobj.res('tile.txt'))
        gfw.world.update()
        if Tile.start:
            dy = -TILE_SPEED * gfw.delta_time
        else:
            dy = 0

        for obj in gfw.world.objects_at(gfw.layer.tile):
            obj.move(dy)

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.sound_time > gfw.delta_time * play_speed:
                sound.pause()
            if obj.success_tile:
                check_start = True
                obj.sound_time += gfw.delta_time

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.check_disappearing_tile() == True and obj.success_tile == True:
                gfw.world.remove(obj)
            if obj.check_disappearing_tile() == True and obj.success_tile == False:
                obj.image = gfw.image.load(gobj.res('놓친타일.png'))
                END = True
        stage_gen.update(dy)


def draw():
    gfw.world.draw()

    #gobj.draw_collision_box()

def handle_event(e):
    global sound, check_start
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.change(result)
    for obj in gfw.world.objects_at(gfw.layer.tile):
        obj.handle_event(e)
        if obj.success_tile:
            obj.image = gfw.image.load(gobj.res('빈타일.png'))
            if check_start:
                sound.resume()
            elif check_start == False:
                Tile.start = True

            obj.sound_time = gfw.delta_time
       # elif obj.miss_tile:
       #     obj.image = gfw.image.load(gobj.res('놓친타일.png'))
       #     gfw.world.draw()
       #     sound.stop()
       #     gfw.change(result)
       #     END = True
       #     return True
    return True

def exit():
    global sound
    del sound
    gfw.time.sleep(0.7)
    pass

if __name__=='__main__':
    gfw.run_main()