import os
import sys

import pbd_dump
from pbd import definitions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:")
        print("\tpython pbd_dump.py <pbd file>")
        exit(0)
    input_path = os.path.abspath(sys.argv[1])
    file_name = os.path.basename(input_path)
    file_name = file_name.replace(".", "-")
    output_path = os.path.join(os.path.dirname(input_path), file_name)
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    with open(input_path, 'rb') as pbd_file:
        nodes = pbd_dump.extract_nodes(pbd_file)
        file_count = 0
        analyse_count = 0
        for node in nodes:
            for ch in node.chunks:
                ch.save(pbd_file, output_path)
                print("{} file data saved successfully".format(ch.object_name))
                file_count += 1
                dot_index = ch.object_name.rfind(".")
                if dot_index == -1:
                    continue
                ext = ch.object_name[dot_index + 1:]
                if ext.lower() in ("win", "fun", "udo"):
                    group = definitions.Group(os.path.join(output_path, ch.object_name))
                    group.analyse("raw", output_path)
                    analyse_count += 1
        print("finish extracting {} files".format(file_count))
        print("finish analyse {} files".format(analyse_count))