import random
from pico2d import *
import gfw
import gobj

GENERATION_TILE_SIZE = 50, 75
LONG_TILE_SIZE = 50, 150

class Tile:
    SCORE =0
    start = None
    TYPE_1, TYPE_2, TYPE_3 = range(3)

    def __init__(self, type, x, y):
        self.x, self.y = x, y
        if type == Tile.TYPE_1:
            self.image = gfw.image.load(gobj.res('시작타일.png'))
            self.rect = GENERATION_TILE_SIZE[0], GENERATION_TILE_SIZE[1]
        elif type == Tile.TYPE_2:
            self.image = gfw.image.load(gobj.res('타일.png'))
            self.rect = GENERATION_TILE_SIZE[0], GENERATION_TILE_SIZE[1]
        elif type == Tile.TYPE_3:
            self.image = gfw.image.load(gobj.res('긴타일.png'))
            self.rect = GENERATION_TILE_SIZE[0], GENERATION_TILE_SIZE[1]
        self.success_tile = False
        self.sound_time = 0
        self.miss_tile = False
        self.mouse_x=0
        self.mouse_y=0
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    # def handle_event(self, e):
    #     if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
    #         pos = gobj.mouse_xy(e)
    #         self.check_collision(pos)

    def move(self, dy):
        self.y += dy

    def check_collision(self, pos):
        if gobj.pt_in_rect(pos, self.get_bb()):
            self.success_tile = True
            self.image = gfw.image.load(gobj.res('빈타일.png'))
            Tile.SCORE += 1
       # else:
       #     self.miss_tile = True
       #     self.image = gfw.image.load(gobj.res('놓친타일.png'))


    def check_disappearing_tile(self):
        if self.y + self.y < 150:
            return True
        return False
    def get_bb(self):
        return (
            self.x - self.rect[0], self.y - self.rect[1],
            self.x + self.rect[0], self.y + self.rect[1]
        )