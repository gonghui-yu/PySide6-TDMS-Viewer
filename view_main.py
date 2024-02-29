from PySide6.QtCharts import QChart
from PySide6.QtWidgets import QWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy
from ui.tdms_viewer import Ui_TDMSViewer


class ViewMain(QWidget, Ui_TDMSViewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TDMS查看器")

        # 初始化文件选择器
        self.file_path = None
        self.ui_file_dialog_btn.clicked.connect(self.file_dialog_btn_click)

        # 初始化文件内容树
        self.ui_file_content.setHeaderLabel("TDMS文件内容")  # 设置列首
        self.ui_file_content.setStyleSheet("QHeaderView::section{background:rgb(220,220,220);}")  # 设置列首背景
        self.ui_file_content.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # 设置选中整行
        self.ui_file_content.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)  # 设置一次只能选中一行

        # self.ui_file_content.setStyleSheet("QTreeView{show-decoration-selected:1;background:rgb(61,66,77);}"
        #                                    "QTreeView::item{border:2px;color:rgb(255,255,255);}"
        #                                    "QTreeView::item:selected,QTreeView::branch:selected{background:rgb(28,77,"
        #                                    "120);}"
        #                                    "QTreeView::item:hover,QTreeView::branch:hover{background:rgb(64,91,134);}")

        first_level_1 = QTreeWidgetItem()
        first_level_1.setText(0, "第一级 1")
        first_level_2 = QTreeWidgetItem()
        first_level_2.setText(0, "第一级 2")

        self.ui_file_content.addTopLevelItems([first_level_1, first_level_2])
        self.ui_file_content.expandAll()

        second_level_1 = QTreeWidgetItem()
        second_level_1.setText(0, "第二级 1")
        second_level_2 = QTreeWidgetItem()
        second_level_2.setText(0, "第二级 2")

        first_level_1.addChildren([second_level_1, second_level_2])

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
        self.ui_chart.setTitle("波形图")
        self.ui_graph.setChart(self.ui_chart)

        # self.ui_chart.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Expanding)
        # self.ui_chart.sizePolicy().setVerticalStretch(6)

    def file_dialog_btn_click(self):
        self.file_path = QFileDialog.getOpenFileName(self, "选择TDMS文件", "", "*.tdms")[0]
        self.ui_file_path.setPlainText(self.file_path)

        # 判断文件路径是否合法

        # 读取文件
