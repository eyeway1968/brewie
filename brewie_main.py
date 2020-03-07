# always seem to need this
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

# This is our window from QtCreator
# create class for our Raspberry Pi GUI
class Ui(QtWidgets.QMainWindow):
 # access variables inside of the UI's file
 
 ### functions for the buttons to call
 
 def PressedBtn(self):
  print("button pressed")


 def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs) # Call the inherited classes __init__ method
  uic.loadUi('brewie.ui', self) # Load the .ui file
  
  
  self.dial.valueChanged.connect(lambda: setCurrentIndex(self))
  
  def setCurrentIndex(self):
    currentIndex = self.dial.value()
    self.label.setText(str(currentIndex))
  

  #self.show() # Show the GUI


 

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
window.show()
app.exec_() # Start the application 
 ### Hooks to for buttons
