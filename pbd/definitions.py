import os
import re
import struct
from datetime import datetime
import json

from pbd.system_enums import enum_main, EnumInfo
from pbd.types import g_types


def get_qualified_name(object_name, object_type):
    object_type = object_type - 0x4077
    if object_type == 13:
        return object_name + ".win"
    elif object_type == 8:
        return object_name + ".udo"
    elif object_type == 1:
        return object_name + ".str"
    elif object_type == 93:
        return object_name + ".xxy"
    elif object_type == 55:
        return object_name + ".men"
    elif object_type == 0:
        return object_name + ".fun"
    elif object_type == 18:
        return object_name + ".dwo"
    elif object_type == 9:
        return object_name + ".apl"
    else:
        return object_name + ".grp"


dword_10DCD488 = [
    (0, 0), (1, 0), (1, 1), (0, 2), (0, 2), (1, 2), (1, 3), (2, 4),
    (0, 6), (0, 6), (0, 6), (1, 6), (1, 7), (1, 8), (1, 9), (0, 10),
    (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (1, 10), (1, 11), (2, 12),
    (2, 14), (2, 16), (0, 18), (0, 18), (4, 18), (0, 22), (0, 22), (0, 22),
    (1, 22), (1, 23), (2, 24), (1, 26), (2, 27), (1, 29), (0, 30), (0, 30),
    (0, 30), (1, 30), (1, 31), (1, 32), (1, 33), (0, 34), (0, 34), (0, 34),
    (0, 34), (0, 34), (0, 34), (0, 34), (0, 34), (1, 34), (0, 35), (0, 35),
    (0, 35), (0, 35), (2, 35), (1, 37), (2, 38), (1, 40), (2, 41), (2, 43),
    (1, 45), (2, 46), (1, 48), (3, 49), (0, 52), (0, 52), (0, 52), (0, 52),
    (3, 52), (2, 55), (1, 57), (2, 58), (0, 60), (0, 60), (3, 60), (2, 63),
    (2, 65), (2, 67), (2, 69), (2, 71), (2, 73), (2, 75), (2, 77), (2, 79),
    (2, 81), (2, 83), (2, 85), (2, 87), (2, 89), (2, 91), (2, 93), (2, 95),
    (2, 97), (2, 99), (2, 101), (2, 103), (2, 105), (2, 107), (2, 109), (2, 111),
    (2, 113), (2, 115), (2, 117), (2, 119), (2, 121), (2, 123), (2, 125), (2, 127),
    (2, 129), (2, 131), (2, 133), (2, 135), (2, 137), (2, 139), (2, 141), (2, 143),
    (2, 145), (2, 147), (2, 149), (2, 151), (2, 153), (2, 155), (2, 157), (2, 159),
    (2, 161), (2, 163), (2, 165), (2, 167), (2, 169), (2, 171), (2, 173), (2, 175),
    (2, 177), (2, 179), (2, 181), (2, 183), (2, 185), (2, 187), (2, 189), (2, 191),
    (2, 193), (2, 195), (2, 197), (2, 199), (2, 201), (2, 203), (2, 205), (2, 207),
    (2, 209), (2, 211), (0, 213), (0, 213), (0, 213), (0, 213), (0, 213), (0, 213),
    (0, 213), (0, 213), (0, 213), (0, 213), (0, 213), (1, 213), (2, 214), (0, 216),
    (0, 216), (1, 216), (1, 217), (1, 218), (1, 219), (1, 220), (0, 221), (2, 221),
    (1, 223), (0, 224), (0, 224), (0, 224), (3, 224), (2, 227), (3, 229), (5, 232),
    (6, 237), (3, 243), (1, 246), (1, 247), (3, 248), (0, 251), (0, 251), (2, 251),
    (3, 253), (2, 256), (3, 258), (2, 261), (0, 263), (4, 263), (4, 267), (4, 271),
    (1, 275), (4, 276), (1, 280), (0, 281), (2, 281), (1, 283), (0, 284), (4, 284),
    (4, 288), (4, 292), (3, 296), (1, 299), (1, 300), (0, 301), (2, 301), (3, 303),
    (2, 306), (1, 308), (2, 309), (0, 311), (5, 311), (0, 316), (0, 316), (0, 316),
    (3, 316), (0, 319), (1, 319), (0, 320), (0, 320), (0, 320), (0, 320), (2, 320),
    (2, 322), (2, 324), (2, 326), (2, 328), (2, 330), (0, 332), (0, 332), (1, 332),
    (0, 333), (0, 333), (2, 333), (0, 335), (0, 335), (0, 335), (4, 335), (0, 339),
    (0, 339), (0, 339), (1, 339), (1, 340), (1, 341), (1, 342), (2, 343), (2, 345),
    (1, 347), (0, 348), (1, 348), (1, 349), (1, 350), (1, 351), (4, 352), (4, 356),
    (2, 360), (2, 362), (0, 364), (1, 364), (0, 365), (1, 365), (0, 366), (1, 366),
    (1, 367), (1, 368), (1, 369), (2, 370), (0, 372), (0, 372), (0, 372), (0, 372),
    (0, 372), (0, 372), (2, 372), (0, 374), (0, 374), (1, 374), (0, 375), (0, 375),
    (0, 375), (1, 375), (1, 376), (0, 377), (0, 377), (0, 377), (0, 377), (0, 377),
    (2, 377), (3, 379), (1, 382), (2, 383), (1, 385), (3, 386), (0, 389), (0, 389),
    (0, 389), (0, 389), (0, 389), (0, 389), (0, 389), (0, 389), (2, 389), (2, 391),
    (0, 393), (1, 393), (1, 394), (2, 395), (2, 397), (2, 399), (0, 401), (0, 401),
    (0, 401), (0, 401), (1, 401), (1, 402), (5, 403), (1, 408), (0, 409), (2, 409),
    (2, 411), (1, 413), (0, 414), (2, 414), (1, 416), (2, 417), (1, 419), (1, 420),
    (2, 421), (0, 423), (0, 423), (0, 423), (1, 423), (0, 424), (0, 424), (2, 424),
    (3, 426), (2, 429), (1, 431), (1, 432), (1, 433), (2, 434), (2, 436), (2, 438),
    (2, 440), (1, 442), (3, 443), (3, 446), (3, 449), (3, 452), (1, 455), (1, 456),
    (1, 457), (1, 458), (1, 459), (0, 460), (1, 460), (1, 461), (2, 462), (1, 464),
    (1, 465), (2, 466), (2, 468), (0, 470), (1, 470), (6, 471), (6, 477), (2, 483),
    (0, 485), (1, 485), (1, 486), (0, 487), (3, 487), (3, 490), (3, 493), (3, 496),
    (0, 499), (1, 499), (0, 500), (0, 500), (0, 500), (0, 500), (0, 500), (0, 500),
    (0, 500), (0, 500), (0, 500), (0, 500), (2, 500), (3, 502), (3, 505), (0, 508),
    (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508),
    (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508),
    (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (0, 508), (3, 508),
    (3, 511), (2, 514), (1, 516), (2, 517), (1, 519), (0, 520), (2, 520), (3, 522),
    (3, 525), (3, 528), (3, 531), (3, 534), (3, 537), (3, 540), (0, 543), (3, 543),
    (3, 546), (3, 549), (0, 552), (2, 552), (0, 554), (0, 554), (1, 554), (1, 555),
    (1, 556), (1, 557), (0, 558), (0, 558), (0, 558), (0, 558), (2, 558), (1, 560),
    (2, 561), (1, 563), (1, 564), (2, 565), (0, 567), (0, 567), (0, 567), (1, 567),
    (1, 568), (1, 569), (1, 570), (0, 571), (0, 571), (0, 571), (0, 571), (0, 571),
    (0, 571), (2, 571), (0, 573), (0, 573), (0, 573), (1, 573), (3, 574), (3, 577),
    (3, 580), (0, 583), (0, 583), (1, 583), (0, 584), (1, 584), (1, 585), (1, 586),
    (1, 587), (1, 588), (1, 589), (0, 590), (0, 590), (0, 590), (3, 590), (3, 593),
    (0, 596), (0, 596), (0, 596), (1, 596), (1, 597), (1, 598), (1, 599), (0, 600),
    (0, 600), (0, 600), (0, 600), (0, 600), (0, 600), (0, 600), (1, 600), (1, 601),
    (0, 602), (3, 602), (0, 605), (2, 605), (1, 607), (1, 608), (2, 609), (3, 611),
    (2, 614), (0, 616), (2, 616), (1, 618), (0, 619), (3, 619), (1, 622), (2, 623),
    (2, 625), (1, 627), (0, 628), (1, 628), (1, 629), (2, 630), (1, 632), (1, 633),
    (2, 634), (0, 636), (2, 636), (0, 638), (1, 638), (1, 639), (2, 640), (2, 642),
    (0, 644), (0, 644), (0, 644), (1, 644), (1, 645), (1, 646), (1, 647), (1, 648),
    (1, 649), (2, 650), (1, 652), (1, 653), (2, 654), (2, 656), (0, 658), (1, 658),
    (1, 659), (1, 660), (1, 661), (1, 662), (2, 663), (0, 665), (1, 665), (1, 666),
    (2, 667), (2, 669), (0, 671), (2, 671), (0, 673), (1, 673), (1, 674), (1, 675),
    (1, 676), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677), (0, 677),
    (0, 677), (0, 677), (0, 677), (0, 677), (3, 677), (2, 680), (3, 682), (6, 685),
    (6, 691), (1, 697), (0, 698), (0, 698), (0, 698), (0, 698), (0, 698), (0, 698),
    (2, 698), (0, 700), (0, 700), (0, 700), (1, 700), (0, 701), (0, 701), (0, 701),
    (0, 701), (0, 701), (0, 701), (2, 701), (2, 703), (1, 705), (1, 706), (0, 707),
    (0, 707), (0, 707), (2, 707), (3, 709), (0, 712), (0, 712), (3, 712), (0, 715),
    (0, 715), (3, 715), (3, 718), (2, 721)
]


def dump(data):
    return ' '.join([hex(int(x)) for x in data])


def load_buffer(file_name):
    with open(file_name, 'r') as file:
        buffer = file.read()
    buffer = buffer.replace('\n', ' ').strip()
    int_buffer = [int(x, 0x10) for x in buffer.split(' ')]
    return bytes(int_buffer)


def write_json(file, json_obj):
    # with open(file_name, 'w') as file:
    json.dump(json_obj, file, indent=4)


def extract_string(buffer, start_index):
    ch = buffer[start_index: start_index + 2].decode('utf16')
    output = ''
    while ch and ch != '\0':
        output += ch
        start_index += 2
        ch = buffer[start_index: start_index + 2].decode('utf16')
    return output


def update_glbsym_types():
    if glb_types:
        for glb_sym in glb_symbol:
            if glb_sym.type_id & 0x8000 > 0:
                index = glb_sym.type_id & 0x3fff
                if len(glb_types) > index:
                    glb_sym.type_name = glb_types[index].name


def get_type_name(type_id):
    global glb_types
    if type_id == 0:
        return 'undef'
    elif type_id > 0x8000:
        if len(glb_types) > type_id - 0x8000:
            return glb_types[type_id - 0x8000].name
        else:
            return "[{}]".format(hex(type_id))
    else:
        return g_types.get(type_id) or "[{}]".format(hex(type_id))


class ConstRef(object):
    def __init__(self, name, m_4, type_id):
        self.name = name
        self.m_4 = m_4
        self.type_id = type_id
        self.type_name = get_type_name(self.type_id)

    def __str__(self):
        return "{}:{}".format(self.name, self.type_name)


class LookupItem(object):
    def __init__(self, init_buffer, const_, local_types=None):
        # m_4 is the size of array if 0xFFFF (-1) means no array otherwise array
        self.m_0, self.m_4, m_8, val_pos, self.m_10, self.type_id = struct.unpack("<IIIIHH", init_buffer)
        self.name = const_.get_string(m_8)
        self.value = val_pos
        if g_types.get(self.type_id):
            self.type_name = g_types.get(self.type_id)
        else:
            if local_types and self.type_id > 0x8000:
                ty_id = self.type_id - 0x8000
                # print(ty_id)
                # print(local_types[ty_id])
                self.type_name = local_types[ty_id].name or hex(self.type_id)
            else:
                self.type_name = "[{}]".format(hex(self.type_id))
        # self.type_name = g_types.get(self.type_id) or hex(self.type_id)
        if self.m_4 != 0xFFFF and self.m_10 == 0x2d00:
            self.is_array = True
            self.array_dim = const_.get_byte(self.m_4)

            self.type_name += "[{}]".format(", ".join([""]*(self.array_dim)))

    def update_value(self, const_):
        if self.type_id == 0x5:
            self.value = const_.get_decimal(self.value)
        elif self.type_id == 0x6:
            if self.value > 0x80000000:
                self.value = self.value - 0x80000000
            self.value = '"{}"'.format(const_.get_string(self.value))
        elif self.type_id == 0x7:
            self.value = "FALSE" if self.value & 0xFFFF == 0 else "TRUE"
        elif self.type_id == 0x4:
            self.value = const_.get_double(self.value)
        elif self.type_id == 0x14:
            self.value = const_.get_long(self.value)
        else:
            if self.type_id > 0x8000:
                typ_id = self.type_id - 0x8000
                if glb_types[typ_id].m_10 == 0x1540:
                    typ_id2 = glb_types[typ_id].value
                    typ_id3 = glb_symbol[typ_id2].value
                    if typ_id3 in range(0x4000, 0x4999):
                        enm = enum_main.get(typ_id3)
                        if enm and enm.get(self.value & 0xFFFF):
                            self.value = "{}!".format(enm.get(self.value & 0xFFFF).name)
                # print("type for id1: ")
                # print(glb_types[typ_id].__dict__())
                else:
                    # typ_id2 = glb_types[typ_id].value
                    self.value = glb_types[typ_id].name

                # print("glb symbol for id1: ")
                # print(glb_symbol[typ_id])

                # print("type for id2: ")
                # print(glb_types[typ_id2].__dict__())
                # print("glb symbol for id2: ")
                # print(glb_symbol[typ_id2])

    def __dict__(self):
        ret = dict()
        ret["name"] = self.name
        ret["m_0"] = hex(self.m_0)
        ret["m_4"] = hex(self.m_4)
        ret["value"] = str(self.value)
        ret["m_10"] = hex(self.m_10)
        ret["type_id"] = hex(self.type_id)
        ret["type"] = self.type_name
        return ret


class Lookup(object):
    def __init__(self, file, local_types=None):
        self._index = 0
        self.header = dump(file.read(0x6))
        self.const_ = ConstData(file)
        item_buffer_size = struct.unpack("<H", file.read(0x2))[0]
        item_buffer = file.read(item_buffer_size)
        self.items = list()
        index = 0
        while index < len(item_buffer):
            self.items.append(LookupItem(item_buffer[index: index + 0x14], self.const_, local_types))
            index += 0x14

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.items):
            self._index += 1
            return self.items[self._index - 1]
        raise StopIteration

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, val):
        self.items[key] = val

    def __dict__(self):
        ret = dict()
        ret["header"] = self.header
        ret["items"] = [item.__dict__() for item in self.items]
        return ret

    def update_items_value(self, const_):
        for item in self.items:
            item.update_value(const_)


