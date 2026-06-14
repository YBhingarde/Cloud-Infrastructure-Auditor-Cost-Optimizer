import json

def load_settings():
    with open("config/settings.json", "r") as file:
        return json.load(file)