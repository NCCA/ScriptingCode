from PySide2 import QtCore,QtWidgets
from shiboken2 import wrapInstance 
import maya.OpenMayaUI as omui
# based on https://www.patreon.com/posts/pyside2-for-maya-21014669

def getMayaMainWindow() :
  mainWindow=omui.MQtUtil.mainWindow() # will be a pointer
  # so need to convert to QtWidget note on earlier versions
  # of Maya may need to use long() python3 is int
  return wrapInstance(int(mainWindow),QtWidgets.QWidget) 


class SimpleDialog(QtWidgets.QDialog) :
  def __init__(self,parent=getMayaMainWindow()) :
    super(SimpleDialog,self).__init__(parent)
    self.setWindowTitle("Simple Dialog")
    self.setMinimumWidth(200)
    

if __name__ == "__main__" :
  try :
    dialog.deleteLater()
  except :
    pass
  dialog=SimpleDialog()
  dialog.show()
