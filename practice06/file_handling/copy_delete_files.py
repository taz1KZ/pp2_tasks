import shutil #Use it to copy, move, or remove files and directories, create archives, or query disk usage information.(on high level)
import os # to delete os.delete or os.rmdir()

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")

# Backup file
shutil.copy("sample.txt", "sample_backup.txt")

# Delete safely
file_name = "sample_copy.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted")
else:
    print("File not found")