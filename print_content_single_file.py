import pathlib
import re

pattern = re.compile(r'(?i)SELECT\s*\*')

file_to_open = pathlib.Path('folder_to_scan', 'Bonds_select.txt')

with open(file_to_open, 'r') as file:
    content = file.read()

matches = pattern.finditer(content)

def main():
    for match in matches:
        print(match)



if __name__ == '__main__':
    main()