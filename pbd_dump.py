import os
import struct
import sys
from datetime import datetime


# Print iterations progress
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


class Header:
    id = 'HDR*'

    def __init__(self, file):
        self.program_name = file.read(24).decode('utf16')
        file.seek(4, 1)
        self.program_version = file.read(8).decode('utf16')
        self.creation_date = datetime.utcfromtimestamp(struct.unpack("<I", file.read(4))[0])
        file.seek(2, 1)
        self.library_comment = file.read(512).decode('utf16')
        self.offset_scc_data = struct.unpack("<I", file.read(4))[0]
        self.size_scc_data = struct.unpack("<I", file.read(4))[0]
        file.seek(458, 1)


class Bitmap:
    id = 'FRE*'

    def __init__(self, file):
        self.offset_next_block = struct.unpack("<I", file.read(4))[0]
        self.data = file.read(504)


class Node:
    id = 'NOD*'

    def __init__(self, file):
        self.loc = file.tell()
        self.offset_left = struct.unpack("<I", file.read(4))[0]
        self.offset_parent = struct.unpack("<I", file.read(4))[0]
        self.offset_right = struct.unpack("<I", file.read(4))[0]
        self.space_left = struct.unpack("<H", file.read(2))[0]
        self.first_object_pos = struct.unpack("<H", file.read(2))[0]
        self.entry_count = struct.unpack("<H", file.read(2))[0]
        self.last_object_pos = struct.unpack("<H", file.read(2))[0]
        file.seek(8, 1)
        self.chunks = []
        for x in range(self.entry_count):
            chunk = read_block(file)
            if not isinstance(chunk, Chunk):
                raise Exception("file format error: expect chunk block")
            self.chunks.append(chunk)
        file.seek(self.space_left, 1)


class Chunk:
    id = 'ENT*'

    def __init__(self, file):
        self.version = file.read(8).decode('utf16')
        self.offset_first_data_block = struct.unpack("<I", file.read(4))[0]
        self.object_size = struct.unpack("<I", file.read(4))[0]
        self.object_date = datetime.utcfromtimestamp(struct.unpack("<I", file.read(4))[0])
        self.comment_length = struct.unpack("<H", file.read(2))[0]
        length = struct.unpack("<H", file.read(2))[0]
        self.object_name = file.read(length).decode('utf16').strip('\x00')
        self.data = b''

    def save(self, input_stream, base_path):
        current_pos = input_stream.tell()
        print('start load data for file: {}'.format(self.object_name))
        print_progress_bar(0, self.object_size, prefix='Progress:', suffix='Complete')
        input_stream.seek(self.offset_first_data_block)
        file_path = os.path.join(base_path, self.object_name)
        with open(file_path, 'wb') as file:
            try:
                dat = read_block(input_stream)
                if not isinstance(dat, Data):
                    raise Exception(
                        "file format error: expect a data block while reading object: {}".format(self.object_name))
                file.write(dat.blob)
                progress = len(dat.blob)
                print_progress_bar(progress, self.object_size, prefix='Progress:', suffix='Complete')
                while dat.offset_next:
                    input_stream.seek(dat.offset_next)
                    dat = read_block(input_stream)
                    if not isinstance(dat, Data):
                        raise Exception(
                            "file format error: expect a data block while reading object: {}".format(self.object_name))
                    file.write(dat.blob)
                    progress += len(dat.blob)
                    print_progress_bar(progress, self.object_size, prefix='Progress:', suffix='Complete')
            finally:
                input_stream.seek(current_pos)
            # file.write(self.data)

    def load_data(self, file):
        current_pos = file.tell()
        print('start load data for file: {}'.format(self.object_name))
        print_progress_bar(0, self.object_size, prefix='Progress:', suffix='Complete')
        file.seek(self.offset_first_data_block)
        dat = read_block(file)
        if not isinstance(dat, Data):
            file.seek(current_pos)
            raise Exception("file format error: expect a data block")
        self.data += dat.blob
        while dat.offset_next:
            file.seek(dat.offset_next)
            dat = read_block(file)
            if not isinstance(dat, Data):
                file.seek(current_pos)
                raise Exception("file format error: expect a data block")
            self.data += dat.blob
            print_progress_bar(len(self.data), self.object_size, prefix='Progress:', suffix='Complete')
        file.seek(current_pos)


class Data:
    id = 'DAT*'

    def __init__(self, file):
        self.offset_next = struct.unpack("<I", file.read(4))[0]
        length = struct.unpack("<H", file.read(2))[0]
        self.blob = file.read(length)


def read_block(file):
    _id = file.read(4).decode()
    if _id == Header.id:
        return Header(file)
    elif _id == Bitmap.id:
        return Bitmap(file)
    elif _id == Node.id:
        return Node(file)
    elif _id == Chunk.id:
        return Chunk(file)
    elif _id == Data.id:
        return Data(file)


def get_node(file, parent_node):
    if not isinstance(parent_node, Node):
        return None, None
    left_node = None
    right_node = None
    if parent_node.offset_left:
        file.seek(parent_node.offset_left)
        _node = read_block(file)
        if isinstance(_node, Node):
            left_node = _node
    if parent_node.offset_right:
        file.seek(parent_node.offset_right)
        _node = read_block(file)
        if isinstance(_node, Node):
            right_node = _node
    return left_node, right_node


def extract_nodes(file):
    # read header
    _ = read_block(file)
    # read bitmap
    _ = read_block(file)
    while True:
        temp = read_block(file)
        if isinstance(temp, Node):
            first_node = temp
            break

    _nodes = [first_node]
    index = 0
    while index < len(_nodes):
        node_1, node_2 = get_node(file, _nodes[index])
        found = False
        if node_1:
            for _node in _nodes:
                if _node.loc == node_1.loc:
                    found = True
                    break
            if not found:
                _nodes.append(node_1)
        found = False
        if node_2:
            for _node in _nodes:
                if _node.loc == node_2.loc:
                    found = True
                    break
            if not found:
                _nodes.append(node_2)
        index += 1
    return _nodes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("\tpython pbd_dump.py <pbd file>")
        exit(0)

    # prepare input and output path
    input_path = os.path.abspath(sys.argv[1])
    file_name = os.path.basename(input_path)
    file_name = file_name.replace(".", "-")
    output_path = os.path.join(os.path.dirname(input_path), file_name)
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    with open(input_path, 'rb') as pbd_file:
        nodes = extract_nodes(pbd_file)
        file_count = 0
        for node in nodes:
            for ch in node.chunks:
                ch.save(pbd_file, output_path)
                print("{} file data saved successfully".format(ch.object_name))
                file_count += 1
        print("finish extracting {} files".format(file_count))
