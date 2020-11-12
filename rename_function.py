import os


class RenameFunction:
    """Класс для работы с переименовыванием файлов"""
    def __init__(self, path_files):
        self.path_files = path_files

    def reading_name_files_from_folder(self):
        """Возвращает список файлов из указанной директории path_files"""
        return os.listdir(self.path_files)

    def 