import os


class RenameFunction:
    """Класс для работы с переименовыванием файлов"""

    def __init__(self):
        self.list_of_files = ""
        self.path_files = ""

    def read_files_from_folder(self):
        self.list_of_files = os.listdir(self.path_files)
        os.chdir(self.path_files)

    def replace_char(self, replace_src, replace_dist):
        """Производит замену с replace_src на replace_dist каждого файла списка list_of_files"""
        replace_src = replace_src.strip()
        replace_dist = replace_dist.strip()
        self.read_files_from_folder()
        for name in self.list_of_files:
            os.rename(name, name.replace(replace_src, replace_dist))

    def delete_char(self, num_of_chars, begin):
        """Удаляет num_of_chars символов сначала строки, если флаг begin=True
         и с конца строки, если begin=False"""
        self.read_files_from_folder()
        if begin:
            for name in self.list_of_files:
                os.rename(name, name[int(num_of_chars):])
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index - int(num_of_chars)] + name[index:])

    def add_char(self, chars, begin):
        """Добавялет chars символов в начало строки, если begin=True, если нет, то в конец"""
        chars = chars.strip()
        self.read_files_from_folder()
        if begin:
            for name in self.list_of_files:
                os.rename(name, "" + chars + name)
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index] + str(chars) + name[index:])
