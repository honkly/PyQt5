# -*- coding: utf-8 -*-
"""
    【简介】
    信号和槽例子


"""


from PyQt5.QtWidgets import  QPushButton ,  QApplication, QWidget 
from  PyQt5.QtWidgets import QMessageBox  
import sys 


app =  QApplication([])
widget =  QWidget()

def showMsg():
     QMessageBox.information(widget, "信息提示框", "ok")
     
btn =  QPushButton( "点我", widget)
btn.clicked.connect(  showMsg)
widget.show()
sys.exit(app.exec_())