class EventInfo(object):
    def __init__(self, init_buffer):
        self._id, self.index, self.parent_id = struct.unpack("<HHH", init_buffer)


class Events(object):
    def __init__(self, parent):
        self.parent = parent
        self._events = list()

    def add_event(self, init_buffer):
        self._events.append(EventInfo(init_buffer))

    def get_event_name(self, _id):
        for ev in self._events:
            if ev._id == _id:
                parent_name = get_type_name(ev.parent_id)
                return "{}::{}".format(parent_name, self.parent.ref_func.items[ev.index].name)
                # if ev.parent_id > 0x8000:
                #     parent_name = glb_types[parent_id].name
                # if parent_name != "":
                #
                # else:
                #     return "{{{}}}::{}".format(ev.parent_id, self.parent.ref_func.items[ev.index].name)
        raise Exception("event id: {} is not register in event table".format(_id))


class GlobalSym(object):
    def __init__(self, init_buffer, const_):
        m_0, self.m_4, self.type_id, self.value, self.m_a = struct.unpack("<IHHHH", init_buffer)
        self.name = const_.get_string(m_0)
        self.type_name = g_types.get(self.type_id) or 'type_' + hex(self.type_id)

    def __str__(self):
        return "name: {}, m_4: {}, type_id: {}, value: {}, m_a: {}".format(self.name, hex(self.m_4),
                                                                           hex(self.type_id), hex(self.value),
                                                                           hex(self.m_a))

    def __dict__(self):
        ret = dict()
        ret["name"] = self.name
        ret["m_4"] = hex(self.m_4)
        ret["type_id"] = hex(self.type_id)
        ret["value"] = hex(self.value)
        ret["m_a"] = hex(self.m_a)
        return ret


