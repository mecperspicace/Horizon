from pystyle import Colors, Write

def success(message):
    Write.Print("[ Success ] " + message, interval=0.005, color=Colors.green)

def error(message):
    Write.Print("[ Error ] " + message, interval=0.005, color=Colors.red)

def info(message):
    Write.Print("[ Info ] " + message, interval=0.005, color=Colors.blue)