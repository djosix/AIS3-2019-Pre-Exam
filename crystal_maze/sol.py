import sys, time
from firstblood.all import *

HOST = sys.argv[1]
PORT = int(sys.argv[2])

def test(path):
    t = time.time()
    c = uio.tcp(HOST, PORT).lines([move + '\n' for move in path])
    result = [c.readline() for _ in range(2 + len(path))][-1].strip().split()[1]
    print(time.time() - t)
    if result == 'ok':
        return True
    elif result not in ('timeout', 'wall'):
        print(result)
        sys.exit()
    return False

moves = {
    'up': lambda x, y: (x, y + 1),
    'right': lambda x, y: (x + 1, y),
    'down': lambda x, y: (x, y - 1),
    'left': lambda x, y: (x - 1, y),
}

def dfs(path=[], visited=[(0, 0)]):
    pos = visited[-1]
    for move, move_func in moves.items():
        pos_ = move_func(*pos)
        if pos_ not in visited:
            path_ = path + [move]
            if test(path_):
                dfs(path_, visited + [pos_])

dfs()
