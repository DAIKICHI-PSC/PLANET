import json
import os

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QIcon

from .layout import FormBuilder
from .images import app_icon
from . import formreg

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MAP = json.load(open(os.path.join(BASE, 'kako_map.json'), encoding='utf-8'))


class _ListClose(QObject):
    def __init__(self, form_obj):
        super().__init__()
        self._fo = form_obj

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            self._fo.w.hide()
            f1 = formreg.get_form('Form1')
            if f1 is not None:
                f1.w.show()
            event.ignore()
            return True
        return False


class ListForm:
    def __init__(self, name):
        self.name = name
        fb = FormBuilder(name)
        self.w = fb.build()
        self.w.setWindowIcon(QIcon(app_icon()))
        self.controls = fb.controls
        self._close = _ListClose(self)
        self.w.installEventFilter(self._close)
        for pb, kako in _MAP.get(name, {}).items():
            if pb in self.controls:
                self.controls[pb].mousePressEvent = (lambda e, k=kako: self._open_kako(k))
        formreg.register(name, self)

    def _open_kako(self, kako_name):
        self.w.hide()
        kf = formreg.get_form(kako_name)
        if kf is None:
            from .kako import make_kako
            kf = make_kako(kako_name)
        kf.w.show()

    def show(self):
        self.w.show()


def make_list(name):
    return ListForm(name)
