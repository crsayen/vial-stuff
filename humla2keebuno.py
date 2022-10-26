import json
import time

with open('./humla.json', 'r') as f:
    data = json.load(f)

def transform_row(row):
    return [row[2:-2]] if row[0] == -1 else [["KC_TRNS", *(row[0:5])], [*(row[5:]) , "KC_TRNS"]]

def transform_layer(layer):
    return [r for l in [transform_row(row) for row in layer] for r in l]

data["layout"] = [transform_layer(layer) for layer in data['layout']]

with open(f'./keebuno-{time.strftime("%y%m%d%H%M%S")}.vil', 'w') as f: 
    f.write(json.dumps(data, indent = 2))