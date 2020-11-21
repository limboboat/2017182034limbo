from pico2d import *
import gfw
import gobj
import main_state
canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

def start():
    gfw.push(main_state)

def build_world():
    gfw.world.init(['bg','title'])
    center = (canvas_width // 2, canvas_height // 2)
    bg = gobj.ImageObject('메뉴배경.png', center)
    gfw.world.add(gfw.layer.bg, bg)
    pos = (center[0], canvas_height*0.87)
    title = gobj.ImageObject('음악선택이미지.png', pos)
    gfw.world.add(gfw.layer.title, title)

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.change(main_state)

    # print('ms.he()', e.type, e)
def handle_mouse(e):
    pass

def exit():
    print("menu_state exits")
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()