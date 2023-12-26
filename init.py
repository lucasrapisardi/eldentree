from player import Player

def create_char():
    print("""
        In shadows concealed, a hero's tale untold,
        Forgotten echoes of bravery... I can't remember the hero's name...""")
    name = input("\n")
    print(f"""
        Oh, how could I forgot it?!\n In shadows concealed, a hero's tale untold,
        Forgotten echoes of bravery, lost in the fold.
        Silent whispers of valor, {name} history left in the cold.""")
    return name

if __name__ == '__main__':

    print("""
 __    __ _     _                                  __   _   _              __ _     _           _                 
/ / /\ \ \ |__ (_)___ _ __   ___ _ __ ___    ___  / _| | |_| |__   ___    /__\ | __| | ___ _ __| |_ _ __ ___  ___ 
\ \/  \/ / '_ \| / __| '_ \ / _ \ '__/ __|  / _ \| |_  | __| '_ \ / _ \  /_\ | |/ _` |/ _ \ '__| __| '__/ _ \/ _ \\
 \  /\  /| | | | \__ \ |_) |  __/ |  \__ \ | (_) |  _| | |_| | | |  __/ //__ | | (_| |  __/ |  | |_| | |  __/  __/
  \/  \/ |_| |_|_|___/ .__/ \___|_|  |___/  \___/|_|    \__|_| |_|\___| \__/ |_|\__,_|\___|_|   \__|_|  \___|\___|
                     |_|                                                                                                                                                                     
""")
    
    start = input('\t\t\t\t\tPress enter to continue')
    player = Player(create_char())