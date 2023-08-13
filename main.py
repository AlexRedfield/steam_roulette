import random
import vdf
from subprocess import run

import sqlite3
def get_library() -> list:
    d = vdf.load(open('D:\Steam\steamapps\libraryfolders.vdf'))
    raw_lib = list(d.get('libraryfolders').get('0').get('apps').keys())
    except_list = [228980, 431960]
    return list(set(raw_lib) - set(except_list))


def roulette(games: list):
    luck = random.choice(games)
    cmd_str = f'Start steam://rungameid/{luck} -perfectworld'
    run(cmd_str, shell=True)


if __name__ == '__main__':
    library = get_library()
    roulette(library)
