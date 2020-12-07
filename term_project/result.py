from pico2d import *
import gfw
import gobj
from tile import Tile
import highscore
SCORE_FONT_SIZE=110
TITLE_FONT_SIZE=30
def enter():
    global title_font, score_font
    gfw.world.init(['bg','button'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('결과배경.png', center))
    pos = get_canvas_width() // 2, 150
    gfw.world.add(gfw.layer.button, gobj.ImageObject('결과화면 버튼.png', pos))
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
    title_font.draw(400 *0.05, 600*0.5, "최고기록:", (0, 0, 0))
    title_font.draw(400 * 0.1, 152, "Q", (21, 159, 179))
    highscore.draw(400 *0.4, 600*0.5)

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

    handle_mouse(e)


capture1 = False
capture2 = False
def handle_mouse(e):
    global capture1, capture2
    if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
        pos = gobj.mouse_xy(e)
        if not capture1:
            if pos[1]<=170 and pos[1]>=120 and pos[0]>=100 and pos[0]<=290:
                capture1 = True
        if not capture2:
            if pos[1]<=170 and pos[1]>=120 and pos[0]>=10 and pos[0]<=90:
                capture2 = True
    if e.type == SDL_MOUSEBUTTONUP and e.button == SDL_BUTTON_LEFT:
        pos = gobj.mouse_xy(e)
        if capture1:
            if pos[1]<=170 and pos[1]>=120 and pos[0]>=100 and pos[0]<=290:
                return gfw.pop()
        if capture2:
            if pos[1]<=170 and pos[1]>=120 and pos[0]>=10 and pos[0]<=90:
                return gfw.quit()

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()