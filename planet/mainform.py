from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtGui import QColor, QTextCursor, QIcon
from PySide6.QtWidgets import (
    QPlainTextEdit, QInputDialog, QMessageBox, QFileDialog,
    QApplication,
)

from .layout import FormBuilder
from .splitter import splitter
from .vbcommon import cv, cv2, vbval
from .images import app_icon
from . import formreg

def _input(parent, title, prompt, default=''):
    text, ok = QInputDialog.getText(parent, title, prompt, text=default)
    if not ok:
        return ''
    return text


def _msg(parent, text, title='情報', critical=False):
    if critical:
        QMessageBox.critical(parent, title, text)
    else:
        QMessageBox.information(parent, title, text)


def _yn(parent, text, title='確認', default_yes=False):
    default = QMessageBox.Yes if default_yes else QMessageBox.No
    r = QMessageBox.question(parent, title, text,
                             QMessageBox.Yes | QMessageBox.No, default)
    return r == QMessageBox.Yes


def read_nc_file(path):
    data = open(path, 'rb').read()
    if data.startswith(b'\xef\xbb\xbf'):
        text = data.decode('utf-8-sig')
    else:
        try:
            text = data.decode('cp932')
        except UnicodeDecodeError:
            text = data.decode('utf-8', errors='replace')
    return text


def lines_from_nc(text):
    if text and text[-1] != '\n':
        text += '\r\n'
    nc = splitter(text)
    if nc is None:
        return []
    out = []
    for line in nc:
        parts = []
        j = 0
        while line.command[j] != '':
            parts.append(line.command[j] + line.value[j])
            j += 1
        out.append(' '.join(parts))
    return out


def align_line_text(line):
    nc = splitter(line + '\r\n')
    if nc is None:
        return ''
    parts = []
    j = 0
    while nc[0].command[j] != '':
        parts.append(nc[0].command[j] + nc[0].value[j])
        j += 1
    return ' '.join(parts)


class MainText(QPlainTextEdit):
    def __init__(self, parent_form):
        super().__init__()
        self.pf = parent_form
        self.pre_line = 0
        self.pre_offset = 0
        self.hide_sel = True
        self.nav_keys = (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right, Qt.Key_Enter, Qt.Key_Return)

    def keyPressEvent(self, e):
        if e.key() in self.nav_keys:
            cur = self.textCursor()
            self.pre_line = cur.blockNumber()
            self.pre_offset = cur.positionInBlock()
        super().keyPressEvent(e)

    def keyReleaseEvent(self, e):
        if e.key() in self.nav_keys:
            cur = self.textCursor()
            post_line = cur.blockNumber()
            if post_line != self.pre_line:
                if self.pf.chk_sync.isChecked():
                    self.pf.sync_search(self, post_line)
                self.pf.align_line(self, self.pre_line, post_line, cur.positionInBlock())
        super().keyReleaseEvent(e)

    def focusOutEvent(self, e):
        if self.hide_sel and self.textCursor().hasSelection():
            self.textCursor().clearSelection()
            self.setTextCursor(self.textCursor())
        super().focusOutEvent(e)


class _CloseFilter(QObject):
    def __init__(self, form_obj):
        super().__init__()
        self._fo = form_obj

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            if not _yn(self._fo.w, '現在の内容は破棄されます。\n終了しますか？'):
                event.ignore()
                return True
            if self._fo.sim is not None:
                self._fo.sim.force_close()
            self._fo.quit_app()
        return False


