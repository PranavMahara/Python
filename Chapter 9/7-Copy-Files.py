import shutil

newpath = r"C:\ABC"
oldpath = r"C:\ABCDE"
shutil.copy(newpath, oldpath)
print("COPIED")