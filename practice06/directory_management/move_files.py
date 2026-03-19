import shutil
# Copy file to directory
shutil.copy("sample.txt", "dir1/sample.txt")
# Move file
shutil.move("dir1/sample.txt", "dir1/dir2/sample_moved.txt")
print("File moved and copied")