import json
import os
import pathlib

os.chdir(pathlib.Path(__file__).parent.absolute())

with open(r'fusion input\First preset\config_enemy_weights.json','r') as f:
    first_config_weights = json.loads(f.read())

with open(r'fusion input\Second preset\config_enemy_weights.json','r') as f:
    second_config_weights = json.loads(f.read())

with open(r'fusion input\First preset\defaults.json','r') as f:
    first_defaults = json.loads(f.read())

with open(r'fusion input\Second preset\defaults.json','r') as f:
    second_defaults = json.loads(f.read())

new_defaults = first_defaults.copy()
new_config = {**first_config_weights,**second_config_weights}

with open(r'fusion output\config_enemy_weights.json','w') as f:
    f.write(json.dumps(new_config,indent=2))

new_defaults['Bosses'] = {**first_defaults['Bosses'],**second_defaults['Bosses']}
new_defaults['Enemies'] = {**first_defaults['Enemies'],**second_defaults['Enemies']}
new_defaults['ItemTableData'] = {key:list(set(first_defaults['ItemTableData'][key]) | set(second_defaults['ItemTableData'][key])) for key in first_defaults['ItemTableData']}
for itemTable in first_defaults['ItemTables']:
    if itemTable == 'IsWandOnly':
        new_defaults['ItemTables']['IsWandOnly'] = {**first_defaults['ItemTables']['IsWandOnly'],**second_defaults['ItemTables']['IsWandOnly']}
    else:
        new_defaults['ItemTables'][itemTable] = list(set(first_defaults['ItemTables'][itemTable]) | set(second_defaults['ItemTables'][itemTable]))

with open(r'fusion output\defaults.json','w') as f:
    f.write(json.dumps(new_defaults,indent=2))