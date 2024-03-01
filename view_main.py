import os.path

from PySide6 import QtCore
from PySide6.QtCore import Slot, Signal, QThread, QObject
from PySide6.QtCharts import QChart, QValueAxis, QDateTimeAxis, QLineSeries
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, \
    QTableWidgetItem
from PySide6.QtCore import Qt
from ui.tdms_viewer import Ui_TDMSViewer

from model_tdms import ModelTDMS


class ViewMain(QWidget, Ui_TDMSViewer):
    signal_read_file_content = Signal(str)
    signal_read_file_properties = Signal(str)
    signal_read_group_properties = Signal(str, str)
    signal_read_channel_properties = Signal(str, str, str)
    signal_read_file_points = Signal(str, int, int)
    signal_read_group_points = Signal(str, str, int, int)
    signal_read_channel_points = Signal(str, str, str, int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TDMS查看器")

        # 属性
        self.file_path = None  # 保存选择的TDMS文件路径

        # 初始化文件选择器
        self.ui_file_dialog_btn.clicked.connect(self.slot_file_dialog_btn_click)

        # 初始化文件内容树
        self.ui_file_content.setHeaderLabel("TDMS文件内容")  # 设置列首
        self.ui_file_content.setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")  # 设置列首背景
        self.ui_file_content.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # 设置选中整行
        self.ui_file_content.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)  # 设置一次只能选中一行

        self.ui_file_content.clicked.connect(self.slot_read_file)

        # self.ui_file_content.setStyleSheet("QTreeView{show-decoration-selected:1;background:rgb(61,66,77);}"
        #                                    "QTreeView::item{border:2px;color:rgb(255,255,255);}"
        #                                    "QTreeView::item:selected,QTreeView::branch:selected{background:rgb(28,77,"
        #                                    "120);}"
        #                                    "QTreeView::item:hover,QTreeView::branch:hover{background:rgb(64,91,134);}")

        # 初始化属性列表
        self.ui_property_list.setColumnCount(2)  # 设置列数，不设置列首不显示
        self.ui_property_list.setRowCount(10)
        self.ui_property_list.setHorizontalHeaderLabels(["属性名称", "属性值"])  # 设置列首
        self.ui_property_list.verticalHeader().setVisible(False)  # 隐藏行首
        self.ui_property_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑单元格内容
        # 设置列首背景
        self.ui_property_list.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")
        # 自动调整列宽
        self.ui_property_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 设置可以手动在列首调整列宽
        self.ui_property_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)

        # 初始化数据列表
        self.ui_data_list.setColumnCount(10)  # 设置列数，不设置列首不显示
        self.ui_data_list.setRowCount(20)
        self.ui_data_list.setHorizontalHeaderLabels([])  # 设置列首
        self.ui_data_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑单元格内容
        # 设置列首背景
        self.ui_data_list.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")

        # 初始化波形图
        self.ui_chart = QChart()
        self.ui_graph.setChart(self.ui_chart)
        self.ui_chart.addSeries(QLineSeries())
        self.ui_chart.createDefaultAxes()  # 创建默认坐标轴，基于已经添加到chart中的series
        self.ui_chart.legend().setVisible(True)  # 显示图例
        self.ui_chart.legend().setAlignment(Qt.AlignRight)  # 图例显示在波形图右侧
        self.ui_graph.setRenderHint(QPainter.Antialiasing)  # 反锯齿绘制

        # 设置初始比例，因为QChart不能在.ui中设置初始比例
        self.splitter_right.setStretchFactor(0, 8)
        self.splitter_right.setStretchFactor(1, 2)

        self.model_tdms = ModelTDMS()

        self.signal_read_file_content.connect(self.model_tdms.slot_read_file_content)

        self.signal_read_file_properties.connect(self.model_tdms.slot_read_file_properties)
        self.signal_read_group_properties.connect(self.model_tdms.slot_read_group_properties)
        self.signal_read_channel_properties.connect(self.model_tdms.slot_read_channel_properties)

        self.signal_read_file_points.connect(self.model_tdms.slot_read_file_points)
        self.signal_read_group_points.connect(self.model_tdms.slot_read_group_points)
        self.signal_read_channel_points.connect(self.model_tdms.slot_read_channel_points)

        self.model_tdms.signal_update_file_content.connect(self.slot_update_file_content)
        self.model_tdms.signal_update_properties.connect(self.slot_update_properties)
        self.model_tdms.signal_update_points.connect(self.slot_update_points)

        self.model_tdms.start()

        self.file_path = r"C:\Users\YUGONGHUI\Desktop\Data\20240228_055622.tdms"
        self.signal_read_file_content.emit(self.file_path)

        self.ui_start_index.setMaximum(2147483647)
        self.ui_start_index.setMinimum(0)
        self.ui_start_index.setValue(0)
        self.ui_samples.setMaximum(2147483647)
        self.ui_samples.setMinimum(0)
        self.ui_samples.setValue(10)
        self.ui_is_all_samples.setChecked(False)

    def __del__(self):
        # 窗口关闭不执行
        print("析构函数")
        # self.model_tdms.quit()

    @Slot()
    def slot_file_dialog_btn_click(self):
        self.file_path = QFileDialog.getOpenFileName(self, "选择TDMS文件", "", "*.tdms")[0]
        self.ui_file_path.setPlainText(self.file_path)
        if self.file_path is not None:
            self.signal_read_file_content.emit(self.file_path)

    @Slot(dict)
    def slot_update_file_content(self, file_content):
        # 文件层级
        first_level_item = QTreeWidgetItem()
        first_level_item.setText(0, os.path.split(self.file_path)[1])
        self.ui_file_content.addTopLevelItem(first_level_item)

        # 组层级
        for group in file_content.keys():
            second_level_item = QTreeWidgetItem()
            second_level_item.setText(0, group)
            first_level_item.addChild(second_level_item)
            # 通道层级
            for channel in file_content[group]:
                third_level_item = QTreeWidgetItem()
                third_level_item.setText(0, channel)
                second_level_item.addChild(third_level_item)

        self.ui_file_content.expandAll()

    @Slot()
    def slot_read_file(self):
        if self.ui_file_content.currentItem().parent() is None:
            # 文件层
            # 读取文件属性
            self.signal_read_file_properties.emit(self.file_path)
            # 读取文件数据
            self.signal_read_file_points.emit(self.file_path,
                                              self.ui_start_index.value(),
                                              self.ui_samples.value())
        elif self.ui_file_content.currentItem().child(0) is None:
            # 通道层
            # 读取通道属性
            self.signal_read_channel_properties.emit(self.file_path,
                                                     self.ui_file_content.currentItem().parent().text(0),
                                                     self.ui_file_content.currentItem().text(0)
                                                     )
            # 读取通道数据
            self.signal_read_channel_points.emit(self.file_path,
                                                 self.ui_file_content.currentItem().parent().text(0),
                                                 self.ui_file_content.currentItem().text(0),
                                                 self.ui_start_index.value(),
                                                 self.ui_samples.value())

        else:
            # 组层
            # 读取组属性
            self.signal_read_group_properties.emit(self.file_path,
                                                   self.ui_file_content.currentItem().text(0))
            # 读取组数据
            self.signal_read_group_points.emit(self.file_path,
                                               self.ui_file_content.currentItem().text(0),
                                               self.ui_start_index.value(),
                                               self.ui_samples.value())

    @Slot(dict)
    def slot_update_properties(self, properties):
        if len(properties) == 0:
            self.ui_property_list.clear()
        else:
            i = 0
            for key, value in properties.items():
                item_key = QTableWidgetItem(key)
                self.ui_property_list.setItem(i, 0, item_key)

                item_value = QTableWidgetItem(str(value))
                self.ui_property_list.setItem(i, 1, item_value)
                i = i + 1

    @Slot(dict)
    def slot_update_points(self, points):
        pass