class StmtParamInfo(object):
    def __init__(self, start, end):
        self.start_pos = start
        self.end_pos = end


class StmtInfo(object):
    def __init__(self, loc, const_):
        self.m_0, self.m_1, m_1_page_id, self.select_stmt_loc, select_stmt_page_id, \
        self.m_3, _, sql_params_loc, _, self.m_5, _, \
        sql_string_loc, page_id, self.m_7, _, self.m_8, _, \
        self.m_9, parameter_count, self.m_11, \
        m_12, self.m_13 = struct.unpack("IHHHHHHHHHHHHHHHHIIIII", const_.buff_1[loc: loc + 0x38])
        if page_id > 0x8000:
            page_id = page_id - 0x8000
            sql_string_loc = (page_id * 0x10000) + sql_string_loc
        if select_stmt_page_id > 0x8000:
            select_stmt_page_id = select_stmt_page_id - 0x8000
            self.select_stmt_loc = (select_stmt_page_id * 0x10000) + self.select_stmt_loc
        if m_1_page_id > 0x8000:
            m_1_page_id = m_1_page_id - 0x8000
            self.m_1 = (m_1_page_id * 0x10000) + self.m_1
        self.creation_date = datetime.utcfromtimestamp(m_12)
        self.params = list()
        if sql_string_loc != 0xffff:
            self.sql_string = const_.get_string(sql_string_loc)
        else:
            self.sql_string = ''
        if sql_params_loc != 0xffff:
            for item in const_.data_locs:
                if sql_params_loc == item["loc"] and item["type"] == 0x1:
                    for _ in range(parameter_count):
                        start = const_.get_short(sql_params_loc)
                        sql_params_loc += 2
                        end = const_.get_short(sql_params_loc)
                        sql_params_loc += 2
                        self.params.append(StmtParamInfo(start, end))


