from time import sleep
from configuration import env

SOURCE_PATH = env.source_path

def open_file(file):
    with open(f'{SOURCE_PATH}{file}', 'r') as file_open:
        lines = file_open.readlines()
        count = 0
    
    for line in lines:
        if line != '\n':
            count += 1
            print(count, line.strip())
        else:
            print(line.strip())
        sleep(1)

def open_title(file):
    sleep(1)
    with open(f'{SOURCE_PATH}{file}', 'r') as file_open:
        lines = file_open.read()
        print(lines)
    sleep(1)

open_title('prologo.txt')
open_file('intro.txt')
