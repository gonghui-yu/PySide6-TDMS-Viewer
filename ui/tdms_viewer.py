# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdms_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHeaderView,
    QListView, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTreeView, QWidget)

class Ui_TDMSViewer(object):
    def setupUi(self, TDMSViewer):
        if not TDMSViewer.objectName():
            TDMSViewer.setObjectName(u"TDMSViewer")
        TDMSViewer.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(TDMSViewer.sizePolicy().hasHeightForWidth())
        TDMSViewer.setSizePolicy(sizePolicy)
        TDMSViewer.setMinimumSize(QSize(1366, 768))
        self.gridLayout_3 = QGridLayout(TDMSViewer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_all = QSplitter(TDMSViewer)
        self.splitter_all.setObjectName(u"splitter_all")
        self.splitter_all.setMinimumSize(QSize(0, 0))
        self.splitter_all.setOrientation(Qt.Horizontal)
        self.splitter_all.setHandleWidth(1)
        self.splitter_all.setChildrenCollapsible(False)
        self.splitter_left = QSplitter(self.splitter_all)
        self.splitter_left.setObjectName(u"splitter_left")
        self.splitter_left.setMinimumSize(QSize(200, 100))
        self.splitter_left.setOrientation(Qt.Vertical)
        self.splitter_left.setHandleWidth(1)
        self.splitter_left.setChildrenCollapsible(False)
        self.widget = QWidget(self.splitter_left)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.file_dialog_btn = QPushButton(self.widget)
        self.file_dialog_btn.setObjectName(u"file_dialog_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.file_dialog_btn.sizePolicy().hasHeightForWidth())
        self.file_dialog_btn.setSizePolicy(sizePolicy2)
        self.file_dialog_btn.setMinimumSize(QSize(30, 30))
        self.file_dialog_btn.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.file_dialog_btn, 0, 1, 1, 1)

        self.file_path = QPlainTextEdit(self.widget)
        self.file_path.setObjectName(u"file_path")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.file_path.sizePolicy().hasHeightForWidth())
        self.file_path.setSizePolicy(sizePolicy3)
        self.file_path.setMinimumSize(QSize(0, 100))
        self.file_path.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.file_path, 0, 0, 2, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.splitter_left.addWidget(self.widget)
        self.group_tree = QTreeView(self.splitter_left)
        self.group_tree.setObjectName(u"group_tree")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(6)
        sizePolicy4.setHeightForWidth(self.group_tree.sizePolicy().hasHeightForWidth())
        self.group_tree.setSizePolicy(sizePolicy4)
        self.group_tree.setMinimumSize(QSize(0, 0))
        self.group_tree.setAutoFillBackground(False)
        self.splitter_left.addWidget(self.group_tree)
        self.property_list = QListView(self.splitter_left)
        self.property_list.setObjectName(u"property_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(3)
        sizePolicy5.setHeightForWidth(self.property_list.sizePolicy().hasHeightForWidth())
        self.property_list.setSizePolicy(sizePolicy5)
        self.property_list.setMinimumSize(QSize(0, 0))
        self.splitter_left.addWidget(self.property_list)
        self.splitter_all.addWidget(self.splitter_left)
        self.splitter_right = QSplitter(self.splitter_all)
        self.splitter_right.setObjectName(u"splitter_right")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(8)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.splitter_right.sizePolicy().hasHeightForWidth())
        self.splitter_right.setSizePolicy(sizePolicy6)
        self.splitter_right.setMinimumSize(QSize(500, 400))
        self.splitter_right.setOrientation(Qt.Vertical)
        self.splitter_right.setHandleWidth(1)
        self.splitter_right.setChildrenCollapsible(False)
        self.wave_graph = QGraphicsView(self.splitter_right)
        self.wave_graph.setObjectName(u"wave_graph")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(6)
        sizePolicy7.setHeightForWidth(self.wave_graph.sizePolicy().hasHeightForWidth())
        self.wave_graph.setSizePolicy(sizePolicy7)
        self.wave_graph.setMinimumSize(QSize(0, 100))
        self.splitter_right.addWidget(self.wave_graph)
        self.data_list = QListView(self.splitter_right)
        self.data_list.setObjectName(u"data_list")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(4)
        sizePolicy8.setHeightForWidth(self.data_list.sizePolicy().hasHeightForWidth())
        self.data_list.setSizePolicy(sizePolicy8)
        self.data_list.setMinimumSize(QSize(0, 100))
        self.splitter_right.addWidget(self.data_list)
        self.splitter_all.addWidget(self.splitter_right)

        self.gridLayout_3.addWidget(self.splitter_all, 0, 0, 1, 1)


        self.retranslateUi(TDMSViewer)

        QMetaObject.connectSlotsByName(TDMSViewer)
    # setupUi

    def retranslateUi(self, TDMSViewer):
        TDMSViewer.setWindowTitle(QCoreApplication.translate("TDMSViewer", u"Form", None))
        self.file_dialog_btn.setText("")
    # retranslateUi

