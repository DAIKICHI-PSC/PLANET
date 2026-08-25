import os

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox, QLineEdit, QComboBox, QPlainTextEdit

from .layout import FormBuilder
from .images import app_icon
from . import formreg
from . import kako_logic

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class _KakoClose(QObject):
    def __init__(self, form_obj):
        super().__init__()
        self._fo = form_obj

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            self._fo.w.hide()
            lf = formreg.get_form(self._fo.list_name)
            if lf is not None:
                lf.w.show()
            event.ignore()
            return True
        return False


class KakoForm:
    def __init__(self, name):
        self.name = name
        parts = name.split('_')
        self.list_name = 'List_' + '_'.join(parts[1:-1])
        fb = FormBuilder(name)
        self.w = fb.build()
        self.w.setWindowIcon(QIcon(app_icon()))
        self.controls = fb.controls
        self._out = self.controls.get('TextBox1')
        self._txt = ''
        b1 = self.controls.get('Button1')
        b2 = self.controls.get('Button2')
        b3 = self.controls.get('Button3')
        if b1 is not None:
            b1.clicked.connect(self.generate)
        if b2 is not None:
            b2.clicked.connect(self.run_action)
        if b3 is not None:
            b3.clicked.connect(self.append_action)
        self._close = _KakoClose(self)
        self.w.installEventFilter(self._close)
        formreg.register(name, self)

    # ---- helpers referenced by the generated Button1 code ----
    def txt(self, name):
        if name == 'TextBox1':
            return self._txt
        w = self.controls.get(name)
        if w is None:
            return ''
        if isinstance(w, QPlainTextEdit):
            return w.toPlainText()
        if isinstance(w, QComboBox):
            return w.currentText()
        if isinstance(w, QLineEdit):
            return w.text()
        return ''

    def cbindex(self, name):
        w = self.controls.get(name)
        if isinstance(w, QComboBox):
            return w.currentIndex()
        return 0

    def a(self, line):
        self._txt += line + '\r\n'

    def set_out(self, s):
        self._txt = str(s)

    def settxt(self, name, s):
        w = self.controls.get(name)
        if w is None:
            return
        if isinstance(w, QPlainTextEdit):
            w.setPlainText(str(s))
        elif isinstance(w, (QLineEdit, QComboBox)):
            w.setText(str(s))

    def outtext(self):
        return self._txt

    def msgbox(self, text, title='情報'):
        QMessageBox.information(self.w, title, str(text))

    # ---- button actions ----
    def generate(self):
        fn = getattr(kako_logic, 'gen_' + self.name, None)
        if fn is None:
            return
        self._txt = ''
        fn(self)
        if self._out is not None:
            self._out.setPlainText(self._txt)

    def run_action(self):
        f1 = formreg.get_form('Form1')
        if f1 is not None:
            f1.run(self.outtext())

    def append_action(self):
        f1 = formreg.get_form('Form1')
        if f1 is not None:
            f1.append_to_left(self.outtext())

    def show(self):
        self.w.show()


def make_kako(name):
    return KakoForm(name)
