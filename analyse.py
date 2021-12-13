import sys

from pbd import definitions

# group = definitions.Group(sys.argv[1])
# lines = group.classes[0].routines[0].analyse(format="C")
# with open((group.group_name or "output") + ".code", "w") as file:
#     file.write("\n".join(lines))
# def analyse(file_name, _format="raw"):
#     group = definitions.Group(file_name)
#     group.analyse(_format)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:")
        print("\tpython analyse.py <input_file_name>")
        exit(0)
    group = definitions.Group(sys.argv[1])
    group.analyse(_format="raw")
