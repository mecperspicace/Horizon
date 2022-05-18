import load
from pystyle import Colors, Write
import logger

apikey = ""

def getValue(message):
    return Write.Input(message + " -> ", Colors.yellow_to_red, interval=0.005)

if __name__ == '__main__':
    logger.init()
    load.load()
    logger.success("Successfully log into " + getValue("Enter your api key"))