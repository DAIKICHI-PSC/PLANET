import math
import time

from PySide6.QtCore import Qt, QEvent, QObject, QTimer, QPointF, QRectF, QSize
from PySide6.QtGui import (
    QIcon, QPainter, QPen, QColor, QFont, QPolygonF, QBrush, QCursor, QAction,
    QKeySequence, QShortcut,
)
from PySide6.QtWidgets import (
    QWidget, QMenu, QMenuBar, QSizePolicy, QListWidget, QListWidgetItem,
    QMainWindow,
    QHBoxLayout, QVBoxLayout,
)

from .splitter import splitter
from .vbcommon import vbval, vbs
from .images import app_icon
from . import formreg

PPM = 96.0 / 25.4
STEP_DELAY = 0.008


class _HideOnClose(QObject):
    def __init__(self, form_obj):
        super().__init__()
        self._fo = form_obj

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            if getattr(self._fo, '_force_close', False):
                return False
            if self._fo.mi.get(9) is not None and not self._fo.mi[9].isEnabled():
                event.ignore()
                return True
            self._fo.w.hide()
            event.ignore()
            return True
        return False


class Canvas(QWidget):
    def __init__(self, sim):
        super().__init__()
        self.sim = sim
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def paintEvent(self, e):
        self.sim._draw(self)

    def mousePressEvent(self, e):
        self.sim._mouse_down(e)

    def mouseReleaseEvent(self, e):
        self.sim._mouse_up(e)

    def mouseMoveEvent(self, e):
        self.sim._mouse_move(e)

    def wheelEvent(self, e):
        self.sim._mouse_wheel(e.angleDelta().y())

    def contextMenuEvent(self, e):
        if self.sim._ctx is not None:
            self.sim._ctx.exec_(e.globalPos().toPoint() if hasattr(e.globalPos(), 'toPoint') else e.globalPos())


