# always seem to need this
import sys
 
# This gets the Qt stuff
#import PyQt5
from PyQt5 import QtWidgets, uic 

 
# This is our window from QtCreator

 
# create class for our Raspberry Pi GUI
class Ui(QtWidgets.QMainWindow):
 # access variables inside of the UI's file
 
 ### functions for the buttons to call
 
 
 def __init__(self):
  super(Ui, self).__init__() # Call the inherited classes __init__ method
  uic.loadUi('brewie.ui', self) # Load the .ui file
  self.show() # Show the GUI
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application 
 ### Hooks to for buttons
  
# def main():
#  # a new app instance
#  app = QtWidgets.QApplication(sys.argv)
#  form = Ui()
#  form.show()
#  # without this, the script exits immediately.
#  sys.exit(app.exec_())
 
# # python bit to figure how who started This
# if __name__ == "__main__":
#  main()
 ### functions for the buttons to call