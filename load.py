from pystyle import Colors, Colorate, Center, System, Anime

banner = '''                                 ▄▄                              
▀████▀  ▀████▀▀                  ██                              
  ██      ██                                                     
  ██      ██    ▄██▀██▄▀███▄███▀███  █▀▀▀███  ▄██▀██▄▀████████▄  
  ██████████   ██▀   ▀██ ██▀ ▀▀  ██  ▀  ███  ██▀   ▀██ ██    ██  
  ██      ██   ██     ██ ██      ██    ███   ██     ██ ██    ██  
  ██      ██   ██▄   ▄██ ██      ██   ███  ▄ ██▄   ▄██ ██    ██  
▄████▄  ▄████▄▄ ▀█████▀▄████▄  ▄████▄███████  ▀█████▀▄████  ████▄
                                                                '''

def load():
    System.Size(140, 40)
    System.Title("Horizon")
    System.Clear()
    Anime.Fade(Center.XCenter(banner), Colors.yellow_to_red, Colorate.Vertical, time=3, interval=0.025)
    print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter(banner), 1))
    print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter("by MecPerspicace | v1.0"), 1))
    print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter("For $EGLD donation : erd19jcvvj7v7re6pnmypjds2yvlzrwdvp0l8lxr5qn2mdlns7jt8xrqtccly5"), 1))
    print("\n")