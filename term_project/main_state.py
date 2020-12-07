from pico2d import *
import gfw
import gobj
import result
import stage_gen
import highscore
from tile import Tile

TILE_SPEED = 600
canvas_width = 400
canvas_height = 600

sound = None
sound2 = None
sound3 = None
END = False
check_start = False
play_sound_time = 0
play_speed = 41

font = None
SCORE_HEIGHT = 30
FONT_SIZE = 20
score_x = canvas_width // 2 - 30
score_y = canvas_height -30
SCORE_TEXT_COLOR = (10, 10, 10)
PAUSE_TILE = False
collision_count = 0

def enter():
    global sound, check_start, font, title_font, sound2, sound3

    gfw.world.init(['bg', 'tile', 'ui'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('메인배경.png', center))
    gfw.world.add(gfw.layer.ui, gobj.ImageObject('시작 제목.png', (200, 100)))
    stage_gen.load(gobj.res('tile.txt'))
    sound = load_music(gobj.res('반짝반짝작은별.mp3'))
    sound2 = load_music(gobj.res('반짝반짝작은별2.mp3'))
    sound3 = load_music(gobj.res('반짝반짝작은별3.mp3'))
    font = gfw.font.load(gobj.res('NanumGothic.TTF'), FONT_SIZE + 20)
    title_font = gfw.font.load(gobj.res('NanumGothic.TTF'), FONT_SIZE)
    highscore.load(FONT_SIZE)

    global END, check_start, play_speed, collision_count
    END = False
    check_start = False
    play_sound_time = 0
    collision_count = 0
    Tile.start = False
    Tile.SCORE = 0

    evts = get_events()
    for e in evts:
        handle_event(e)


def update():
    global speed, sound, END, check_start, play_speed, PAUSE_TILE, collision_count, title_font,TILE_SPEED, sound2, sound3
    if Tile.start:
        if check_start == False:
            gfw.world.clear_at(gfw.layer.ui)
            sound.play()
            check_start = True
    if END:
        if stage_gen.get_map_index() < 200:
            sound.stop()
        elif stage_gen.get_map_index() < 380:
            sound2.stop()
        elif stage_gen.get_map_index() < 580:
            sound3.stop()

        gfw.change(result)
    else:

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.miss_tile == True:
                obj.image = gfw.image.load(gobj.res('놓친타일.png'))
                #END = True

        gfw.world.update()
        if Tile.start:
            if PAUSE_TILE == False:
                dy = -TILE_SPEED * gfw.delta_time
        else:
            dy = 0

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if PAUSE_TILE == False:
                obj.move(dy)

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.sound_time > gfw.delta_time * play_speed:
                if stage_gen.get_map_index() < 190:
                    sound.pause()
                elif stage_gen.get_map_index() < 380:
                    sound2.pause()
                elif stage_gen.get_map_index() < 570:
                    sound3.pause()

            if obj.success_tile:
                check_start = True
                obj.sound_time += gfw.delta_time

        for obj in gfw.world.objects_at(gfw.layer.tile):
            if obj.check_disappearing_tile() == True and obj.success_tile == True:
                gfw.world.remove(obj)
            if obj.check_disappearing_tile() == True and obj.success_tile == False:
                obj.image = gfw.image.load(gobj.res('놓친타일.png'))
                obj.miss_tile = True
                END = True
            if stage_gen.get_map_index() == 570:
                END = True
            if stage_gen.get_map_index() ==193:
                TILE_SPEED = 650
                sound.stop()
            elif stage_gen.get_map_index() ==198:
                sound2.play()
            elif stage_gen.get_map_index() ==375:
                TILE_SPEED = 670
                sound2.stop()
            elif stage_gen.get_map_index() ==388:
                sound3.play()

        if PAUSE_TILE == False:
             stage_gen.update(dy)


def draw():
    global font, END, title_font
    gfw.world.draw()
    if check_start == False:
        title_font.draw(60, 125, "반짝반짝 작은 별", SCORE_TEXT_COLOR)
        title_font.draw(60, 80, "최고 점수:", SCORE_TEXT_COLOR)
        highscore.draw(150, 80)

    font.draw(score_x, score_y, "%.0f" % Tile.SCORE, (255, 0, 0))

                # gobj.draw_collision_box()

def handle_event(e):
    global sound, check_start, score, END, PAUSE_TILE, collision_count,sound2,sound3
    if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
        pos = gobj.mouse_xy(e)


    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            return gfw.change(result)
        elif e.key == SDLK_p:
            PAUSE_TILE = True
            sound.pause()
        elif e.key == SDLK_s:
            PAUSE_TILE = False
            sound.resume()

    for obj in gfw.world.objects_at(gfw.layer.tile):
        obj.handle_event(e)

        if obj.success_tile:
            if check_start:
                if stage_gen.get_map_index() > 0:
                    sound.resume()
                elif stage_gen.get_map_index() > 193:
                    sound2.resume()
                elif stage_gen.get_map_index() > 370:
                    sound3.resume()
                continue
            elif check_start == False:
                Tile.start = True
        obj.sound_time = 0



def exit():
    global sound ,sound2, sound3
    del sound, sound2, sound3
    gfw.time.sleep(0.7)
    pass

if __name__ == '__main__':
    gfw.run_main()