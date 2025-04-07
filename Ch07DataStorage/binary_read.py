import os
from pathlib import Path

#os kullanarak

current_dir=os.path.dirname(__file__)
file_path=os.path.join(current_dir,"example1.bin")
with open(file_path,"rb") as file:
    data=file.read()
    print("Okuanan veri:",data)

current_dir2=Path(__file__).parent
file_path2=current_dir2/'example2.bin'

with open(file_path2,"rb") as file:
    data=file.read()
    print("Okuanan veri2:",data)