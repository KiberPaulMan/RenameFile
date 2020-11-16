import os


class RenameFunction:
    """Класс для работы с переименовыванием файлов"""
    def __init__(self, path_files):
        self.list_of_files = os.listdir(path_files)

    def replace_char(self, input_str):
        """Производит замену с replace_src на replace_dist каждого файла списка list_of_files"""
        replace_src = (input_str.split(',')[0]).strip()
        replace_dist = (input_str.split(',')[1]).strip()
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
