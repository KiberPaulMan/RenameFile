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
        """Производит замену с replace_src на replace_dist каждого файла списка list_of_files"""
        for name in self.list_of_files:
            os.rename(name, name.replace(replace_src, replace_dist))

    def delete_char(self, num_of_chars, begin=True):
        """Удаляет num_of_chars символов сначала строки, если флаг begin=True
         и с конца строки, если begin=False"""
        if begin:
            for name in self.list_of_files:
                os.rename(name, name[num_of_chars:])
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index - num_of_chars] + name[index:])

    def add_char(self, chars, begin=True):
        """Добавялет chars символов в начало строки, если begin=True, если нет, то в конец"""
        if begin:
            for name in self.list_of_files:
                os.rename(name, name.rjust(len(name)+len(str(chars)), str(chars)))
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index] + str(chars) + name[index:])
