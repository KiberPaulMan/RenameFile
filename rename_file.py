from tkinter import Tk, filedialog, Text, Button, Label, Radiobutton, Toplevel, IntVar
from tkinter.messagebox import *
from rename_function import RenameFunction

# Создаем объект класса RenameFunction
rf = RenameFunction()
bg_root_color = "#81cc96"


def read_files_from_directory(event):
    dir_field.delete(1.0, "end")
    rf.path_files = filedialog.askdirectory()
    dir_field.insert(1.0, rf.path_files)
    rf.read_files_from_folder()


def press_button_replace():
    top_replace = Toplevel()
    top_replace.title("Заменить")
    top_replace.geometry("250x250")
    top_replace.resizable(width=False, height=False)
    top_replace.config(bg="lightblue")
    bg_top_color = "white"
    submenu_replace_label1 = Label(top_replace, text="Заменить с:", height=1, bg="lightblue")
    submenu_replace_text1 = Text(top_replace, height=1, bg=bg_top_color, fg='black', takefocus=True)
    submenu_replace_label2 = Label(top_replace, text="Заменить на:", width=15, height=1, bg="lightblue")
    submenu_replace_text2 = Text(top_replace, height=1, bg=bg_top_color, fg='black', takefocus=True)
    submenu_replace_label1.pack()
    submenu_replace_text1.pack()
    submenu_replace_label2.pack()
    submenu_replace_text2.pack()
    btn = Button(top_replace, text='Заменить')
    btn['command'] = lambda: rf.replace_char(submenu_replace_text1.get(1.0, "end"),
                                             submenu_replace_text2.get(1.0, "end"))
    btn.pack(side="bottom")


def press_button_delete():
    top_del = Toplevel()
    top_del.title("Заменить")
    top_del.geometry("250x250")
    top_del.resizable(width=False, height=False)
    top_del.config(bg="lightblue")
    bg_top_color = "white"
    submenu_delete_label1 = Label(top_del, text="Введите количество символов для удаления с начала строки:", height=1, bg="lightblue")
    submenu_delete_text1 = Text(top_del, height=1, bg=bg_top_color, fg='black')
    submenu_delete_label1.pack()
    submenu_delete_text1.pack()
    btn2 = Button(top_del, text='Удалить')
    if click.get():
        print('begin', click.get())

    # if r_but_del_begin_str.focus:
    #     print("begin")
    #     # btn2['command'] = lambda: rf.delete_char(submenu_delete_text1.get(1.0, "end"), True)
    # if r_but_del_end_str.focus:
    #     print("end")
    #     # btn2['command'] = lambda: rf.delete_char(submenu_delete_text1.get(1.0, "end"), False)
    btn2.pack(side="bottom")


# Основное окно
root = Tk()
root['bg'] = "#81cc96"
root.title("Rename Files")
root.geometry("600x400")
root.resizable(width=False, height=False)


# Label для директории
dir_label = Label(root, text="Открыть папку:", width=15, height=1, bg=bg_root_color)  # , bg="#81cc96"
dir_label.place(x=250, y=50)

# Поле для ввода и вывода пути к директории
dir_field = Text(root, width=35, height=1, bg="#404040", fg='white')
dir_field.place(x=160, y=70)


# Кнопка для выбора директории с файлами
btn_choice_dir = Button(root, text='...', height=1)
btn_choice_dir.place(x=444, y=70)
btn_choice_dir.bind("<Button-1>", read_files_from_directory)


# --------------------NEW CODE-------------------------------
r_but_replace = Radiobutton(root, text='Заменить', bg=bg_root_color, value=0)
r_but_replace['command'] = press_button_replace
# r_but_replace.config(state="disable")
r_but_replace.place(x=90, y=120)


click = IntVar()
click.set(0)

r_but_del_begin_str = Radiobutton(root, text='Удалить с начала строки', bg=bg_root_color, value=1, variable=click)
r_but_del_begin_str['command'] = press_button_delete

# r_but_del_begin_str['variable'] = click
# r_but_replace.config(state="disable")
r_but_del_begin_str.place(x=190, y=105)

r_but_del_end_str = Radiobutton(root, text='Удалить с конца строки', bg=bg_root_color, value=2, variable=click)
r_but_del_end_str['command'] = press_button_delete

# r_but_del_begin_str['variable'] = click2
# r_but_replace.config(state="disable")
r_but_del_end_str.place(x=190, y=135)

r_but_add_begin_str = Radiobutton(root, text='Добавить с начала строки', bg=bg_root_color, value=3)
# r_but_replace.config(state="disable")
r_but_add_begin_str.place(x=380, y=105)

r_but_add_end_str = Radiobutton(root, text='Добавить в конец строки', bg=bg_root_color, value=4)
# r_but_replace.config(state="disable")
r_but_add_end_str.place(x=380, y=135)


# Главный цикл программы
root.mainloop()
