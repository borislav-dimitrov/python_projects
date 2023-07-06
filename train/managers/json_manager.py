import json


class JsonFileManager:
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = json.load(file)
                return content
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON file '{file_path}'.")
            return None

    @staticmethod
    def write_file(content, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(content, file, indent=4)
            print(f"Data written to '{file_path}' successfully.")
        except Exception as e:
            print(f"Error writing data to file '{file_path}': {e}")
