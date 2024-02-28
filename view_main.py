from PySide6.QtWidgets import QWidget, QAbstractItemView
from ui.tdms_viewer import Ui_TDMSViewer


class ViewMain(QWidget, Ui_TDMSViewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TDMS查看器")

        self.group_tree.header().show()
