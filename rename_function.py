import os


class RenameFunction:
    """Класс для работы с переименовыванием файлов"""

    def __init__(self):
        self.list_of_files = ""
        self.path_files = ""

    def read_files_from_folder(self):
        self.list_of_files = os.listdir(self.path_files)
        os.chdir(self.path_files)

    def replace_char(self, input_str):
        """Производит замену с replace_src на replace_dist каждого файла списка list_of_files"""
        replace_src = (input_str.split(',')[0]).strip()
        replace_dist = (input_str.split(',')[1]).strip()
        # os.chdir(self.path_files)
        self.read_files_from_folder()
        for name in self.list_of_files:
            os.rename(name, name.replace(replace_src, replace_dist))

    def delete_char(self, input_str):
        """Удаляет num_of_chars символов сначала строки, если флаг begin=True
         и с конца строки, если begin=False"""
        num_of_chars = int((input_str.split(',')[0]).strip())
        begin = int((input_str.split(',')[1]).strip())
        # os.chdir(self.path_files)
        self.read_files_from_folder()
        if begin == 1:
            for name in self.list_of_files:
                os.rename(name, name[num_of_chars:])
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index - num_of_chars] + name[index:])

    def add_char(self, input_str):
        """Добавялет chars символов в начало строки, если begin=True, если нет, то в конец"""
        chars = (input_str.split(',')[0]).strip()
        begin = int((input_str.split(',')[1]).strip())
        # os.chdir(self.path_files)
        self.read_files_from_folder()
        # print(os.getcwd())
        # print("chars = {0}\t begin = {1}".format(chars, begin))
        # print(self.list_of_files)
        if begin == 1:
            for name in self.list_of_files:
                os.rename(name, "" + chars + name)
        else:
            for name in self.list_of_files:
                index = name.rfind('.')
                os.rename(name, name[:index] + str(chars) + name[index:])
