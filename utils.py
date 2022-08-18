import oead
import json
import random

with open(r"resources\defaults.json","r") as defaults:
    DEFAULTS = json.loads(defaults.read())

with open(r"resources\config_enemy_weights.json",'r') as weights:
    WEIGHTS = json.loads(weights.read())

with open(r'resources (modded)\\defaults.json','r') as defaults:
    DEFAULTS_MODDED = json.loads(defaults.read())

with open(r"resources (modded)\\config_enemy_weights.json",'r') as weights:
    WEIGHTS_MODDED = json.loads(weights.read())

with open(r"resources\config_randomizer.json",'r') as boss_prob:
    BOSS_PROB = json.loads(boss_prob.read())['bossProb']

truetableenemies = []
for enemy in list(DEFAULTS['Enemies']):
    for _ in range(WEIGHTS[enemy]):
        truetableenemies.append(enemy)

truetableenemiesmodded = []
for enemy in list(DEFAULTS_MODDED['Enemies']):
    for _ in range(WEIGHTS_MODDED[enemy]):
        truetableenemiesmodded.append(enemy)

truetablebosses = []
for boss in list(DEFAULTS['Bosses']):
    for _ in range(WEIGHTS[boss]):
        truetablebosses.append(boss)

truetablebossesmodded = []
for boss in list(DEFAULTS_MODDED['Bosses']):
    for _ in range(WEIGHTS_MODDED[boss]):
        truetablebossesmodded.append(boss)

truetablearrows = []
for arrow in list(DEFAULTS['ArrowWeights']):
    for _ in range(DEFAULTS['ArrowWeights'][arrow]):
        truetablearrows.append(arrow)

WEIGHTEDENEMIES = truetableenemies
WEIGHTEDENEMIESMODDED = truetableenemiesmodded
WEIGHTEDBOSSES = truetablebosses
WEIGHTEDBOSSESMODDED = truetablebossesmodded
WEIGHTEDARROW = truetablearrows

def get_item_table(type_weapon):

    if type_weapon in DEFAULTS['ItemTableData']:
        return ["Weapon_" + type_weapon + "_" + DEFAULTS['ItemTableData'][type_weapon][i] for i in range(len(DEFAULTS['ItemTableData'][type_weapon]))]
    
    else:
        return []

def get_item_table_modded(type_weapon):

    if type_weapon in DEFAULTS_MODDED['ItemTableData']:
        return ["Weapon_" + type_weapon + "_" + DEFAULTS_MODDED['ItemTableData'][type_weapon][i] for i in range(len(DEFAULTS_MODDED['ItemTableData'][type_weapon]))]
    
    else:
        return []

def is_enemy(unit_config_name):

    if unit_config_name[0:5] == "Enemy":
        for blacklistflag in DEFAULTS['BlacklistFlags']:
            if blacklistflag in unit_config_name:
                return False
        return True

    return False

def is_enemy_modded(unit_config_name):

    if unit_config_name[0:5] == "Enemy":
        for blacklistflag in DEFAULTS_MODDED['BlacklistFlags']:
            if blacklistflag in unit_config_name:
                return False
        return True

    return False

def get_random_weapons(unit_config_name) -> list:

    item_tables = DEFAULTS['ItemTables']

    if unit_config_name in item_tables['IsWandOnly']:
        return [item_tables['IsWandOnly'][unit_config_name]]

    elif unit_config_name in item_tables['IsBowOnly']:
        return [random.choice(get_item_table('Bow'))]

    elif unit_config_name in item_tables['IsLswordOnly']:
        return [random.choice(get_item_table('Lsword'))]

    elif unit_config_name in item_tables['IsLynel']:
        rand_number = random.randint(0,2)
        chosen_bow = random.choice(get_item_table('Bow'))
        if rand_number == 0:
            return [chosen_bow,random.choice(get_item_table('Sword')),random.choice(get_item_table('Shield'))]
        elif rand_number == 1:
            return [chosen_bow,random.choice(get_item_table('Lsword'))]
        else:
            return [chosen_bow,random.choice(get_item_table('Spear'))]

    elif unit_config_name in item_tables['IsNoWeapon']:
        return []

    elif unit_config_name in item_tables['IsOneWeapon']:
        chosen_type = random.choice(['Spear','Sword','Lsword'])
        return [random.choice(get_item_table(chosen_type))]

    elif unit_config_name in item_tables['IsTwoWeapons']:
        chosen_types = [random.choice(['Spear','Sword','Lsword','Shield']),random.choice(['Spear','Sword','Lsword'])]
        return [random.choice(get_item_table(chosen_types[i])) for i in range(2)]

    elif unit_config_name in item_tables['IsThreeWeapons']:
        chosen_types = [random.choice(['Spear','Sword','Lsword','Shield']),random.choice(['Spear','Sword','Lsword']),random.choice(['Spear','Sword','Lsword'])]
        return [random.choice(get_item_table(chosen_types[i])) for i in range(3)]

    elif unit_config_name in item_tables['IsNormal']:
        rand_number = random.randint(0,3)
        if rand_number == 0:
            return [random.choice(get_item_table('Bow'))]
        elif rand_number == 1:
            return [random.choice(get_item_table('Spear'))]
        elif rand_number == 2:
            return [random.choice(get_item_table('Lsword'))]
        else:
            return [random.choice(get_item_table('Sword')),random.choice(get_item_table('Shield'))]

