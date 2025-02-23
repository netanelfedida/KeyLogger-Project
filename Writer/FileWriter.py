from datetime import datetime
from IWriter import IWriter
import os

class FileWriter(IWriter):
    def send_data(self, data, machine_name):
        base_dir = "data"
        machine_dir = os.path.join('..', base_dir, machine_name)
        os.makedirs(machine_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        file_path = os.path.join(machine_dir, timestamp + ".txt")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data)

if __name__ == "__main__":
    writer = FileWriter()
    writer.send_data("hello world", "Yossi")
