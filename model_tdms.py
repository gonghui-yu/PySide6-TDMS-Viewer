import datetime
import time

import numpy as np
from PySide6.QtCore import QThread, Slot, Signal, QDateTime, QTime
from nptdms import TdmsFile, timestamp


class ModelTDMS(QThread):
    signal_update_file_content = Signal(list)
    signal_update_properties = Signal(list, list)
    signal_update_points = Signal(list)

    def __init__(self):
        super().__init__()

        # 计算本地时间和UTC时间差，因nptdms获取时间为UTC时间，需转换
        now_stamp = time.time()
        local_time_now = datetime.datetime.fromtimestamp(now_stamp)
        utc_time_now = datetime.datetime.utcfromtimestamp(now_stamp)
        self.time_offset = local_time_now - utc_time_now

    @Slot(str)
    def slot_read_file_content(self, tdms_file_path):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            # 创建字典，保存文件内容（通道、属性列表）
            file_content = []
            for group in tdms_file.groups():
                channel_name_list = []
                for channel in group.channels():
                    channel_name_list.append(channel.name)

                file_content.append({
                    "group_name": group.name,
                    "channel_name_list": channel_name_list
                })

            # 发送文件内容到界面
            self.signal_update_file_content.emit(file_content)
            # 关闭文件
            tdms_file.close()
            '''
            [
                {
                    "group_name": str,
                    "channel_name_list": [str]
                }
            ]
            '''


    @Slot(str)
    def slot_read_file_properties(self, tdms_file_path):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            name_list = ["Name"]
            value_list = [tdms_file.properties["name"]]

            for item in tdms_file.properties.items():
                if item[0] != "name":
                    name_list.append(item[0])
                    if type(item[1]) is timestamp.TdmsTimestamp:
                        # 将nptdms的UTC时间类型转换为datetime的本地时间类型
                        value_list.append(item[1].as_datetime() + self.time_offset)
                    elif type(item[1]) is float:
                        value_list.append("{:f}".format(float(item[1])))
                    else:
                        value_list.append(item[1])

            self.signal_update_properties.emit(name_list, value_list)

    @Slot(str, str)
    def slot_read_group_properties(self, tdms_file_path, group_name):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            name_list = ["Name"]
            value_list = [group_name]
            for item in tdms_file[group_name].properties.items():
                name_list.append(item[0])
                if type(item[1]) is timestamp.TdmsTimestamp:
                    # 将nptdms的UTC时间类型转换为datetime的本地时间类型
                    value_list.append(item[1].as_datetime() + self.time_offset)
                elif type(item[1]) is float:
                    value_list.append("{:f}".format(float(item[1])))
                else:
                    value_list.append(item[1])

            self.signal_update_properties.emit(name_list, value_list)

    @Slot(str, str, str)
    def slot_read_channel_properties(self, tdms_file_path, group_name, channel_name):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path, True) as tdms_file:
            channel = tdms_file[group_name][channel_name]
            name_list = ["Name", "Data Type", "Length"]
            value_list = [channel_name, channel.dtype, len(channel[:])]

            for item in channel.properties.items():
                name_list.append(item[0])
                if type(item[1]) is timestamp.TdmsTimestamp:
                    # 将nptdms的UTC时间类型转换为datetime的本地时间类型
                    value_list.append(item[1].as_datetime() + self.time_offset)
                elif type(item[1]) is float:
                    # 浮点数不以科学计数法显示
                    value_list.append("{:f}".format(float(item[1])))
                else:
                    value_list.append(item[1])

            self.signal_update_properties.emit(name_list, value_list)

    @Slot(str, bool, int, int)
    def slot_read_file_points(self, tdms_file_path, all_samples, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = []
            for group in tdms_file.groups():
                for channel in group.channels():
                    if all_samples is True:
                        y = np.array(channel[:])
                    else:
                        y = np.array(channel[start_index:start_index + samples])

                    if "wf_start_time" in channel.properties.keys():
                        t0 = channel.properties["wf_start_time"].astype(datetime.datetime) + self.time_offset
                        dt = channel.properties["wf_increment"]
                        unit = channel.properties["NI_UnitDescription"]

                    channel_dict = {
                        "group_name": group.name,
                        "channel_name": channel.name,
                        "unit": unit,
                        "t0": t0,
                        "dt": dt,
                        "y": y
                    }
                    points.append(channel_dict)

            # 发送文件数据
            self.signal_update_points.emit(points)

    @Slot(str, str, bool, int, int)
    def slot_read_group_points(self, tdms_file_path, group_name, all_samples, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = []  # 用于保存组数据
            for channel in tdms_file[group_name].channels():
                if all_samples is True:
                    y = np.array(channel[:])
                else:
                    y = np.array(channel[start_index:start_index + samples])

                if "wf_start_time" in channel.properties.keys():
                    t0 = channel.properties["wf_start_time"].astype(datetime.datetime) + self.time_offset
                    dt = channel.properties["wf_increment"]
                    unit = channel.properties["NI_UnitDescription"]

                channel_dict = {
                    "group_name": group_name,
                    "channel_name": channel.name,
                    "unit": unit,
                    "t0": t0,
                    "dt": dt,
                    "y": y
                }
                points.append(channel_dict)
            # 发送组数据
            self.signal_update_points.emit(points)

    @Slot(str, str, str, bool, int, int)
    def slot_read_channel_points(self, tdms_file_path, group_name, channel_name, all_samples, start_index, samples):
        # 打开TDMS文件
        with TdmsFile.open(tdms_file_path) as tdms_file:
            points = []
            # y = []  # 用于保存通道数据
            channel = tdms_file[group_name][channel_name]
            # 读取通道数据
            if all_samples is True:
                y = np.array(channel[:])
            else:
                y = np.array(channel[start_index:start_index + samples])

            if "wf_start_time" in channel.properties.keys():
                t0 = channel.properties["wf_start_time"].astype(datetime.datetime) + self.time_offset
                dt = channel.properties["wf_increment"]
                unit = channel.properties["NI_UnitDescription"]

            channel_dict = {
                                "group_name": group_name,
                                "channel_name": channel_name,
                                "unit": unit,
                                "t0": t0,
                                "dt": dt,
                                "y": y
                            }
            points.append(channel_dict)

            # 发送通道数据
            self.signal_update_points.emit(points)