def get_random_weapons_modded(unit_config_name) -> list:

    item_tables = DEFAULTS_MODDED['ItemTables']

    if unit_config_name in item_tables['IsWandOnly']:
        return [item_tables['IsWandOnly'][unit_config_name]]

    elif unit_config_name in item_tables['IsBowOnly']:
        return [random.choice(get_item_table('Bow'))]

    elif unit_config_name in item_tables['IsLswordOnly']:
        return [random.choice(get_item_table('Lsword'))]

    elif unit_config_name in item_tables['IsLynel']:
        rand_number = random.randint(0,2)
        chosen_bow = random.choice(get_item_table('Bow'))
        if rand_number == 0:
            return [chosen_bow,random.choice(get_item_table('Sword')),random.choice(get_item_table('Shield'))]
        elif rand_number == 1:
            return [chosen_bow,random.choice(get_item_table('Lsword'))]
        else:
            return [chosen_bow,random.choice(get_item_table('Spear'))]

    elif unit_config_name in item_tables['IsNoWeapon']:
        return []

    elif unit_config_name in item_tables['IsOneWeapon']:
        chosen_type = random.choice(['Spear','Sword','Lsword'])
        return [random.choice(get_item_table(chosen_type))]

    elif unit_config_name in item_tables['IsTwoWeapons']:
        chosen_types = [random.choice(['Spear','Sword','Lsword','Shield']),random.choice(['Spear','Sword','Lsword'])]
        return [random.choice(get_item_table(chosen_types[i])) for i in range(2)]

    elif unit_config_name in item_tables['IsThreeWeapons']:
        chosen_types = [random.choice(['Spear','Sword','Lsword','Shield']),random.choice(['Spear','Sword','Lsword']),random.choice(['Spear','Sword','Lsword'])]
        return [random.choice(get_item_table(chosen_types[i])) for i in range(3)]

    elif unit_config_name in item_tables['IsNormal']:
        rand_number = random.randint(0,3)
        if rand_number == 0:
            return [random.choice(get_item_table('Bow'))]
        elif rand_number == 1:
            return [random.choice(get_item_table('Spear'))]
        elif rand_number == 2:
            return [random.choice(get_item_table('Lsword'))]
        else:
            return [random.choice(get_item_table('Sword')),random.choice(get_item_table('Shield'))]

