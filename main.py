import oead
import json
from bcml import util
from randomize_map_or_pack import randomize_map,randomize_pack
import os

with open(r"resources\config_randomizer.json",'r') as config_file:
    RANDO_CONFIG = json.loads(config_file.read())

with open(r"resources\file_list.json",'r') as file_list:
    FILE_LIST = json.loads(file_list.read())

WELCOME = str(
    "    /\\                          /\\\n"
    + "   /__\\     Welcome to the     /__\\\n"
    + "  /\\  /\\   BotW Ene-mizer!    /\\  /\\\n"
    + " /__\\/__\\                    /__\\/__\\\n"
    + "\n"
    + "Your settings are as follows: \n"
    + "\n"
    + "Randomize MainField: " + str(RANDO_CONFIG['randomizeMainField'])
    + "\nRandomize Shrines: " + str(RANDO_CONFIG['randomizeShrines'])
    + "\nRandomize DLC Shrines: " + str(RANDO_CONFIG['randomizeDLCshrines'])
    + "\nRandomize Divine Beasts: " + str(RANDO_CONFIG['randomizeDivineBeasts'])
    + "\nRandomize Trials of the Sword: " + str(RANDO_CONFIG['randomizeTrials'])
    + "\nChaos mode activated: " + str(RANDO_CONFIG['chaosMode'])
    + "\nNormal Enemy / Boss ratio: " + str(RANDO_CONFIG['bossProb'])
    + "\n\nIf you want to modify them, feel free to modify resources\config_randomizer.json ."
)

def randomize_all_mainfield(chaosmode = RANDO_CONFIG['chaosMode']):
    for file in FILE_LIST['MainField files']:
        
        file_data = util.get_game_file(file, aoc=False).read_bytes()
        file_data = randomize_map(file_data,chaosmode,file,aoc=False)

        folder = os.path.join('Enemizer\\content\\Map\\MainField\\'+file[18:21])
        os.makedirs(folder, exist_ok=True)

        with open('Enemizer\\content\\'+file,'wb') as f:
            f.write(file_data)

def randomize_all_non_dlc_shrines(chaosmode = RANDO_CONFIG['chaosMode']):
    for file in FILE_LIST['Base packs']:

        file_data = util.get_game_file(file, aoc=False).read_bytes()
        file_data = randomize_pack(file_data,chaosmode,file,aoc=False)

        folder = os.path.join('Enemizer\\content\\Pack')
        os.makedirs(folder, exist_ok=True)

        with open('Enemizer\\content\\'+file,'wb') as f:
            f.write(file_data)

def randomize_all_dlc_shrines(chaosmode = RANDO_CONFIG['chaosMode']):
    for file in FILE_LIST['DLC shrine packs']:

        file_data = util.get_game_file(file, aoc=True).read_bytes()
        file_data = randomize_pack(file_data,chaosmode,file,aoc=True)

        folder = os.path.join('Enemizer\\aoc\\0010\\Pack')
        os.makedirs(folder, exist_ok = True)

        with open('Enemizer\\aoc\\0010\\'+file,'wb') as f:
            f.write(file_data)