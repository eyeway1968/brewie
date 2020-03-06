# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
#from PyQt5 import uic
from PyQt5.uic import loadUi

# This is our window from QtCreator
# create class for our Raspberry Pi GUI
class Ui(QMainWindow):
 # access variables inside of the UI's file
 
 ### functions for the buttons to call
 
 def PressedBtn(self):
  print("button pressed")


 def __init__(self):
  super(self.__class__, self).__init__() # Call the inherited classes __init__ method
  loadUi('brewie.ui', self) # Load the .ui file
  
  self.btn1.clicked.connect(lambda:openOtherForm(self))
  self.dial.valueChanged.connect(lambda: setCurrentIndex(self))
  
  def setCurrentIndex(self):
    currentIndex = self.dial.value()
    self.label.setText(str(currentIndex))
  def openOtherForm(self):
        self.hide()
        otherview = SecondWindow(self)
        otherview.show()  

  #self.show() # Show the GUI

class SecondWindow(QDialog):
  def __init__(self, parent = None):
    super(SecondWindow, self).__init__(parent)
    loadUi('second.ui', self)
    self.button2.clicked.connect(self.goBackToOtherForm)
  def goBackToOtherForm(self):
        self.parent().show()
        self.close()

def main():
 app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
 window = Ui() # Create an instance of our class
 window.show()
 sys.exit(app.exec_()) # Start the application 
 ### Hooks to for buttons


if __name__ == '__main__':         
    main()
 