class ConstData(object):
    def __init__(self, file, buffer_1=b'', buffer_2=b''):
        if file:
            length1, length2 = struct.unpack("<II", file.read(8))
            self.buff_1 = file.read(length1) if length1 else b''
            self.buff_2 = file.read(length2) if length2 else b''
            # self._map = list()
            # index = 0
            # while index < len(self.buff_2):
            #     self._map.append(struct.unpack("<IHH", self.buff_2[index: index + 8]))
            #     index += 8
        else:
            self.buff_1 = buffer_1
            self.buff_2 = buffer_2
        self.data_locs = []
        index = 0
        if self.buff_2:
            while index < len(self.buff_2):
                item = dict()
                item["loc"], item["type"], item["count"] = struct.unpack("<IHH", self.buff_2[index: index + 8])
                index += 8
                self.data_locs.append(item)

    def data_at(self, loc):
        for item in self.data_locs:
            if item["loc"] == loc and item["type"] == 9:
                return StmtInfo(loc, self)
        # cannot find element add it manually
        # return StmtInfo(loc, self)

    def get_bytes(self, start, end):
        return self.buff_1[start:end]

    def get_const_ref(self, loc):
        name_loc, m_4, type_id = struct.unpack("<IHH", self.buff_1[loc: loc + 8])
        name = self.get_string(name_loc)
        return ConstRef(name, m_4, type_id)

    def get_byte(self, loc):
        return struct.unpack("<B", self.buff_1[loc: loc + 1])[0]

    def get_uint(self, loc):
        return struct.unpack("<I", self.buff_1[loc: loc + 4])[0]

    def get_int(self, loc):
        return struct.unpack("<i", self.buff_1[loc: loc + 4])[0]

    def get_short(self, loc):
        return struct.unpack("<h", self.buff_1[loc: loc + 2])[0]

    def get_ushort(self, loc):
        return struct.unpack("<H", self.buff_1[loc: loc + 2])[0]

    def get_string(self, loc):
        return extract_string(self.buff_1, loc)

    def get_longlong(self, loc):
        return struct.unpack("<q", self.buff_1[loc: loc + 8])[0]

    def get_double(self, loc):
        if loc + 8 >= len(self.buff_1):
            return "ERROR"
        return struct.unpack("<d", self.buff_1[loc: loc + 8])[0]

    def get_decimal(self, loc):
        buffer = self.buff_1[loc: loc + 0x10]
        neg = buffer[0xe] != 0
        power = buffer[0xf]
        number_buff = buffer[:0xe] + b"\x00\x00"
        n1, n2 = struct.unpack("<QQ", number_buff)
        number = ((n2 << 0x40) | n1) / (10 ** power)
        if neg:
            number = number * -1
        return number
        # print(dump(self.buff_1[loc: loc + 0x10]))
        # return 0

    def get_long(self, loc):
        return struct.unpack("<q", self.buff_1[loc: loc + 8])[0]


class ParamInfo(object):
    def __init__(self, init_buffer=None, m_28_buffer=None, **kwargs):
        if init_buffer and m_28_buffer:
            self.name_index, self.m_4, self.type_id, self.m_a = struct.unpack("<IiHH", init_buffer)
            self.name = m_28_buffer.get_string(self.name_index)
            # if g_types.get(self.type_id):
            #     self.type_name = g_types.get(self.type_id)
            self.type_name = get_type_name(self.type_id)
            # else:
            #     self.type_name = 'undef'
            # self.type_name = g_types.get(self.type_id) or 'undef'
        else:
            self.name = kwargs.get('name') or ''
            if not self.name:
                raise Exception("cannot initialize parameter without name")
            self.type_id = kwargs.get('type_id') or 0
            self.type_name = get_type_name(self.type_id)
            self.m_4 = kwargs.get('m_4') or 0
            self.m_a = kwargs.get('m_a') or 0

    def __dict__(self):
        ret = dict()
        ret["name"] = self.name
        ret["m_4"] = hex(self.m_4)
        ret["type"] = "{} - {}".format(hex(self.type_id), self.type_name)
        ret["m_a"] = hex(self.m_a)
        return ret

    def __str__(self):
        return 'name: "{}",  m_4: {},  type(id-name): {} - "{}",  m_a: {}'.format(self.name,
                                                                                  self.m_4,
                                                                                  hex(self.type_id),
                                                                                  self.type_name, self.m_a)


