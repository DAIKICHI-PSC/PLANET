import math

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

from .layout import FormBuilder
from .splitter import splitter
from .vbcommon import vbval, vbs
from .images import app_icon
from . import formreg


def _intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    a2 = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    b1 = (x3 - x4) * (y1 - y3) + (y3 - y4) * (x3 - x1)
    b2 = (x3 - x4) * (y2 - y3) + (y3 - y4) * (x3 - x2)
    return (a1 * a2) < 0.0 and (b1 * b2) < 0.0


def _circle_dot_hit(r, x, y):
    r -= 0.001
    return (0 - x) * (0 - x) + (0 - y) * (0 - y) <= r * r


def _utcrs_crl_lne(ax, ay, bx, by, my_rad):
    my_rad -= 0.001
    res = 0
    for sx0, sy0 in ((ax - bx, ay - by), (bx - ax, by - ay)):
        sx = sx0
        sy = sy0
        length = math.sqrt((sx * sx) + (sy * sy))
        if length > 0:
            length = 1 / length
        sx *= length
        sy *= length
        nx = sy * -1
        ny = sx
        sx = nx * -1 * my_rad
        sy = ny * -1 * my_rad
        d = (ax * nx + ay * ny) * -1
        denom = (nx * sx + ny * sy)
        if denom == 0:
            continue
        t = (nx * 0 + ny * 0 + d) * -1 / denom
        if 0 <= t <= 1:
            cx = 0 + t * sx
            cy = 0 + t * sy
            acx = cx - ax
            acy = cy - ay
            bcx = cx - bx
            bcy = cy - by
            if (acx * bcx) + (acy * bcy) <= 0:
                res = 1
    return res


