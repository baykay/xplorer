import os
from termcolor import colored

os.system('clear')
path = input(colored('Enter path: ', 'green'))


# show all files in folder
def show():
    files = os.listdir(path)
    for ind, file in enumerate(files):
        print(ind, file)


# show help menu
def option():
    print('\nshow             ==>     to show items in folder')
    # print('help             ==>     to show this options')
    print('cls              ==>     to clear the terminal window')
    print('format           ==>     to change the format of files')
    print('rename           ==>     to rename all files in folder')
    print('quit             ==>     to quit the script')
    print('dir              ==>     to show the current working directory')
    print('num              ==>     to show the number of items in the folder')


# to rename all files in directory
def rename():
    new_name = input('Enter new name: ')
    for files in os.listdir(os.chdir(path)):
        os.renames(files, new_name)
    for new_name in os.listdir(os.getcwd()):
        print(new_name)


def newpath():
    newDir = input("Enter new path: ")
    try:
        if os.path.exists(newDir):
            os.chdir(newDir)  ## TODO
            path = newDir
    except:
        print('Invalid path provided...')


# to change files format
def reformat_files():
    ext = input('Enter format to change to: ')
    for files in os.listdir(os.chdir(path)):
        os.move(files, files + ext)
        done = os.listdir(os.getcwd())
        for fil in done:
            print(fil)


# quit command to quit the script
def quit_scr():
    print('Goodbye, catch you next time.')
    # pyautogui.hotkey('ctrl', 'c')
    os.system('clear')
    exit(0)


# cls command to clear the text off the terminal screen
def cls():
    os.system('clear')


# folder command to show the current working directory
def folder():
    print(colored('You are currently in: ' + path, 'green'))


# to show the total number of files in the folder
def num_files():
    files = os.listdir(path)
    count = len(files)
    if count == 1:
        print(colored('There is ' + str(count) + ' item in this folder', 'yellow'))
    else:
        print(colored('There are ' + str(count) + ' items in this folder.', 'yellow'))




# the commander
try:
    def cmd():
        option()
        command = input(colored('command > ', 'green'))
        # if command == 'help':
        #     os.system('clear')
        #     option()
        if command == 'change':
            os.system('clear')
            newpath()
        if command == 'quit':
            while command:
                quit_scr()
        elif command == 'show':
            os.system('clear')
            show()
        elif command == 'format':
            os.system('clear')
            reformat_files()
        elif command == 'cls':
            cls()
        elif command == 'rename':
            os.system('clear')
            rename()
        elif command == 'dir':
            os.system('clear')
            folder()
        elif command == 'num':
            os.system('clear')
            num_files()
        else:
            os.system('clear')
            print('Invalid command, type help for more info.')
except:
    newpath()


def runner():
    while path:
        if os.path.exists(path):
            cmd()
        else:
            print('Invalid path')
            exit(1)


runner()