class FuncInfo(object):
    def __init__(self, init_buffer=None, **kwargs):
        global const_28
        global const_30
        self._routine = None
        if init_buffer and const_28 and const_30:
            name_index, \
            self.m_4, \
            buff_30_index, \
            self.m_c, \
            self.m_10, \
            self.m_14, \
            self.index, \
            self.m_18, \
            self.m_1a, \
            self.return_type_id, \
            parameter_count, \
            self.m_1f, \
            self.m_20, \
            self.m_22, \
            self.m_24, \
            self.m_28, \
            self.m_2c, \
            self.m_2e, = struct.unpack("<IIIIIHHHHHBBHHIIHH", init_buffer)
            self.name = const_28.get_string(name_index)
            self.delegate_name = const_28.get_string(self.m_c)
            self.footprint = const_28.get_string(self.m_4)
            index = buff_30_index
            self.parameters = list()
            for x in range(parameter_count):
                self.parameters.append(ParamInfo(const_30.get_bytes(index, index + 0xc), const_28))
                index += 0xc
        else:
            self.name = kwargs.get('name') or ''
            if not self.name:
                raise Exception('cannot initialize function without name')
            self.footprint = kwargs.get('footprint') or ''
            self.delegate_name = kwargs.get('delegate_name') or ''
            self.parameters = kwargs.get('parameters') or []
            self.m_10 = kwargs.get('m_10') or 0
            self.m_14 = kwargs.get('m_14') or 0
            self.index = kwargs.get('m_16') or 0
            self.m_18 = kwargs.get('m_18') or 0
            self.m_1a = kwargs.get('m_1a') or 0
            self.return_type_id = kwargs.get('return_type_id') or 0
            self.m_1f = kwargs.get('m_1f') or 0
            self.m_20 = kwargs.get('m_20') or 0
            self.m_22 = kwargs.get('m_22') or 0
            self.m_24 = kwargs.get('m_24') or 0
            self.m_28 = kwargs.get('m_28') or 0
            self.m_2c = kwargs.get('m_2c') or 0
            self.m_2e = kwargs.get('m_2e') or 0
        self.return_type = get_type_name(self.return_type_id)
        access = (self.m_1f >> 4) & 0x3
        if access == 1:
            self.access = "private"
        elif access == 2:
            self.access = "proteced"
        else:
            self.access = "public"
        self.is_event = (self.m_1f & 0x1) == 1

    @property
    def routine(self):
        return self._routine

    @routine.setter
    def routine(self, val):
        self._routine = val
        if val:
            val.func_info = self

    def __dict__(self):
        ret = dict()
        ret["access"] = self.access
        ret["event"] = self.is_event
        ret["name"] = self.name
        ret["footprint"] = self.footprint
        ret["delegate"] = self.delegate_name
        ret["m_4"] = hex(self.m_4)
        ret["m_c"] = hex(self.m_c)
        ret["m_10"] = hex(self.m_10)
        ret["m_14"] = hex(self.m_14)
        ret["index"] = hex(self.index)
        ret["m_18"] = hex(self.m_18)
        ret["m_1a"] = hex(self.m_1a)
        ret["m_1f"] = hex(self.m_1f)
        ret["m_20"] = hex(self.m_20)
        ret["m_22"] = hex(self.m_22)
        ret["m_24"] = hex(self.m_24)
        ret["m_28"] = hex(self.m_28)
        ret["m_2c"] = hex(self.m_2c)
        ret["m_2e"] = hex(self.m_2e)
        ret["return type"] = "{} - {}".format(hex(self.return_type_id), self.return_type)
        ret["parameters"] = [par.__dict__() for par in self.parameters]
        return ret

    def __str__(self):
        lines = list()
        lines.append('access = {}'.format(self.access))
        lines.append('name = {}'.format(self.name))
        lines.append('footprint = {}'.format(self.footprint))
        lines.append('delegate = {}'.format(self.delegate_name))
        lines.append('m_4 = {}'.format(hex(self.m_4)))
        lines.append('m_c = {}'.format(hex(self.m_c)))
        lines.append('m_10 = {}'.format(hex(self.m_10)))
        lines.append('m_14 = {}'.format(hex(self.m_14)))
        lines.append('index = {}'.format(hex(self.index)))
        lines.append('m_18 = {}'.format(hex(self.m_18)))
        lines.append('m_1a = {}'.format(hex(self.m_1a)))
        lines.append('return type(id-name) = {} - {}'.format(hex(self.return_type_id), self.return_type))

        lines.append('parameters: ')
        for par in self.parameters:
            lines.append('   {}'.format(str(par)))
        lines.append('m_1f = {}'.format(hex(self.m_1f)))
        lines.append('m_20 = {}'.format(hex(self.m_20)))
        lines.append('m_22 = {}'.format(hex(self.m_22)))
        lines.append('m_24 = {}'.format(hex(self.m_24)))
        lines.append('m_28 = {}'.format(hex(self.m_28)))
        lines.append('m_2c = {}'.format(hex(self.m_2c)))
        lines.append('m_2e = {}'.format(hex(self.m_2e)))
        return '\n'.join(lines)


class ClassSlot(object):
    def __init__(self, buffer):
        global glb_types
        self.m_0, \
        type_id, \
        self.enum_size, \
        self.m_6, \
        self.m_8, \
        self.m_a, \
        self.m_c, \
        self.m_e = struct.unpack("<HHHHHHHH", buffer)
        self.type_id = type_id & 0x3fff
        self.name = glb_types[self.type_id].name


class DefSlot(object):
    def __init__(self, buffer):
        global glb_types
        type_id, \
        parent_id, \
        self.func_count, \
        self.l_func_count, \
        self.event_count, \
        self.m_a, \
        self.m_c, \
        self.m_e, \
        self.m_10, \
        self.m_12, \
        self.m_14, \
        self.m_16, \
        self.m_18, \
        self.m_1a, \
        self.m_1c, \
        self.m_1e = struct.unpack("<HHHHHHHHHHHHHHHH", buffer)
        self.class_id = type_id & 0x3fff
        self.parent_id = None if parent_id == 0xc000 else parent_id & 0x3fff
        self.class_name = glb_types[self.class_id].name
        if self.parent_id:
            self.parent_name = glb_types[self.parent_id].name
        else:
            self.parent_name = ''


from pbd.pcode import g_codes


class PCode(object):
    def __init__(self, id, args):
        self.id = id
        self.name = g_codes[id]["name"]
        self.args = args
        self.func = g_codes[id].get("func")

    def __repr__(self):
        return '<PCode  {}>'.format(self.name)


class LineCode(object):
    def __init__(self, number, code_loc, code_buffer):
        self._index = 0
        self.number = number
        self.code_loc = code_loc
        self.codes = list()
        index = 0
        while index < len(code_buffer):
            code_id = struct.unpack("<H", code_buffer[index: index + 2])[0]
            index += 2
            args = list()
            arg_index = 0
            while arg_index < g_codes[code_id]["arg_num"]:
                args.append(struct.unpack("<H", code_buffer[index: index + 2])[0])
                index += 2
                arg_index += 1
            self.codes.append(PCode(code_id, args))

    def __repr__(self):
        return '<LineCode  {0}>'.format(self.number)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.codes):
            self._index += 1
            return self.codes[self._index - 1]
        raise StopIteration

    def __len__(self):
        return len(self.codes)


