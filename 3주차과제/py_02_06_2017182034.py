from pico2d import *
import helper as h

RES_DIR='../3주차과제'
dx=0
dy=0
x=0
y=85
tx=-1
ty=-1
speed=1
list_num=0
num=1
goal=[0]

def handle_events():
    global running ,x,y,tx,ty,speed,list_num,goal,num
    evts = get_events()


    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        if (e.type,e.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
            running = False
        if (e.type,e.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
            tx=e.x
            ty=600-e.y
            goal+=[tx]
            goal+=[ty]
            num+=2

def speed_events():
    global running, x, y, tx, ty, speed,dx,dy,list_num,goal,num

    dx=goal[list_num+1]-x
    dy=goal[list_num+2]-y
    evts = get_events()

    if (speed!=1):
        if (dx>-speed) and (dx<speed) and (dy/speed<1) and (dy/speed>-1):
            speed=1
            list_num+=2

    for e in evts:
            if e.type == SDL_QUIT:
                running = False
            if (e.type,e.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                running = False
            if (e.type,e.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
               speed+=1
               tx = e.x
               ty = 600 - e.y
               goal += [tx]
               goal += [ty]
               num+=2



open_canvas()

grass = load_image(RES_DIR + '/grass.png')
character = load_image(RES_DIR + '/run_animation.png')


frame = 0

running=True

while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)

    update_canvas()

    handle_events()




    if (tx==-1):
       x += 1
    elif num > list_num+2 :
           if h.move_toward([x, y], [h.delta([x, y], [goal[list_num+1],goal[list_num+2]], speed)[0], h.delta([x, y], [goal[list_num+1],goal[list_num+2]], speed)[1]], [goal[list_num+1],goal[list_num+2]]) != ([goal[list_num+1],goal[list_num+2]], True):
              x = x + h.delta([x, y], [goal[list_num+1],goal[list_num+2]], speed)[0]
              y = y + h.delta([x, y], [goal[list_num+1],goal[list_num+2]], speed)[1]
              speed_events()
           else :
                list_num += 2




    frame = (frame + 1) % 8

close_canvas()