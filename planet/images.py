import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES_DIR = os.path.join(BASE, 'Resources')
EMB_DIR = os.path.join(BASE, 'embedded')

_cache = {}


def find_image(form, name):
    if name is None:
        return None
    key = (form, name)
    if key in _cache:
        return _cache[key]
    path = None
    if name.startswith('resx:'):
        ref = name[5:].replace('.', '_')
        for f in os.listdir(EMB_DIR):
            if f.startswith(form + '__') and f.endswith('.png') and f.split('__', 1)[1] == ref + '.png':
                path = os.path.join(EMB_DIR, f)
                break
    else:
        cand = os.path.join(RES_DIR, name + '.png')
        if os.path.exists(cand):
            path = cand
    _cache[key] = path
    return path


def app_icon():
    return os.path.join(RES_DIR, 'PLANET.ico')
