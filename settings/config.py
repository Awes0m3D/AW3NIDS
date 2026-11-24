import json
import sys
from pathlib import Path


class ConfigManager:

    def __init__(self):
        # Determine the project/settings directory
        if getattr(sys, "frozen", False):
            # Running as a packaged PyInstaller application
            self.base_dir = Path(sys.executable).resolve().parent
        else:
            # Running normally from Python
            self.base_dir = Path(__file__).resolve().parent.parent

        # Settings file location
        self.settings_dir = self.base_dir / "settings"
        self.settings_dir.mkdir(parents=True, exist_ok=True)

        self.path = self.settings_dir / "settings.json"

        self.load()

    def load(self):
        if not self.path.exists():
            self.data = {}
            self.save()
            return

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = json.load(file)

        except (json.JSONDecodeError, OSError):
            self.data = {}
            self.save()

    def save(self):
        self.settings_dir.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()