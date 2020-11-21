import random
from pico2d import *
import gfw
import gobj

class Tile:

    TYPE_1, TYPE_2, TYPE_3 = range(3)

    def __init__(self, type, x, y):
        self.x, self.y = x, y
        if type == Tile.TYPE_1:
            self.image = gfw.image.load(gobj.res('시작타일.png'))
            self.rect = 50, 75
        elif type == Tile.TYPE_2:
            self.image = gfw.image.load(gobj.res('타일.png'))
            self.rect = 50, 75
        elif type == Tile.TYPE_3:
            self.image = gfw.image.load(gobj.res('긴타일.png'))
            self.rect = 50, 150
        index = type

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                Tile.remove()
                return True
        return False

    def move(self, dy):
        self.y += dy
        if self.y + self.y < 0:
            gfw.world.remove(self)

    def get_bb(self):
        return (
            self.x - self.rect[0], self.y - self.rect[1],
            self.x + self.rect[0], self.y + self.rect[1]
        )