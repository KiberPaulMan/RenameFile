from rename_function import RenameFunction


files_path = "C:\\Users\putincev\Desktop\photos"
rf = RenameFunction(files_path)
files = rf.reading_name_files_from_folder()
print(files)

rf.add_char(1, True)
print(rf.reading_name_files_from_folder())

