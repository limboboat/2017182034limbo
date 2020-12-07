from pico2d import *
import gfw
import gobj
import main_state
canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height
main_sound = None
def start():
    gfw.push(main_state)

def build_world():
    global title
    gfw.world.init(['bg','title'])
    center = (canvas_width // 2, canvas_height // 2)
    bg = gobj.ImageObject('메뉴배경.png', center)
    gfw.world.add(gfw.layer.bg, bg)
    pos = (center[0], canvas_height*0.87)
    title = gobj.ImageObject('음악선택이미지.png', pos)
    gfw.world.add(gfw.layer.title, title)
    global main_sound
    main_sound = load_music(gobj.res('반짝반짝작은별.mp3'))

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    global main_sound
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            main_sound.stop()
            del main_sound
            return gfw.push(main_state)
    handle_mouse(e)


capture = False
def handle_mouse(e):
    global main_sound, capture , title
    if e.type == SDL_MOUSEMOTION:
        pos = gobj.mouse_xy(e)
        if not capture:
            if pos[1]<=canvas_height*0.87+50 and pos[1]>=canvas_height*0.87-50:
                main_sound.play()
                for obj in gfw.world.objects_at(gfw.layer.title):
                    obj.image = gfw.image.load(gobj.res('음악선택이미지클릭.png'))
                capture = True
                return False
        if capture:
            if pos[1]>canvas_height*0.87+50 or pos[1]<canvas_height*0.87-50:
                main_sound.stop()
                for obj in gfw.world.objects_at(gfw.layer.title):
                    obj.image = gfw.image.load(gobj.res('음악선택이미지.png'))
                capture = False
                return False
    if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
        pos = gobj.mouse_xy(e)
        if pos[1]<=canvas_height*0.87 and pos[1]>=canvas_height*0.87-50 and pos[0]>canvas_width//2 and pos[0]<canvas_width*0.9:
            main_sound.stop()
            del main_sound
            return gfw.push(main_state)
    return False

def exit():

    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()