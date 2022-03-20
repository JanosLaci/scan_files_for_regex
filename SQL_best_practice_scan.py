import pathlib

path_to_scan = pathlib.Path('folder_to_scan')

def scan_for_select_star(input_path=path_to_scan):
    for path in input_path.iterdir():
        print(path.name)




def main():
    scan_for_select_star()

if __name__ == '__main__':
    main()