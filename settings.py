import json
import os

class UserSettingsManager:
    """
    Управляет сохранением, загрузкой и использованием пользовательских настроек.
    """
    def __init__(self, settings_file='user_settings.json', default_settings=None):
        self.settings_file = settings_file
        self.default_settings = default_settings if default_settings is not None else {
            "language": "русский",
            "user_name": "Гость",
        }
        self.current_settings = {}
        self._load_settings()

    def _load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    loaded_data = json.load(f)
                    self.current_settings = {**self.default_settings, **loaded_data}
                print(f"Настройки успешно загружены из '{self.settings_file}'")
            except json.JSONDecodeError:
                print(f"Ошибка чтения файла настроек '{self.settings_file}'. Используются настройки по умолчанию.")
                self.current_settings = self.default_settings.copy()
            except Exception as e:
                print(f"Неизвестная ошибка при загрузке настроек: {e}. Используются настройки по умолчанию.")
                self.current_settings = self.default_settings.copy()
        else:
            print(f"Файл настроек '{self.settings_file}' не найден. Используются настройки по умолчанию.")
            self.current_settings = self.default_settings.copy()
            self._save_settings()

    def _save_settings(self):
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.current_settings, f, ensure_ascii=False, indent=4)
            print(f"Настройки успешно сохранены в '{self.settings_file}'")
        except Exception as e:
            print(f"Ошибка при сохранении настроек в '{self.settings_file}': {e}")

    def get_setting(self, key):
        return self.current_settings.get(key)

    def set_setting(self, key, value):
        old_value = self.current_settings.get(key)
        if old_value != value:
            self.current_settings[key] = value
            self._save_settings()
            print(f"Настройка '{key}' изменена на '{value}' и сохранена.")
        else:
            print(f"Настройка '{key}' уже имеет значение '{value}'. Изменений не требуется.")

    def get_all_settings(self):
        return self.current_settings.copy()