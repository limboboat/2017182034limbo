from pico2d import *
import gfw
import gobj

def enter():
    gfw.world.init(['bg'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('결과배경.png', center))
def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        elif e.key == SDLK_s:
            return gfw.change(menu_state)

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()