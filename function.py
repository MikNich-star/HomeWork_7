import os
import os.path


def show_files() -> object:
    files_list = []
    for el in os.listdir(os.getcwd()):
        if not os.path.isdir(os.path.join('.', el)):
            files_list.append(el)
    return files_list


def dir_list() -> object:
    dir_list = []
    with os.scandir(os.getcwd()) as files:
        dirs = [file.name for file in files if file.is_dir()]
        dir_list.append(dirs)
    return dir_list
