import pickle
from pico2d import *
import time
import gfw

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 1
last_rank = -1
font = None
class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load(size):
    global font, image
    font = gfw.font.load('res/NanumGothic.TTF', size)

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
        # print("Scores:", scores)
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_rank = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_rank = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_rank <= MAX_SCORE_COUNT:
        save()

def draw(x,y):
    global font, last_rank

    for e in scores:
        str = " {:.0f}".format(e.score)
        color = (10, 10, 10)
        font.draw(x, y, str, color)
        #font.draw(320, y, time.asctime(time.localtime(e.time)), color)


def update():
    pass