import json

def getSettings(filename = "config.json") -> dict:
    with open(filename,"r",encoding="utf-8") as excelLineSettingFile:  
        settings = json.load(excelLineSettingFile)
    return settings