class Routine(object):
    def __init__(self, file, id1, id2, parent_class):
        global glb_types
        self.id_1 = id1
        self.id_2 = id2
        self.func_info = None
        # self.glb_vars = parent.glb_vars
        # self.glb_const = parent.glb_const
        # self.types = parent.types
        self.parent = parent_class
        self.group_name = parent_class.group_name
        # self.ref_funcs = parent.ref_func.items
        code_len, line_len, self.unk_len = struct.unpack("<HHH", file.read(0x6))
        code_buffer = file.read(code_len) if code_len > 0 else b''
        lines = list()
        for _ in range(line_len):
            lines.append(file.read(4))

        self.lines = list()
        self.vars = list()
        index = 0
        while index < line_len:
            line_number, data_offset = struct.unpack("<HH", lines[index])
            if index == 0 and data_offset != 0:
                data_offset = 0
            if index + 1 < line_len:
                _, data_offset_2 = struct.unpack("<HH", lines[index + 1])
                line_code = code_buffer[data_offset: data_offset_2]
            else:
                line_code = code_buffer[data_offset:]
            self.lines.append(LineCode(line_number, data_offset, line_code))
            index += 1

        self.vars = Lookup(file, glb_types)
        self.const_ = ConstData(file)
        self.vars.update_items_value(self.const_)
        # for var in self.vars:
        #     if var.type_id == 0x5:
        #         var.value = self.const_.get_decimal(var.value)
        #     elif var.type_id == 0x6:
        #         var.value = '"{}"'.format(self.const_.get_string(var.value))
        #     elif var.type_id == 0x4:
        #         var.value = self.const_.get_double(var.value)
        #     elif var.type_id == 0x14:
        #         var.value = self.const_.get_long(var.value)
        self.stack = list()

    def inspect_line(self, line_index):
        for line in self.lines:
            if line.number == line_index:
                print("Line #: {}        Code Loc: {}".format(line.number, line.code_loc))
                for code in line.codes:
                    print("{}: {}".format(code.name, code.args))

    def convert_to_c(self, lines):
        index = 0
        while index < len(lines):
            line = lines[index]
            mat = re.match(r'^(\s*)([0-9.]+):\s+if not\s*(.+)goto line ([0-9.]+)', line)
            if mat and index + 1 < len(lines):
                lines[index] = "{}{}:  if {} {{".format(mat.groups()[0], mat.groups()[1], mat.groups()[2].strip())
                index2 = index + 1
                while index2 < len(lines):
                    next_line = lines[index2]
                    mat_2 = re.match(r'^\s*([0-9.]+):\s+', next_line)
                    if mat_2 and mat_2.groups()[0] == mat.groups()[3]:
                        # if the previous line is goto loc this means 
                        # this is if else statement
                        prev_line = lines[index2 - 1]
                        mat_3 = re.match(r'^\s*([0-9.]+):\s+goto line\s+([0-9.]+)', prev_line)
                        if mat_3 and float(mat_3.groups()[0]) < float(mat_3.groups()[1]):
                            lines[index2 - 1] = mat.groups()[0] + "} else {"
                            index3 = index2
                            while index3 < len(lines):
                                else_line = lines[index3]
                                mat_4 = re.match(r'^\s*([0-9.]+):.*', else_line)
                                if mat_4 and mat_4.groups()[0] == mat_3.groups()[1]:
                                    lines.insert(index3, "{}{}:  }}".format(mat.groups()[0], mat_3.groups()[1]))
                                    break
                                else:
                                    lines[index3] = "    " + else_line
                                index3 += 1
                        else:
                            lines.insert(index2, "{}{}:  }}".format(mat.groups()[0], mat.groups()[3]))
                        break
                    else:
                        lines[index2] = "    " + next_line
                    index2 += 1
            index += 1

            # detect while loop
        index = 0
        while index < len(lines):
            line = lines[index]
            # first condition goto line lower than current line number
            mat = re.match(r'^\s*([0-9.]+):\s+goto line\s+([0-9.]+)', line)
            if mat and float(mat.groups()[0]) > float(mat.groups()[1]):
                # second condition the next line is }
                if index + 1 < len(lines):
                    next_line = lines[index + 1]
                    mat_2 = re.match(r'^\s*([0-9.]+):\s+}', next_line)
                    if mat_2:
                        # 3rd condition the goto line is point to if stmt
                        index2 = 0
                        while index2 < len(lines):
                            if_line = lines[index2]
                            mat_3 = re.match(r'^(\s*)([0-9.]+):\s+if(.*)', if_line)
                            if mat_3 and mat_3.groups()[1] == mat.groups()[1]:
                                # change the line at index2 to while instead of if
                                lines[index2] = "{}{}:  while{}".format(mat_3.groups()[0], mat_3.groups()[1],
                                                                        mat_3.groups()[2])
                                # remove goto line # line
                                lines.remove(line)
                                break
                            index2 += 1
            index += 1

        # detect for loop
        index = 0
        while index < len(lines):
            line = lines[index]
            # first condition detect goto line #.7
            mat = re.match(r'^\s*([0-9.]+):\s+goto line ([0-9]+\.7)', line)
            if not mat:
                index += 1
                continue
            prev_line = lines[index - 1]
            mat = re.match(r'^(\s*)([0-9.]+):\s+(\w+)\s*=\s*([0-9]+)', prev_line)
            if not mat:
                index += 1
                continue
            space, line_number, identifier, value = mat.groups()
            if index + 2 >= len(lines):
                continue
            next_line = lines[index + 1]
            last_line = lines[index + 2]
            mat = re.match(r'^\s*([0-9.]+):\s+(\w+)\s*\+\+', next_line)
            if not mat:
                index += 1
                continue
            if mat.groups()[1] != identifier:
                index += 1
                continue
            continue_line_number = mat.groups()[0]
            mat = re.match(r'^\s*[0-9.]+:\s+if\s*(.*){', last_line)
            if not mat:
                index += 1
                continue
            condition = mat.groups()[0].strip('() ')
            lines[index - 1] = "{0}{1}:  for({2}={3}; {4}; {2}++) {{".format(space, line_number, identifier, value,
                                                                             condition)
            lines.remove(line)
            lines.remove(next_line)
            lines.remove(last_line)
            # replace continue
            index2 = index
            while index2 < len(lines):
                mat = re.match(r'^(\s*[0-9.]+):\s+goto line\s+([0-9.]+)', lines[index2])
                if mat and mat.groups()[1] == continue_line_number:
                    lines[index2] = "{}:  continue".format(mat.groups()[0])
                    break
                index2 += 1

        # removing non-use line number 
        # get all goto lines

        important_lines = list()
        for line in lines:
            mat = re.match(r'^\s*([0-9.]+):\s+goto line\s+([0-9.]+)', line)
            if mat:
                important_lines.append(mat.groups()[1])
        index = 0
        while index < len(lines):
            line = lines[index]
            mat = re.match(r'^(\s*)([0-9.]+):\s+(.*)$', line)
            if mat and not mat.groups()[1] in important_lines:
                lines[index] = "{}{}".format(mat.groups()[0], mat.groups()[2])
            index += 1
        return lines

    def debug(self):
        global glb_symbol
        expr = list()
        expr.append("define:")
        if self.func_info:
            func_info = self.func_info
            expr.append("    {} {} {} {} ({})".format(func_info.access, "event" if func_info.is_event else "",
                                                      func_info.return_type,
                                                      func_info.name,
                                                      ", ".join([param.name for param in func_info.parameters])))
        expr.append("")
        # expr.append("global:")
        # for var in glb_symbol:
        #     expr.append('    declare {} as {} = {}'.format(var.name, var.type_name, hex(var.value)))
        # expr.append("")
        expr.append("local:")
        for var in self.vars:
            expr.append('    declare {} as {} = {}'.format(var.name, var.type_name, var.value))
        expr.append("")
        expr.append("start:")
        for line in self.lines:
            expr.append("    line {}:".format(line.number))
            for code in line.codes:
                expr.append("        {} ({})".format(code.name, ", ".join([str(x) for x in code.args])))
        return expr

    def analyse(self, format="raw"):
        global glb_symbol
        expr = list()
        expr.append("define:")
        if self.func_info:
            func_info = self.func_info
            expr.append("    {} {} {} {} ({})".format(func_info.access, "event" if func_info.is_event else "",
                                                      func_info.return_type,
                                                      func_info.name,
                                                      ", ".join([param.name for param in func_info.parameters])))
        expr.append("")
        # expr.append("global:")
        # for var in glb_symbol:
        #     expr.append('    declare {} as {} = {}'.format(var.name, var.type_name, hex(var.value)))
        # expr.append("")
        expr.append("local:")
        for var in self.vars:
            expr.append('    declare {} as {} = {}'.format(var.name, var.type_name, var.value))
        expr.append("")
        expr.append("start:")
        for line in self.lines:
            line_expr = list()
            code_pos = 0
            next_stmt = 0
            for code in line.codes:
                if not code.func:
                    with open('error.txt', 'w') as output_file:
                        output_file.write('\n'.join(expr))
                        output_file.write('\ncurrent line:\n')
                        output_file.write(' '.join(line_expr))
                        output_file.write('\nstack:\n')
                        output_file.write('\n'.join(self.stack))
                    raise Exception(
                        "Error at line: {0},  code: {1},  args: {2}".format(line.number, code.name, code.args))
                try:
                    ret = code.func(self.stack, code, self)
                except Exception as ex:
                    with open('error.txt', 'w') as output_file:
                        output_file.write('\n'.join(expr))
                        output_file.write('\ncurrent line: \n')
                        output_file.write(' '.join(line_expr))
                        output_file.write('\nstack:\n')
                        output_file.write('\n'.join(self.stack))
                    print("Error at line: {0},  code: {1},  args: {2}".format(line.number, code.name, code.args))
                    raise ex
                if ret:
                    # to register the start of the statement assume first stmt start pos = 0
                    # then save location in next_stmt to use in next append
                    if len(line_expr) == 0:
                        line_expr.append("{}:  {}".format(line.number, ret))
                        next_stmt = code_pos + 1
                    else:
                        line_expr.append("{}.{}:  {}".format(line.number, next_stmt, ret))
                        next_stmt = code_pos + 1
                code_pos += 1
            # try to solve if expressoin problem
            # index = 0
            # while index < len(expr):
            # mat = re.match(r"")
            if not line_expr:
                expr.append("{}:".format(line.number))
            for exp in line_expr:
                expr.append(exp)
            # expr.append("{}:  {}".format(line.number, '\n'.join(line_expr)))
        # index = 0
        # while index < len(expr):
        #     index += 1
        if format.lower() == "raw":
            if self.stack:
                expr.append("stack:")
                for stk in self.stack:
                    expr.append("    " + stk)
            return expr
        elif format.lower() == "c":
            return self.convert_to_c(expr)


