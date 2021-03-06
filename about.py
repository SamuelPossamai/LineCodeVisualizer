#!/usr/bin/env python3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication

Ui_About, _ = uic.loadUiType("about.ui")

class About(QDialog, Ui_About):

    def __init__(self, parent=None):

        QDialog.__init__(self, parent=parent)
        Ui_About.__init__(self)
        self.setupUi(self)

        self.okButton.clicked.connect(self.close)

def __runfile__():

    app = QApplication(sys.argv)

    main = About()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    __runfile__()
