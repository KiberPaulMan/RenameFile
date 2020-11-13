import sys
from PyQt5 import QtWidgets
from gui import Ui_MainWindow  # импорт нашего сгенерированного файла
from rename_function import RenameFunction


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())


files_path = "C:\\Users\putincev\Desktop\photos"
rf = RenameFunction(files_path)
files = rf.reading_name_files_from_folder()
print(files)


# rf.add_char(1, True)
# print(rf.reading_name_files_from_folder())

