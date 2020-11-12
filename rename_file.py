import os


# 1. открыть папку с файлами и считать их в список
files_path = "C:\\Users\putincev\Desktop\photos"

spisok = os.listdir(files_path)

for x in spisok:
    print(x)


