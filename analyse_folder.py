import os
import sys

from pbd import definitions

if len(sys.argv) != 2:
    print("Usage: ")
    print("\tpython analyse_folder.py <folder path>")
    exit(0)
if not os.path.isdir(sys.argv[1]):
    print("the input parameter is not a directory")
    exit(1)
for file in os.listdir(sys.argv[1]):
    dot_index = file.rfind(".")
    if dot_index == -1:
        continue
    ext = file[dot_index + 1:]
    if not ext.lower() in ("win", "fun", "udo"):
        print("{} skipped from analysis".format(file))
        continue
    # print(file)
    group = definitions.Group(os.path.join(sys.argv[1], file))
    group.analyse("raw", sys.argv[1])
    print("{} successfully analysed".format(file))