def _geometry_hit(heimen, xmv, zmv, ymv, ncx, ncy, ncz, exx, exy, exz, zhit, d, xd, mill, guard):
    zl = 10000.0
    hit = False
    bound = d + xd + mill * 2
    if heimen == 'X':
        # X axis, XZ plane
        if xmv == 1 and guard and ncy < bound and ncy > bound * -1:
            if ncz > zhit and ncx < d + xd:
                hit = True
            else:
                px2 = ncz if zmv == 0 else exz
                py2 = exx
                if _intersect(ncz, ncx, px2, py2, zhit, d + xd, zl, d + xd) or \
                   _intersect(ncz, ncx, px2, py2, zhit, d + xd, zhit, (d + xd) * -1) or \
                   _intersect(ncz, ncx, px2, py2, zhit, (d + xd) * -1, zl, (d + xd) * -1):
                    hit = True
        # Z axis, XZ plane
        if zmv == 1 and guard and ncy < bound and ncy > bound * -1:
            if ncz > zhit and ncx < d + xd:
                hit = True
            else:
                px2 = exz
                py2 = ncx if xmv == 0 else exx
                if _intersect(ncz, ncx, px2, py2, zhit, d + xd, zl, d + xd) or \
                   _intersect(ncz, ncx, px2, py2, zhit, d + xd, zhit, (d + xd) * -1) or \
                   _intersect(ncz, ncx, px2, py2, zhit, (d + xd) * -1, zl, (d + xd) * -1):
                    hit = True
        # Y axis, XZ plane
        if ymv == 1 and guard and ncz > zhit:
            if _circle_dot_hit(d + xd, ncx, ncy) or _circle_dot_hit(d + xd, ncx, ncy + mill * 2) or _circle_dot_hit(d + xd, ncx, ncy + mill * -2):
                hit = True
            else:
                if xmv == 0:
                    if _circle_dot_hit(d + xd, ncx, exy) or _circle_dot_hit(d + xd, ncx, exy + mill * 2) or _circle_dot_hit(d + xd, ncx, exy + mill * -2):
                        hit = True
                    elif _utcrs_crl_lne(ncx, ncy, ncx, exy, d + xd) == 1 or _utcrs_crl_lne(ncx, ncy + mill * 2, ncx, exy + mill * 2, d + xd) == 1 or _utcrs_crl_lne(ncx, ncy + mill * -2, ncx, exy + mill * -2, d + xd) == 1:
                        hit = True
                else:
                    if _circle_dot_hit(d + xd, exx, exy) or _circle_dot_hit(d + xd, exx, exy + mill * 2) or _circle_dot_hit(d + xd, exx, exy + mill * -2):
                        hit = True
                    elif _utcrs_crl_lne(ncx, ncy, exx, exy, d + xd) == 1 or _utcrs_crl_lne(ncx, ncy + mill * 2, exx, exy + mill * 2, d + xd) == 1 or _utcrs_crl_lne(ncx, ncy + mill * -2, exx, exy + mill * -2, d + xd) == 1:
                        hit = True
    else:
        # Y axis, YZ plane
        if ymv == 1 and guard and ncx < bound and ncx > bound * -1:
            if ncz > zhit and ncy < d + xd:
                hit = True
            else:
                px2 = ncz if zmv == 0 else exz
                py2 = exy
                if _intersect(ncz, ncy, px2, py2, zhit, d + xd, zl, d + xd) or \
                   _intersect(ncz, ncy, px2, py2, zhit, d + xd, zhit, (d + xd) * -1) or \
                   _intersect(ncz, ncy, px2, py2, zhit, (d + xd) * -1, zl, (d + xd) * -1):
                    hit = True
        # Z axis, YZ plane
        if zmv == 1 and guard and ncx < bound and ncx > bound * -1:
            if ncz > zhit and ncy < d + xd:
                hit = True
            else:
                px2 = exz
                py2 = ncy if ymv == 0 else exy
                if _intersect(ncz, ncy, px2, py2, zhit, d + xd, zl, d + xd) or \
                   _intersect(ncz, ncy, px2, py2, zhit, d + xd, zhit, (d + xd) * -1) or \
                   _intersect(ncz, ncy, px2, py2, zhit, (d + xd) * -1, zl, (d + xd) * -1):
                    hit = True
        # X axis, YZ plane
        if xmv == 1 and guard and ncz > zhit:
            if _circle_dot_hit(d + xd, ncx, ncy) or _circle_dot_hit(d + xd, ncx, ncy + mill * 2) or _circle_dot_hit(d + xd, ncx, ncy + mill * -2):
                hit = True
            else:
                if ymv == 0:
                    if _circle_dot_hit(d + xd, exx, ncy) or _circle_dot_hit(d + xd, exx + mill * 2, ncy) or _circle_dot_hit(d + xd, exx + mill * -2, ncy):
                        hit = True
                    elif _utcrs_crl_lne(ncx, ncy, exx, ncy, d + xd) == 1 or _utcrs_crl_lne(ncx + mill * 2, ncy, exx + mill * 2, ncy, d + xd) == 1 or _utcrs_crl_lne(ncx + mill * -2, ncy, exx + mill * -2, ncy, d + xd) == 1:
                        hit = True
                else:
                    if _circle_dot_hit(d + xd, exx, exy) or _circle_dot_hit(d + xd, exx + mill * 2, exy) or _circle_dot_hit(d + xd, exx + mill * -2, exy):
                        hit = True
                    elif _utcrs_crl_lne(ncx, ncy, exx, exy, d + xd) == 1 or _utcrs_crl_lne(ncx + mill * 2, ncy, exx + mill * 2, exy, d + xd) == 1 or _utcrs_crl_lne(ncx + mill * -2, ncy, exx + mill * -2, exy, d + xd) == 1:
                        hit = True
    return hit


class _HideFilter(QObject):
    def __init__(self, form_obj):
        super().__init__()
        self._fo = form_obj

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            self._fo.w.hide()
            event.ignore()
            return True
        return False


