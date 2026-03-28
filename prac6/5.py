from pathlib import Path

# 1. Файл жасау және жазу
file = Path("test.txt")
file.write_text("Hello\nPathlib Example")

# 2. Оқу
print(file.read_text())

# 3. Папка жасау
folder = Path("data")
folder.mkdir(exist_ok=True)

# 4. Файлды көшіру (қолмен)
new_file = folder / "test_copy.txt"
new_file.write_text(file.read_text())

# 5. .txt файлдарды табу
for f in Path(".").glob("*.txt"):
    print("TXT файл:", f)