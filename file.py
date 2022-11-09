from pathlib import Path

path = Path("/home/delight/Documents/wedding program.docx")

pathes = Path.cwd()
print(pathes.is_absolute())

new_dir = Path.home() / "new_directory"
# new_dir.mkdir()

file_path = new_dir / "file1.txt"
# file_path.touch()

# for path in new_dir.iterdir():
#     print(path)

for path in list(new_dir.iterdir()):
    print(path)