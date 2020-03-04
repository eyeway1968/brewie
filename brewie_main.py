# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

 
# This is our window from QtCreator
# create class for our Raspberry Pi GUI
class Ui(QMainWindow):
 # access variables inside of the UI's file
 
 ### functions for the buttons to call
 
 def PressedBtn(self):
  print("button pressed")


 def __init__(self, parent=None):
  super(self.__class__, self).__init__(parent) # Call the inherited classes __init__ method
  uic.loadUi('brewie.ui', self) # Load the .ui file
  
  self.btn1.clicked.connect(lambda:setCurrentIndex(self))
  self.dial.valueChanged.connect(lambda: setCurrentIndex(self))

  def setCurrentIndex(self):
    currentIndex = self.dial.value()
    self.label.setText(str(currentIndex))
    

  #self.show() # Show the GUI


 

app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
window.show()
app.exec_() # Start the application 
 ### Hooks to for buttons



 
