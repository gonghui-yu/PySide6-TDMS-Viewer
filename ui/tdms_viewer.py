# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdms_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPlainTextEdit, QPushButton,
    QScrollBar, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QTableView, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import ui.resource_rc

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
        self.gridLayout_5 = QGridLayout(TDMSViewer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_all = QSplitter(TDMSViewer)
        self.splitter_all.setObjectName(u"splitter_all")
        self.splitter_all.setOrientation(Qt.Horizontal)
        self.splitter_all.setHandleWidth(2)
        self.splitter_all.setChildrenCollapsible(False)
        self.splitter_left = QSplitter(self.splitter_all)
        self.splitter_left.setObjectName(u"splitter_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_left.sizePolicy().hasHeightForWidth())
        self.splitter_left.setSizePolicy(sizePolicy1)
        self.splitter_left.setMinimumSize(QSize(200, 0))
        self.splitter_left.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_left.setOrientation(Qt.Vertical)
        self.splitter_left.setHandleWidth(2)
        self.splitter_left.setChildrenCollapsible(False)
        self.widget = QWidget(self.splitter_left)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.ui_file_dialog_btn = QPushButton(self.widget)
        self.ui_file_dialog_btn.setObjectName(u"ui_file_dialog_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ui_file_dialog_btn.sizePolicy().hasHeightForWidth())
        self.ui_file_dialog_btn.setSizePolicy(sizePolicy3)
        self.ui_file_dialog_btn.setMinimumSize(QSize(30, 30))
        self.ui_file_dialog_btn.setMaximumSize(QSize(30, 30))
        self.ui_file_dialog_btn.setStyleSheet(u"background-image:url(:/file dialog btn.png)")
        self.ui_file_dialog_btn.setIconSize(QSize(16, 16))
        self.ui_file_dialog_btn.setCheckable(False)

        self.gridLayout.addWidget(self.ui_file_dialog_btn, 0, 1, 1, 1)

        self.ui_file_path = QPlainTextEdit(self.widget)
        self.ui_file_path.setObjectName(u"ui_file_path")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ui_file_path.sizePolicy().hasHeightForWidth())
        self.ui_file_path.setSizePolicy(sizePolicy4)
        self.ui_file_path.setMinimumSize(QSize(0, 100))
        self.ui_file_path.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.ui_file_path, 0, 0, 2, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.splitter_left.addWidget(self.widget)
        self.ui_file_content = QTreeWidget(self.splitter_left)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.ui_file_content.setHeaderItem(__qtreewidgetitem)
        self.ui_file_content.setObjectName(u"ui_file_content")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(6)
        sizePolicy5.setHeightForWidth(self.ui_file_content.sizePolicy().hasHeightForWidth())
        self.ui_file_content.setSizePolicy(sizePolicy5)
        self.ui_file_content.setMinimumSize(QSize(0, 0))
        self.ui_file_content.setAutoFillBackground(False)
        self.ui_file_content.setMidLineWidth(0)
        self.splitter_left.addWidget(self.ui_file_content)
        self.ui_property_list = QTableWidget(self.splitter_left)
        self.ui_property_list.setObjectName(u"ui_property_list")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.ui_property_list.sizePolicy().hasHeightForWidth())
        self.ui_property_list.setSizePolicy(sizePolicy6)
        self.ui_property_list.setMinimumSize(QSize(0, 0))
        self.splitter_left.addWidget(self.ui_property_list)
        self.widget_2 = QWidget(self.splitter_left)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.ui_start_index = QSpinBox(self.widget_2)
        self.ui_start_index.setObjectName(u"ui_start_index")

        self.verticalLayout.addWidget(self.ui_start_index)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.ui_samples = QSpinBox(self.widget_2)
        self.ui_samples.setObjectName(u"ui_samples")

        self.verticalLayout_2.addWidget(self.ui_samples)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.ui_is_all_samples = QCheckBox(self.widget_2)
        self.ui_is_all_samples.setObjectName(u"ui_is_all_samples")

        self.verticalLayout_3.addWidget(self.ui_is_all_samples)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.splitter_left.addWidget(self.widget_2)
        self.splitter_all.addWidget(self.splitter_left)
        self.splitter_right = QSplitter(self.splitter_all)
        self.splitter_right.setObjectName(u"splitter_right")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(8)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.splitter_right.sizePolicy().hasHeightForWidth())
        self.splitter_right.setSizePolicy(sizePolicy8)
        self.splitter_right.setMinimumSize(QSize(500, 0))
        self.splitter_right.setOrientation(Qt.Vertical)
        self.splitter_right.setHandleWidth(2)
        self.splitter_right.setChildrenCollapsible(False)
        self.ui_graph = QChartView(self.splitter_right)
        self.ui_graph.setObjectName(u"ui_graph")
        sizePolicy5.setHeightForWidth(self.ui_graph.sizePolicy().hasHeightForWidth())
        self.ui_graph.setSizePolicy(sizePolicy5)
        self.ui_graph.setMinimumSize(QSize(0, 0))
        self.splitter_right.addWidget(self.ui_graph)
        self.widget_3 = QWidget(self.splitter_right)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ui_data_list = QTableView(self.widget_3)
        self.ui_data_list.setObjectName(u"ui_data_list")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(4)
        sizePolicy9.setHeightForWidth(self.ui_data_list.sizePolicy().hasHeightForWidth())
        self.ui_data_list.setSizePolicy(sizePolicy9)
        self.ui_data_list.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.ui_data_list)

        self.ui_data_list_scroll_bar = QScrollBar(self.widget_3)
        self.ui_data_list_scroll_bar.setObjectName(u"ui_data_list_scroll_bar")
        self.ui_data_list_scroll_bar.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.ui_data_list_scroll_bar)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.splitter_right.addWidget(self.widget_3)
        self.splitter_all.addWidget(self.splitter_right)

        self.gridLayout_5.addWidget(self.splitter_all, 0, 0, 1, 1)


        self.retranslateUi(TDMSViewer)

        QMetaObject.connectSlotsByName(TDMSViewer)
    # setupUi

    def retranslateUi(self, TDMSViewer):
        TDMSViewer.setWindowTitle(QCoreApplication.translate("TDMSViewer", u"Form", None))
        self.ui_file_dialog_btn.setText("")
        self.label.setText(QCoreApplication.translate("TDMSViewer", u"\u5f00\u59cb\u7d22\u5f15", None))
        self.label_2.setText(QCoreApplication.translate("TDMSViewer", u"\u70b9\u6570", None))
        self.ui_is_all_samples.setText(QCoreApplication.translate("TDMSViewer", u"\u6240\u6709\u70b9", None))
    # retranslateUi

