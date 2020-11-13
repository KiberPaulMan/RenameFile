import sys
from PyQt5 import QtWidgets
from gui_function import GuiFunction
from rename_function import RenameFunction


rf = RenameFunction()
app = QtWidgets.QApplication([])
application = GuiFunction("C:\\users\%username%\Desktop")
application.ui.toolButton.clicked.connect(application.print_folder)

application.show()
print(rf.list_of_files)
sys.exit(app.exec())
