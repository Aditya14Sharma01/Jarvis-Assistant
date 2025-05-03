import shutil
import datetime
time = datetime.datetime.now().strftime("%H:%M:%S")
source_path = "1"
destination_path = f"Command_Line_Record/Command_Line_{source_path}_{time}.txt"
shutil.move(source_path, destination_path)