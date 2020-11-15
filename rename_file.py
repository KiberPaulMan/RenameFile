import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
from rename_function import RenameFunction

# Create app
app = QtWidgets.QApplication(sys.argv)

# Init app
MainWindow = QtWidgets.QMainWindow()
MainWindow.setFixedSize(580, 400) # ?????
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def get_folder_path():
    path_folder = "C:\\Users\%username%\desktop"
    dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', path_folder, QtWidgets.QFileDialog.ShowDirsOnly)
    ui.textEdit_2.setText(dir_)
    rf = RenameFunction(dir_)


ui.toolButton.clicked.connect(get_folder_path)



# Mail loop app
sys.exit(app.exec_())
