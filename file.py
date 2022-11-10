from pathlib import Path

path = Path("/home/delight/Documents/wedding program.docx")

pathes = Path.cwd()
print(pathes.is_absolute())

new_dir = Path.home() / "new_directory"
new_dir.mkdir()

file_path = new_dir / "file1.txt"
file_path.touch()

for path in new_dir.iterdir():
    print(path)

for path in list(new_dir.iterdir()):
    print(path)

for path in new_dir.glob("*.txt"):
    print(path)

#   writing and reading csv file
temperature_readings = [68, 65, 68, 70, 74, 72]

file_path = Path.home() / "temperatures.txt"
with file_path.open(mode="a", encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")