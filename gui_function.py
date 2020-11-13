from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from rename_function import RenameFunction


class GuiFunction(QtWidgets.QMainWindow):
    def __init__(self, path_folder):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path_folder = path_folder

        # подключение клик-сигнал к слоту print_folder
        # self.ui.toolButton.clicked.connect(self.print_folder)

    def print_folder(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', self.path_folder, QtWidgets.QFileDialog.ShowDirsOnly)
        rf = RenameFunction()
        rf.reading_name_files_from_folder(dir_)
