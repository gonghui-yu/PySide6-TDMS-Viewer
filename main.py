from PySide6.QtWidgets import QApplication

import sys

from view_main import ViewMain

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ViewMain()

    window.show()

    app.exec()
