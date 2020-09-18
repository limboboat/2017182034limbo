from pico2d import *

open_canvas()
grass = load_image('C:/Users/msi/2d_project/3주차과제/grass.png')
character = load_image('C:/Users/msi/2d_project/3주차과제/animation_sheet.png')

x=0
frame = 0
action=0
while(x<800):
    clear_canvas_now()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 100*action, 100, 100, x, 85)
    update_canvas()
    get_events()

    x += 2
    if x%100 ==0:
        action=(action+1)%4

    frame = (frame + 1) % 8

    delay(0.005)


close_canvas()
