# PySide6-TDMS-Viewer
## 指令
```commandline
pyside6-uic .\ui\tdms_viewer.ui -o .\ui\tdms_viewer.py
pyside6-ucc .\resource.qrc -o .\resource_rc.py

pip freeze > requirements.txt
pip install -r requirements.txt
```