from pico2d import *
import gfw
import gobj
import result
import stage_gen
from tile import Tile

canvas_width = 400
canvas_height = 600

sound = None
END = False
check_start = False
play_sound_time = 0
play_speed = 40

TILE_SPEED = 600
PAUSE_TILE = False

font = None
SCORE_HEIGHT = 30
FONT_SIZE = 20
score_x = canvas_width // 2 - 30
score_y = canvas_height -30
SCORE_TEXT_COLOR = (10, 10, 10)

collision_count = 0

def enter():
    global sound, check_start, font, title_font,title_font2
    gfw.world.init(['bg', 'tile', 'ui', 'score'])
    center = get_canvas_width() // 2, get_canvas_height() // 2

    gfw.world.add(gfw.layer.bg, gobj.ImageObject('메인배경.png', center))
    gfw.world.add(gfw.layer.ui, gobj.ImageObject('시작 제목.png', (200,100)))

    stage_gen.load(gobj.res('tile.txt'))
    sound = load_music(gobj.res('반짝반짝작은별.mp3'))

    font = gfw.font.load(gobj.res('NanumGothic.TTF'), FONT_SIZE+20)
    title_font = gfw.font.load(gobj.res('NanumGothic.TTF'), FONT_SIZE)

    evts = get_events()
    for e in evts:
        handle_event(e)

def update():
    gfw.world.update()
    global speed, sound, END, check_start, play_speed, PAUSE_TILE, collision_count,title_font
    if Tile.start:
        if check_start == False:
            gfw.world.clear_at(gfw.layer.ui)
            sound.play()
            check_start = True

    if END:
        sound.stop()
        gfw.change(result)
    else:
        count=0
        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.success_tile:
                count+=1

        Tile.SCORE=count

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.miss_tile == True:
                obj.image = gfw.image.load(gobj.res('놓친타일.png'))
                END = True

        if Tile.start:
            if PAUSE_TILE == False:
                dy = -TILE_SPEED * gfw.delta_time
        else:
            dy = 0

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.success_tile:
                if check_start:
                    sound.resume()
                obj.sound_time = gfw.delta_time

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if PAUSE_TILE == False:
                obj.move(dy)

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.sound_time > gfw.delta_time * play_speed:
                sound.pause()
            if obj.success_tile:
                check_start = True
                obj.sound_time += gfw.delta_time

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.check_disappearing_tile() == True and obj.success_tile == False:
                obj.image = gfw.image.load(gobj.res('놓친타일.png'))
                obj.miss_tile = True
                END = True
        if PAUSE_TILE == False:
            stage_gen.update(dy)



def draw():
    global font, END, title_font
    gfw.world.draw()
    if check_start == False:
        title_font.draw(60, 125, "반짝반짝 작은 별", SCORE_TEXT_COLOR)
        title_font.draw(60, 80, "최고 점수:", SCORE_TEXT_COLOR)

    font.draw(score_x, score_y, "%.0f" % Tile.SCORE, (255,0,0))


    #gobj.draw_collision_box()

def handle_event(e):
    count =0
    if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
        pos = gobj.mouse_xy(e)
        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.check_collision(pos):
                    count += 1
        if count != 1:
            End = True
    global sound, check_start, END, PAUSE_TILE, collision_count
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.change(result)
        elif e.key == SDLK_p:
            PAUSE_TILE = True
        elif e.key == SDLK_s:
            PAUSE_TILE = False

    for obj in gfw.world.objects_at(gfw.layer.tile):
        obj.handle_event(e)
        if obj.success_tile:
            if check_start == False:
                Tile.start = True


def exit():
    global sound
    del sound
    gfw.time.sleep(0.7)
    pass

if __name__=='__main__':
    gfw.run_main()