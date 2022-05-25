import load
from pystyle import Colors, Write
from hashlib import sha256
import os
import randomizer


def get_value(message):
    return Write.Input(message + " -> ", Colors.yellow_to_red, interval=0.005, hide_cursor=False)


def get_action(file_name):
    return "decrypting" if str(file_name).endswith('.encrypt') else "crypting"


def progress_bar(progress, total):
    percent = 100 * (progress / total)
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    if percent < 30:
        print(Colors.red + f"\r|{bar}| {percent:.2f}%", end="\r")
        return
    if percent < 60:
        print(Colors.yellow + f"\r|{bar}| {percent:.2f}%", end="\r")
        return
    print(Colors.green + f"\r|{bar}| {percent:.2f}%", end="\r")


if __name__ == '__main__':
    load.load()
    file = get_value("Enter the file you want to crypt/decrypt")

    if get_action(file) == "decrypting":
        key = get_value('Enter the key')
        keys = sha256(key.encode('utf-8')).digest()
        Write.Print("Start " + get_action(file) + " the file : " + file + "\n", Colors.yellow_to_red, interval=0.005)

        with open(file, 'rb') as src_file:

            target_file = file.replace('.encrypt', '')

            with open(target_file, 'wb') as exit_file:
                i = 0
                while src_file.peek():
                    c = ord(src_file.read(1))
                    j = i % len(keys)
                    b = bytes([c ^ keys[j]])
                    exit_file.write(b)
                    i = i + 1
                    progress_bar(i, os.stat(file).st_size)

        os.remove(file)

    else:

        key = randomizer.random_char(64)
        keys = sha256(key.encode('utf-8')).digest()

        Write.Print("Start " + get_action(file) + " the file : " + file + "\n", Colors.yellow_to_red, interval=0.005)
        Write.Print("With the key : " + key + "\n", Colors.yellow_to_red, interval=0.005)

        with open(file, 'rb') as src_file:

            target_file = file + '.encrypt'

            with open(target_file, 'wb') as exit_file:
                i = 0
                while src_file.peek():
                    c = ord(src_file.read(1))
                    j = i % len(keys)
                    b = bytes([c ^ keys[j]])
                    exit_file.write(b)
                    i = i + 1
                    progress_bar(i, os.stat(file).st_size)

        os.remove(file)

    Write.Print("Successfully " + get_action(file) + " into : " + target_file + " " * 100, Colors.green_to_yellow,
                interval=0.005)

    input('')
