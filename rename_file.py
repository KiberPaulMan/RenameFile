from tkinter import Tk, filedialog, Text, \
    Button, Radiobutton, Checkbutton
from rename_function import RenameFunction


def read_files_from_directory(event):
    text.delete(1.0, "end")
    name = filedialog.askdirectory()
    text.insert(1.0, name)

# https://younglinux.info/tkinter/bind.php
rf = RenameFunction("C:\\")

# Основное окно
root = Tk()
root['bg'] = "#81cc96"
root.title("Rename Files")
root.geometry("600x400")
root.resizable(width=False, height=False)

# Поле для ввода и вывода пути к директории
text = Text(root, width=35, height=1, bg="#404040", fg='white')
text.place(x=160, y=70)

# Поле для ввода символов
text2 = Text(root, width=15, height=1, bg="#404040", fg='white')
text2.place(x=240, y=160)

# Кнопка для
button = Button(root, text='...', height=1)
button.place(x=444, y=70)
# При клике на ЛКМ вызывает функцию read_files_from_directory
button.bind("<Button-1>", read_files_from_directory)

button2 = Button(root, text='Rename', height=1)
button2.place(x=500, y=360)
# При клике на ЛКМ вызывает функцию read_files_from_directory
# button2.bind("<Button-1>", choice_method)

r_button1 = Radiobutton(root, text='Replace chars', value=0)
r_button1.place(x=100, y=250)
# r_button1.bind("<Button-1>", ask_press_button_replace)

r_button2 = Radiobutton(root, text='Delete chars', value=1)
r_button2.place(x=255, y=250)

r_button3 = Radiobutton(root, text='Add chars', value=2)
r_button3.place(x=400, y=250)

сh_button1 = Checkbutton(root, text="Add begin line", variable=0)
сh_button2 = Checkbutton(root, text="Add end line", variable=1)

сh_button1.place(x=250, y=300)
сh_button2.place(x=250, y=330)

root.mainloop()
