import math
from collections import namedtuple

RTV = namedtuple('RTV', ['A', 'B', 'C'])


def vbval(s):
    if s is None:
        return 0.0
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).lstrip()
    if not s:
        return 0.0
    i = 0
    if i < len(s) and s[i] in '+-':
        i += 1
    j = i
    dot = False
    while j < len(s) and (s[j].isdigit() or (s[j] == '.' and not dot)):
        if s[j] == '.':
            dot = True
        j += 1
    if j == i:
        return 0.0
    try:
        return float(s[:j])
    except ValueError:
        return 0.0


def vbint(x):
    x = float(x)
    if x != x or x in (float('inf'), float('-inf')):
        return x
    return math.floor(x)


def vdiv(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        if a == 0:
            return float('nan')
        return float('inf') if a > 0 else float('-inf')
    return a / b


def vasin(x):
    try:
        return math.asin(float(x))
    except (ValueError, OverflowError):
        return float('nan')


def vacos(x):
    try:
        return math.acos(float(x))
    except (ValueError, OverflowError):
        return float('nan')


def vsqrt(x):
    try:
        return math.sqrt(float(x))
    except (ValueError, OverflowError):
        return float('nan')


def vbcstr(x):
    if isinstance(x, bool):
        return 'True' if x else 'False'
    if isinstance(x, int):
        return str(x)
    x = float(x)
    if x != x:
        return 'NaN'
    if x == float('inf'):
        return '\u221e'
    if x == float('-inf'):
        return '-\u221e'
    if x == 0:
        return '0'
    neg = x < 0
    ax = abs(x)
    if ax >= 1e15 or ax < 1e-4:
        s = f'{ax:.14E}'
        m, e = s.split('E')
        m = m.rstrip('0').rstrip('.')
        exp = int(e)
        es = ('+' if exp >= 0 else '-') + f'{abs(exp):02d}'
        s = m + 'E' + es
    else:
        e = math.floor(math.log10(ax))
        dec = max(0, 14 - int(e))
        s = f'{ax:.{dec}f}'
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
    return ('-' if neg else '') + s


def vbs(x):
    x = float(x)
    if x != x:
        return 'NaN'
    if x == float('inf'):
        return '\u221e'
    if x == float('-inf'):
        return '-\u221e'
    if x == 0:
        return ' 0'
    neg = x < 0
    ax = abs(x)
    if ax >= 1e6 or ax < 1e-5:
        s = f'{ax:.5E}'
        m, e = s.split('E')
        m = m.rstrip('0').rstrip('.')
        exp = int(e)
        es = ('+' if exp >= 0 else '-') + f'{abs(exp):02d}'
        s = m + 'E' + es
    else:
        s = vbcstr(ax)
        if 0 < ax < 1 and s.startswith('0.'):
            s = s[1:]
    return ('-' if neg else ' ') + s


def cv(num):
    cal = (num + 0.0005) * 1000
    cal = vbint(cal) / 1000
    st = vbs(cal).replace(' ', '')
    st = st.replace('-.', '-0.')
    if vbval(st) != 0 and '.' not in st:
        st = st + '.0'
    if vbval(st) != 0 and vbint(vbval(st)) == 0:
        st = '0' + st
    return st


def cv2(num):
    cal = (num + 0.009) * 100
    cal = vbint(cal) / 100
    st = vbs(cal).replace(' ', '')
    st = st.replace('-.', '-0.')
    if vbval(st) != 0 and '.' not in st:
        st = st + '.0'
    if vbval(st) != 0 and vbint(vbval(st)) == 0:
        st = '0' + st
    return st


def cv3(num):
    cal = num + 0.5
    cal = vbint(cal)
    return vbs(cal).replace(' ', '')


def cv4(num):
    cal = (num + 0.05) * 10
    cal = vbint(cal) / 10
    st = vbs(cal).replace(' ', '')
    st = st.replace('-.', '-0.')
    if vbval(st) != 0 and '.' not in st:
        st = st + '.0'
    if vbval(st) != 0 and vbint(vbval(st)) == 0:
        st = '0' + st
    return st


def tank(big, small, degree):
    if degree < 45:
        cal = ((big - small) / 2 / math.tan(degree * (math.pi / 180)) + 0.0005) * 1000
    else:
        cal = ((big - small) / 2 * math.tan((90 - degree) * (math.pi / 180)) + 0.0005) * 1000
    cal = vbint(cal) / 1000
    return cal


def tank2(kei, degree):
    if degree < 45:
        cal = (kei / 2 / math.tan(degree * (math.pi / 180)) + 0.0005) * 1000
    else:
        cal = (kei / 2 * math.tan((90 - degree) * (math.pi / 180)) + 0.0005) * 1000
    cal = vbint(cal) / 1000
    return cal


def tann(nagate, degree):
    if degree < 45:
        cal = (nagate * math.tan(degree * (math.pi / 180)) + 0.0005) * 1000
    else:
        cal = (nagate / math.tan((90 - degree) * (math.pi / 180)) + 0.0005) * 1000
    cal = vbint(cal) / 1000
    return cal


def rt(degree, r):
    b = (180 - degree) / 2
    c = 90 - b
    cal = (math.tan(c * (math.pi / 180)) * r + 0.0005) * 1000
    cal = vbint(cal) / 1000
    a = cal
    cal = (math.sin(degree * (math.pi / 180)) * a + 0.0005) * 1000
    cal = vbint(cal) / 1000
    bb = cal
    if degree < 45:
        cal = (bb / math.tan(degree * (math.pi / 180)) + 0.0005) * 1000
    else:
        cal = (bb * math.tan((90 - degree) * (math.pi / 180)) + 0.0005) * 1000
    cal = vbint(cal) / 1000
    c2 = cal
    return RTV(a, bb, c2)


def vbnarrow(s):
    out = []
    for ch in s:
        cp = ord(ch)
        if 0xFF01 <= cp <= 0xFF5E:
            out.append(chr(cp - 0xFEE0))
        elif cp == 0x3000:
            out.append(' ')
        else:
            out.append(ch)
    return ''.join(out)
