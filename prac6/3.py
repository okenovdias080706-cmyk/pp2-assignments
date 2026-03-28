import os
import shutil

# 1. Папка жасау
os.makedirs("test_folder/subfolder", exist_ok=True)

# 2. Файл жасау
with open("test_folder/file1.txt", "w") as f:
    f.write("File 1")

with open("test_folder/file2.py", "w") as f:
    f.write("print('Hello')")

# 3. Папка ішін көру
print("Файлдар тізімі:")
print(os.listdir("test_folder"))

# 4. .txt файлдарды табу
print("TXT файлдар:")
for file in os.listdir("test_folder"):
    if file.endswith(".txt"):
        print(file)

# 5. Көшіру
shutil.copy("test_folder/file1.txt", "test_folder/subfolder/file1_copy.txt")

# 6. Жылжыту
shutil.move("test_folder/file2.py", "test_folder/subfolder/file2.py")