def get_random_enemy(config_data,ischaosactive,ratio):

    if ischaosactive:
        if random.randint(1,BOSS_PROB) == 1:
            enemy =  random.choice(list(DEFAULTS['Bosses']))
        else:
            enemy =  random.choice(list(DEFAULTS['Enemies']))
    else:
        if random.randint(1,BOSS_PROB) == 1:
            enemy = random.choice(WEIGHTEDBOSSES)
        else:
            enemy = random.choice(WEIGHTEDENEMIES)

    if enemy in DEFAULTS['Enemies']:
        parameters = DEFAULTS['Enemies'][enemy]
    else:
        parameters = DEFAULTS['Bosses'][enemy]

    config_data['!Parameters'] = to_oead(parameters)
    #print(dict(config_data['!Parameters']))

    if 'Guardian_A_Fixed' in config_data['UnitConfigName'] and not 'Guardian_A_Fixed' in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 2.5)

    if "Golem" in enemy and "Little" not in enemy and enemy != "Enemy_Golem_Fire_R":
        config_data['!Parameters']['GolemSleepType'] = random.choice(["SleepForward_B", "SleepForward_A"])
        config_data['!Parameters']['GolemWeakPointLocation'] = random.choice(["Point_A", "Point_B", "Point_C"])

    if "Giant" in enemy:
        armors = {"GiantArmor1": "L", "GiantArmor2": "R"}
        for param in armors:
            if param in config_data["!Parameters"]:
                dict(config_data["!Parameters"]).pop(param)
            if random.randint(0, 2) != 0:
                config_data["!Parameters"][param] = f"GiantGreave_{random.choice(['Wood', 'Iron'])}_{armors[param]}"
        config_data['!Parameters']['EquipItem3'] = random.choice(get_item_table('Bow'))
        config_data['!Parameters']['EquipItem4'] = random.choice(get_item_table('Spear'))
        config_data['!Parameters']['EquipItem5'] = random.choice(get_item_table('Sword'))

    config_data['UnitConfigName'] = enemy

    if "ArrowName" in config_data['!Parameters']:
        config_data['!Parameters']['ArrowName'] = random.choice(WEIGHTEDARROW)

    if enemy in DEFAULTS['ItemTables']['IsWandOnly'] or enemy in DEFAULTS['ItemTables']['IsBowOnly'] or enemy in DEFAULTS['ItemTables']['IsOneWeapon']:
        weapon = get_random_weapons(enemy)[0]
        config_data['!Parameters']['EquipItem1'] = weapon

    elif enemy in DEFAULTS['ItemTables']['IsLswordOnly']:
        config_data['!Parameters']['EquipItem1'] = get_random_weapons(enemy)[0]
        config_data['!Parameters']['EquipItem3'] = 'Weapon_Sword_043'

    elif enemy in DEFAULTS['ItemTables']['IsLynel']:
        lynel_weapons = get_random_weapons(enemy)
        if len(lynel_weapons) == 3:
            config_data['!Parameters']['EquipItem3'] = lynel_weapons[2]
            config_data['!Parameters']['EquipItem1'] = lynel_weapons[0]
            config_data['!Parameters']['EquipItem2'] = lynel_weapons[1]
        else:
            config_data['!Parameters']['EquipItem1'] = lynel_weapons[1]
            config_data['!Parameters']['EquipItem2'] = lynel_weapons[0]

    elif enemy in DEFAULTS['ItemTables']['IsTwoWeapons']:
        guardian_weapons = get_random_weapons(enemy)
        config_data['!Parameters']['EquipItem1'] = guardian_weapons[0]
        config_data['!Parameters']['EquipItem2'] = guardian_weapons[1]

    elif enemy in DEFAULTS['ItemTables']['IsThreeWeapons']:
        guardian_weapons = get_random_weapons(enemy)
        config_data['!Parameters']['EquipItem1'] = guardian_weapons[0]
        config_data['!Parameters']['EquipItem2'] = guardian_weapons[1]
        config_data['!Parameters']['EquipItem3'] = guardian_weapons[2]
        
    elif enemy in DEFAULTS['ItemTables']['IsNormal']:
        enemy_weapons = get_random_weapons(enemy)
        if len(enemy_weapons) == 2:
            config_data['!Parameters']['EquipItem1'] = enemy_weapons[0]
            config_data['!Parameters']['EquipItem2'] = enemy_weapons[1]
        else:
            config_data['!Parameters']['EquipItem1'] = enemy_weapons[0]

    if "LinksToRail" in config_data:
        dict(config_data).pop("LinksToRail")
    if "OnlyOne" in config_data:
        dict(config_data).pop("OnlyOne")
    if "Scale" in config_data:
        dict(config_data).pop("Scale")
    if "Guardian_C" in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 30.0)
    if "Keese" in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 2.5)

    if str(hex(config_data['HashId'])) in DEFAULTS['IchigekiActors']:
        config_data["!Parameters"]["IsIchigekiActor"] = True

    return config_data

