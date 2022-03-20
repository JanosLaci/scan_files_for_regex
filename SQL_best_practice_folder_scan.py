import os
import pathlib

path_to_folder = pathlib.Path('.', 'folder_to_scan')


def scan_folder_select_star(folder_to_scan=path_to_folder):
    with os.scandir(folder_to_scan) as dir_iterator:
        for file in dir_iterator:
            print(file.name)


def main():
    scan_folder_select_star()



if __name__ == '__main__':
    main()
    list_dir = os.listdir(path_to_folder)
    print(list_dir)