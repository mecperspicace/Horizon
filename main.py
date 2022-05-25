import load
from pystyle import Colors, Write
import hashlib
import os


def get_value(message):
    return Write.Input(message + " -> ", Colors.yellow_to_red, interval=0.005)


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

    key = hashlib.sha256(get_value("Enter the key").encode('utf-8'))

    Write.Print("Start " + get_action(file) + " the file : " + file + "\n", Colors.yellow_to_red, interval=0.005)
    Write.Print("With the key : " + key.hexdigest() + "\n", Colors.yellow_to_red, interval=0.005)

    with open(file, 'rb') as src_file:

        if file.endswith('.encrypt'):
            target_file = file.replace('.encrypt', '')
        else:
            target_file = file + '.encrypt'

        with open(target_file, 'wb') as exit_file:

            i = 0
            while src_file.peek():
                c = ord(src_file.read(1))
                j = i % len(key.digest())
                b = bytes([c ^ key.digest()[j]])
                exit_file.write(b)
                i = i + 1
                progress_bar(i, os.stat(file).st_size)

    os.remove(file)

    Write.Print("Successfully " + get_action(file) + " into : " + target_file + " " * 100, Colors.green_to_yellow,
                interval=0.005)

    input('')
