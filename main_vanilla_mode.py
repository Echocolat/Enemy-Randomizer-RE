import oead
import json
from bcml import util
from randomize_map_or_pack import randomize_map,randomize_pack
import os
import botw_flag_util.generator as flag_util
from bcml.install import install_mod, link_master_mod
import shutil
from pathlib import Path

with open(r"resources\config_randomizer.json",'r') as config_file:
    RANDO_CONFIG = json.loads(config_file.read())

with open(r"resources\file_list.json",'r') as file_list:
    FILE_LIST = json.loads(file_list.read())

class Generator:
    def __init__(self, be: bool):
        self.big_endian = be

    actor: bool = False
    revival: list = [1, 1]
    directory: str = "Enemizer"
    bigendian: bool = True
    verbose: bool = False

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
    + "\nAuto Install with BCML: " + str(RANDO_CONFIG['autoinstall'])
    + "\n\nIf you want to modify them, feel free to modify resources\config_randomizer.json .\n\n"
    + "Are you okay with these settings ? y/n : "
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

def randomize_divine_beasts(chaosmode = RANDO_CONFIG['chaosMode']):
    for file in FILE_LIST['Divine Beast packs']:

        file_data = util.get_game_file(file, aoc=True).read_bytes()
        file_data = randomize_pack(file_data,chaosmode,file,aoc=True)

        folder = os.path.join('Enemizer\\aoc\\0010\\Pack')
        os.makedirs(folder, exist_ok = True)

        with open('Enemizer\\aoc\\0010\\'+file,'wb') as f:
            f.write(file_data)

def randomize_trials(chaosmode = RANDO_CONFIG['chaosMode']):
    for file in FILE_LIST['Trials files']:

        file_data = util.get_game_file(file, aoc=True).read_bytes()
        file_data = randomize_map(file_data,chaosmode,file,aoc=True)

        folder = os.path.join('Enemizer\\aoc\\0010\\Map\\AocField\\'+file[17:20])
        os.makedirs(folder, exist_ok = True)

        with open('Enemizer\\aoc\\0010\\'+file,'wb') as f:
            f.write(file_data)

def main():
    if input(WELCOME) != 'y':
        print('Canceled randomization')
    else:
        if RANDO_CONFIG['randomizeMainField']:
            randomize_all_mainfield()
        if RANDO_CONFIG['randomizeShrines']:
            randomize_all_non_dlc_shrines()
        if RANDO_CONFIG['randomizeDLCshrines']:
            randomize_all_dlc_shrines()
        if RANDO_CONFIG['randomizeDivineBeasts']:
            randomize_divine_beasts()
        if RANDO_CONFIG['randomizeTrials']:
            randomize_trials()
        bootup_path = Path("Enemizer\\content\\Pack\\Bootup.pack")
        bootup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(util.get_game_file("Pack/Bootup.pack"), bootup_path)
        flag_util.generate(Generator(util.get_settings("wiiu")))
        if RANDO_CONFIG['autoinstall']:
            mod_path = Path("Enemizer\\info.json")
            mod_meta = {
                "name": "Enemizer v2 by Echocolat",
                "image": "",
                "url": "",
                "desc": "",
                "version": "2.0.0",
                "options": {},
                "depends": [],
                "showCompare": False,
                "showConvert": False,
                "platform": "wiiu" if util.get_settings("wiiu") == True else "switch",
                "id": "",
            }

            mod_path.write_text(json.dumps(mod_meta))
            install_mod(mod=mod_path, merge_now=True)
            link_master_mod()

if __name__ == '__main__':
    main()