class CncSim:
    def __init__(self):
        self.w = QMainWindow()
        self.w.setObjectName('CNC_SIM')
        self.w.setWindowTitle('PLANET　自動盤シミュレータ')
        central = QWidget()
        self.w.setCentralWidget(central)

        # listboxes (original: ＭＳ ゴシック 12pt, ItemHeight=16 / lb3: 12, hidden)
        self._lh1 = 16
        self._lh3 = 12
        self.lb1 = QListWidget(central)
        self.lb2 = QListWidget(central)
        self.lb3 = QListWidget(central)
        self.lb3.hide()
        lf = QFont('MS Gothic', 12)
        self.lb1.setFont(lf)
        self.lb2.setFont(lf)
        self.lb2.currentRowChanged.connect(self._on_lb2)

        # canvas
        self.canvas = Canvas(self)

        # layout: left column (lb1 top fills, lb2 bottom fixed) + canvas right
        left = QWidget(central)
        lv = QVBoxLayout(left)
        lv.setContentsMargins(0, 0, 0, 0)
        lv.setSpacing(44)
        lv.addWidget(self.lb1, 1)
        self.lb2.setFixedHeight(132)
        lv.addWidget(self.lb2)
        left.setFixedWidth(232)
        h = QHBoxLayout(central)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(6)
        h.addWidget(left)
        h.addWidget(self.canvas, 1)

        self.w.showMaximized()

        # menu
        self.mi = {}
        self._build_menu()
        self._ctx = self._build_ctx()

        self.program = ''
        self._timer = QTimer(self.w)
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._tick)
        self._timer.start()

        self._hide_filter = _HideOnClose(self)
        self.w.installEventFilter(self._hide_filter)
        QShortcut(QKeySequence(Qt.Key_Enter), self.w, self._key_enter)
        QShortcut(QKeySequence(Qt.Key_Return), self.w, self._key_enter)
        QShortcut(QKeySequence(Qt.Key_Escape), self.w, self._key_esc)
        formreg.register('CNC_SIM', self)
        self._reset_state()

    def show(self):
        self.w.show()
        self.w.raise_()
        self.w.activateWindow()

    def force_close(self):
        self.ExitFlag = 1
        self.ExitLoop = 1
        self._force_close = True
        self.w.close()

    # ---------------- menu ----------------
    def _act(self, num, label, checkable=False, checked=False, handler=None, sep=False):
        a = QAction(label, self.w)
        if checkable:
            a.setCheckable(True)
            a.setChecked(checked)
        if handler:
            a.triggered.connect(handler)
        self.mi[num] = a
        return a

    def _build_menu(self):
        self.mb = QMenuBar(self.w)
        self.w.setMenuBar(self.mb)

        m35 = self.mb.addMenu('操作(&C)')
        m8 = m35.addMenu('倍率(&Z)')
        for n, lab, val in ((19, '１倍', 1), (20, '５倍', 5), (21, '１０倍', 10),
                            (22, '２０倍', 20), (23, '５０倍', 50), (50, '１００倍', 100), (51, '２００倍', 200)):
            self._act(n, lab, False, False, lambda v=val: self._zoom_to(v))
            m8.addAction(self.mi[n])
        m35.addSeparator()
        self._act(5, '拡大(&W)', False, False, self.mi5)
        m35.addAction(self.mi[5])
        self._act(6, '縮小(&S)', False, False, self.mi6)
        m35.addAction(self.mi[6])
        m35.addSeparator()
        m15 = m35.addMenu('移動(&Q)')
        self._act(17, '画面を掴んで移動', True, True, self.mi17)
        m15.addAction(self.mi[17])
        self._act(18, 'クリックした位置を中央に移動', True, False, self.mi18)
        m15.addAction(self.mi[18])
        m35.addSeparator()
        self._act(14, '原点に戻す(&A)', False, False, self.mi14)
        m35.addAction(self.mi[14])

        m4 = self.mb.addMenu('表示(&V)')
        self._act(31, 'ガイドブッシュを表示(&B)', True, True)
        m4.addAction(self.mi[31])
        self._act(30, '現在の工具だけ表示(&H)', True, False)
        m4.addAction(self.mi[30])
        m4.addSeparator()
        self._act(2, '画面にプログラムを表示(&X)', True, False)
        m4.addAction(self.mi[2])
        self._act(1, '画面に加工点を表示(&T)', True, False)
        m4.addAction(self.mi[1])
        m4.addSeparator()
        self._act(34, '画面のスムージング(&G)', True, False)
        m4.addAction(self.mi[34])

        m54 = self.mb.addMenu('加工後検証ツール(&G)')
        self._act(37, '加工点を手動移動(&I)', True, False, self.mi37)
        m54.addAction(self.mi[37])
        self._act(72, '手動移動時に画面も移動(&S)', True, False)
        m54.addAction(self.mi[72])
        m54.addSeparator()
        self._act(16, '加工点上を自動移動(&M)', True, False, self.mi16)
        m54.addAction(self.mi[16])
        self._act(49, '工具軌跡上を自動移動(&D)', True, False, self.mi49)
        m54.addAction(self.mi[49])
        self._act(48, '工具軌跡に沿って画面をスクロール(&K)', True, False, self.mi48)
        m54.addAction(self.mi[48])

        m3 = self.mb.addMenu('加工動作検証ツール(&T)')
        self._act(10, 'プログラムを一行で停止(&F)', False, False)
        m3.addAction(self.mi[10])
        m3.addSeparator()
        m12 = m3.addMenu('実行スピード(&P)')
        self._act(26, 'Ｘ１', True, True, lambda: self._speed(1))
        m12.addAction(self.mi[26])
        self._act(27, 'Ｘ２', True, False, lambda: self._speed(2))
        m12.addAction(self.mi[27])
        self._act(28, 'Ｘ４', True, False, lambda: self._speed(4))
        m12.addAction(self.mi[28])
        self._act(24, 'Ｘ8', True, False, lambda: self._speed(8))
        m12.addAction(self.mi[24])
        self._act(25, 'Ｘ16', True, False, lambda: self._speed(16))
        m12.addAction(self.mi[25])
        m3.addSeparator()
        self._act(40, 'ブロックスキップを有効にする(&B)', True, False)
        m3.addAction(self.mi[40])
        self._act(44, 'M99 PでプログラムをNまで飛ばす(&J)', True, True)
        m3.addAction(self.mi[44])
        self._act(43, 'M99でプログラムを終了(&E)', True, True)
        m3.addAction(self.mi[43])
        m3.addSeparator()
        self._act(42, 'M80-M81間の/を有効にする(&Z)', True, False)
        m3.addAction(self.mi[42])
        self._act(46, 'M31-M33を穴あけ工具とする(&Q)', True, False)
        m3.addAction(self.mi[46])
        self._act(47, 'T1100-T1400までを穴あけ工具とする(&A)', True, False)
        m3.addAction(self.mi[47])

        self._act(9, '実行(&S)', False, False, self.mi9)
        self.mb.addAction(self.mi[9])

        self._act(38, '加工点を前に移動(&N)', False, False, self.mi38)
        self.mb.addAction(self.mi[38])
        self._act(39, '加工点を次に移動(&M)', False, False, self.mi39)
        self.mb.addAction(self.mi[39])
        self._act(52, '停止(&Z)', False, False, self.mi52)
        self.mb.addAction(self.mi[52])
        self._act(53, '加速(&X)', False, False, self.mi53)
        self.mb.addAction(self.mi[53])

        self.mi[38].setVisible(False)
        self.mi[39].setVisible(False)
        self.mi[52].setVisible(False)
        self.mi[53].setVisible(False)

    def _build_ctx(self):
        self._ctx = QMenu(self.w)
        c_zoom = self._ctx.addMenu('倍率(&Z)')
        for n, lab, val in ((62, '１倍', 1), (63, '５倍', 5), (64, '１０倍', 10),
                            (65, '２０倍', 20), (66, '５０倍', 50), (67, '１００倍', 100), (68, '２００倍', 200)):
            a = QAction(lab, self.w); a.triggered.connect(lambda v=val: self._zoom_to(v))
            self.mi[n] = a
            c_zoom.addAction(a)
        self._ctx.addSeparator()
        a = QAction('拡大(&W)', self.w); a.triggered.connect(self.mi5)
        self.mi[70] = a
        self._ctx.addAction(a)
        a = QAction('縮小(&S)', self.w); a.triggered.connect(self.mi6)
        self.mi[71] = a
        self._ctx.addAction(a)
        self._ctx.addSeparator()
        c_move = self._ctx.addMenu('移動(&Q)')
        a = QAction('画面を掴んで移動', self.w); a.setCheckable(True); a.setChecked(True)
        a.triggered.connect(self.mi58)
        self.mi[58] = a
        c_move.addAction(a)
        a = QAction('クリックした位置を中央に移動', self.w); a.setCheckable(True)
        a.triggered.connect(self.mi59)
        self.mi[59] = a
        c_move.addAction(a)
        self._ctx.addSeparator()
        a = QAction('原点に戻す(&A)', self.w); a.triggered.connect(self.mi14)
        self.mi[55] = a
        self._ctx.addAction(a)
        return self._ctx

    # ---------------- state ----------------
    def _reset_state(self):
        self.Zai = 0.0
        self.Bush = 0.0
        self.Clear = 0.0
        self.points = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.tool = []
        self.LT = []
        self.TMPPointCounter = []
        self.PBA = []
        self.PBB = []
        self.CurTool = 0
        self.TMPNCX = 40.0
        self.TMPNCZ = 0.001
        self.GainedZ = 0.0
        self.Spin = 1
        self.FCounter = 0
        self.SFcounter = 0
        self.DotPos = 0
        self.MVCounter1 = 0
        self.MVCounter2 = 0
        self.IL = 0
        self.MoveDot = 1
        self.GainX = 0.0
        self.GainZ = 0.0
        self.NCScale = 1.0
        self.EXNCScale = 1.0
        self.TRPosX = 0.0
        self.TRPosY = 0.0
        self.RefPosX = 0.0
        self.RefPosY = 0.0
        self.MouseXA = 0
        self.MouseYA = 0
        self.MouseDownFlag = 0
        self.PicMouseFlag = 0
        self.ExitLoop = 0
        self.ExitFlag = 0
        self.Speed = 1

    def set_program(self, text):
        self.program = text

    # ---------------- setei ----------------
    def _add(self, lw, text, h):
        it = QListWidgetItem(text)
        it.setSizeHint(QSize(1, h))
        lw.addItem(it)
        return it

    def setei(self, d, gl, cl):
        self.Zai = d
        self.Bush = gl
        self.Clear = cl
        self.points = [(0, d / 2), (-3000, d / 2), (-3000, d / 2 * -1), (0, d / 2 * -1), (0, d / 2)]
        self.CurTool = 0
        self.tool = [{'TMPPoint': [(0, 0)], 'L': [0]}]
        self.TMPPointCounter = [0]
        self.TMPNCX = 40
        self.TMPNCZ = 0.001
        self.TMPPointCounter[0] = 0
        self.tool[0]['TMPPoint'] = [(self.TMPNCZ, self.TMPNCX / -2)]
        self.tool[0]['L'] = [0]
        self.LT = [{'TLPoint': [(0, 0)], 'T': [''], 'L': [0]}]
        # guide bushes
        self.PBA = [(0, 0), (0, -10), (-2, -10), (gl * -1, -3), (gl * -1, 0), (0, 0)]
        self.PBB = [(0, 0), (0, 10), (-2, 10), (gl * -1, 3), (gl * -1, 0), (0, 0)]
        gx = (d / 2 + 0.001) * -1
        gz = cl * -1
        self.PBA = [(x + gz, y + gx) for (x, y) in self.PBA]
        gx = d / 2 + 0.001
        gz = cl * -1
        self.PBB = [(x + gz, y + gx) for (x, y) in self.PBB]
        # view (centered lazily on first paint once the canvas is sized)
        self.TRPosX = 400.0
        self.TRPosY = 300.0
        self.RefPosX = 0
        self.RefPosY = 0
        self._need_center = True
        self.MouseDownFlag = 0
        self.PicMouseFlag = 0
        self.GainX = 0
        self.GainZ = 0
        self.NCScale = 1
        self.EXNCScale = 1
        self.lb1.clear()
        self.lb2.clear()
        self._add(self.lb2, '選択なし', self._lh1)
        self.lb3.clear()
        self._add(self.lb3, '選択なし', self._lh3)
        self.ExitFlag = 0
        self.GainedZ = 0

    def _new_tool(self):
        self.tool.append({'TMPPoint': [(self.TMPNCZ, self.TMPNCX / -2)], 'L': [0]})
        self.TMPPointCounter.append(0)
        self.LT.append({'TLPoint': [(0, 0)], 'T': [''], 'L': [0]})

    # ---------------- helpers ----------------
    def r_center(self, x1, y1, x2, y2, r, g):
        h = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if h == 0 or r * r - h * h / 4 < 0:
            nan = float('nan')
            return (nan, nan, nan, nan)
        d = math.sqrt(r * r - h * h / 4)
        if g == 3:
            d *= -1
        xc = (x1 + x2) / 2 + (y2 - y1) * d / h
        yc = (y1 + y2) / 2 - (x2 - x1) * d / h
        c1 = math.acos(max(-1, min(1, (x1 - xc) / r))) * 180 / math.pi
        c2 = math.acos(max(-1, min(1, (x2 - xc) / r))) * 180 / math.pi
        if (x1 > x2 and y1 < y2 and g == 2) or (x1 > x2 and y1 > y2 and g == 2) or \
           (x1 < x2 and y1 > y2 and g == 3) or (x1 < x2 and y1 < y2 and g == 3):
            c1 *= -1
            c2 *= -1
        return (xc, yc, c1, c2)

    def r_pos(self, xc, yc, r, degree):
        ang = math.pi * degree / 180
        return (math.cos(ang) * r + xc, math.sin(ang) * r + yc)

    def _scale_center(self):
        if not (self.EXNCScale > 0):
            self.EXNCScale = self.NCScale if self.NCScale > 0 else 1.0
        if not (self.NCScale > 0):
            self.NCScale = 1.0
        ratio = self.NCScale / self.EXNCScale
        self.TRPosX = self.TRPosX - (self.RefPosX - self.RefPosX * ratio)
        self.TRPosY = self.TRPosY - (self.RefPosY - self.RefPosY * ratio)
        self.RefPosX = self.RefPosX - (self.RefPosX - self.RefPosX * ratio)
        self.RefPosY = self.RefPosY - (self.RefPosY - self.RefPosY * ratio)

    def _calculate_engine(self):
        gz = self.GainZ
        self.points = [(x + gz, y) for (x, y) in self.points]
        self.GainedZ += gz
        for t in self.tool:
            t['TMPPoint'] = [(x + gz, y) for (x, y) in t['TMPPoint']]
        for lt in self.LT:
            lt['TLPoint'] = [(x + gz, y) for (x, y) in lt['TLPoint']]
        c = self.CurTool
        self.TMPPointCounter[c] += 1
        self.tool[c]['TMPPoint'].append((self.TMPNCZ, self.TMPNCX / -2))
        self.tool[c]['L'].append(self.IL)
        self.canvas.update()
        time.sleep(STEP_DELAY / max(self.Speed, 1))

    # ---------------- run ----------------
    def run(self):
        nc = splitter(self.program)
        if nc is None:
            self.mi[9].setEnabled(True)
            return
        self.mi[9].setEnabled(False)
        from PySide6.QtWidgets import QApplication
        pump = QApplication.instance().processEvents
        nc_x = 40.0
        nc_z = 0.0
        ex_x = 40.0
        ex_z = 0.0
        g_zero = 0
        dwel = 0
        hasaki = 0
        heimen = 'X'
        shift = 0.0
        mill = 0.0
        f = 0.5
        mx = 0.0
        mz = 0.0
        mp = 0
        g92 = 0
        g92f = 0
        g92s = 0.0
        g92o = 0.0
        g92z = 0.0
        g92r = 0.0
        g2_g3 = 0
        r_size = 0.0
        m99pn = 0
        zbs = 0
        mi = self.mi
        chk = lambda n: mi[n].isChecked()
        for i in range(len(nc)):
            self.IL = i
            xmv = zmv = 0
            dwel = 0
            hasaki = 0
            r_size = 0.0
            g2_g3 = 0
            line = ''
            cb = 0
            while nc[i].command[cb] != '':
                cmd = nc[i].command[cb]
                val = nc[i].value[cb]
                if m99pn == 0:
                    line += cmd + val + ' '
                    if cmd == 'X':
                        if g92 == 1 and g92f == 1:
                            g92s = nc_x
                            g92f = 0
                        ex_x = nc_x
                        nc_x = vbval(val)
                        xmv = 1
                    elif cmd == 'U':
                        if dwel == 0 and hasaki == 0:
                            if g92 == 1 and g92f == 1:
                                g92s = nc_x
                                g92f = 0
                            ex_x = nc_x
                            nc_x += vbval(val)
                            xmv = 1
                    elif cmd == 'Z':
                        if g92 == 0:
                            ex_z = nc_z
                            nc_z = vbval(val)
                            zmv = 1
                        else:
                            g92z = vbval(val)
                    elif cmd == 'W':
                        if hasaki == 0:
                            if g92 == 0:
                                ex_z = nc_z
                                nc_z += vbval(val)
                                zmv = 1
                            else:
                                g92z = nc_z + vbval(val)
                    elif cmd == 'G':
                        gv = vbval(val)
                        if gv == 0:
                            g_zero = 0; dwel = 0; g92 = 0
                        if gv in (1, 2, 3):
                            g_zero = 1; dwel = 0; g92 = 0; g92r = 0
                        if gv == 2:
                            g2_g3 = 2
                        if gv == 3:
                            g2_g3 = 3
                        if gv == 4:
                            dwel = 1
                        if gv in (40, 41, 42):
                            hasaki = 1
                        if gv == 92:
                            g92 = 1; g92f = 1
                    elif cmd == 'R':
                        r_size = vbval(val)
                        g92r = vbval(val)
                    elif cmd == 'T':
                        tv = vbval(val)
                        if tv >= 100:
                            heimen = 'X'; shift = 0.0; mill = 0.0
                            if cb + 1 < len(nc[i].command) and nc[i].command[cb + 1] == '(':
                                pnc = splitter(nc[i].value[cb + 1].replace(')', '') + '\r\n')
                                if pnc:
                                    pc = 0
                                    while pnc[0].command[pc] != '':
                                        pc_cmd = pnc[0].command[pc]
                                        if pc_cmd == 'X':
                                            heimen = 'X'; shift = vbval(pnc[0].value[pc])
                                        elif pc_cmd == 'Y':
                                            heimen = 'Y'; shift = vbval(pnc[0].value[pc])
                                        elif pc_cmd == 'D':
                                            mill = vbval(pnc[0].value[pc])
                                        pc += 1
                            if chk(47):
                                if tv in (1100, 1200, 1300, 1400):
                                    nc_x = 0; self.TMPNCX = 0
                                else:
                                    nc_x = 40; self.TMPNCX = 40
                            else:
                                nc_x = 40; self.TMPNCX = 40
                            ex_x = nc_x
                            ex_z = nc_z
                            self.TMPNCZ = shift + 0.001
                            g_zero = 0
                            mp = 0
                            self.CurTool += 1
                            self._add(self.lb2, 'T' + nc[i].value[cb] + 'を選択', self._lh1)
                            self._add(self.lb3, str(i), self._lh3)
                            self._new_tool()
                            self.tool[self.CurTool]['TMPPoint'] = [(self.TMPNCZ, self.TMPNCX / -2)]
                    elif cmd == 'F':
                        f = vbval(val)
                        if g92 == 1:
                            g92o = f
                    elif cmd == '/':
                        if chk(40) or zbs == 1:
                            break
                    elif cmd == 'M':
                        mv = vbval(val)
                        if mv == 99:
                            if chk(43) and (cb + 1 >= len(nc[i].command) or nc[i].command[cb + 1] != 'P'):
                                self.ExitFlag = 1
                            elif chk(44) and cb + 1 < len(nc[i].command) and nc[i].command[cb + 1] == 'P' and vbval(nc[i].value[cb + 1]) > 0:
                                line += nc[i].command[cb + 1] + nc[i].value[cb + 1] + ' '
                                m99pn = vbval(nc[i].value[cb + 1])
                        elif mv == 80:
                            if chk(42):
                                zbs = 1
                        elif mv == 81:
                            if chk(42):
                                zbs = 0
                        elif 31 <= mv <= 33:
                            if chk(46):
                                heimen = 'X'; shift = 0.0; mill = 0.0
                                if cb + 1 < len(nc[i].command) and nc[i].command[cb + 1] == '(':
                                    pnc = splitter(nc[i].value[cb + 1].replace(')', '') + '\r\n')
                                    if pnc:
                                        pc = 0
                                        while pnc[0].command[pc] != '':
                                            pc_cmd = pnc[0].command[pc]
                                            if pc_cmd == 'X':
                                                heimen = 'X'; shift = vbval(pnc[0].value[pc])
                                            elif pc_cmd == 'Y':
                                                heimen = 'Y'; shift = vbval(pnc[0].value[pc])
                                            elif pc_cmd == 'D':
                                                mill = vbval(pnc[0].value[pc])
                                            pc += 1
                                nc_x = 0
                                ex_x = nc_x
                                ex_z = nc_z
                                self.TMPNCX = 0
                                self.TMPNCZ = shift + 0.001
                                g_zero = 0
                                mp = 0
                                self.CurTool += 1
                                self._add(self.lb2, 'M' + nc[i].value[cb] + 'を選択', self._lh1)
                                self._add(self.lb3, str(i), self._lh3)
                                self._new_tool()
                                self.tool[self.CurTool]['TMPPoint'] = [(self.TMPNCZ, self.TMPNCX / -2)]
                if cmd == 'N' and vbval(val) == m99pn and chk(44):
                    line += cmd + val + ' '
                    m99pn = 0
                cb += 1

            self._add(self.lb1, line, self._lh1)
            self.lb1.setCurrentRow(self.lb1.count() - 1)

            if chk(10):
                self.ExitLoop = 0
                while self.ExitLoop != 1:
                    pump()

            if nc_x == ex_x and g2_g3 == 0:
                xmv = 0
            if nc_z == ex_z and g2_g3 == 0:
                zmv = 0
            if g2_g3 > 0:
                rc = self.r_center(ex_z, ex_x / 2, nc_z, nc_x / 2, r_size, g2_g3)
                if any(math.isnan(v) for v in rc):
                    g2_g3 = 0
            if xmv == 0 or zmv == 0 or r_size == 0:
                g2_g3 = 0

            if g92 == 0:
                if xmv == 1 and zmv == 0 and g2_g3 == 0:
                    if g_zero == 0:
                        f = 0.5
                    f = f * self.Speed
                    mx = abs(ex_x - nc_x)
                    spin = int(mx / f)
                    if spin <= 0:
                        spin = 1
                    f = mx / spin
                    if nc_x < ex_x:
                        f = f * -1
                    self.GainZ = 0
                    self._timer.stop()
                    rcount = 0
                    while True:
                        self.TMPNCX += f
                        if rcount + 1 == spin:
                            self.TMPNCX = nc_x
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                elif xmv == 0 and zmv == 1 and g2_g3 == 0:
                    if g_zero == 0:
                        f = 0.5
                    f = f * self.Speed
                    mz = abs(ex_z - nc_z)
                    spin = int(mz / f)
                    if spin <= 0:
                        spin = 1
                    f = mz / spin
                    if nc_z < ex_z:
                        f = f * -1
                    self.GainZ = f
                    self._timer.stop()
                    rcount = 0
                    while True:
                        if rcount + 1 == spin:
                            self.GainZ = nc_z - self.GainedZ
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                elif xmv == 1 and zmv == 1 and g2_g3 == 0:
                    if g_zero == 0:
                        f = 0.5
                    f = f * self.Speed
                    mx = abs(ex_x - nc_x)
                    mz = abs(ex_z - nc_z)
                    if mx >= mz:
                        spin = int(mx / f)
                    else:
                        spin = int(mz / f)
                    if spin <= 0:
                        spin = 1
                    f = mx / spin
                    self.GainZ = mz / spin
                    if nc_x < ex_x:
                        f = f * -1
                    if nc_z < ex_z:
                        self.GainZ = self.GainZ * -1
                    self._timer.stop()
                    rcount = 0
                    while True:
                        self.TMPNCX += f
                        if rcount + 1 == spin:
                            self.TMPNCX = nc_x
                        if rcount + 1 == spin:
                            self.GainZ = nc_z - self.GainedZ
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                elif xmv == 1 and zmv == 1 and g2_g3 > 0:
                    if g_zero == 0:
                        f = 0.5
                    f = f * self.Speed
                    mx = abs(ex_x - nc_x)
                    mz = abs(ex_z - nc_z)
                    devider = int(mx / f) if mx > mz else int(mz / f)
                    if devider <= 0:
                        devider = 1
                    dx1 = ex_x / 2
                    dx2 = nc_x / 2
                    rc = list(self.r_center(ex_z, dx1, nc_z, dx2, r_size, g2_g3))
                    move_degree = abs(rc[2] - rc[3])
                    each = move_degree / devider
                    exzz = ex_z
                    exxx = ex_x
                    self._timer.stop()
                    rcount = 0
                    while True:
                        if g2_g3 == 2:
                            rc[2] -= each
                        else:
                            rc[2] += each
                        pos = self.r_pos(rc[0], rc[1], r_size, rc[2])
                        self.TMPNCX += pos[1] * 2 - exxx
                        self.GainZ = pos[0] - exzz
                        if rcount + 1 == devider:
                            self.TMPNCX = nc_x
                        if rcount + 1 == devider:
                            self.GainZ = nc_z - self.GainedZ
                        self._calculate_engine()
                        exzz = exzz + self.GainZ
                        exxx = self.TMPNCX
                        rcount += 1
                        if rcount >= devider:
                            break
                        pump()
                    self._timer.start()
                if xmv == 1 or zmv == 1:
                    c = self.CurTool
                    self.LT[c]['TLPoint'].append((self.TMPNCZ, self.TMPNCX / -2))
                    deg = 0.0
                    kakudo = ''
                    if xmv == 1 and zmv == 1 and g2_g3 == 0:
                        mx = abs(ex_x - nc_x) / 2
                        mz = abs(ex_z - nc_z)
                        deg = mz / mx if mx > mz else mx / mz
                        deg = int((math.atan(deg) * 180 / math.pi + 0.0005) * 1000) / 1000
                        kakudo = '（角度：' + vbs(deg).replace(' ', '') + '°）'
                    self.LT[c]['T'].append(line + kakudo)
                    self.LT[c]['L'].append(i)
                    mp += 1
            else:
                if xmv == 1:
                    f = 0.5
                    f *= self.Speed
                    if g92r != 0:
                        mx = abs(ex_x - nc_x) + abs(g92r * 2)
                    else:
                        mx = abs(ex_x - nc_x)
                    spin = int(mx / f)
                    if spin <= 0:
                        spin = 1
                    f = mx / spin
                    if nc_x < ex_x:
                        f = f * -1
                    self.GainZ = 0
                    self._timer.stop()
                    rcount = 0
                    while True:
                        self.TMPNCX += f
                        if rcount + 1 == spin:
                            self.TMPNCX = (nc_x + g92r * 2) if g92r != 0 else nc_x
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                    if xmv == 1 or zmv == 1:
                        c = self.CurTool
                        self.LT[c]['TLPoint'].append((self.TMPNCZ, self.TMPNCX / -2))
                        self.LT[c]['T'].append(line)
                        self.LT[c]['L'].append(i)
                        mp += 1
                    f = g92o
                    f *= self.Speed
                    if g92r != 0:
                        mx = abs(g92r * 2)
                    mz = abs(nc_z - g92z)
                    spin = int(mz / f)
                    if spin <= 0:
                        spin = 1
                    if g92r != 0:
                        f = mx / spin
                    self.GainZ = mz / spin
                    self._timer.stop()
                    rcount = 0
                    while True:
                        if g92r != 0:
                            self.TMPNCX += f
                        if rcount + 1 == spin:
                            if g92r != 0:
                                self.TMPNCX = nc_x
                        if rcount + 1 == spin:
                            self.GainZ = g92z - self.GainedZ
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                    f = 0.5
                    f *= self.Speed
                    if g92r != 0:
                        mx = abs(ex_x - nc_x)
                    spin = int(mx / f)
                    if spin <= 0:
                        spin = 1
                    f = mx / spin
                    self.GainZ = 0
                    self._timer.stop()
                    rcount = 0
                    while True:
                        self.TMPNCX += f
                        if rcount + 1 == spin:
                            self.TMPNCX = ex_x
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                    f = g92o
                    f *= self.Speed
                    spin = int(mz / f)
                    if spin <= 0:
                        spin = 1
                    f = mz / spin
                    self.GainZ = f * -1
                    self._timer.stop()
                    rcount = 0
                    while True:
                        if rcount + 1 == spin:
                            self.GainZ = nc_z - self.GainedZ
                        self._calculate_engine()
                        rcount += 1
                        if rcount >= spin:
                            break
                        pump()
                    self._timer.start()
                    nc_x = g92s
            if self.ExitFlag == 1:
                break
        self.mi[9].setEnabled(True)
        self.lb2.setEnabled(True)

    # ---------------- timer ----------------
    def _tick(self):
        self.SFcounter += 1
        if self.SFcounter == 5:
            self.FCounter += self.MoveDot
            self.SFcounter = 0
        self.MVCounter1 += self.MoveDot
        self.MVCounter2 += self.MoveDot
        self.canvas.update()

    # ---------------- keys ----------------
    def _key_enter(self):
        self.ExitLoop = 1

    def _key_esc(self):
        self.ExitFlag = 1

    # ---------------- mouse ----------------
    def _mouse_down(self, e):
        if e.button() == Qt.LeftButton:
            if self.PicMouseFlag == 0:
                self.MouseDownFlag = 1
                self.MouseXA = e.position().x()
                self.MouseYA = e.position().y()
            else:
                cx = self.canvas.width() / 2
                cy = self.canvas.height() / 2
                self.TRPosX = self.TRPosX - e.position().x() + cx
                self.TRPosY = self.TRPosY - e.position().y() + cy
                self.RefPosX = self.RefPosX - e.position().x() + cx
                self.RefPosY = self.RefPosY - e.position().y() + cy
        elif e.button() == Qt.RightButton:
            pass

    def _mouse_up(self, e):
        self.MouseDownFlag = 0

    def _mouse_move(self, e):
        if self.MouseDownFlag == 1:
            self.TRPosX = e.position().x() - self.MouseXA + self.TRPosX
            self.TRPosY = e.position().y() - self.MouseYA + self.TRPosY
            self.RefPosX = e.position().x() - self.MouseXA + self.RefPosX
            self.RefPosY = e.position().y() - self.MouseYA + self.RefPosY
        self.MouseXA = e.position().x()
        self.MouseYA = e.position().y()

    def _mouse_wheel(self, delta):
        steps = delta / 120
        if self.NCScale + steps > 0:
            self.EXNCScale = self.NCScale
            self.NCScale = self.NCScale + steps
            self._scale_center()

    # ---------------- menu handlers ----------------
    def _speed(self, v):
        self.Speed = v
        for n in (26, 27, 28, 24, 25):
            self.mi[n].setChecked(False)
        self.mi[26 if v == 1 else 27 if v == 2 else 28 if v == 4 else 24 if v == 8 else 25].setChecked(True)

    def _zoom_to(self, v):
        self.EXNCScale = self.NCScale
        self.NCScale = v
        self._scale_center()

    def mi5(self):
        self.EXNCScale = self.NCScale
        self.NCScale = self.NCScale + 1
        self._scale_center()

    def mi6(self):
        if self.NCScale - 1 > 0:
            self.EXNCScale = self.NCScale
            self.NCScale = self.NCScale - 1
            self._scale_center()

    def mi14(self):
        self.TRPosX = self.canvas.width() / 2
        self.TRPosY = self.canvas.height() / 2
        self.RefPosX = 0
        self.RefPosY = 0

    def mi9(self):
        if self.mi[9].isEnabled():
            self.mi[9].setEnabled(False)
            self.lb2.setEnabled(False)
            self.setei(self.Zai, self.Bush, self.Clear)
            self.run()

    def mi17(self):
        self._move_mode(1)

    def mi18(self):
        self._move_mode(2)

    def mi58(self):
        self._move_mode(1)

    def mi59(self):
        self._move_mode(2)

    def _move_mode(self, mode):
        self.PicMouseFlag = mode - 1
        self.canvas.setCursor(Qt.OpenHandCursor if mode == 1 else Qt.CrossCursor)
        self.mi[17].setChecked(mode == 1)
        self.mi[18].setChecked(mode == 2)
        self.mi[58].setChecked(mode == 1)
        self.mi[59].setChecked(mode == 2)

    def mi37(self):
        self.mi[38].setVisible(self.mi[37].isChecked())
        self.mi[39].setVisible(self.mi[37].isChecked())

    def mi16(self):
        self._sync_follow_vis()

    def mi48(self):
        self._sync_follow_vis()

    def mi49(self):
        self._sync_follow_vis()

    def _sync_follow_vis(self):
        on = self.mi[16].isChecked() or self.mi[48].isChecked() or self.mi[49].isChecked()
        self.mi[52].setVisible(on)
        self.mi[53].setVisible(on)

    def mi38(self):
        r = self.lb2.currentRow()
        if r > 0 and r < len(self.LT):
            if self.DotPos - 1 >= 0:
                self.DotPos -= 1
            row = self.LT[r]['L'][self.DotPos]
            if 0 <= row < self.lb1.count():
                self.lb1.setCurrentRow(row)

    def mi39(self):
        r = self.lb2.currentRow()
        if r > 0 and r < len(self.LT):
            if self.DotPos + 1 <= len(self.LT[r]['TLPoint']) - 1:
                self.DotPos += 1
            row = self.LT[r]['L'][self.DotPos]
            if 0 <= row < self.lb1.count():
                self.lb1.setCurrentRow(row)

    def mi52(self):
        if self.MoveDot == 0:
            self.MoveDot = 1
            self.mi[52].setText('停止(&Z)')
        else:
            self.MoveDot = 0
            self.mi[52].setText('移動(&Z)')

    def mi53(self):
        if self.MoveDot != 0:
            self.MoveDot += 3

    def _on_lb2(self):
        self.MVCounter1 = 0
        self.MVCounter2 = 0
        self.DotPos = 0
        r = self.lb2.currentRow()
        if r > 0 and self.mi[9].isEnabled():
            self.lb1.setCurrentRow(int(self.lb3.item(r).text()))

    # ---------------- draw ----------------
    def _draw(self, widget):
        if getattr(self, '_need_center', False) and widget.width() > 50:
            self.TRPosX = widget.width() / 2
            self.TRPosY = widget.height() / 2
            self._need_center = False
        if not (self.NCScale > 0):
            self.NCScale = 1.0
            self.EXNCScale = 1.0
        k = self.NCScale * PPM
        if not (k > 0):
            return
        p = QPainter(widget)
        try:
            self._draw_body(p, widget, k)
        finally:
            p.end()

    def _draw_body(self, p, widget, k):
        mi = self.mi
        sel = self.lb2.currentRow()
        if sel > 0 and mi[9].isEnabled() and mi[48].isChecked():
            if 0 <= sel < len(self.TMPPointCounter) and self.TMPPointCounter[sel] > 0 and sel < len(self.tool):
                pts = self.tool[sel]['TMPPoint']
                if self.MVCounter2 > len(pts) - 1:
                    self.MVCounter2 = 0
                x, y = pts[self.MVCounter2]
                self.TRPosX = x * PPM * -self.NCScale + widget.width() / 2
                self.TRPosY = y * PPM * -self.NCScale + widget.height() / 2
                self.RefPosX = self.TRPosX
                self.RefPosY = self.TRPosY
        if sel > 0 and mi[9].isEnabled() and mi[37].isChecked() and mi[72].isChecked() and sel < len(self.LT):
            lpts = self.LT[sel]['TLPoint']
            if self.DotPos > len(lpts) - 1:
                self.DotPos = 0
            x, y = lpts[self.DotPos]
            self.TRPosX = x * PPM * -self.NCScale + widget.width() / 2
            self.TRPosY = y * PPM * -self.NCScale + widget.height() / 2
            self.RefPosX = self.TRPosX
            self.RefPosY = self.TRPosY
        smooth = mi[34].isChecked()
        p.setRenderHint(QPainter.Antialiasing, smooth)
        p.setRenderHint(QPainter.TextAntialiasing, smooth)
        p.fillRect(widget.rect(), QColor('white'))
        p.translate(self.TRPosX, self.TRPosY)
        p.scale(k, k)
        lw = 1.0 / k

        def poly(pts):
            return QPolygonF([QPointF(x, y) for (x, y) in pts])

        # workpiece
        pen = QPen(QColor('black'), lw)
        p.setPen(pen)
        p.drawPolyline(poly(self.points))

        # tool paths
        sel = self.lb2.currentRow()
        running = not mi[9].isEnabled()
        ntool = len(self.tool)
        if sel >= ntool:
            sel = ntool - 1
        if mi[30].isChecked():
            if not running:
                if sel > 0 and sel < len(self.TMPPointCounter) and self.TMPPointCounter[sel] > 0:
                    p.setPen(QPen(QColor('red'), lw))
                    p.drawPolyline(poly(self.tool[sel]['TMPPoint']))
            elif 0 <= self.CurTool < len(self.TMPPointCounter) and self.TMPPointCounter[self.CurTool] > 0:
                p.setPen(QPen(QColor('red'), lw))
                p.drawPolyline(poly(self.tool[self.CurTool]['TMPPoint']))
        else:
            for i in range(ntool):
                if i < len(self.TMPPointCounter) and self.TMPPointCounter[i] > 0:
                    col = 'red' if (running and i == ntool - 1) or (not running and sel > 0 and i == sel) else 'blue'
                    p.setPen(QPen(QColor(col), lw))
                    p.drawPolyline(poly(self.tool[i]['TMPPoint']))

        # machining points (画面に加工点を表示)
        if mi[1].isChecked():
            ax = 0.05
            p.setPen(QPen(QColor('green'), lw))
            if running:
                c = self.CurTool
                if 0 <= c < len(self.LT) and self.LT[c]['T']:
                    lt = self.LT[c]
                    mp = len(lt['T']) - 1
                    if mp < len(lt['TLPoint']):
                        x, y = lt['TLPoint'][mp]
                        if x != 0 or y != 0:
                            p.drawEllipse(QPointF(x, y), ax / 2, ax / 2)
            elif sel > 0 and sel < len(self.LT):
                lt = self.LT[sel]
                for i in range(len(lt['T'])):
                    if i < len(lt['TLPoint']):
                        x, y = lt['TLPoint'][i]
                        p.drawEllipse(QPointF(x, y), ax / 2, ax / 2)

        # program (画面にプログラムを表示)
        # 原版と同様: 文字位置は加工点に追従、文字サイズはズーム(NCScale)に比例して拡大縮小
        if mi[2].isChecked():
            p.save()
            p.resetTransform()
            fnt = QFont('MS Gothic')
            fnt.setPointSizeF(12.0 * self.NCScale)
            p.setFont(fnt)
            p.setPen(QPen(QColor('green')))

            def scr(x, y):
                return QPointF(self.TRPosX + x * k, self.TRPosY + y * k)

            if running:
                c = self.CurTool
                if 0 <= c < len(self.LT) and self.LT[c]['T']:
                    lt = self.LT[c]
                    mp = len(lt['T']) - 1
                    if mp < len(lt['TLPoint']):
                        x, y = lt['TLPoint'][mp]
                        p.drawText(scr(x, y), lt['T'][mp])
            elif sel > 0 and sel < len(self.LT):
                lt = self.LT[sel]
                for i in range(len(lt['T'])):
                    if i < len(lt['TLPoint']):
                        x, y = lt['TLPoint'][i]
                        p.drawText(scr(x, y), lt['T'][i])
            p.restore()

        # 点を点滅 (加工点上を自動移動)
        if mi[16].isChecked() and sel > 0 and sel < len(self.LT):
            lt = self.LT[sel]
            if self.FCounter > len(lt['TLPoint']) - 1:
                self.FCounter = 0
            if self.FCounter < len(lt['TLPoint']):
                x, y = lt['TLPoint'][self.FCounter]
                if self.FCounter < len(lt['L']) and 0 <= lt['L'][self.FCounter] < self.lb1.count():
                    self.lb1.setCurrentRow(lt['L'][self.FCounter])
                p.setPen(QPen(QColor('green'), lw))
                p.drawEllipse(QPointF(x, y), 0.125, 0.125)

        # 工具軌跡点滅用点描画
        if sel > 0 and mi[9].isEnabled() and mi[49].isChecked() and sel < len(self.tool) \
           and 0 <= sel < len(self.TMPPointCounter) and self.TMPPointCounter[sel] > 0:
            pts = self.tool[sel]['TMPPoint']
            if self.MVCounter1 > len(pts) - 1:
                self.MVCounter1 = 0
            if self.MVCounter1 < len(pts):
                x, y = pts[self.MVCounter1]
                if self.MVCounter1 < len(self.tool[sel]['L']) and 0 <= self.tool[sel]['L'][self.MVCounter1] < self.lb1.count():
                    self.lb1.setCurrentRow(self.tool[sel]['L'][self.MVCounter1])
                p.setPen(QPen(QColor('green'), lw))
                p.drawEllipse(QPointF(x, y), 0.125, 0.125)

        # 工具軌跡トレース用点描画
        if sel > 0 and mi[9].isEnabled() and mi[48].isChecked() and sel < len(self.tool) \
           and 0 <= sel < len(self.TMPPointCounter) and self.TMPPointCounter[sel] > 0:
            pts = self.tool[sel]['TMPPoint']
            if 0 <= self.MVCounter2 < len(pts):
                x, y = pts[self.MVCounter2]
                if self.MVCounter2 < len(self.tool[sel]['L']) and 0 <= self.tool[sel]['L'][self.MVCounter2] < self.lb1.count():
                    self.lb1.setCurrentRow(self.tool[sel]['L'][self.MVCounter2])
                p.setPen(QPen(QColor('green'), lw))
                p.drawEllipse(QPointF(x, y), 0.125, 0.125)

        # 加工点を移動
        if sel > 0 and mi[9].isEnabled() and mi[37].isChecked() and sel < len(self.LT):
            lpts = self.LT[sel]['TLPoint']
            if self.DotPos > len(lpts) - 1:
                self.DotPos = 0
            if 0 <= self.DotPos < len(lpts):
                x, y = lpts[self.DotPos]
                p.setPen(QPen(QColor('green'), lw))
                p.drawEllipse(QPointF(x, y), 0.125, 0.125)

        # guide bushes
        if mi[31].isChecked():
            p.setPen(QPen(QColor('black'), lw))
            p.setBrush(QBrush(QColor(169, 169, 169)))
            p.drawPolygon(poly(self.PBA))
            p.drawPolygon(poly(self.PBB))


def make_sim():
    return CncSim()