class Form1:
    def __init__(self):
        self.sim = None
        self.chk = None
        self.save_path = ''
        self.save_path2 = ''

        fb = FormBuilder('Form1')
        self.w = fb.build()
        self.w.setWindowIcon(QIcon(app_icon()))
        self.w.setObjectName('Form1')
        self.controls = fb.controls

        self.te1 = self._make_editor('TextBox1')
        self.te2 = self._make_editor('TextBox2')

        formreg.register('Form1', self)

        c = self.controls
        c['PictureBox1'].mousePressEvent = lambda e, f=self: _msg(f.w,
            "PLANET V1.0\nhttp://www.daiyanet.co.jp/")
        c['PictureBox2'].mousePressEvent = lambda e, f=self: f.open_list('List_Maebiki')
        c['PictureBox3'].mousePressEvent = lambda e, f=self: f.open_list('List_Mizo')
        c['PictureBox4'].mousePressEvent = lambda e, f=self: f.open_list('List_Cal')
        c['PictureBox9'].mousePressEvent = lambda e, f=self: f.open_list('List_Ura')
        c['PictureBox18'].mousePressEvent = lambda e, f=self: f.open_list('List_Cross')
        c['PictureBox22'].mousePressEvent = lambda e, f=self: f.open_list('List_Drill')
        c['PictureBox26'].mousePressEvent = lambda e, f=self: f.open_list('List_Cut')
        c['PictureBox5'].mousePressEvent = lambda e, f=self: f.run(f.te1.toPlainText())
        c['PictureBox6'].mousePressEvent = lambda e, f=self: f.new_left()
        c['PictureBox7'].mousePressEvent = lambda e, f=self: f.open_left()
        c['PictureBox8'].mousePressEvent = lambda e, f=self: f.save_as_left()
        c['PictureBox13'].mousePressEvent = lambda e, f=self: f.save_left()
        c['PictureBox10'].mousePressEvent = lambda e, f=self: f.new_right()
        c['PictureBox11'].mousePressEvent = lambda e, f=self: f.open_right()
        c['PictureBox12'].mousePressEvent = lambda e, f=self: f.save_as_right()
        c['PictureBox14'].mousePressEvent = lambda e, f=self: f.save_right()
        c['PictureBox15'].mousePressEvent = lambda e, f=self: f.chk1()
        c['PictureBox16'].mousePressEvent = lambda e, f=self: f.chk2()
        c['PictureBox17'].mousePressEvent = lambda e, f=self: f.chk3()
        c['PictureBox19'].mousePressEvent = lambda e, f=self: f.add_offset('X')
        c['PictureBox20'].mousePressEvent = lambda e, f=self: f.add_offset('Z')
        c['PictureBox21'].mousePressEvent = lambda e, f=self: f.add_offset('Y')
        c['PictureBox23'].mousePressEvent = lambda e, f=self: f.add_offset('F')
        c['PictureBox24'].mousePressEvent = lambda e, f=self: f.replace_op()
        c['PictureBox25'].mousePressEvent = lambda e, f=self: f.time_report()
        c['Button1'].clicked.connect(lambda: self.remove_markers())

        marks = [
            ('CheckBox2', 'G0 ', '●G0 '),
            ('CheckBox3', 'T', '●T'),
            ('CheckBox4', 'M', '●M'),
            ('CheckBox5', 'G', '●G'),
            ('CheckBox6', 'F', '●F'),
            ('CheckBox7', 'S', '●S'),
            ('CheckBox8', 'O', '●O'),
            ('CheckBox9', 'N', '●N'),
            ('CheckBox10', 'P', '●P'),
            ('CheckBox11', 'G1 ', '●G1 '),
            ('CheckBox12', 'X', '●X'),
            ('CheckBox13', 'Y', '●Y'),
            ('CheckBox14', 'Z', '●Z'),
            ('CheckBox15', 'R', '●R'),
        ]
        for name, plain, marked in marks:
            c[name].toggled.connect(lambda on, p=plain, m=marked: self.toggle_mark(p, m, on))

        c['CheckBox1'].toggled.connect(self.on_sync_toggled)
        self.chk_sync = c['CheckBox1']

        self._close_filter = _CloseFilter(self)
        self.w.installEventFilter(self._close_filter)

    def quit_app(self):
        app = QApplication.instance()
        if app is not None:
            app.quit()

    def _make_editor(self, name):
        orig = self.controls[name]
        geo = orig.geometry()
        font = orig.font()
        orig.deleteLater()
        te = MainText(self)
        te.setParent(self.w)
        te.setGeometry(geo)
        te.setFont(font)
        te.setLineWrapMode(QPlainTextEdit.NoWrap)
        te.raise_()
        self.controls[name] = te
        return te

    # ---------------- navigation ----------------
    def open_list(self, name):
        self.w.hide()
        form = formreg.get_form(name)
        if form is None:
            from .lists import make_list
            form = make_list(name)
        form.show()

    def run(self, text):
        d = _input(self.w, '情報', '材料の素材径を入力して下さい。')
        if d == '':
            return
        gl = _input(self.w, '情報', 'ガイドブッシュの超硬長を入力して下さい。', '15')
        if gl == '':
            return
        cl = _input(self.w, '情報', '刃先基準位置からガイドブッシュまでの距離を入力して下さい。', '2')
        if cl == '':
            return
        if self.sim is None:
            from .cnc_sim import CncSim
            self.sim = CncSim()
        self.sim.show()
        self.sim.set_program(text)
        self.sim.setei(float(vbval(d)), float(vbval(gl)), float(vbval(cl)))

    # ---------------- editors ----------------
    def on_sync_toggled(self, on):
        self.te1.hide_sel = not on
        self.te2.hide_sel = not on

    def sync_search(self, src, post_line):
        other = self.te2 if src is self.te1 else self.te1
        lines = src.toPlainText().split('\n')
        if post_line >= len(lines):
            return
        sc = lines[post_line].replace(' ', '')
        if not sc:
            return
        if 'M' not in sc:
            return
        if len(sc) != 4:
            return
        tpos = other.toPlainText().find(sc)
        if tpos < 0:
            return
        cur = other.textCursor()
        cur.setPosition(tpos)
        cur.setPosition(tpos + len(sc), QTextCursor.KeepAnchor)
        other.setTextCursor(cur)
        other.centerCursor()

    def align_line(self, te, line_no, post_line, offset):
        doc = te.document()
        block = doc.findBlockByNumber(line_no)
        if not block.isValid():
            return
        old = block.text()
        new = align_line_text(old)
        if new == '' or new == old:
            return
        cur = QTextCursor()
        cur.setPosition(block.position())
        cur.setPosition(block.position() + block.length(), QTextCursor.KeepAnchor)
        cur.insertText(new)

    def toggle_mark(self, plain, marked, on):
        for te in (self.te1, self.te2):
            t = te.toPlainText()
            if on:
                t = t.replace(plain, marked)
            else:
                t = t.replace(marked, plain)
            te.setPlainText(t)

    def remove_markers(self):
        for te in (self.te1, self.te2):
            te.setPlainText(te.toPlainText().replace('●', ''))

    def append_to_left(self, text):
        self.te1.setPlainText(self.te1.toPlainText() + text + '\r\n')

    # ---------------- file ops ----------------
    def new_left(self):
        if not _yn(self.w, '現在の内容は破棄されます。\n新規作成しますか？'):
            return
        self.save_path = ''
        self.te1.setPlainText('')
        self.controls['Label1'].setText('')

    def open_left(self):
        path, _ = QFileDialog.getOpenFileName(self.w, '開く', '', 'すべてのファイル(*.*)|*.*')
        if not path:
            return
        self.save_path = path
        self.controls['Label1'].setText(self.save_path)
        text = read_nc_file(path)
        lines = lines_from_nc(text)
        self.te1.setPlainText('\r\n'.join(lines) if lines else '')

    def save(self, path, text):
        data = text.encode('cp932', errors='replace')
        open(path, 'wb').write(data)

    def save_as_left(self):
        path, _ = QFileDialog.getSaveFileName(self.w, '名前を付けて保存', '', 'すべてのファイル(*.*)|*.*')
        if not path:
            return
        self.save_path = path
        self.save(self.save_path, self.te1.toPlainText())
        self.controls['Label1'].setText(self.save_path)

    def save_left(self):
        if not _yn(self.w, '上書きしますか？'):
            return
        if self.save_path == '':
            self.save_as_left()
        else:
            self.save(self.save_path, self.te1.toPlainText())
            self.controls['Label1'].setText(self.save_path)

    def new_right(self):
        if not _yn(self.w, '現在の内容は破棄されます。\n新規作成しますか？'):
            return
        self.save_path2 = ''
        self.te2.setPlainText('')
        self.controls['Label2'].setText('')

    def open_right(self):
        path, _ = QFileDialog.getOpenFileName(self.w, '開く', '', 'すべてのファイル(*.*)|*.*')
        if not path:
            return
        self.save_path2 = path
        self.controls['Label2'].setText(self.save_path2)
        text = read_nc_file(path)
        lines = lines_from_nc(text)
        self.te2.setPlainText('\r\n'.join(lines) if lines else '')

    def save_as_right(self):
        path, _ = QFileDialog.getSaveFileName(self.w, '名前を付けて保存', '', 'すべてのファイル(*.*)|*.*')
        if not path:
            return
        self.save_path2 = path
        self.save(self.save_path2, self.te2.toPlainText())
        self.controls['Label2'].setText(self.save_path2)

    def save_right(self):
        if not _yn(self.w, '上書きしますか？'):
            return
        if self.save_path2 == '':
            self.save_as_right()
        else:
            self.save(self.save_path2, self.te2.toPlainText())
            self.controls['Label2'].setText(self.save_path2)

    # ---------------- check ----------------
    def _prepare_chk(self):
        if self.chk is None:
            from .cnc_chk import CncChk
            self.chk = CncChk()
        self.chk.show()
        lst = self.chk.controls['ListBox1']
        lst.clear()
        for line in self.te1.toPlainText().split('\n'):
            lst.addItem(line)
        self.chk.set_program(self.te1.toPlainText())
        return self.chk

    def chk1(self):
        d = _input(self.w, '情報', '材料の素材径を入力して下さい。')
        if d == '':
            return
        xd = _input(self.w, '情報', '径方向（ＸＹ）の安全マージンを入力して下さい。\n材料径＋入力値以上の範囲を安全圏とします。', '1.0')
        if xd == '':
            return
        zd = _input(self.w, '情報', '軸方向（Ｚ）の安全マージンを入力して下さい。\nＺ０＋入力値以下の範囲を安全圏とします。', '-0.5')
        if zd == '':
            return
        chk = self._prepare_chk()
        chk.check_hit(float(vbval(d)), float(vbval(xd)), float(vbval(zd)))

    def chk2(self):
        d = _input(self.w, '情報', '材料の素材径を入力して下さい。')
        if d == '':
            return
        xd = _input(self.w, '情報', '径方向（ＸＹ）の安全マージンを入力して下さい。\n材料径＋入力値以上の範囲を安全圏とします。', '0.4')
        if xd == '':
            return
        zd = _input(self.w, '情報', '軸方向（Ｚ）の安全マージンを入力して下さい。\nＺ０＋入力値以下の範囲を安全圏とします。', '-0.2')
        if zd == '':
            return
        fd = _input(self.w, '情報', '安全な送りの最大値を入力して下さい。\n入力値以下の送りを安全とします。', '0.05')
        if fd == '':
            return
        chk = self._prepare_chk()
        chk.check_hit_f(float(vbval(d)), float(vbval(xd)), float(vbval(zd)), float(vbval(fd)))

    def chk3(self):
        d = _input(self.w, '情報', '工具位置決めのＺ値を入力して下さい。', '5.0')
        if d == '':
            return
        cd = _input(self.w, '情報', 'クリアランスを入力して下さい。\n位置決めのＺ値＋入力値で接触とします。', '0.5')
        if cd == '':
            return
        zd = _input(self.w, '情報', 'Ｚ軸の安全マージンを入力して下さい。\n入力値以上の範囲を安全圏とします。', '-0.5')
        if zd == '':
            return
        fd = _input(self.w, '情報', '安全な送りの最大値を入力して下さい。\n入力値以下の送りを安全とします。', '0.05')
        if fd == '':
            return
        chk = self._prepare_chk()
        chk.check_hit_d(float(vbval(d)) + float(vbval(cd)), float(vbval(zd)), float(vbval(fd)))

    # ---------------- offsets ----------------
    def add_offset(self, axis):
        if self.te2.toPlainText() == '':
            _msg(self.w, '右側編集画面にプログラムがありません。')
            return
        prompts = {
            'X': '右側編集画面の全Ｘ軸に入力値を加算します。\nＸに加算する値を入力して下さい。',
            'Z': '右側編集画面の全Ｚ軸に入力値を加算します。\nＺに加算する値を入力して下さい。',
            'Y': '右側編集画面の全Ｙ軸に入力値を加算します。\nＹに加算する値を入力して下さい。',
            'F': '右側編集画面の全Ｆ値に入力値を加算します。\nＦに加算する値を入力して下さい。',
        }
        av = _input(self.w, '情報', prompts[axis])
        if av == '':
            return
        off = float(vbval(av))
        text = self.te2.toPlainText()
        if text and text[-1] != '\n':
            text += '\r\n'
        nc = splitter(text)
        if nc is None:
            return
        out = []
        for line in nc:
            parts = []
            j = 0
            while line.command[j] != '':
                cmd = line.command[j]
                val = line.value[j]
                if cmd == axis:
                    val = cv(float(vbval(val)) + off)
                parts.append(cmd + val)
                j += 1
            out.append(' '.join(parts))
        self.te2.setPlainText('\r\n'.join(out) if out else '')

    def replace_op(self):
        if self.te2.toPlainText() == '':
            _msg(self.w, '右側編集画面にプログラムがありません。')
            return
        st = _input(self.w, '情報', '右側編集画面で検索する文字列を入力して下さい。')
        if st == '':
            return
        rt = _input(self.w, '情報', '検索した文字列と置き換える文字列を入力して下さい。')
        if rt == '':
            return
        self.te2.setPlainText(self.te2.toPlainText().replace(st, '●' + rt))

    # ---------------- time report ----------------
    def time_report(self):
        if self.te1.toPlainText() == '':
            _msg(self.w, '左側編集画面にプログラムがありません。')
            return
        g0f = _input(self.w, '情報', 'Ｇ０に相当するＦ値を入力して下さい。', '2.0')
        if g0f == '':
            return
        kf = _input(self.w, '情報', '安全に加工する事が出来る送りの最大値を入力して下さい。', '0.05')
        if kf == '':
            return
        g0f_v = float(vbval(g0f))
        kf_v = float(vbval(kf))

        nc = splitter(self.te1.toPlainText())
        if nc is None:
            return

        import math
        f = 0.01
        s = 500.0
        g0s = 1000.0
        ex = 60.0
        ey = 60.0
        ez = 0.0

        process_second_g0 = 0.0
        process_second_g1 = 0.0
        process_second_g92 = 0.0
        process_length_g0 = 0.0
        process_length_g1 = 0.0
        process_length_g92 = 0.0
        process_f = 0.0
        process_s = 0.0
        cf = 0
        cs = 0
        dwell = 0.0

        for i in range(len(nc)):
            x, y, z = ex, ey, ez
            g4 = g40 = g41 = g42 = g50 = 0
            g92 = 0
            g92fx = 0
            g_mode = 0
            g92x = 0.0
            g92w = 0.0
            j = 0
            while nc[i].command[j] != '':
                cmd = nc[i].command[j]
                val = float(vbval(nc[i].value[j]))
                if cmd == 'F':
                    f = float(vbval(nc[i].value[j]))
                elif cmd == 'S':
                    s = float(vbval(nc[i].value[j]))
                elif cmd == 'X':
                    x = float(vbval(nc[i].value[j]))
                    if g92fx == 1:
                        g92x = float(vbval(nc[i].value[j]))
                        g92fx = 0
                elif cmd == 'Y':
                    y = float(vbval(nc[i].value[j]))
                elif cmd == 'Z':
                    z = float(vbval(nc[i].value[j]))
                    if g92 == 1:
                        g92w = abs(float(vbval(nc[i].value[j])) - ez)
                elif cmd == 'U':
                    if g4 == 0 and g40 == 0 and g41 == 0 and g42 == 0 and g50 == 0:
                        x = ex + float(vbval(nc[i].value[j]))
                    elif g4 == 1:
                        dwell += float(vbval(nc[i].value[j]))
                elif cmd == 'V':
                    y = ey + float(vbval(nc[i].value[j]))
                elif cmd == 'W':
                    if g40 == 0 and g41 == 0 and g42 == 0 and g50 == 0 and g92 == 0:
                        z = ez + abs(float(vbval(nc[i].value[j])))
                    elif g92 == 1:
                        g92w = float(vbval(nc[i].value[j]))
                elif cmd == 'G':
                    if val == 0:
                        g_mode = 0
                        g92 = 0
                    elif val in (1, 2, 3):
                        g_mode = 1
                        g92 = 0
                    elif val == 4:
                        g4 = 1
                    elif val == 40:
                        g40 = 1
                    elif val == 41:
                        g41 = 1
                    elif val == 42:
                        g42 = 1
                    elif val == 50:
                        g50 = 1
                    elif val == 92:
                        g92 = 1
                        g92fx = 1
                        g_mode = 0
                elif cmd == 'T':
                    if float(vbval(nc[i].value[j])) >= 100:
                        x = 60
                        y = 60
                        g_mode = 0
                j += 1
            xm = abs(x - ex)
            ym = abs(y - ey)
            zm = abs(z - ez)
            move_length = xm / 2
            if ym > move_length:
                move_length = ym / 2
            if zm > move_length:
                move_length = zm
            if move_length > 0:
                if g_mode == 0:
                    process_second_g0 += move_length / g0f_v * (60 / g0s)
                    process_length_g0 += move_length
                elif g_mode == 1:
                    process_second_g1 += move_length / f * (60 / s)
                    process_length_g1 += move_length
                if g92 == 1:
                    process_second_g92 += abs(x - g92x) / 2 / g0f_v * (60 / g0s)
                    process_second_g92 += g92w / g0f_v * (60 / g0s)
                    process_second_g92 += g92w / f * (60 / s)
                    process_length_g92 += g92w * 2 + abs(x - g92x) / 2
                if f <= kf_v:
                    process_f += f
                    cf += 1
                process_s += s
                cs += 1
            ex = g92x if g92 == 1 else x
            ey = y
            ez = z

        def i(x):
            return int(x)

        process_second = i(process_second_g0) + i(process_second_g1) + i(dwell) + i(process_second_g92)
        process_length = i(process_length_g0) + i(process_length_g1) + i(process_length_g92)

        report = ''
        report += '総加工時間は ' + cv2(process_second) + '秒(' + cv2(process_second / 60) + '分' + cv2(process_second - 60 * int(process_second / 60)) + '秒) です。\n\n'
        report += '１時間で ' + cv2(3600 / process_second) + '個 加工出来ます。\n'
        report += '１日で ' + cv2(3600 / process_second * 24) + '個 加工出来ます。\n\n'
        report += 'Ｇ４での一時停止時間は ' + cv2(dwell) + '秒 です。\n'
        report += 'Ｇ０の移動時間は ' + cv2(process_second_g0) + '秒 です。\n'
        report += 'Ｇ１の加工時間は ' + cv2(process_second_g1) + '秒 です。\n'
        report += 'Ｇ９２の加工時間は ' + cv2(process_second_g92) + '秒 です。\n\n'
        report += '総平面移動距離は ' + cv2(process_length) + 'mm です。\n'
        report += 'Ｇ０の平面移動距離は ' + cv2(process_length_g0) + 'mm です。\n'
        report += 'Ｇ１の平面加工距離は ' + cv2(process_length_g1) + 'mm です。\n'
        report += 'Ｇ９２の平面加工距離は ' + cv2(process_length_g92) + 'mm です。\n\n'
        report += '加工する際の送りの平均は F' + cv(process_f / cf) + ' です。\n'
        report += '回転数の平均は S' + cv2(process_s / cs) + ' です。'
        _msg(self.w, report)


def make_form1():
    f = Form1()
    return f
