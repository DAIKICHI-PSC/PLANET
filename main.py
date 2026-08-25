import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from planet.mainform import Form1


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('PLANET')
    app.setFont(QFont('MS UI Gothic', 9))
    form = Form1()
    form.w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
