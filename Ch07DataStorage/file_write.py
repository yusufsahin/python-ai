import os
from pathlib import Path
# os kullanarak dosya oluşturma
current_dir= os.path.dirname(__file__)
file_path= os.path.join(current_dir,"example1.txt")
with open(file_path,"w") as file:
    file.write("Hello World!\n")
    file.write("Bu, os modülü ile belirtilen dosya yoludur.\n")

#pathlib kullanarak dosya yolu oluşturma
current_dir=Path(__file__).parent
file_path= current_dir / "example2.txt"
with open(file_path,"w") as file:
    file.write("Hello World!\n")
    file.write("Bu, pathlib modülü ile belirtilen dosya yoludur.\n")
