import os
import shutil

# 1. Файл құру және жазу
with open("example.txt", "w") as f:
    f.write("Hello\n")
    f.write("Python File Practice\n")

# 2. Файлды оқу
with open("example.txt", "r") as f:
    print("Бастапқы мазмұны:")
    print(f.read())

# 3. Қосу (append)
with open("example.txt", "a") as f:
    f.write("New line added\n")

# 4. Қайта оқу
with open("example.txt", "r") as f:
    print("Жаңартылған мазмұны:")
    print(f.read())

# 5. Көшіру (backup)
shutil.copy("example.txt", "backup_example.txt")

# 6. Қауіпсіз өшіру
if os.path.exists("backup_example.txt"):
    os.remove("backup_example.txt")
    print("Backup файл өшірілді")