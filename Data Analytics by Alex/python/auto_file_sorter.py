import os ,shutil

path = r"C:/Users/user/Documents/Programming/Data Analytics by Alex/python/sorter project/"

file_names = os.listdir(path)
folder_names = ["csv files", "image files", "video files"]

# Check if folders exist; if not, create them
folder_paths = {folder: os.path.join(path, folder) for folder in folder_names}

for folder, folder_path in folder_paths.items():
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Move files to their respective folders
for file in file_names:
    file_path = os.path.join(path, file)

    if file.endswith(".csv"):
        shutil.move(file_path, folder_paths["csv files"])
    elif file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        shutil.move(file_path, folder_paths["image files"])
    elif file.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        shutil.move(file_path, folder_paths["video files"])
