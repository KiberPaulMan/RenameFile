from tkinter import Tk, filedialog, Text, Button, Label, Radiobutton, IntVar, Frame, Entry
from rename_function import RenameFunction

# Создаем объект класса RenameFunction
rf = RenameFunction()

# Цвета виджетов программы
bg_root_color = '#77d1c1'
bg_frame_color = bg_root_color
bg_dir_field_color = '#ebfaf6'
bg_entry_field_color = '#ebfaf6'
bg_submenu_label_color = bg_root_color


def read_files_from_directory(event):
    dir_field.delete(1.0, "end")
    rf.path_files = filedialog.askdirectory()
    dir_field.insert(1.0, rf.path_files)
    rf.read_files_from_folder()


def frame_destroy():
    for widget in frame.winfo_children():
        widget.destroy()


def press_button_replace():
    frame_destroy()
    frame.place(relx=0.32, rely=0.5, width=220, height=170)
    submenu_replace_label1 = Label(frame, text="Заменить с:", height=1, bg=bg_submenu_label_color)
    entry_replace1 = Entry(frame)
    entry_replace1.config({"background": bg_entry_field_color})
    submenu_replace_label2 = Label(frame, text="Заменить на:", width=15, height=1, bg=bg_submenu_label_color)
    entry_replace2 = Entry(frame)
    entry_replace2.config({"background": bg_entry_field_color})
    submenu_replace_label1.pack()
    entry_replace1.pack()
    submenu_replace_label2.pack()
    entry_replace2.pack()
    btn = Button(frame, text='Заменить')
    btn['command'] = lambda: rf.replace_char(entry_replace1.get(),
                                             entry_replace2.get())
    btn.pack(side='bottom')


def press_button_delete():
    frame_destroy()
    frame.place(relx=0.32, rely=0.5, width=220, height=170)
    submenu_delete_label = Label(frame, text="Введите количество символов\n для удаления из строки:", height=2, bg=bg_submenu_label_color)
    entry_delete = Entry(frame)
    entry_delete.config({"background": bg_entry_field_color})
    submenu_delete_label.pack()
    entry_delete.pack()
    btn = Button(frame, text='Удалить')
    if r_but.get() == 1:
        btn['command'] = lambda: rf.delete_char(entry_delete.get(), True)
    if r_but.get() == 2:
        btn['command'] = lambda: rf.delete_char(entry_delete.get(), False)
    btn.pack(side="bottom")


def press_button_add():
    frame_destroy()
    frame.place(relx=0.32, rely=0.5, width=220, height=170)
    submenu_add_label = Label(frame, text="Введите символы для\n добавления в строку:", height=2, bg=bg_submenu_label_color)
    entry_add = Entry(frame)
    entry_add.config({"background": bg_entry_field_color})
    submenu_add_label.pack()
    entry_add.pack()
    btn = Button(frame, text='Добавить')
    if r_but.get() == 3:
        btn['command'] = lambda: rf.add_char(entry_add.get(), True)
    if r_but.get() == 4:
        btn['command'] = lambda: rf.add_char(entry_add.get(), False)
    btn.pack(side="bottom")


# Основное окно
root = Tk()
root['bg'] = bg_root_color
root.title("Rename Files")
root.geometry("600x400")
root.resizable(width=False, height=False)


# Label для директории
dir_label = Label(root, text="Открыть папку:", width=15, height=1, bg=bg_root_color)
dir_label.place(x=250, y=50)

# Поле для ввода и вывода пути к директории
dir_field = Text(root, width=35, height=1, bg=bg_dir_field_color)
dir_field.place(x=160, y=70)


# Кнопка для выбора директории с файлами
btn_choice_dir = Button(root, text='...', height=1)
btn_choice_dir.place(x=444, y=70)
btn_choice_dir.bind("<Button-1>", read_files_from_directory)


r_but = IntVar()
r_but.set(5)
r_but_replace = Radiobutton(root, text='Заменить', bg=bg_root_color, value=0, variable=r_but)
r_but_replace['command'] = press_button_replace
r_but_replace.place(x=90, y=120)


r_but_del_begin_str = Radiobutton(root, text='Удалить с начала строки', bg=bg_root_color, value=1, variable=r_but)
r_but_del_begin_str['command'] = press_button_delete
r_but_del_begin_str.place(x=190, y=105)


r_but_del_end_str = Radiobutton(root, text='Удалить с конца строки', bg=bg_root_color, value=2, variable=r_but)
r_but_del_end_str['command'] = press_button_delete
r_but_del_end_str.place(x=190, y=135)


r_but_add_begin_str = Radiobutton(root, text='Добавить с начала строки', bg=bg_root_color, value=3, variable=r_but)
r_but_add_begin_str['command'] = press_button_add
r_but_add_begin_str.place(x=380, y=105)

r_but_add_end_str = Radiobutton(root, text='Добавить в конец строки', bg=bg_root_color, value=4, variable=r_but)
r_but_add_end_str['command'] = press_button_add
r_but_add_end_str.place(x=380, y=135)

frame = Frame(root)
frame['bg'] = bg_frame_color


# Главный цикл программы
root.mainloop()
