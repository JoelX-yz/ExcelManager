import json

def getSettings(filename = "config.json") -> dict:
    with open(filename,"r",encoding="utf-8") as excelLineSettingFile:  
        settings = json.load(excelLineSettingFile)
    return settings


# From excel formatted json to python library type json
def getDirection(filename = "POS.json") -> dict:
    with open(filename,encoding="utf-8") as positionFile:
        pos = json.load(positionFile)
    
    # load data into a dictionary
    directions = {}
    for item in pos:
        directions[item["Name"]] = item["Direction"]
    
    with open("CustomerDirections.json", "w") as outfile:
        json.dump(directions, outfile)

    return directions

# Load json for reading and editing

def updateDirections(result):
    with open("CustomerDirections.json", "rw") as jsonfile:
        pos = json.load(jsonfile)
    
    #   clean empty ones
    for cx in pos.keys():
        if pos[cx] == "":
            pos.pop(cx)
    
    #   load current ones
    customers = result[0][0]
    for cx in customers.values():
        if cx.name not in pos:
            pos[cx.name] = ""
