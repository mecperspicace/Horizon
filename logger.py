from pystyle import Colors, Write
import logging

def init():
    logging.basicConfig(filename=".log",
                        format='%(asctime)s %(message)s',
                        filemode='w',
                        datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

def success(message):
    Write.Print("[ Success ] " + message, interval=0.005, color=Colors.green)
    logger.info(message)

def error(message):
    Write.Print("[ Error ] " + message, interval=0.005, color=Colors.red)
    logger.error(message)

def info(message):
    Write.Print("[ Info ] " + message, interval=0.005, color=Colors.blue)
    logger.info(message)