import json
import os

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QFont, QPixmap, QCursor, QColor, QPalette
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QGroupBox,
    QCheckBox, QComboBox, QListWidget, QScrollArea, QFrame,
)

from .images import find_image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT_DIR = os.path.join(BASE, 'layout')

FONT_MAP = {
    'ＭＳ ゴシック': 'MS Gothic',
    'MS ゴシック': 'MS Gothic',
    'ＭＳ 明朝': 'MS Mincho',
    'MS 明朝': 'MS Mincho',
    'ＭＳ UI ゴシック': 'MS UI Gothic',
    'MS UI Gothic': 'MS UI Gothic',
}


def make_font(spec):
    if not spec:
        return None
    family = FONT_MAP.get(spec.get('name'), spec.get('name'))
    size = spec.get('size', 8.25)
    style = spec.get('style', 'Regular')
    f = QFont(family)
    f.setPointSizeF(float(size))
    if style in ('Bold', 'BoldItalic'):
        f.setBold(True)
    if style in ('Italic', 'BoldItalic'):
        f.setItalic(True)
    return f


class _AnchorInfo:
    def __init__(self, widget, parent, anchors, x, y, w, h):
        self.widget = widget
        self.parent = parent
        self.anchors = set(anchors)
        self.left = x
        self.top = y
        self.right = parent.width() - (x + w)
        self.bottom = parent.height() - (y + h)
        self.w0 = w
        self.h0 = h

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            pw = self.parent.width()
            ph = self.parent.height()
            a = self.anchors
            if 'Left' in a and 'Right' in a:
                x, w = self.left, pw - self.left - self.right
            elif 'Left' in a:
                x, w = self.left, self.w0
            else:
                x, w = pw - self.right - self.w0, self.w0
            if 'Top' in a and 'Bottom' in a:
                y, h = self.top, ph - self.top - self.bottom
            elif 'Top' in a:
                y, h = self.top, self.h0
            else:
                y, h = ph - self.bottom - self.h0, self.h0
            self.widget.setGeometry(x, y, w, h)
        return False


def _install_anchors(widget, parent, anchors, x, y, w, h):
    if not anchors:
        return
    a = set(anchors)
    if a <= {'Top', 'Left'}:
        return
    info = _AnchorInfo(widget, parent, anchors, x, y, w, h)
    parent.installEventFilter(info)


