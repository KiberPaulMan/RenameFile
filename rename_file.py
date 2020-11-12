from rename_function import RenameFunction


files_path = "C:\\Users\putin\OneDrive\Рабочий стол\\test"
rf = RenameFunction(files_path)
files = rf.reading_name_files_from_folder()
print(files)

rf.replace_char('1_', '')
print(rf.reading_name_files_from_folder())



