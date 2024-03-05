# PySide6-TDMS-Viewer
## 指令
```commandline
pyside6-uic .\ui\tdms_viewer.ui -o .\ui\tdms_viewer.py
pyside6-ucc .\resource.qrc -o .\resource_rc.py

pip freeze > requirements.txt
pip install -r requirements.txt
```

## 遗留问题
1. 当Y值全为1时，波形图不显示曲线
2. 波形图游标实现
3. 波形图鼠标拖动放大缩小实现
4. 如何禁用在数据表上的鼠标滚轮