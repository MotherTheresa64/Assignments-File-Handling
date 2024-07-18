# Task 1: Directory Inspector

from os import walk
# After doing some reading it looks like using the 'walk' function is more effective than anything else
# Below is the listed example file path if we had one to use
directory_path = r'E:\\account\\'
# list to store files name
res = []
for (directory_path, dir_names, file_names) in walk(directory_path):
    res.extend(file_names)
print(res)