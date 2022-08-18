from bcml import util
import oead
import json
from utils import is_enemy,get_random_enemy,to_oead,is_enemy_modded,get_random_enemy_modded

def randomize_map(data,ischaos,map_unit,aoc=False):
    
    file_map_decr = oead.byml.from_binary(oead.yaz0.decompress(data))
    if map_unit in ['D-6','E-6','D-7','E-7']:
        ratio = 3
    else:
        ratio = 1
    
    for unit_config in file_map_decr["Objs"]:

        if not is_enemy(unit_config["UnitConfigName"]):
            continue

        unit_config = get_random_enemy(unit_config,ischaos,ratio)

    if map_unit is not None:
        print(f'Randomized {map_unit}')

    return oead.yaz0.compress(oead.byml.to_binary(to_oead(file_map_decr), True))

def randomize_pack(data,ischaos,pack_name,aoc=False):

    sarc = oead.Sarc(data)
    sarc_writer = oead.SarcWriter(endian=oead.Endianness.Big)

    for file in sarc.get_files():
        if file.name.endswith(".smubin") and not file.name.endswith("_NoGrudgeMerge.smubin"):
            sarc_writer.files[file.name] = randomize_map(file.data,ischaos,None,aoc=aoc)
        else:
            sarc_writer.files[file.name] = oead.Bytes(file.data)

    print(f"Randomized '{pack_name}'")

    _, sarc_bytes = sarc_writer.write()
    return sarc_bytes

def randomize_map_modded(data,ischaos,map_unit,aoc=False):
    
    file_map_decr = oead.byml.from_binary(oead.yaz0.decompress(data))
    if map_unit in ['D-6','E-6','D-7','E-7']:
        ratio = 3
    else:
        ratio = 1
    
    for unit_config in file_map_decr["Objs"]:

        if not is_enemy_modded(unit_config["UnitConfigName"]):
            continue

        unit_config = get_random_enemy_modded(unit_config,ischaos,ratio)

    if map_unit is not None:
        print(f'Randomized {map_unit}')

    return oead.yaz0.compress(oead.byml.to_binary(to_oead(file_map_decr), True))

def randomize_pack_modded(data,ischaos,pack_name,aoc=False):

    sarc = oead.Sarc(data)
    sarc_writer = oead.SarcWriter(endian=oead.Endianness.Big)

    for file in sarc.get_files():
        if file.name.endswith(".smubin") and not file.name.endswith("_NoGrudgeMerge.smubin"):
            sarc_writer.files[file.name] = randomize_map_modded(file.data,ischaos,None,aoc=aoc)
        else:
            sarc_writer.files[file.name] = oead.Bytes(file.data)

    print(f"Randomized '{pack_name}'")

    _, sarc_bytes = sarc_writer.write()
    return sarc_bytes