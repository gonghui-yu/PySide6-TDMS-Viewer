# PySide6-TDMS-Viewer
## 指令
```commandline
cd .\ui\ 
pyside6-uic .\tdms_viewer.ui -o .\tdms_viewer.py
pyside6-ucc .\resource.qrc -o .\resource_rc.py

pip freeze > requirements.txt
pip install -r requirements.txt
```