class GroupClass(object):
    def __init__(self, file, class_slot: ClassSlot, group_name):
        self.slot = class_slot
        self.def_slot: DefSlot
        self.enums = list()
        self.routines = list()
        self.events = Events(self)
        self.m_48 = list()
        self.ref_func = None
        self.vars = None
        # self.glb_vars = parent.glb_symbol
        # self.glb_const = parent.glb_const
        # self.types = parent.types
        self.group_name = group_name
        self.m_54 = list()
        self.m_50 = list()
        self.functions = list()

        flag = class_slot.m_0
        if flag & 0x1:
            flag = flag >> 1
            flag = flag & 7
            if flag:
                if flag == 1 and class_slot.enum_size != 0:
                    if not glb_enums:
                        raise Exception("enum data not found")
                    for _ in range(class_slot.enum_size):
                        name_pos, value, m_6 = struct.unpack("<IHH", file.read(0x8))
                        self.enums.append(EnumInfo(glb_enums.const_.get_string(name_pos), value, m_6))
            else:
                self.def_slot = glb_def_slot.pop(0)
                self.read_routines(file)
                for _ in range(self.def_slot.m_18):
                    self.events.add_event(file.read(0x6))
                for _ in range(self.def_slot.m_16):
                    self.m_48.append(dump(file.read(0x4)))

                self.ref_func = Lookup(file)
                self.properties = Lookup(file, glb_types)
                self.properties.update_items_value(glb_const)
                for _ in range(self.def_slot.m_1c):
                    self.m_54.append(dump(file.read(0x8)))
                for _ in range(self.def_slot.m_1a):
                    self.m_50.append(dump(file.read(0x10)))
                for _ in range(self.def_slot.func_count):
                    temp = FuncInfo(file.read(0x30))
                    for route in self.routines:
                        if temp.index == route.id_2:
                            temp.routine = route
                    self.functions.append(temp)

    @property
    def name(self):
        return self.slot.name

    def read_routines(self, file):
        length = struct.unpack("<H", file.read(2))[0]
        if length:
            rout_entries = list()
            for _ in range(length):
                rout_entries.append(struct.unpack("<HH", file.read(0x4)))
            for x in range(length):
                self.routines.append(Routine(file, rout_entries[x][0], rout_entries[x][1], self))

    def analyse(self, current_path, _format):
        if hasattr(self, "properties") and self.properties is not None:
            props = [item for item in self.properties.items if item.m_0 == 8]
            if props:
                with open(os.path.join(current_path, "properties.txt"), "w") as file:
                    for item in props:
                        file.write("{} {} = {}\n".format(item.type_name, item.name, item.value))
            controls = [item for item in self.properties.items if item.m_0 != 8 and item.m_10 == 0xd00]
            if controls:
                with open(os.path.join(current_path, "controls.txt"), "w") as file:
                    for item in controls:
                        file.write("{} {} = {}\n".format(item.type_name, item.name, item.value))
            instanceVars = [item for item in self.properties.items if item.m_0 != 8 and item.m_10 != 0xd00]
            if instanceVars:
                with open(os.path.join(current_path, "instance_vars.txt"), "w") as file:
                    for item in instanceVars:
                        file.write("{} {} = {}\n".format(item.type_name, item.name, item.value))
        for func in self.functions:
            lines = None
            lines_debug = None
            try:
                if func.routine is not None:
                    lines_debug = func.routine.debug()
                    lines = func.routine.analyse(_format)
            except Exception as ex:
                print("function name: " + func.name)
                print("function index: " + str(self.functions.index(func)))
                raise ex
            finally:
                if func.routine is not None and lines_debug is not None:
                    with open(os.path.join(current_path, func.name + ".debug"), "w") as file:
                        file.write("\n".join(lines_debug))
            if func.routine is not None and lines is not None:
                with open(os.path.join(current_path, func.name + ".code"), "w") as file:
                    file.write("\n".join(lines))
                if func.routine.stack:
                    print("warning: stack is not empty in file: {}".format(
                        os.path.join(current_path, func.name + ".code")))