def _yn(parent, text, title='\u78ba\u8a8d'):
    r = QMessageBox.question(parent, title, text,
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    return r == QMessageBox.Yes


class CncChk:
    def __init__(self):
        fb = FormBuilder('CNC_CHK')
        self.w = fb.build()
        self.w.setWindowIcon(QIcon(app_icon()))
        self.controls = fb.controls
        if 'TextBox1' in self.controls:
            self.controls['TextBox1'].setVisible(False)
        self.program = ''
        self._hide_filter = _HideFilter(self)
        self.w.installEventFilter(self._hide_filter)
        formreg.register('CNC_CHK', self)

    def set_program(self, text):
        self.program = text

    def _center_crossed(self, axis_kanji, letter, v):
        msg = axis_kanji + '\u8ef8\u304c\u6750\u6599\u306e\u4e2d\u5fc3\u3092\u8d8a\u3048\u307e\u3057\u305f\uff08' + letter + \
                vbs(v).replace(' ', '') + '\uff09\u3002\n\u6750\u6599\u306f\u5207\u308a\u843d\u3068\u3055\u308c\u307e\u3057\u305f\u304b\uff1f'
        return _yn(self.w, msg)

    def check_hit(self, d, xd, zd):
        self._check_xy(d, xd, zd, 0.0, False)

    def check_hit_f(self, d, xd, zd, fd):
        self._check_xy(d, xd, zd, fd, True)

    def check_hit_d(self, d, zd, fd):
        self._check_d(d, zd, fd)

    def _check_xy(self, d, xd, zd, fd, fmode):
        lst = self.controls['ListBox1']
        lst.clearSelection()
        nc = splitter(self.program)
        if nc is None:
            return
        nc_x = 100.0
        nc_z = 0.0
        nc_y = 100.0
        g_zero = 0
        tanmen = 0.0
        exx = 100.0
        exz = 0.0
        exy = 100.0
        dwel = 0
        hasaki = 0
        heimen = 'X'
        shift = 0.0
        mill = 0.0
        f = 0.0
        for i in range(len(nc)):
            xmv = zmv = ymv = 0
            dwel = 0
            hasaki = 0
            cb = 0
            while nc[i].command[cb] != '':
                cmd = nc[i].command[cb]
                val = nc[i].value[cb]
                if cmd == 'X':
                    exx = nc_x
                    nc_x = vbval(val)
                    xmv = 1
                    if nc_x < 0 and nc_z > tanmen and self._center_crossed('\uff38', 'X', nc_x):
                        tanmen = nc_z
                elif cmd == 'U':
                    if dwel == 0 and hasaki == 0:
                        exx = nc_x
                        nc_x += vbval(val)
                        xmv = 1
                        if nc_x < 0 and nc_z > tanmen and self._center_crossed('\uff38', 'X', nc_x):
                            tanmen = nc_z
                elif cmd == 'Z':
                    exz = nc_z
                    nc_z = vbval(val)
                    zmv = 1
                elif cmd == 'W':
                    if hasaki == 0:
                        exz = nc_z
                        nc_z += vbval(val)
                        zmv = 1
                elif cmd == 'Y':
                    exy = nc_y
                    nc_y = vbval(val)
                    ymv = 1
                    if nc_y < 0 and nc_z > tanmen and self._center_crossed('\uff39', 'Y', nc_y):
                        tanmen = nc_z
                elif cmd == 'V':
                    if hasaki == 0:
                        exy = nc_y
                        nc_y += vbval(val)
                        ymv = 1
                    if nc_y < 0 and nc_z > tanmen and self._center_crossed('\uff39', 'Y', nc_y):
                        tanmen = nc_z
                elif cmd == 'G':
                    gv = vbval(val)
                    if gv == 0:
                        g_zero = 0
                        dwel = 0
                    if gv in (1, 2, 3):
                        g_zero = 1
                        dwel = 0
                    if gv == 4:
                        dwel = 1
                    if gv in (40, 41, 42):
                        hasaki = 1
                elif cmd == 'T':
                    if vbval(val) >= 100:
                        heimen = 'X'
                        shift = 0.0
                        mill = 0.0
                        if cb + 1 < len(nc[i].command) and nc[i].command[cb + 1] == '(':
                            ptext = nc[i].value[cb + 1].replace(')', '')
                            pnc = splitter(ptext + '\r\n')
                            if pnc:
                                pc = 0
                                while pnc[0].command[pc] != '':
                                    pcmd = pnc[0].command[pc]
                                    if pcmd == 'X':
                                        heimen = 'X'
                                        shift = vbval(pnc[0].value[pc])
                                    elif pcmd == 'Y':
                                        heimen = 'Y'
                                        shift = vbval(pnc[0].value[pc])
                                    elif pcmd == 'D':
                                        mill = vbval(pnc[0].value[pc])
                                    pc += 1
                        if heimen == 'X':
                            exx = nc_x
                            nc_x = 100.0
                            nc_y = 0.0
                            xmv = 1
                            g_zero = 0
                        if heimen == 'Y':
                            exy = nc_y
                            nc_x = 0.0
                            nc_y = 100.0
                            ymv = 1
                            g_zero = 0
                elif cmd == 'F':
                    f = vbval(val)
                cb += 1
            z_hit = tanmen + zd + shift - mill
            guard = (f > fd and g_zero == 1) if fmode else (g_zero == 0)
            if _geometry_hit(heimen, xmv, zmv, ymv, nc_x, nc_y, nc_z, exx, exy, exz,
                             z_hit, d, xd, mill, guard):
                lst.setCurrentRow(i)

    def _check_d(self, d, zd, fd):
        lst = self.controls['ListBox1']
        lst.clearSelection()
        nc = splitter(self.program)
        if nc is None:
            return
        nc_x = 100.0
        nc_z = 0.0
        nc_y = 100.0
        g_zero = 0
        f = 0.0
        tanmen = d
        for i in range(len(nc)):
            xmv = zmv = ymv = 0
            t_flag = 0
            m_flag = 0
            dwel = 0
            cb = 0
            while nc[i].command[cb] != '':
                cmd = nc[i].command[cb]
                val = nc[i].value[cb]
                if cmd == 'X':
                    nc_x = vbval(val)
                    xmv = 1
                elif cmd == 'U':
                    if dwel == 0:
                        nc_x += vbval(val)
                        xmv = 1
                elif cmd == 'Z':
                    nc_z = vbval(val)
                    zmv = 1
                elif cmd == 'W':
                    nc_z += vbval(val)
                elif cmd == 'Y':
                    nc_y = vbval(val)
                    ymv = 1
                elif cmd == 'V':
                    nc_y += vbval(val)
                    ymv = 1
                elif cmd == 'G':
                    gv = vbval(val)
                    if gv == 0:
                        g_zero = 0
                        dwel = 0
                    if gv == 1:
                        g_zero = 1
                        dwel = 0
                    if gv == 4:
                        dwel = 1
                elif cmd == 'F':
                    f = vbval(val)
                elif cmd == 'T':
                    t_flag = 1
                elif cmd == 'M':
                    m_flag = 1
                cb += 1
            if zmv == 1 and g_zero == 0 and nc_z > d + zd:
                lst.setCurrentRow(i)
            if f > fd and zmv == 1 and g_zero == 1 and nc_z > d + zd:
                lst.setCurrentRow(i)
            if f <= fd and zmv == 1 and g_zero == 1 and nc_z > d:
                d = nc_z
            if xmv == 1 or ymv == 1:
                lst.setCurrentRow(i)
            if t_flag == 1 and nc_z > tanmen + zd:
                lst.setCurrentRow(i)
            if m_flag == 1 and nc_z > tanmen + zd:
                lst.setCurrentRow(i)


def make_chk():
    return CncChk()
