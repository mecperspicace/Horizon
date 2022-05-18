import load
from pystyle import Colors, Write
import logger
import hashlib
import os

def get_value(message):
    return Write.Input(message + " -> ", Colors.yellow_to_red, interval=0.005)

def get_action(file):
    return "decrypting" if str(file).endswith('.encrypt') else "crypting"

if __name__ == '__main__':
    load.load()
    file = get_value("Enter the file you want to crypt/decrypt")
    key = hashlib.sha256(get_value("Enter the key").encode('utf-8')).digest()
    logger.info("Start " + get_action(file) + " the file : " + file + "\n")
    logger.info("with the key : " + str(key) + "\n")
    with open(file, 'rb') as src_file:
        if file.endswith('.encrypt'):
            target_file = file.replace('.encrypt', '')
        else:
            target_file = file + '.encrypt'
        with open(target_file, 'wb') as exit_file:
            i = 0
            while src_file.peek():
                c = ord(src_file.read(1))
                j = i % len(key)
                b = bytes([c^key[j]])
                exit_file.write(b)
                i = i + 1
                print("i : " + str(i) + " / " + str(os.stat(file).st_size))
    os.remove(file)
    logger.success("Successfully " + get_action(file) + " into : " + target_file)
    input('\n')
