import math
import os.path

import numpy
from PySide6.QtCore import Slot, Signal, QPointF, QDateTime
from PySide6.QtCharts import QChart, QValueAxis, QDateTimeAxis, QLineSeries
from PySide6.QtGui import QPainter, QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, \
    QTableWidgetItem, QStyle
from PySide6.QtCore import Qt
from ui.tdms_viewer import Ui_TDMSViewer

from model_tdms import ModelTDMS


class ViewMain(QWidget, Ui_TDMSViewer):
    signal_read_file_content = Signal(str)
    signal_read_file_properties = Signal(str)
    signal_read_group_properties = Signal(str, str)
    signal_read_channel_properties = Signal(str, str, str)
    signal_read_file_points = Signal(str, bool, int, int)
    signal_read_group_points = Signal(str, str, bool, int, int)
    signal_read_channel_points = Signal(str, str, str, bool, int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TDMS查看器")  # 设置窗口标题

        self.file_path = None  # 保存选择的TDMS文件路径
        self.init_file_dialog()  # 初始化TDMS文件选择弹窗

        self.init_file_content()  # 初始化文件内容数控件

        self.init_property_tab()  # 初始化属性列表

        self.points_tab_model = QStandardItemModel(self.ui_points_tab)  # 新建数据列表数据模型
        self.current_points = []  # 记录当前通道数据，用于滚动条动态显示数据
        self.header_label_list = []  # 数据表列首内容
        self.init_points_tab()  # # 初始化数据列表

        self.ui_chart = QChart()
        self.init_chart()  # 初始化波形图

        self.model_tdms = ModelTDMS()  # 创建ModelTDMS对象
        self.init_model_tdms()  # 初始化ModelTDMS对象

        self.file_path = r"C:\Users\Administrator\Desktop\Test.tdms"
        self.signal_read_file_content.emit(self.file_path)

        self.ui_start_index.setMaximum(2147483647)
        self.ui_start_index.setMinimum(0)
        self.ui_start_index.setValue(0)
        self.ui_samples.setMaximum(2147483647)
        self.ui_samples.setMinimum(0)
        self.ui_samples.setValue(10)
        self.ui_all_samples.setChecked(False)

    def __del__(self):
        # 窗口关闭不执行
        print("析构函数")
        # self.model_tdms.quit()

    def init_file_dialog(self):
        # 初始化文件选择器
        self.ui_file_dialog_btn.clicked.connect(self.slot_file_dialog_btn_click)
        self.ui_file_path.setReadOnly(True)

    def init_file_content(self):
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

    def init_property_tab(self):
        self.ui_prop_tab.setColumnCount(2)  # 设置列数，不设置列首不显示
        self.ui_prop_tab.setRowCount(10)
        self.ui_prop_tab.setHorizontalHeaderLabels(["属性名称", "属性值"])  # 设置列首
        self.ui_prop_tab.verticalHeader().setVisible(False)  # 隐藏行首
        self.ui_prop_tab.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑单元格内容
        # 设置列首背景
        self.ui_prop_tab.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")
        # 自动调整列宽
        self.ui_prop_tab.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 设置可以手动在列首调整列宽
        self.ui_prop_tab.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)

    def init_points_tab(self):
        self.ui_points_tab.setModel(self.points_tab_model)
        self.ui_points_tab.setGridStyle(Qt.PenStyle.SolidLine)  # 设置单元格分隔线类型
        self.ui_points_tab.setShowGrid(True)  # 设置显示单元格分隔线
        self.ui_points_tab.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 不可编辑单元格内容

        # 设置列首
        self.ui_points_tab.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")
        h_header_font = QFont()  # 字体格式
        h_header_font.setPixelSize(13)  # 字号
        h_header_font.setBold(True)  # 加粗
        self.ui_points_tab.horizontalHeader().setFont(h_header_font)  # 设置列首字体格式
        self.ui_points_tab.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)  # 列首内容左对齐

        # 设置行首
        self.ui_points_tab.verticalHeader().setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")  # 行首背景色
        self.ui_points_tab.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignRight)  # 行首内容右对齐
        self.ui_points_tab.verticalHeader().setMinimumWidth(40)  # 设置行首最小宽度

        # 初始化行列数
        self.points_tab_model.setRowCount(20)  # 初始化行数
        self.points_tab_model.setColumnCount(10)  # 初始化列数

        # 隐藏滑动杆
        self.ui_points_tab.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # 初始化垂直滚动条
        self.ui_points_tab_v_bar.setMaximum(0)
        self.ui_points_tab_v_bar.valueChanged.connect(self.slot_point_tab_v_bar_value_change)

        # 清空列首和行首内容
        self.points_tab_model.setHorizontalHeaderLabels(["" for i in range(self.points_tab_model.columnCount())])
        self.points_tab_model.setVerticalHeaderLabels(["" for i in range(self.points_tab_model.rowCount())])

    def init_chart(self):
        self.ui_graph.setChart(self.ui_chart)
        self.ui_chart.addSeries(QLineSeries())
        self.ui_chart.createDefaultAxes()  # 创建默认坐标轴，基于已经添加到chart中的series
        self.ui_chart.legend().setVisible(True)  # 显示图例
        self.ui_chart.legend().setAlignment(Qt.AlignRight)  # 图例显示在波形图右侧
        self.ui_graph.setRenderHint(QPainter.Antialiasing)  # 反锯齿绘制

        # 设置初始比例，因为QChart不能在.ui中设置初始比例
        self.splitter_right.setStretchFactor(0, 8)
        self.splitter_right.setStretchFactor(1, 2)

    def init_model_tdms(self):
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

    @Slot()
    def slot_file_dialog_btn_click(self):
        self.file_path = QFileDialog.getOpenFileName(self, "选择TDMS文件", "", "*.tdms")[0]
        self.ui_file_path.setPlainText(self.file_path)
        if self.file_path is not None:
            self.signal_read_file_content.emit(self.file_path)

    @Slot(list)
    def slot_update_file_content(self, file_content):
        """file_content
            [
                {
                    "group_name": str,
                    "channel_name_list": [str]
                }
            ]
        """
        # 文件层级
        file_level_item = QTreeWidgetItem()
        file_level_item.setText(0, os.path.split(self.file_path)[1])
        self.ui_file_content.addTopLevelItem(file_level_item)

        # 组层级
        for group in file_content:
            group_level_item = QTreeWidgetItem()
            group_level_item.setText(0, group["group_name"])
            file_level_item.addChild(group_level_item)

            # 通道层级
            for channel_name in group["channel_name_list"]:
                channel_level_item = QTreeWidgetItem()
                channel_level_item.setText(0, channel_name)
                group_level_item.addChild(channel_level_item)

        self.ui_file_content.expandAll()

    @Slot()
    def slot_read_file(self):
        if self.ui_file_content.currentItem().parent() is None:
            # 文件层
            # 读取文件属性
            self.signal_read_file_properties.emit(self.file_path)
            # 读取文件数据
            self.signal_read_file_points.emit(self.file_path,
                                              self.ui_all_samples.isChecked(),
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
                                                 self.ui_all_samples.isChecked(),
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
                                               self.ui_all_samples.isChecked(),
                                               self.ui_start_index.value(),
                                               self.ui_samples.value())

    @Slot(list, list)
    def slot_update_properties(self, name_list, value_list):
        self.ui_prop_tab.clear()
        self.ui_prop_tab.setRowCount(len(name_list))
        if len(name_list) != 0 and len(value_list) != 0:
            i = 0
            for name, value in zip(name_list, value_list):
                item_key = QTableWidgetItem(name)
                self.ui_prop_tab.setItem(i, 0, item_key)

                item_value = QTableWidgetItem(str(value))
                self.ui_prop_tab.setItem(i, 1, item_value)
                i = i + 1

    @Slot(list)
    def slot_update_points(self, points):
        """ points
            [{
                "group_name": str,
                "channel_name": str,
                "unit": str,
                "t0": datetime/None,
                "dt": float,
                "y": [float]
            }]
        """
        self.update_points_tab(points)
        self.update_chart(points)

    @Slot()
    def slot_point_tab_v_bar_value_change(self):
        # 当前控件大小能显示多少行
        row_count = int(self.ui_points_tab.height() / self.ui_points_tab.rowHeight(1))
        # 滚动条当前值
        scroll_bar_value = self.ui_points_tab_v_bar.value()

        # 清空数据表
        self.points_tab_model.clear()

        for channel_data in self.current_points:
            points_show_column = []  # 数据表显示一列数据
            for point in channel_data[scroll_bar_value: scroll_bar_value + row_count]:
                points_show_column.append(QStandardItem("{:f}".format(point)))
            self.points_tab_model.appendColumn(points_show_column)

        # 清空数据表后，列首也被清空，需重新设置列首内容
        self.points_tab_model.setHorizontalHeaderLabels(self.header_label_list)

        # 生成列首序号int列表
        v_headers = list(range(scroll_bar_value + 1, (scroll_bar_value + 1 + row_count)))
        # 将int列表转str列表，并赋值给控件列首
        self.points_tab_model.setVerticalHeaderLabels(list(map(str, v_headers)))

        self.ui_points_tab.resizeColumnsToContents()  # 根据内容自动调整列宽

    def update_points_tab(self, points):
        # 当前控件大小能显示多少行
        row_count = int(self.ui_points_tab.height() / self.ui_points_tab.rowHeight(1))
        print(row_count)
        self.points_tab_model.clear()  # 清空数据表
        self.current_points.clear()  # 清空当前记录数据
        self.header_label_list.clear()  # 清空保存的列首

        max_length = 0  # 用于记录数据表滚动条最大值

        for channel in points:
            points_show_column = []  # 数据表显示一列数据

            # 更新数据表滚动条最大值
            if len(channel["y"]) > max_length:
                max_length = len(channel["y"])

            # 保存当前列所有Y轴数据
            self.current_points.append(channel["y"])

            # 组合列首
            self.header_label_list.append(
                channel["group_name"] + "\n" + channel["channel_name"] + "\n" + channel["unit"])

            for point in channel["y"][0: row_count - 1]:
                points_show_column.append(QStandardItem("{:f}".format(point)))
            self.points_tab_model.appendColumn(points_show_column)

        self.points_tab_model.setHorizontalHeaderLabels(self.header_label_list)  # 设置列首内容
        self.ui_points_tab.resizeColumnsToContents()  # 根据内容自动调整列宽

        # 更新数据表滚动条
        self.ui_points_tab_v_bar.setValue(0)
        self.ui_points_tab_v_bar.setMaximum(max_length - row_count + 1)

    def update_chart(self, points):
        """ points
            [{
                "group_name": str,
                "channel_name": str,
                "unit": str,
                "t0": datetime/None,
                "dt": float,
                "y": [float]
            }]
        """
        self.ui_chart.removeAllSeries()  # 清空波形图

        # 只要有一个通道没有时间戳，就使用数字X轴
        is_x_value = False
        for channel in points:
            if channel["t0"] is None:
                is_x_value = True
                break
        # 创建X轴
        if is_x_value is True:  # 创建数字X轴
            axis_x = QValueAxis()
            axis_x.setTitleText("点")
        else:  # 创建时间X轴
            axis_x = QDateTimeAxis()
            axis_x.setTitleText("时间")
            axis_x.setFormat("h:m:s:zzz<br>yyyy-M-d")
        axis_x.setTickCount(10)
        axis_x.setGridLineVisible(True)
        self.ui_chart.setAxisX(axis_x)

        # 创建Y轴
        axis_y = QValueAxis()
        axis_y.setTitleText("值")
        axis_y.setTickCount(10)
        axis_y.setGridLineVisible(True)
        self.ui_chart.setAxisY(axis_y)

        min_x_list, max_x_list, min_y_list, max_y_list = [], [], [], []

        for channel in points:
            line = QLineSeries()
            line.setName(channel["group_name"] + "->" + channel["channel_name"])
            # 创建X轴数据
            if is_x_value is True:
                min_value = 1
                max_value = len(channel["y"]) + 1
                x_list = list(range(min_value, max_value, 1))
            else:
                min_time = channel["t0"].timestamp()
                max_time = min_time + channel["dt"] * len(channel["y"])
                x_list = numpy.linspace(min_time, max_time, len(channel["y"]))

            min_x_list.append(min(x_list))
            max_x_list.append(max(x_list))
            min_y_list.append(min(channel["y"]))
            max_y_list.append(max(channel["y"]))

            # 创建Y轴数据
            point_list = []
            for x, y in zip(x_list, channel["y"]):
                point_list.append(QPointF(x, y))

            line.replace(point_list)
            self.ui_chart.addSeries(line)

        # 设定XY轴范围
        if is_x_value:
            min_x = min(min_x_list)
            max_x = max(max_x_list)
        else:
            min_x = QDateTime.fromSecsSinceEpoch(math.floor(min(min_x_list)))
            max_x = QDateTime.fromSecsSinceEpoch(math.ceil(max(max_x_list)))

        axis_x.setRange(min_x, max_x)
        axis_y.setRange(min(min_y_list), max(max_y_list))
