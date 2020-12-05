from pico2d import *
import gfw
import gobj
from tile import Tile
import highscore
SCORE_FONT_SIZE=110
TITLE_FONT_SIZE=30
def enter():
    global title_font, score_font
    gfw.world.init(['bg'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('결과배경.png', center))
    score_font = gfw.font.load(gobj.res('NanumGothic.TTF'), 100)
    title_font = gfw.font.load(gobj.res('NanumGothic.TTF'), TITLE_FONT_SIZE)
    highscore.load(TITLE_FONT_SIZE)
    highscore.add(Tile.SCORE)

def update():
    gfw.world.update()

def draw():
    global title_font, score_font
    gfw.world.draw()
    title_font.draw(400 * 0.25, 600*0.92, "반짝반짝 작은 별", (255, 255, 255))
    title_font.draw(400 *0.2, 600*0.5, "최고기록:", (0, 0, 0))
    highscore.draw(400 *0.5, 600*0.5)

    count = 0
    tem = Tile.SCORE //10
    if tem == 0:
        score_font.draw(400 * 0.4, 600 * 0.7, "%.0f" % Tile.SCORE, (25, 25, 25))
    elif tem >= 1 and tem < 10:
        score_font.draw(400 * 0.35, 600 * 0.7, "%.0f" % Tile.SCORE, (25, 25, 25))
    elif tem > 10:
        score_font.draw(400 * 0.3, 600 * 0.7, "%.0f" % Tile.SCORE, (25, 25, 25))



def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            return gfw.pop()
        elif e.key == SDLK_s:
            return gfw.pop()

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()