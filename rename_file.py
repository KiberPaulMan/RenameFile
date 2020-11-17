from tkinter import Tk, filedialog, Text, Button, Label, LabelFrame
from tkinter.messagebox import *
from rename_function import RenameFunction

# Создаем объект класса RenameFunction
rf = RenameFunction()


def read_files_from_directory(event):
    dir_field.delete(1.0, "end")
    rf.path_files = filedialog.askdirectory()
    dir_field.insert(1.0, rf.path_files)
    rf.read_files_from_folder()


def press_button_replace_char(event):
    chars = char_field.get(1.0, "end")
    rf.replace_char(chars)


def press_button_delete_char(event):
    chars = char_field.get(1.0, "end")
    rf.delete_char(chars)


def press_button_add_char(event):
    chars = char_field.get(1.0, "end")
    rf.add_char(chars)


# Основное окно
root = Tk()
root['bg'] = "#81cc96"
root.title("Rename Files")
root.geometry("600x400")
root.resizable(width=False, height=False)

# Label для директории
dir_label = Label(root, text="Открыть папку:", width=15, height=1, bg="#81cc96")  # , bg="#81cc96"
dir_label.place(x=250, y=50)

# Поле для ввода и вывода пути к директории
dir_field = Text(root, width=35, height=1, bg="#404040", fg='white')
dir_field.place(x=160, y=70)


# Label для ввода символов
char_label = Label(root, text="Введите символы:", width=15, height=1, bg="#81cc96")  # , bg="#81cc96"
char_label.place(x=250, y=140)

# Поле для ввода символов
char_field = Text(root, width=15, height=1, bg="#404040", fg='white')
char_field.place(x=240, y=160)


# Кнопка для выбора директории с файлами
btn_choice_dir = Button(root, text='...', height=1)
btn_choice_dir.place(x=444, y=70)
btn_choice_dir.bind("<Button-1>", read_files_from_directory)


# Кнопка для выполения метода replace_char
btn_replace = Button(root, text='Заменить', height=1)
btn_replace.place(x=100, y=250)
btn_replace.bind("<Button-1>", press_button_replace_char)


# Кнопка для выполения метода delete_char
btn_del = Button(root, text='Удалить', height=1)
btn_del.place(x=255, y=250)
btn_del.bind("<Button-1>", press_button_delete_char)


# Кнопка для выполения метода delete_char
btn_add = Button(root, text='Добавить', height=1)
btn_add.place(x=400, y=250)
btn_add.bind("<Button-1>", press_button_add_char)


# Главный цикл программы
root.mainloop()