class FormBuilder:
    def __init__(self, form_name):
        path = os.path.join(LAYOUT_DIR, form_name + '.json')
        with open(path, encoding='utf-8') as f:
            self.spec = json.load(f)
        self.controls = {}

    def build(self):
        spec = self.spec
        fp = spec.get('formprops', {})
        cs = spec.get('clientsize') or [640, 480]
        maximized = fp.get('windowstate') == 'Maximized'
        autoscroll = fp.get('autoscroll') is True
        if autoscroll:
            form = QScrollArea()
            form.setFrameShape(QFrame.NoFrame)
            form.setWidgetResizable(False)
            root = QWidget()
            form.setWidget(root)
        else:
            form = QWidget()
            root = form
        form.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        form.setWindowTitle(spec.get('title', ''))
        if maximized:
            form.resize(cs[0], cs[1])
        else:
            form.setFixedSize(cs[0], cs[1])
        if fp.get('backcolor') == 'White':
            form.setAutoFillBackground(True)
            pal = form.palette()
            pal.setColor(form.backgroundRole(), QColor('white'))
            form.setPalette(pal)
            if autoscroll:
                for wgt in (form.viewport(), root):
                    wgt.setAutoFillBackground(True)
                    pal = wgt.palette()
                    pal.setColor(wgt.backgroundRole(), QColor('white'))
                    wgt.setPalette(pal)
        if fp.get('showintaskbar') is False:
            form.setWindowFlag(Qt.Tool)
        by_name = {c['name']: c for c in spec['controls']}

        def make(c, parent):
            t = c['type']
            x, y = c.get('location', [0, 0])
            w, h = c.get('size', [100, 20])
            widget = None
            if t == 'Label':
                widget = QLabel(parent)
                widget.setText(c.get('text', ''))
                f = make_font(c.get('font'))
                if f:
                    widget.setFont(f)
                widget.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                if c.get('autosize'):
                    widget.adjustSize()
                    widget.move(x, y)
                else:
                    widget.setGeometry(x, y, w, h)
            elif t == 'Button':
                widget = QPushButton(parent)
                widget.setText(c.get('text', ''))
                f = make_font(c.get('font'))
                if f:
                    widget.setFont(f)
                widget.setGeometry(x, y, w, h)
            elif t == 'TextBox':
                if c.get('multiline'):
                    widget = QPlainTextEdit(parent)
                    widget.setLineWrapMode(QPlainTextEdit.NoWrap)
                    widget.setGeometry(x, y, w, h)
                    if c.get('text'):
                        widget.setPlainText(c['text'])
                    f = make_font(c.get('font'))
                    if f:
                        widget.setFont(f)
                    widget.setFrameStyle(widget.frameStyle())
                else:
                    widget = QLineEdit(parent)
                    widget.setGeometry(x, y, w, h)
                    widget.setText(c.get('text', ''))
                    f = make_font(c.get('font'))
                    if f:
                        widget.setFont(f)
            elif t == 'GroupBox':
                widget = QGroupBox(parent)
                widget.setTitle(c.get('text', ''))
                widget.setGeometry(x, y, w, h)
            elif t == 'CheckBox':
                widget = QCheckBox(parent)
                widget.setText(c.get('text', ''))
                if c.get('checked'):
                    widget.setChecked(True)
                f = make_font(c.get('font'))
                if f:
                    widget.setFont(f)
                widget.adjustSize()
                widget.move(x, y)
            elif t == 'ComboBox':
                widget = QComboBox(parent)
                widget.setGeometry(x, y, w, h)
                f = make_font(c.get('font'))
                if f:
                    widget.setFont(f)
                for it in c.get('items') or []:
                    widget.addItem(str(it))
                if c.get('items'):
                    if c.get('text'):
                        widget.setCurrentText(str(c['text']))
                    else:
                        widget.setCurrentIndex(-1)
            elif t == 'ListBox':
                widget = QListWidget(parent)
                widget.setGeometry(x, y, w, h)
                f = make_font(c.get('font'))
                if f:
                    widget.setFont(f)
                if c.get('selectionmode') == 'MultiExtended':
                    widget.setSelectionMode(QListWidget.ExtendedSelection)
            elif t == 'PictureBox':
                widget = QLabel(parent)
                widget.setText('')
                img = find_image(spec['name'], c.get('image'))
                if img:
                    pm = QPixmap(img)
                    if c.get('sizemode') == 'AutoSize':
                        widget.setPixmap(pm)
                        widget.adjustSize()
                        widget.move(x, y)
                    else:
                        widget.setPixmap(pm.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                        widget.setGeometry(x, y, w, h)
                else:
                    widget.setGeometry(x, y, w, h)
                widget.setCursor(QCursor(Qt.PointingHandCursor))
            else:
                widget = QWidget(parent)
                widget.setGeometry(x, y, w, h)

            if t != 'GroupBox':
                _install_anchors(widget, parent, c.get('anchor'), x, y, w, h)
            self.controls[c['name']] = widget
            return widget

        def create(name):
            if name in self.controls:
                return self.controls[name]
            c = by_name[name]
            p = c.get('parent')
            if p:
                create(p)
                parent = self.controls[p]
            else:
                parent = root
            return make(c, parent)

        for c in spec['controls']:
            create(c['name'])

        if autoscroll:
            kids = root.findChildren(QWidget)
            cw = max((w.x() + w.width() for w in kids), default=cs[0])
            ch = max((w.y() + w.height() for w in kids), default=cs[1])
            root.resize(cw, ch)

        for name in spec.get('zorder', []):
            w = self.controls.get(name)
            if w is not None and w.parent() is root:
                w.raise_()

        if maximized:
            form.showMaximized()
        return form


def load_spec(form_name):
    path = os.path.join(LAYOUT_DIR, form_name + '.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)