glb_symbol = list()
glb_types: Lookup
const_28: ConstData
const_30: ConstData
glb_enums: Lookup
glb_const: ConstData
glb_def_slot = list()


class Group(object):
    def __init__(self, file_name):
        global glb_const
        global glb_symbol
        global glb_types
        global const_28
        global const_30
        global glb_enums
        global glb_def_slot
        glb_symbol = list()
        glb_def_slot = list()
        self.group_name = ''
        file_path = os.path.abspath(file_name)
        file_name = os.path.basename(file_path)
        if file_name.lower().endswith(".fun"):
            self.group_name = file_name.lower()[:-4]
        with open(file_path, 'rb') as file:
            self.h1, \
            self.h2, \
            self.system_class_id, \
            self.h3, self.h4, \
            c_date_id, \
            m_date_id, \
            self.h5 = struct.unpack("<HHHHIIII", file.read(0x18))
            self.create_date = datetime.utcfromtimestamp(c_date_id)
            self.modification_date = datetime.utcfromtimestamp(m_date_id)

            length_1 = struct.unpack("<H", file.read(2))[0]
            buffer_1 = file.read(length_1 * 0xc)
            glb_const = ConstData(file)
            index = 0
            while index < len(buffer_1):
                glb_symbol.append(GlobalSym(buffer_1[index: index + 0xc], glb_const))
                index += 0xc
            temp = Lookup(file)
            if len(temp) > 0:
                self.group_name = temp[0].name
            # read typedescript
            length_1, length_2 = struct.unpack("<HH", file.read(4))
            const_28 = ConstData(file)
            const_30 = ConstData(file)
            glb_types = Lookup(file)
            glb_enums = Lookup(file)
            update_glbsym_types()
            self.class_slots = list()
            for _ in range(length_1):
                self.class_slots.append(ClassSlot(file.read(0x10)))
            for _ in range(length_2):
                glb_def_slot.append(DefSlot(file.read(0x20)))
            self.classes = list()
            for slot_index in range(length_1):
                self.classes.append(GroupClass(file, self.class_slots[slot_index], self.group_name))

    def analyse(self, _format, base_path=None):
        # if not os.path.exists(self.group_name):
        #     os.mkdir(self.group_name)
        if base_path is None:
            base_path = os.getcwd()
        else:
            base_path = os.path.abspath(base_path)
        base_path = os.path.join(base_path, self.group_name)
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        with open(os.path.join(base_path, "global_symbol.txt"), "w") as file:
            for var in glb_symbol:
                file.write("declare {} as {} = {}\n".format(var.name, var.type_name, hex(var.value)))
        with open(os.path.join(base_path, "global_types.json"), "w") as file:
            for var in glb_types:
                write_json(file, var.__dict__())
        if glb_enums is not None and len(glb_enums) > 0:
            with open(os.path.join(base_path, "global_enums.josn"), "w") as file:
                for var in glb_enums:
                    write_json(file, var.__dict__())
                    # file.write("{}\n".format(var.__dict__()))
        for cl in self.classes:
            current_path = os.path.join(base_path, cl.name)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
            cl.analyse(current_path, _format)
