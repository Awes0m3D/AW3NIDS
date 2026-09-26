import json
from pathlib import Path


class ConfigManager:

    
        def __init__(self):
            self.path = Path("settings/settings.json")
            self.load()

        def load(self):

            if not self.path.exists():
                self.data = {}
                self.save()
            else:
                with open(self.path, "r") as file:
                    self.data = json.load(file)

        def save(self):

            with open(self.path, "w") as file:
                json.dump(self.data, file, indent=4)

        def get(self, key, default=None):
            return self.data.get(key, default)

        def set(self, key, value):
            self.data[key] = value
            self.save()