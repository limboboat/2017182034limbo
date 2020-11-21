import gfw
from pico2d import *
import gobj
from tile import Tile


UNIT_PER_LINE = 77
SCREEN_LINES = 4
BLOCK_SIZE = (100, 150)

lines = []

def load(file):
    global lines, current_y, create_at, map_index
    with open(file, 'r') as f:
        lines = f.readlines()
    current_y = 0
    map_index = 0
    create_at = get_canvas_height() + 2 * BLOCK_SIZE[1]

def update(dy):
    global current_y, create_at
    current_y += dy
    while current_y < create_at:
        create_column()

def create_column():
    global current_y, map_index
    x = BLOCK_SIZE[0] // 2
    for line in range(SCREEN_LINES):
        cw = get(map_index, line)
        create_object(cw, x, current_y)
        x += BLOCK_SIZE[0]
    current_y += BLOCK_SIZE[1]
    map_index += 1
    print('map_index:', map_index)

def create_object(cw, x, y):
    if cw in ['1', '2', '3']:
        obj = Tile(ord(cw) - ord('1'), x, y)
        gfw.world.add(gfw.layer.tile, obj)
        print('creating Tile', cw, x, y)


def get(x, y):
    col = x % UNIT_PER_LINE
    line = (x // UNIT_PER_LINE * SCREEN_LINES) + SCREEN_LINES - 1 - y
    return lines[col][line]

def count():
    return len(lines) // SCREEN_LINES * UNIT_PER_LINE

def test_gen():
    load(gobj.res('tile.txt'))
    print('count=', count())
    line = 0
    for y in range(UNIT_PER_LINE):
        s = ''
        for x in range(SCREEN_LINES):
            s += get(x, y)
        line += 1
    print('%03d:' % line, s)

def clear_lines():
    gfw.world.clear_at(lines)

def test_gen_2():
    global current_y, map_index, create_at, speed
    open_canvas()
    gfw.world.init(['tile'])
    load(gobj.res('tile.txt'))
    #for i in range(UNIT_PER_LINE):
    #    if i == UNIT_PER_LINE:
    #        current_y=0
    #        current_y = 0
    #        map_index = 0
    #        create_at = get_canvas_height() + 2 * BLOCK_SIZE[1]
    #        speed += 0.5
    #        i = 0
    update(0.1)
    close_canvas()

if __name__ == '__main__':
    test_gen_2()