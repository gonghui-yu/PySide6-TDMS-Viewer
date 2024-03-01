import numpy as np
from PySide6.QtCore import QThread, Slot, Signal, QObject
from nptdms import TdmsFile


class ModelTDMS(QThread):
    signal_update_file_content = Signal(dict)
    signal_update_properties = Signal(dict)
    signal_update_points = Signal(dict)

    def __init__(self):
        super().__init__()

    @Slot(str)
    def slot_read_file_content(self, tdms_file_path):
        with TdmsFile.open(tdms_file_path) as tdms_file:
            file_content_dict = {}
            for group in tdms_file.groups():
                channel_list = []
                for channel in group.channels():
                    channel_list.append(channel.name)
                file_content_dict[group.name] = channel_list
            self.signal_update_file_content.emit(file_content_dict)

            tdms_file.close()

    @Slot(str)
    def slot_read_file_properties(self, tdms_file_path):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            self.signal_update_properties.emit(tdms_file.properties)

            tdms_file.close()

    @Slot(str, str)
    def slot_read_group_properties(self, tdms_file_path, group_name):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            self.signal_update_properties.emit(tdms_file[group_name].properties)

            tdms_file.close()

    @Slot(str, str, str)
    def slot_read_channel_properties(self, tdms_file_path, group_name, channel_name):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            self.signal_update_properties.emit(tdms_file[group_name][channel_name].properties)

            tdms_file.close()

    @Slot(str, str)
    def slot_read_file_points(self, tdms_file_path, group_name, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = {}
            for group in tdms_file.groups():
                for channel in group.channels():
                    points[group.name + "->" + channel.name] = [channel.properties["wf_start_time"],
                                                                channel.properties["wf_increment"],
                                                                np.array(channel[start_index:start_index + samples])]
            # 发送文件数据
            self.signal_update_points.emit(points)

            tdms_file.close()

    @Slot(str, str)
    def slot_read_group_points(self, tdms_file_path, group_name, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = {}  # 用于保存组数据
            for channel in tdms_file[group_name].channels():
                points[group_name + "->" + channel.name] = [channel.properties["wf_start_time"],
                                                            channel.properties["wf_increment"],
                                                            np.array(channel[start_index:start_index + samples])]
            # 发送组数据
            self.signal_update_points.emit(points)

            tdms_file.close()

    @Slot(str, str, str, int, int)
    def slot_read_channel_points(self, tdms_file_path, group_name, channel_name, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = {}  # 用于保存组数据
            channel = tdms_file[group_name][channel_name]
            # 读取通道数据
            points[group_name + "->" + channel_name] = [channel.properties["wf_start_time"],
                                                        channel.properties["wf_increment"],
                                                        np.array(channel[start_index:start_index + samples])]
            # 发送通道数据
            self.signal_update_points.emit(points)

            tdms_file.close()