def get_random_enemy_modded(config_data,ischaosactive,ratio):

    if ischaosactive:
        if random.randint(1,int(BOSS_PROB*ratio)) == 1:
            enemy =  random.choice(list(DEFAULTS_MODDED['Bosses']))
        else:
            enemy =  random.choice(list(DEFAULTS_MODDED['Enemies']))
    else:
        if random.randint(1,int(BOSS_PROB*ratio)) == 1:
            enemy = random.choice(WEIGHTEDBOSSESMODDED)
        else:
            enemy = random.choice(WEIGHTEDENEMIESMODDED)

    if enemy in DEFAULTS_MODDED['Enemies']:
        parameters = DEFAULTS_MODDED['Enemies'][enemy]
    else:
        parameters = DEFAULTS_MODDED['Bosses'][enemy]

    config_data['!Parameters'] = to_oead(parameters)
    #print(dict(config_data['!Parameters']))

    if 'Guardian_A_Fixed' in config_data['UnitConfigName'] and not 'Guardian_A_Fixed' in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 2.5)

    if "Golem" in enemy and "Little" not in enemy and enemy != "Enemy_Golem_Fire_R":
        config_data['!Parameters']['GolemSleepType'] = random.choice(["SleepForward_B", "SleepForward_A"])
        config_data['!Parameters']['GolemWeakPointLocation'] = random.choice(["Point_A", "Point_B", "Point_C"])

    if "Giant" in enemy:
        armors = {"GiantArmor1": "L", "GiantArmor2": "R"}
        for param in armors:
            if param in config_data["!Parameters"]:
                dict(config_data["!Parameters"]).pop(param)
            if random.randint(0, 2) != 0:
                config_data["!Parameters"][param] = f"GiantGreave_{random.choice(['Wood', 'Iron'])}_{armors[param]}"
        config_data['!Parameters']['EquipItem3'] = random.choice(get_item_table_modded('Bow'))
        config_data['!Parameters']['EquipItem4'] = random.choice(get_item_table_modded('Spear'))
        config_data['!Parameters']['EquipItem5'] = random.choice(get_item_table_modded('Sword'))

    config_data['UnitConfigName'] = enemy

    if "ArrowName" in config_data['!Parameters']:
        config_data['!Parameters']['ArrowName'] = random.choice(WEIGHTEDARROW)

    if enemy in DEFAULTS_MODDED['ItemTables']['IsWandOnly'] or enemy in DEFAULTS_MODDED['ItemTables']['IsBowOnly'] or enemy in DEFAULTS_MODDED['ItemTables']['IsOneWeapon']:
        weapon = get_random_weapons_modded(enemy)[0]
        config_data['!Parameters']['EquipItem1'] = weapon

    elif enemy in DEFAULTS_MODDED['ItemTables']['IsLswordOnly']:
        config_data['!Parameters']['EquipItem1'] = get_random_weapons_modded(enemy)[0]
        config_data['!Parameters']['EquipItem3'] = 'Weapon_Sword_043'

    elif enemy in DEFAULTS_MODDED['ItemTables']['IsLynel']:
        lynel_weapons = get_random_weapons_modded(enemy)
        if len(lynel_weapons) == 3:
            config_data['!Parameters']['EquipItem3'] = lynel_weapons[2]
            config_data['!Parameters']['EquipItem1'] = lynel_weapons[0]
            config_data['!Parameters']['EquipItem2'] = lynel_weapons[1]
        else:
            config_data['!Parameters']['EquipItem1'] = lynel_weapons[1]
            config_data['!Parameters']['EquipItem2'] = lynel_weapons[0]

    elif enemy in DEFAULTS_MODDED['ItemTables']['IsTwoWeapons']:
        guardian_weapons = get_random_weapons_modded(enemy)
        config_data['!Parameters']['EquipItem1'] = guardian_weapons[0]
        config_data['!Parameters']['EquipItem2'] = guardian_weapons[1]

    elif enemy in DEFAULTS_MODDED['ItemTables']['IsThreeWeapons']:
        guardian_weapons = get_random_weapons_modded(enemy)
        config_data['!Parameters']['EquipItem1'] = guardian_weapons[0]
        config_data['!Parameters']['EquipItem2'] = guardian_weapons[1]
        config_data['!Parameters']['EquipItem3'] = guardian_weapons[2]
        
    elif enemy in DEFAULTS_MODDED['ItemTables']['IsNormal']:
        enemy_weapons = get_random_weapons_modded(enemy)
        if len(enemy_weapons) == 2:
            config_data['!Parameters']['EquipItem1'] = enemy_weapons[0]
            config_data['!Parameters']['EquipItem2'] = enemy_weapons[1]
        else:
            config_data['!Parameters']['EquipItem1'] = enemy_weapons[0]

    if "LinksToRail" in config_data:
        dict(config_data).pop("LinksToRail")
    if "OnlyOne" in config_data:
        dict(config_data).pop("OnlyOne")
    if "Scale" in config_data:
        dict(config_data).pop("Scale")
    if "Guardian_C" in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 30.0)
    if "Keese" in enemy:
        config_data["Translate"][1] = oead.F32(float(config_data["Translate"][1]) + 2.5)

    if str(hex(config_data['HashId'])) in DEFAULTS_MODDED['IchigekiActors']:
        config_data["!Parameters"]["IsIchigekiActor"] = True

    return config_data

def to_oead(obj):

    # Get the object type
    obj_type = type(obj)

    # Check the object type
    if obj_type not in [int, float, list, dict]:
        return obj

    # Handle int values
    if obj_type is int:
        try:
            return oead.S32(obj)
        except:
            return oead.U32(obj)

    # Handle float values
    elif obj_type is float:
        return oead.F32(obj)

    # Handle list values
    elif obj_type is list:

        # Create temp python std list
        _list = list()
        for item in list(obj):
            _list.append(to_oead(item))

        return oead.byml.Array(_list)

    # Handle dict values
    elif obj_type is dict:

        # Create temp python std dict
        _dict = dict()
        for key, value in dict(obj).items():
            _dict[to_oead(key)] = to_oead(value)

        return _dict