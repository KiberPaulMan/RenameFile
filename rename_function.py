import os


class RenameFunction:
    """Класс для работы с переименовыванием файлов"""
    def __init__(self, path_files):
        self.path_files = path_files
        self.list_of_files = self.reading_name_files_from_folder()
        # Переход в директорию path_files для работы с файлами
        os.chdir(self.path_files)

    def reading_name_files_from_folder(self):
        """Возвращает список файлов из указанной директории path_files"""
        return os.listdir(self.path_files)

    def replace_char(self, replace_src, replace_dist):
        for name in self.list_of_files:
            os.rename(name, name.replace(replace_src, replace_dist))

    # name.replace(replace_src, replace_dist)