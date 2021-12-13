import struct

from pbd.system_enums import enum_main
from pbd.system_functions import c_40CF
from pbd import definitions


def pb_return_val(stack, pcode, routine):
    ret_val = ''
    if pcode.id == 1:
        if pcode.args[0] == 1:
            ret_val = stack.pop()
        return 'return {}'.format(ret_val)
    else:
        expr_1 = stack.pop()
        return 'return {}'.format(expr_1)


def pb_copy(stack, pcode, routine):
    vals = []
    for _ in range(pcode.args[0]):
        vals.append(stack.pop())
    vals.reverse()
    stack.append("copy({})".format(", ".join(vals)))
    # return "{} = copy({})".format(stack.pop(), ", ".join(vals))


def pb_negate(stack, pcode, routine):
    val = stack.pop()
    stack.append("{} * -1".format(val))
    # if pcode.id in (0x76, 0x77, 0x78, 0x79):
    #     int_val = int(val)
    #     stack.append(str(int_val * -1))
    # elif pcode.id in (0x7a, 0x7b, 0x7c):
    #     float_val = float(val)
    #     stack.append(str(float_val * -1.0))


def pb_div(stack, pcode, routine):
    if len(stack) < 2:
        raise Exception("pb_div need 2 args")
    expr_2 = routine.stack.pop()
    expr_1 = stack.pop()
    stack.append("{} / {}".format(expr_1, expr_2))

def pb_mod(stack, pcode, routine):
    if len(stack) < 2:
        raise Exception("pb_mod need 2 args")
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    stack.append("{} % {}".format(expr_1, expr_2))


def pb_mul(stack, pcode, routine):
    if len(stack) < 2:
        raise Exception("pb_mul need 2 args")
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    stack.append("{} * {}".format(expr_1, expr_2))


def pb_power(stack, pcode, routine):
    if len(stack) < 2:
        raise Exception("pb_power need to args")
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    stack.append("{}^{}".format(expr_1, expr_2))


def pb_add(stack, pcode, routine):
    if len(stack) < 2:
        raise Exception("pb_add need 2 args")
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    stack.append("{} + {}".format(expr_1, expr_2))


def pb_add_assign(stack, pcode, routine):
    right = stack.pop()
    left = stack.pop()
    return "{} += {}".format(left, right)


def pb_sub_assign(stack, pcode, routine):
    right = stack.pop()
    left = stack.pop()
    return "{} -= {}".format(left, right)


def pb_mul_assign(stack, pcode, routine):
    right = stack.pop()
    left = stack.pop()
    return "{} *= {}".format(left, right)


def pb_sub(stack, pcode, routine):
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    stack.append("{} - {}".format(expr_1, expr_2))


def pb_call_func(stack, pcode, routine):
    if pcode.id == 0x13:
        pars = list()
        for i in range(0, pcode.args[1]):
            pars.append(stack.pop())
        pars.reverse()
        # print(pcode.args)
        # print(routine.parent.ref_func.items[pcode.args[0]].name)
        # stack.append("{}()".format(event_main[pcode.args[0]]))
        # if pcode.args[0] == 188:
        #     print(routine.parent.properties.__dict__())
        # print([item.__dict__() for item in routine.parent.ref_func.items])
        # stack.append(routine.parent.ref_func.items[pcode.args[0]].name)
        stack.append("event {}({})".format(routine.parent.events.get_event_name(pcode.args[0]), ", ".join(pars)))
        return
    elif pcode.id == 0x1bc:
        class_type = pcode.args[1] & 0xc000
        class_index = pcode.args[1] & 0x3fff
        if class_type == 0x4000:
            if pcode.args[1] != 0x40CF:
                raise Exception("unknown module no.: {}".format(hex(pcode.args[1])))
            func = c_40CF.get(pcode.args[0])
            if not func:
                raise Exception("unknown function index: {}".format(hex(pcode.args[0])))
            stack.append(func.name)
        elif class_type == 0x8000:
            # print("routine name: ", routine.parent.ref_func.items[pcode.args[0]].name)
            # if routine.types[class_index].name == routine.group_name:
            stack.append(routine.parent.ref_func.items[pcode.args[0]].name)
            # raise Exception("unknown module no.: {}".format(hex(pcode.args[1])))
        else:
            raise Exception("unknown class type and id: {}".format(hex(pcode.args[1])))
        
    elif pcode.id in (0x1bd, 0x1be, 0x1bf, 0x1c0, 0x21c):
        func = stack.pop()
        if type(func) == str:
            # if pcode.args[2] != 0:
            #     raise Exception("arg 3 of the pcode is not equal to 0")
            pars = list()
            for _ in range(pcode.args[1]):
                pars.append(stack.pop())
            pars.reverse()
            stack.append("{}({})".format(func, ", ".join(pars)))
        else:
            if func.parameters:
                pars = list()
                for x in range(len(func.parameters)):
                    pars.append(stack.pop())
                pars.reverse()
                stack.append("{}({})".format(func.name, ", ".join(pars)))
            else:
                stack.append("{}()".format(func.name))
    elif pcode.id in (0x2c, 0x171, 0x14d, 0x14e, 0x21b):  # dot function call
        temp = struct.pack("HH", pcode.args[0], pcode.args[1])
        loc = struct.unpack("I", temp)[0]
        params_count = pcode.args[2]
        func_type = pcode.args[3]  # note if this value = 4 means event if 0 means regular function
        func_id = routine.const_.get_ushort(loc)
        loc += 2
        type_id = routine.const_.get_ushort(loc)
        loc += 2
        name_loc = routine.const_.get_uint(loc)
        func_name = routine.const_.get_string(name_loc)
        params = list()
        while params_count > 0:
            params.append(stack.pop())
            params_count -= 1
        parent = stack.pop()
        params.reverse()
        stack.append("{}.{}({})".format(parent, func_name, ", ".join(params)))
    # elif pcode.id == 0x13:
    #     print(pcode.args)
    #     stack.append("{}()".format(pcode.args[0]))

def pb_in_func(stack, pcode, routine):
    text = stack.pop()
    func_name = ''
    if pcode.id == 0x162:
        func_name = 'BOOL'
    elif pcode.id == 0x163:
        func_name = 'BINARY'
    elif pcode.id == 0x164:
        func_name = 'DATE'
    elif pcode.id == 0x165:
        func_name = 'TIME'
    elif pcode.id == 0x166:
        func_name = 'DateTime'
    elif pcode.id == 0x167:
        func_name = 'CHAR'
    elif pcode.id == 0x168:
        func_name = 'HANDLE'
    elif pcode.id == 0x169:
        func_name = 'ENUM'
    elif pcode.id == 0x18f:
        func_name = 'COS'
    elif pcode.id == 0x19b:
        func_name = 'LOG'
    elif pcode.id == 0x19c:
        func_name = 'LOG10'
    elif pcode.id == 0x1a1:
        func_name = 'SIN'
    elif pcode.id == 0x194:
        func_name = 'ISDATE'
    elif pcode.id == 0x195:
        func_name = 'ISNULL'
    elif pcode.id == 0x196:
        func_name = 'ISNUMBER'
    elif pcode.id == 0x197:
        func_name = 'ISTIME'
    elif pcode.id == 0x198:
        func_name = 'ISVALID'
    elif pcode.id == 0x199:
        func_name = 'LEN'
    elif pcode.id == 0x19a:
        func_name = 'LEN'
    elif pcode.id == 0x19d:
        func_name = 'LOWER'
    elif pcode.id == 0x18d:
        func_name = 'BLOB'
    elif pcode.id == 0x190:
        func_name = 'EXP'
    elif pcode.id == 0x19e:
        func_name = 'PI'
    elif pcode.id in (0x18a, 0x1d8, 0x1d9, 0x18b, 0x20d):
        func_name = 'ABS'
    elif pcode.id == 0x1a2:
        func_name = 'SQRT'
    elif pcode.id == 0x1a3:
        func_name = 'TAN'
    elif pcode.id == 0x1a4:
        func_name = 'UPPER'
    elif pcode.id in (0x90, 0x91, 0x92, 0x95, 0x96, 0x97, 0x99, 0x9a, 0x9b, 0x9c, 0x9d, 0x9e,
                      0x1ef, 0x1f0, 0x1f1, 0x228, 0x229, 0x22a):
        func_name = 'INT'
    elif pcode.id in (0x18e, 0x1da):
        func_name = 'CEIL'
    stack.append("{}({})".format(func_name, text))


def pb_create(stack, pcode, routine):
    ref = routine.const_.get_byte(pcode.args[0])
    stack.append("Create({})".format(routine.const_.get_string(ref)))

def pb_create_obj(stack, pcode, routine):
    ref = routine.const_.get_byte(pcode.args[0])
    stack.append("CreateObject({})".format(routine.const_.get_string(ref)))

def pb_push(stack, pcode, routine):
    if pcode.id in (0x1a9, 0x1aa):
        index = pcode.args[0]
        stack.append("ref " + routine.vars[index].name)
    if pcode.id in (0x1e, 0x30, 0x11d, 0x11e, 0x14f, 0x150, 0x151, 0x152, 0x172, 0x200, 0x202, 0x203):
        index = pcode.args[0]
        stack.append(routine.vars[index].name)
    elif pcode.id in (0x2f, 0x11f, 0x1a6, 0x153, 0x154, 0x201):
        index = pcode.args[0]
        stack.append("{}".format(definitions.glb_symbol[index].name))
    elif pcode.id == 0x120:
        index = pcode.args[0]
        stack.append("ref {}".format(routine.vars[index].name))


def pb_push_const_enum(stack, pcode, routine):
    stack.append(enum_main[pcode.args[1]][pcode.args[0]].name + "!")


def pb_push_this(stack, pcode, routine):
    stack.append('this')


def pb_push_parent(stack, pcode, routine):
    stack.append('parent')


def pb_destory(stack, pcode, routine):
    return "Destroy({})".format(stack.pop())

def pb_push_const(stack, pcode, routine):
    if pcode.id == 0x3c:
        if pcode.args[0] == 0:
            stack.append('false')
        else:
            stack.append('true')
        return
    if pcode.id == 0x223:
        stack.append(str(pcode.args[0]))
    elif pcode.id == 0x32:
        temp = struct.pack("<H", pcode.args[0])
        data = struct.unpack("<h", temp)[0]
        stack.append(str(data))
    elif pcode.id == 0x33:
        stack.append(str(pcode.args[0]))
    else:
        temp = struct.pack("<HH", pcode.args[0], pcode.args[1])
        data = struct.unpack("<I", temp)[0]
        if pcode.id == 0x34:
            data = struct.unpack("<i", temp)[0]
            stack.append(str(data))
        elif pcode.id == 0x35:
            stack.append(str(data))
        elif pcode.id == 0x36:
            stack.append(str(routine.const_.get_decimal(data)))
        elif pcode.id == 0x38:
            stack.append(str(routine.const_.get_double(data)))
        elif pcode.id == 0x3b:
            stack.append('"{}"'.format(routine.const_.get_string(data)))
        elif pcode.id == 0x20:
            temp = routine.const_.get_const_ref(data)
            stack.append(str(temp))
        elif pcode.id == 0x1ff:
            stack.append(str(routine.const_.get_longlong(data)))


def pb_dot(stack, pcode, routine):
    right = stack.pop()
    left = stack.pop()
    stack.append("{}.{}".format(left, right))


def pb_db_commit(stack, pcode, routine):
    stack.pop()
    return "COMMIT;"


def pb_db_rollback(stack, pcode, routine):
    stack.pop()
    return "ROLLBACK;"


def pb_db_delete(stack, pcode, routine):
    page_id = pcode.args[1] - 0x8000
    loc = (page_id * 0x10000) + pcode.args[0]
    stmt = definitions.glb_const.data_at(loc)
    if not stmt or not stmt.sql_string:
        raise Exception("empty delete statement")
    stack.pop()
    pars = list()
    for _ in range(pcode.args[2]):
        pars.append(stack.pop())
    pars.reverse()
    index = 0
    par_index = 0
    new_stmt = ""
    for par_info in stmt.params:
        new_stmt += stmt.sql_string[index:par_info.start_pos] + ":" + pars[par_index]
        index = par_info.end_pos
        par_index += 1
    new_stmt += stmt.sql_string[index:]
    return new_stmt


def pb_db_insert(stack, pcode, routine):
    # prepare location
    page_id = pcode.args[1] - 0x8000
    loc = (page_id * 0x10000) + pcode.args[0]
    stmt = definitions.glb_const.data_at(loc)
    if not stmt or not stmt.sql_string:
        raise Exception("empty insert statement")
    stack.pop()
    pars = list()
    for _ in range(pcode.args[2]):
        pars.append(stack.pop())
    pars.reverse()
    index = 0
    par_index = 0
    new_stmt = ''
    for par_info in stmt.params:
        new_stmt += stmt.sql_string[index:par_info.start_pos] + ":" + pars[par_index]
        index = par_info.end_pos
        par_index += 1
    new_stmt += stmt.sql_string[index:]
    return new_stmt


def pb_db_execute(stack, pcode, routine):
    arg_1 = stack.pop()
    arg_2 = stack.pop()
    return "DBExecImmediate({}, {})".format(arg_2, arg_1)


def pb_db_update(stack, pcode, routine):
    page_id = pcode.args[1] - 0x8000
    loc = (page_id * 0x10000) + pcode.args[0]
    stmt = definitions.glb_const.data_at(loc)
    if not stmt or not stmt.sql_string:
        raise Exception("empty update statement")
    stack.pop()
    pars = list()
    pars_count = pcode.args[2]
    if stmt.sql_string.lower().startswith("updateblob"):
        pars_count += 1
    for _ in range(pars_count):
        pars.append(stack.pop())
    pars.reverse()
    index = 0
    par_index = 0
    new_stmt = ''
    for par_info in stmt.params:
        new_stmt += stmt.sql_string[index:par_info.start_pos] + ":" + pars[par_index]
        index = par_info.end_pos
        par_index += 1
    new_stmt += stmt.sql_string[index:]
    return new_stmt
    # return "\n".join(lines)


def pb_db_select(stack, pcode, routine):
    page_id = pcode.args[1] - 0x8000
    loc = (page_id * 0x10000) + pcode.args[0]
    stmt = definitions.glb_const.data_at(loc)
    if stmt.select_stmt_loc == 0xffff:
        raise Exception("no select statement found")
    stmt_1 = definitions.glb_const.data_at(stmt.select_stmt_loc)
    if not stmt_1 or not stmt_1.sql_string:
        raise Exception("empty select statement")
    stack.pop()
    pars = list()
    for _ in range(len(stmt_1.params)):
        pars.append(stack.pop())
    pars.reverse()
    find_from = stmt_1.sql_string.upper().find("FROM")
    if find_from == -1:
        raise Exception("select statement without from keyword")
    lines = list()
    lines.append(stmt_1.sql_string[:find_from])
    lines.append("INTO {}".format(", ".join([":" + x for x in stack])))
    while stack:
        stack.pop()
    where_stmt = ''
    index = find_from
    param_index = 0    
    for par_info in stmt_1.params:
        where_stmt += stmt_1.sql_string[index:par_info.start_pos] + ":" + pars[param_index]
        index = par_info.end_pos
        param_index += 1
    where_stmt += stmt_1.sql_string[index:]
    lines.append(where_stmt)
    return "\n".join(lines)


def pb_db_open(stack, pcode, routine):
    arg_2 = stack.pop()
    arg_1 = stack.pop()
    return "db_open_dyn({}, {})".format(arg_1, arg_2)


def pb_db_prepare(stack, pcode, routine):
    if len(stack) == 3:
        sqlca = stack.pop()
        sql = stack.pop()
        sqlsa = stack.pop()
        return "prepare {} from {} using {}".format(sqlsa, sql, sqlca)
    elif len(stack) == 2:
        sql = stack.pop()
        sqlsa = stack.pop()
        return "prepare {} from {}".format(sqlsa, sql)


def pb_db_fetch(stack, pcode, routine):
    sqlsa = stack.pop()
    cursor = stack.pop()
    ret_val =  "FETCH {}:{} into {}".format(cursor, sqlsa, ', '.join(stack))
    while len(stack) > 0:
        stack.pop()
    return ret_val


def pb_db_close(stack, pcode, routine):
    if len(stack) == 2:
        sqlsa = stack.pop()
        cursor = stack.pop()
        return "CLOSE {}:{}".format(cursor, sqlsa)
    else:
        cursor = stack.pop()
        return "CLOSE {}".format(cursor)


def pb_jump(stack, pcode, routine):
    line_number = ""
    lines = routine.lines
    for i in range(len(lines)):
        if i == len(lines) - 1:
            if pcode.args[0] == lines[i].code_loc:
                line_number = str(lines[i].number)
            else:
                line_number = "end"
        else:
            if pcode.args[0] >= lines[i].code_loc and pcode.args[0] < lines[i + 1].code_loc:
                start_point = lines[i].code_loc
                jump_bytes = 0
                code_index = 0
                found = False
                if pcode.args[0] == start_point:
                    line_number = "{}".format(lines[i].number)
                    break
                for code in lines[i].codes:
                    jump_bytes = (len(code.args) + 1) * 2
                    start_point += jump_bytes
                    code_index += 1
                    if pcode.args[0] == start_point:
                        line_number = "{}.{}".format(lines[i].number, code_index)
                        found = True
                        break
                if found:
                    break
                # line_number = "{}:{}".format(lines[i].number, (pcode.args[0] - lines[i].code_loc) // 2)
                # break
            
    # for line in routine.lines:
    #     if line.code_loc == pcode.args[0]:
    #         line_number = line.number
    if pcode.id == 4:
        return "goto line {}".format(line_number)
    else:
        temp = stack.pop()
        
        if pcode.id == 3:
            return "if not {}    goto line {}".format(temp, line_number)
        elif pcode.id == 2:
            return "if {}    goto line {}".format(temp, line_number)


def pb_array_lowerbound(stack, pcode, routine):
    expr = stack.pop()
    stack.append("lowerbound({})".format(expr))


def pb_array_upperbound(stack, pcode, routine):
    expr = stack.pop()
    stack.append("upperbound({})".format(expr))


def pb_build_array_list(stack, pcode, routine):
    if pcode.id == 0x1b2:
        vars = list()
        for x in range(pcode.args[2]):
            vars.append(str(stack.pop()))
        stack.append("ArrayList({})".format(', '.join(vars[::-1])))


def pb_array_index2(stack, pcode, routine):
    pb_array_index(stack, pcode, routine)
    pb_dot(stack, pcode, routine)

def pb_complex_array_index(stack, pcode, routine):
    temp = stack.pop()
    temp = stack.pop()
    if pcode.args[0] != 1:
        expr_2 = stack.pop()
        expr_1 = stack.pop()
        stack.append("{}, {}".format(expr_1, expr_2))

def pb_array_index(stack, pcode, routine):
    index = stack.pop()
    array = stack.pop()
    stack.append("{}[{}]".format(array, index))


def pb_assign(stack, pcode, routine):
    right = stack.pop()
    left = stack.pop()
    return "{} = {}".format(left, right)


def pb_math(stack, pcode, routine):
    if pcode.id in (0x19f, 0x1a0, 0x20e):
        expr_1 = stack.pop()
        stack.append("rand({})".format(expr_1))
    elif pcode.id in (0x1e0, 0x1e1, 0x1e2, 0x1e3, 0x1e4, 0x217):
        if len(stack) < 2:
            raise Exception("max need 2 args")
        expr_2 = stack.pop()
        expr_1 = stack.pop()
        stack.append("max({}, {})".format(expr_1, expr_2))
    elif pcode.id in (0x1db, 0x1dc, 0x1dd, 0x1de, 0x1df, 0x216):
        if len(stack) < 2:
            raise Exception("max need 2 args")
        expr_2 = stack.pop()
        expr_1 = stack.pop()
        stack.append("min({}, {})".format(expr_1, expr_2))


def pb_is(stack, pcode, routine):
    temp = stack.pop()
    func = ''
    if pcode.id == 0x194:
        func = 'ISDATE'
    elif pcode.id == 0x195:
        func = 'ISNULL'
    elif pcode.id == 0x196:
        func = 'ISNUMBER'
    elif pcode.id == 0x197:
        func = 'ISTIME'
    elif pcode.id == 0x198:
        func = 'ISVALID'
    stack.append("{}({})".format(func, temp))

# def pb_string_len(stack, pcode, reutine):
#     temp = stack.pop()
#     stack.append("len({})".format(temp))


def pb_incr(stack, pcode, routine):
    return "{} ++".format(stack.pop())


def pb_decr(stack, pcode, routine):
    return "{} --".format(stack.pop())


def pb_not(stack, pcode, routine):
    expr = stack.pop()
    stack.append("not {}".format(expr))


def pb_compare(stack, pcode, routine):
    expr_2 = stack.pop()
    expr_1 = stack.pop()
    op = ''
    if pcode.id in (0x20f, 0x241, 0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xab,
                    0xac, 0xad, 0xae, 0xaf, 0xb0, 0xb1, 0xb2, 0xb3, 0xb5,
                    0x11a, 0x17d):
        op = ' == '
    elif pcode.id in (0x210, 0x242, 0xb6, 0xb7, 0xb8, 0xb9, 0xba, 0xbb,
                      0xbc, 0xbd, 0xbe, 0xbf, 0xc0, 0xc1, 0xc2, 0xc3, 0xc4,
                      0xc5, 0x11b, 0x17e):
        op = ' != '
    elif pcode.id in (0x211, 0x243, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcb,
                      0xcc, 0xcd, 0xce, 0xcf, 0xd0, 0xd1, 0x17f):
        op = ' > '
    elif pcode.id in (0x212, 0x244, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7,
                      0xd8, 0xd9, 0xda, 0xdb, 0xdc, 0xdd, 0x180):
        op = ' < '
    elif pcode.id in (0x213, 0x245, 0xde, 0xdf, 0xe0, 0xe1, 0xe2, 0xe3,
                      0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0x181):
        op = ' >= '
    elif pcode.id in (0x214, 0x246, 0xea, 0xeb, 0xec, 0xed, 0xee, 0xef,
                      0xf0, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0x182, 0x246):
        op = ' <= '
    elif pcode.id in (0x25, 0x184):
        op = " or "
    elif pcode.id in (0x24, 0x183):
        op = " and "
    else:
        return
    stack.append("({} {} {})".format(expr_1, op, expr_2))


def pb_lvalue_expr(stack, pcode, routine):
    return stack.pop()


def pb_dup_stack(stack, pcode, routine):
    item = stack[0]
    stack.insert(1, item)


def pb_empty(stack, pcode, routine):
    pass


g_codes = [
    {'index': 0x0, 'name': 'SM_RETURN', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5c440, 'func': pb_empty},
    {'index': 0x1, 'name': 'SM_STORE_RETURN_VAL', 'arg_num': 1, 'unknown': 0x100, 'addr': 0x10d5c550, 'func': pb_return_val},
    {'index': 0x2, 'name': 'SM_JUMPTRUE', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d5c510, 'func': pb_jump},
    {'index': 0x3, 'name': 'SM_JUMPFALSE', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d5c4f0,'func': pb_jump},
    {'index': 0x4, 'name': 'SM_JUMP', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5cfa0, 'func': pb_jump},
    {'index': 0x5, 'name': 'SM_DBSTART', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5d880},
    {'index': 0x6, 'name': 'SM_DBCOMMIT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5cd40, 'func': pb_db_commit},
    {'index': 0x7, 'name': 'SM_DBROLLBACK', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5d020, 'func': pb_db_rollback},
    {'index': 0x8, 'name': 'SM_DBSTOP', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5d800},
    {'index': 0x9, 'name': 'SM_DBCLOSE', 'arg_num': 0, 'unknown': 0xfffffffe, 'addr': 0x10d5d540, 'func': pb_db_close},
    {'index': 0xa, 'name': 'SM_DBOPEN', 'arg_num': 1, 'unknown': 0x100, 'addr': 0x10d5d900},
    {'index': 0xb, 'name': 'SM_DBDELETE', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5d0a0, 'func': pb_db_delete},
    {'index': 0xc, 'name': 'SM_DBUPDATE', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5db00, 'func': pb_db_update},
    {'index': 0xd, 'name': 'SM_DBEXECUTE', 'arg_num': 1, 'unknown': 0x100, 'addr': 0x10d5d320},
    {'index': 0xe, 'name': 'SM_DBFETCH', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5d490, 'func': pb_db_fetch},
    {'index': 0xf, 'name': 'SM_DBINSERT', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5cdc0, 'func': pb_db_insert},
    {'index': 0x10, 'name': 'SM_DBSELECT', 'arg_num': 4, 'unknown': 0x100, 'addr': 0x10d5e0a0, 'func': pb_db_select},
    {'index': 0x11, 'name': 'SM_DESTROY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c490, 'func': pb_destory},
    {'index': 0x12, 'name': 'SM_HALT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5aad0},
    {'index': 0x13, 'name': 'SM_EVENTCALL', 'arg_num': 5, 'unknown': 0x0, 'addr': 0x10d5ade0, 'func': pb_call_func},
    {'index': 0x14, 'name': 'SM_LVALUE_EXPR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5dbb0, 'func': pb_lvalue_expr},
    {'index': 0x15, 'name': 'SM_DBEXECUTEDYN', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5d760},
    {'index': 0x16, 'name': 'SM_DBPREPARE', 'arg_num': 0, 'unknown': 0xfffffffd, 'addr': 0x10d5d5f0, 'func': pb_db_prepare},
    {'index': 0x17, 'name': 'SM_DBOPENDYN', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5dcf0, 'func': pb_db_open},
    {'index': 0x18, 'name': 'SM_DBEXECDYNPROC', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5da80},
    {'index': 0x19, 'name': 'SM_DBDESCRIBE', 'arg_num': 0, 'unknown': 0xfffffffe, 'addr': 0x10d5cea0},
    {'index': 0x1a, 'name': 'SM_DBSELECTBLOB', 'arg_num': 4, 'unknown': 0x100, 'addr': 0x10d5d220, 'func': pb_db_select},
    {'index': 0x1b, 'name': 'SM_DBUPDATEBLOB', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5cf80, 'func': pb_db_update},
    {'index': 0x1c, 'name': 'SM_DBSELECTCLOB', 'arg_num': 5, 'unknown': 0x100, 'addr': 0x10d5d300, 'func': pb_db_select},
    {'index': 0x1d, 'name': 'SM_DBUPDATECLOB', 'arg_num': 4, 'unknown': 0x100, 'addr': 0x10d542a0, 'func': pb_db_update},
    {'index': 0x1e, 'name': 'SM_PUSH_LOCAL_VAR', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54650, 'func': pb_push},
    {'index': 0x1f, 'name': 'SM_PUSH_SHARED_VAR', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54a40},
    {'index': 0x20, 'name': 'SM_PUSH_CONST_REF', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d54b00, 'func': pb_push_const},
    {'index': 0x21, 'name': 'SM_PUSH_THIS', 'arg_num': 0, 'unknown': 0x1, 'addr': 0x10d54b80, 'func': pb_push_this},
    {'index': 0x22, 'name': 'SM_PUSH_PARENT', 'arg_num': 0, 'unknown': 0x1, 'addr': 0x10d54cf0, 'func': pb_push_parent},
    {'index': 0x23, 'name': 'SM_PUSH_PRIMARY', 'arg_num': 0, 'unknown': 0x1, 'addr': 0x10d5de60},
    {'index': 0x24, 'name': 'SM_AND', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5dee0, 'func': pb_compare},
    {'index': 0x25, 'name': 'SM_OR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5df80, 'func': pb_compare},
    {'index': 0x26, 'name': 'SM_NOT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d58340, 'func': pb_not},
    {'index': 0x27, 'name': 'SM_DOT', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d56cb0, 'func': pb_dot},
    {'index': 0x28, 'name': 'SM_INDEX', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c590, 'func': pb_array_index},
    {'index': 0x29, 'name': 'SM_GLOBFUNCCALL', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x2a, 'name': 'SM_SYSFUNCCALL', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x2b, 'name': 'SM_DLLFUNCCALL', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d59e90},
    {'index': 0x2c, 'name': 'SM_DOTFUNCCALL', 'arg_num': 4, 'unknown': 0x0, 'addr': 0x10d595c0, 'func': pb_call_func},
    {'index': 0x2d, 'name': 'SM_CREATE', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d5c590, 'func': pb_create},
    {'index': 0x2e, 'name': 'SM_ARRAYLIST', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d54d80},
    {'index': 0x2f, 'name': 'SM_PUSH_LOCAL_GLOBREF', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55100, 'func': pb_push},
    {'index': 0x30, 'name': 'SM_PUSH_LOCAL_ARGREF', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55480, 'func': pb_push},
    {'index': 0x31, 'name': 'SM_PUSH_SHARED_GLOBREF', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55800},
    {'index': 0x32, 'name': 'SM_PUSH_CONST_INT', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55850, 'func': pb_push_const},
    {'index': 0x33, 'name': 'SM_PUSH_CONST_UINT', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d558f0, 'func': pb_push_const},
    {'index': 0x34, 'name': 'SM_PUSH_CONST_LONG', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55940, 'func': pb_push_const},
    {'index': 0x35, 'name': 'SM_PUSH_CONST_ULONG', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55990, 'func': pb_push_const},
    {'index': 0x36, 'name': 'SM_PUSH_CONST_DEC', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55a20, 'func': pb_push_const},
    {'index': 0x37, 'name': 'SM_PUSH_CONST_FLOAT', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55a80},
    {'index': 0x38, 'name': 'SM_PUSH_CONST_DOUBLE', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55b40, 'func': pb_push_const},
    {'index': 0x39, 'name': 'SM_PUSH_CONST_TIME', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55ba0},
    {'index': 0x3a, 'name': 'SM_PUSH_CONST_DATE', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55c00},
    {'index': 0x3b, 'name': 'SM_PUSH_CONST_STRING', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d55c60, 'func': pb_push_const},
    {'index': 0x3c, 'name': 'SM_PUSH_CONST_BOOL', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55cb0, 'func': pb_push_const},
    {'index': 0x3d, 'name': 'SM_PUSH_CONST_ENUM', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d50f30, 'func': pb_push_const_enum},
    {'index': 0x3e, 'name': 'SM_CNV_INT_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d50fb0, 'func': pb_empty},
    {'index': 0x3f, 'name': 'SM_CNV_INT_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d50ff0, 'func': pb_empty},
    {'index': 0x40, 'name': 'SM_CNV_INT_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51030, 'func': pb_empty},
    {'index': 0x41, 'name': 'SM_CNV_INT_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d510c0, 'func': pb_empty},
    {'index': 0x42, 'name': 'SM_CNV_INT_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51110, 'func': pb_empty},
    {'index': 0x43, 'name': 'SM_CNV_INT_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51230, 'func': pb_empty},
    {'index': 0x44, 'name': 'SM_CNV_UINT_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51270, 'func': pb_empty},
    {'index': 0x45, 'name': 'SM_CNV_UINT_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d512b0, 'func': pb_empty},
    {'index': 0x46, 'name': 'SM_CNV_UINT_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51340, 'func': pb_empty},
    {'index': 0x47, 'name': 'SM_CNV_UINT_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51390, 'func': pb_empty},
    {'index': 0x48, 'name': 'SM_CNV_UINT_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51770, 'func': pb_empty},
    {'index': 0x49, 'name': 'SM_CNV_LONG_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d517b0, 'func': pb_empty},
    {'index': 0x4a, 'name': 'SM_CNV_LONG_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51840, 'func': pb_empty},
    {'index': 0x4b, 'name': 'SM_CNV_LONG_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51880, 'func': pb_empty},
    {'index': 0x4c, 'name': 'SM_CNV_LONG_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51a10, 'func': pb_empty},
    {'index': 0x4d, 'name': 'SM_CNV_ULONG_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51aa0, 'func': pb_empty},
    {'index': 0x4e, 'name': 'SM_CNV_ULONG_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51af0, 'func': pb_empty},
    {'index': 0x4f, 'name': 'SM_CNV_ULONG_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51e30, 'func': pb_empty},
    {'index': 0x50, 'name': 'SM_CNV_DEC_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51eb0, 'func': pb_empty},
    {'index': 0x51, 'name': 'SM_CNV_DEC_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d521a0, 'func': pb_empty},
    {'index': 0x52, 'name': 'SM_CNV_FLOAT_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d4ebf0, 'func': pb_empty},
    {'index': 0x53, 'name': 'SM_ADD_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4ec60, 'func': pb_add},
    {'index': 0x54, 'name': 'SM_ADD_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4ed40, 'func': pb_add},
    {'index': 0x55, 'name': 'SM_ADD_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4edb0, 'func': pb_add},
    {'index': 0x56, 'name': 'SM_ADD_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4ee20, 'func': pb_add},
    {'index': 0x57, 'name': 'SM_ADD_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4eed0, 'func': pb_add},
    {'index': 0x58, 'name': 'SM_ADD_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4ef40, 'func': pb_add},
    {'index': 0x59, 'name': 'SM_ADD_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f210, 'func': pb_add},
    {'index': 0x5a, 'name': 'SM_SUB_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f280, 'func': pb_sub},
    {'index': 0x5b, 'name': 'SM_SUB_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f360, 'func': pb_sub},
    {'index': 0x5c, 'name': 'SM_SUB_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f3d0, 'func': pb_sub},
    {'index': 0x5d, 'name': 'SM_SUB_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f440, 'func': pb_sub},
    {'index': 0x5e, 'name': 'SM_SUB_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f4f0, 'func': pb_sub},
    {'index': 0x5f, 'name': 'SM_SUB_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f560, 'func': pb_sub},
    {'index': 0x60, 'name': 'SM_SUB_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f830, 'func': pb_sub},
    {'index': 0x61, 'name': 'SM_MULT_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f8a0, 'func': pb_mul},
    {'index': 0x62, 'name': 'SM_MULT_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f980, 'func': pb_mul},
    {'index': 0x63, 'name': 'SM_MULT_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f9f0, 'func': pb_mul},
    {'index': 0x64, 'name': 'SM_MULT_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fa60, 'func': pb_mul},
    {'index': 0x65, 'name': 'SM_MULT_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fb10, 'func': pb_mul},
    {'index': 0x66, 'name': 'SM_MULT_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fbc0, 'func': pb_mul},
    {'index': 0x67, 'name': 'SM_MULT_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4feb0, 'func': pb_mul},
    {'index': 0x68, 'name': 'SM_DIV_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fec0, 'func': pb_div},
    {'index': 0x69, 'name': 'SM_DIV_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fee0, 'func': pb_div},
    {'index': 0x6a, 'name': 'SM_DIV_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fef0, 'func': pb_div},
    {'index': 0x6b, 'name': 'SM_DIV_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4ff00, 'func': pb_div},
    {'index': 0x6c, 'name': 'SM_DIV_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fff0, 'func': pb_div},
    {'index': 0x6d, 'name': 'SM_DIV_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d500c0, 'func': pb_div},
    {'index': 0x6e, 'name': 'SM_DIV_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50310, 'func': pb_div},
    {'index': 0x6f, 'name': 'SM_POWER_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d503d0, 'func': pb_power},
    {'index': 0x70, 'name': 'SM_POWER_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50550, 'func': pb_power},
    {'index': 0x71, 'name': 'SM_POWER_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50600, 'func': pb_power},
    {'index': 0x72, 'name': 'SM_POWER_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d506e0, 'func': pb_power},
    {'index': 0x73, 'name': 'SM_POWER_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50840, 'func': pb_power},
    {'index': 0x74, 'name': 'SM_POWER_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50930, 'func': pb_power},
    {'index': 0x75, 'name': 'SM_POWER_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50c60, 'func': pb_power},
    {'index': 0x76, 'name': 'SM_NEGATE_INT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50c80, 'func': pb_negate},
    {'index': 0x77, 'name': 'SM_NEGATE_UINT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50cc0, 'func': pb_negate},
    {'index': 0x78, 'name': 'SM_NEGATE_LONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50ce0, 'func': pb_negate},
    {'index': 0x79, 'name': 'SM_NEGATE_ULONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50d00, 'func': pb_negate},
    {'index': 0x7a, 'name': 'SM_NEGATE_DEC', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50d60, 'func': pb_negate},
    {'index': 0x7b, 'name': 'SM_NEGATE_FLOAT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d50d80, 'func': pb_negate},
    {'index': 0x7c, 'name': 'SM_NEGATE_DOUBLE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d580b0, 'func': pb_negate},
    {'index': 0x7d, 'name': 'SM_CAT_STRING', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d58170, 'func': pb_add},
    {'index': 0x7e, 'name': 'SM_CAT_BINARY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d4c850, 'func': pb_add},
    {'index': 0x7f, 'name': 'SM_ASSIGN_ARRAY', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4c950, 'func': pb_assign},
    {'index': 0x80, 'name': 'SM_ASSIGN_INT', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4c9f0, 'func': pb_assign},
    {'index': 0x81, 'name': 'SM_ASSIGN_UINT', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cb30, 'func': pb_assign},
    {'index': 0x82, 'name': 'SM_ASSIGN_LONG', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cbd0, 'func': pb_assign},
    {'index': 0x83, 'name': 'SM_ASSIGN_ULONG', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cc70, 'func': pb_assign},
    {'index': 0x84, 'name': 'SM_ASSIGN_DEC', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cd10, 'func': pb_assign},
    {'index': 0x85, 'name': 'SM_ASSIGN_FLOAT', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cdb0, 'func': pb_assign},
    {'index': 0x86, 'name': 'SM_ASSIGN_DOUBLE', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cf50, 'func': pb_assign},
    {'index': 0x87, 'name': 'SM_ASSIGN_BLOB', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4cff0, 'func': pb_assign},
    {'index': 0x88, 'name': 'SM_ASSIGN_STRING', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4d0b0, 'func': pb_assign},
    {'index': 0x89, 'name': 'SM_ASSIGN_TIME', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4d170, 'func': pb_assign},
    {'index': 0x8a, 'name': 'SM_ASSIGN_OBINST', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4d210, 'func': pb_assign},
    {'index': 0x8b, 'name': 'SM_ASSIGN_ANCESTOR', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4d2e0, 'func': pb_assign},
    {'index': 0x8c, 'name': 'SM_ASSIGN_ENUM', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d511b0, 'func': pb_assign},
    {'index': 0x8d, 'name': 'SM_CNV_UINT_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d516b0, 'func': pb_empty},
    {'index': 0x8e, 'name': 'SM_CNV_LONG_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51910, 'func': pb_empty},
    {'index': 0x8f, 'name': 'SM_CNV_ULONG_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51b90, 'func': pb_empty},
    {'index': 0x90, 'name': 'SM_CNV_DEC_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51fd0, 'func': pb_in_func},
    {'index': 0x91, 'name': 'SM_CNV_FLOAT_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d522c0, 'func': pb_in_func},
    {'index': 0x92, 'name': 'SM_CNV_DOUBLE_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d516f0, 'func': pb_in_func},
    {'index': 0x93, 'name': 'SM_CNV_LONG_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51950, 'func': pb_empty},
    {'index': 0x94, 'name': 'SM_CNV_ULONG_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51c20, 'func': pb_empty},
    {'index': 0x95, 'name': 'SM_CNV_DEC_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52010, 'func': pb_in_func},
    {'index': 0x96, 'name': 'SM_CNV_FLOAT_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52300, 'func': pb_in_func},
    {'index': 0x97, 'name': 'SM_CNV_DOUBLE_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d519d0, 'func': pb_in_func},
    {'index': 0x98, 'name': 'SM_CNV_ULONG_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51d30, 'func': pb_empty},
    {'index': 0x99, 'name': 'SM_CNV_DEC_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52090, 'func': pb_in_func},
    {'index': 0x9a, 'name': 'SM_CNV_FLOAT_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52390, 'func': pb_in_func},
    {'index': 0x9b, 'name': 'SM_CNV_DOUBLE_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51db0, 'func': pb_in_func},
    {'index': 0x9c, 'name': 'SM_CNV_DEC_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d520d0, 'func': pb_in_func},
    {'index': 0x9d, 'name': 'SM_CNV_FLOAT_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d523d0, 'func': pb_in_func},
    {'index': 0x9e, 'name': 'SM_CNV_DOUBLE_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52110, 'func': pb_in_func},
    {'index': 0x9f, 'name': 'SM_CNV_FLOAT_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52460, 'func': pb_empty},
    {'index': 0xa0, 'name': 'SM_CNV_DOUBLE_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d524f0, 'func': pb_empty},
    {'index': 0xa1, 'name': 'SM_CNV_DOUBLE_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52850, 'func': pb_empty},
    {'index': 0xa2, 'name': 'SM_CNV_STRING_TO_CHAR', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d528d0},
    {'index': 0xa3, 'name': 'SM_CNV_CHAR_TO_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52920},
    {'index': 0xa4, 'name': 'SM_CNV_STRING_TO_CHARARRAY', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d529f0},
    {'index': 0xa5, 'name': 'SM_CNV_CHARARRAY_TO_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d46ec0},
    {'index': 0xa6, 'name': 'SM_EQ_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d46f40, 'func': pb_compare},
    {'index': 0xa7, 'name': 'SM_EQ_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47040, 'func': pb_compare},
    {'index': 0xa8, 'name': 'SM_EQ_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d470c0, 'func': pb_compare},
    {'index': 0xa9, 'name': 'SM_EQ_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47140, 'func': pb_compare},
    {'index': 0xaa, 'name': 'SM_EQ_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d471c0, 'func': pb_compare},
    {'index': 0xab, 'name': 'SM_EQ_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47240, 'func': pb_compare},
    {'index': 0xac, 'name': 'SM_EQ_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47340, 'func': pb_compare},
    {'index': 0xad, 'name': 'SM_EQ_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d46ec0, 'func': pb_compare},
    {'index': 0xae, 'name': 'SM_EQ_BOOL', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47420, 'func': pb_compare},
    {'index': 0xaf, 'name': 'SM_EQ_BINARY', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d475e0, 'func': pb_compare},
    {'index': 0xb0, 'name': 'SM_EQ_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d47500, 'func': pb_compare},
    {'index': 0xb1, 'name': 'SM_EQ_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d476c0, 'func': pb_compare},
    {'index': 0xb2, 'name': 'SM_EQ_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d46ec0, 'func': pb_compare},
    {'index': 0xb3, 'name': 'SM_EQ_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d46cf0, 'func': pb_compare},
    {'index': 0xb4, 'name': 'SM_EQ_OBINST', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d46ec0},
    {'index': 0xb5, 'name': 'SM_EQ_ENUM', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47810, 'func': pb_compare},
    {'index': 0xb6, 'name': 'SM_NE_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47890, 'func': pb_compare},
    {'index': 0xb7, 'name': 'SM_NE_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47990, 'func': pb_compare},
    {'index': 0xb8, 'name': 'SM_NE_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47a00, 'func': pb_compare},
    {'index': 0xb9, 'name': 'SM_NE_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47a70, 'func': pb_compare},
    {'index': 0xba, 'name': 'SM_NE_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47af0, 'func': pb_compare},
    {'index': 0xbb, 'name': 'SM_NE_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47b70, 'func': pb_compare},
    {'index': 0xbc, 'name': 'SM_NE_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47c70, 'func': pb_compare},
    {'index': 0xbd, 'name': 'SM_NE_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d47810, 'func': pb_compare},
    {'index': 0xbe, 'name': 'SM_NE_BOOL', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47d50, 'func': pb_compare},
    {'index': 0xbf, 'name': 'SM_NE_BINARY', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d47f10, 'func': pb_compare},
    {'index': 0xc0, 'name': 'SM_NE_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d47e30, 'func': pb_compare},
    {'index': 0xc1, 'name': 'SM_NE_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d48010, 'func': pb_compare},
    {'index': 0xc2, 'name': 'SM_NE_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d47810, 'func': pb_compare},
    {'index': 0xc3, 'name': 'SM_NE_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d46e10, 'func': pb_compare},
    {'index': 0xc4, 'name': 'SM_NE_OBINST', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47810, 'func': pb_compare},
    {'index': 0xc5, 'name': 'SM_NE_ENUM', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48160, 'func': pb_compare},
    {'index': 0xc6, 'name': 'SM_GT_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d481e0, 'func': pb_compare},
    {'index': 0xc7, 'name': 'SM_GT_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d482e0, 'func': pb_compare},
    {'index': 0xc8, 'name': 'SM_GT_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48350, 'func': pb_compare},
    {'index': 0xc9, 'name': 'SM_GT_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d483c0, 'func': pb_compare},
    {'index': 0xca, 'name': 'SM_GT_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48450, 'func': pb_compare},
    {'index': 0xcb, 'name': 'SM_GT_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d484d0, 'func': pb_compare},
    {'index': 0xcc, 'name': 'SM_GT_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d485e0, 'func': pb_compare},
    {'index': 0xcd, 'name': 'SM_GT_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d48790, 'func': pb_compare},
    {'index': 0xce, 'name': 'SM_GT_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d486c0, 'func': pb_compare},
    {'index': 0xcf, 'name': 'SM_GT_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d48860, 'func': pb_compare},
    {'index': 0xd0, 'name': 'SM_GT_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d48970, 'func': pb_compare},
    {'index': 0xd1, 'name': 'SM_GT_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48a40, 'func': pb_compare},
    {'index': 0xd2, 'name': 'SM_LT_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48ac0, 'func': pb_compare},
    {'index': 0xd3, 'name': 'SM_LT_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48bc0, 'func': pb_compare},
    {'index': 0xd4, 'name': 'SM_LT_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48c30, 'func': pb_compare},
    {'index': 0xd5, 'name': 'SM_LT_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48ca0, 'func': pb_compare},
    {'index': 0xd6, 'name': 'SM_LT_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48d30, 'func': pb_compare},
    {'index': 0xd7, 'name': 'SM_LT_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48db0, 'func': pb_compare},
    {'index': 0xd8, 'name': 'SM_LT_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48ec0, 'func': pb_compare},
    {'index': 0xd9, 'name': 'SM_LT_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49070, 'func': pb_compare},
    {'index': 0xda, 'name': 'SM_LT_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d48fa0, 'func': pb_compare},
    {'index': 0xdb, 'name': 'SM_LT_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49140, 'func': pb_compare},
    {'index': 0xdc, 'name': 'SM_LT_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49250, 'func': pb_compare},
    {'index': 0xdd, 'name': 'SM_LT_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49320, 'func': pb_compare},
    {'index': 0xde, 'name': 'SM_GE_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d493a0, 'func': pb_compare},
    {'index': 0xdf, 'name': 'SM_GE_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d494a0, 'func': pb_compare},
    {'index': 0xe0, 'name': 'SM_GE_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49510, 'func': pb_compare},
    {'index': 0xe1, 'name': 'SM_GE_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49580, 'func': pb_compare},
    {'index': 0xe2, 'name': 'SM_GE_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49610, 'func': pb_compare},
    {'index': 0xe3, 'name': 'SM_GE_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49690, 'func': pb_compare},
    {'index': 0xe4, 'name': 'SM_GE_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d497a0, 'func': pb_compare},
    {'index': 0xe5, 'name': 'SM_GE_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49950, 'func': pb_compare},
    {'index': 0xe6, 'name': 'SM_GE_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49880, 'func': pb_compare},
    {'index': 0xe7, 'name': 'SM_GE_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49a20, 'func': pb_compare},
    {'index': 0xe8, 'name': 'SM_GE_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d49b30, 'func': pb_compare},
    {'index': 0xe9, 'name': 'SM_GE_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49c00, 'func': pb_compare},
    {'index': 0xea, 'name': 'SM_LE_INT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49c80, 'func': pb_compare},
    {'index': 0xeb, 'name': 'SM_LE_UINT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49d80, 'func': pb_compare},
    {'index': 0xec, 'name': 'SM_LE_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49df0, 'func': pb_compare},
    {'index': 0xed, 'name': 'SM_LE_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49e60, 'func': pb_compare},
    {'index': 0xee, 'name': 'SM_LE_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49ef0, 'func': pb_compare},
    {'index': 0xef, 'name': 'SM_LE_FLOAT', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49f70, 'func': pb_compare},
    {'index': 0xf0, 'name': 'SM_LE_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4a080, 'func': pb_compare},
    {'index': 0xf1, 'name': 'SM_LE_STRING', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4a230, 'func': pb_compare},
    {'index': 0xf2, 'name': 'SM_LE_TIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4a160, 'func': pb_compare},
    {'index': 0xf3, 'name': 'SM_LE_DATE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4a300, 'func': pb_compare},
    {'index': 0xf4, 'name': 'SM_LE_DATETIME', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4a410, 'func': pb_compare},
    {'index': 0xf5, 'name': 'SM_LE_CHAR', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4d430, 'func': pb_compare},
    {'index': 0xf6, 'name': 'SM_INCR_INT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4d4f0, 'func': pb_incr},
    {'index': 0xf7, 'name': 'SM_INCR_UINT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4d670, 'func': pb_incr},
    {'index': 0xf8, 'name': 'SM_INCR_LONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4d730, 'func': pb_incr},
    {'index': 0xf9, 'name': 'SM_INCR_ULONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4d7f0, 'func': pb_incr},
    {'index': 0xfa, 'name': 'SM_INCR_DEC', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4da10, 'func': pb_incr},
    {'index': 0xfb, 'name': 'SM_INCR_FLOAT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4dae0, 'func': pb_incr},
    {'index': 0xfc, 'name': 'SM_INCR_DOUBLE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e010, 'func': pb_incr},
    {'index': 0xfd, 'name': 'SM_DECR_INT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e0d0, 'func': pb_decr},
    {'index': 0xfe, 'name': 'SM_DECR_UINT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e250, 'func': pb_decr},
    {'index': 0xff, 'name': 'SM_DECR_LONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e310, 'func': pb_decr},
    {'index': 0x100, 'name': 'SM_DECR_ULONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e3d0, 'func': pb_decr},
    {'index': 0x101, 'name': 'SM_DECR_DEC', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e5f0, 'func': pb_decr},
    {'index': 0x102, 'name': 'SM_DECR_FLOAT', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e6c0, 'func': pb_decr},
    {'index': 0x103, 'name': 'SM_DECR_DOUBLE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4a4e0, 'func': pb_decr},
    {'index': 0x104, 'name': 'SM_ADDASSIGN_INT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4a5c0, 'func': pb_add_assign},
    {'index': 0x105, 'name': 'SM_ADDASSIGN_UINT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4a780, 'func': pb_add_assign},
    {'index': 0x106, 'name': 'SM_ADDASSIGN_LONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4a860, 'func': pb_add_assign},
    {'index': 0x107, 'name': 'SM_ADDASSIGN_ULONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4a940, 'func': pb_add_assign},
    {'index': 0x108, 'name': 'SM_ADDASSIGN_DEC', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4aaf0, 'func': pb_add_assign},
    {'index': 0x109, 'name': 'SM_ADDASSIGN_FLOAT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4ac90, 'func': pb_add_assign},
    {'index': 0x10a, 'name': 'SM_ADDASSIGN_DOUBLE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b0b0, 'func': pb_add_assign},
    {'index': 0x10b, 'name': 'SM_SUBASSIGN_INT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b190, 'func': pb_sub_assign},
    {'index': 0x10c, 'name': 'SM_SUBASSIGN_UINT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b350, 'func': pb_sub_assign},
    {'index': 0x10d, 'name': 'SM_SUBASSIGN_LONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b430, 'func': pb_sub_assign},
    {'index': 0x10e, 'name': 'SM_SUBASSIGN_ULONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b510, 'func': pb_sub_assign},
    {'index': 0x10f, 'name': 'SM_SUBASSIGN_DEC', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b6c0, 'func': pb_sub_assign},
    {'index': 0x110, 'name': 'SM_SUBASSIGN_FLOAT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b860, 'func': pb_sub_assign},
    {'index': 0x111, 'name': 'SM_SUBASSIGN_DOUBLE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4bc70, 'func': pb_sub_assign},
    {'index': 0x112, 'name': 'SM_MULTASSIGN_INT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4bd50, 'func': pb_mul_assign},
    {'index': 0x113, 'name': 'SM_MULTASSIGN_UINT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4bf10, 'func': pb_mul_assign},
    {'index': 0x114, 'name': 'SM_MULTASSIGN_LONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4bff0, 'func': pb_mul_assign},
    {'index': 0x115, 'name': 'SM_MULTASSIGN_ULONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4c0d0, 'func': pb_mul_assign},
    {'index': 0x116, 'name': 'SM_MULTASSIGN_DEC', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4c280, 'func': pb_mul_assign},
    {'index': 0x117, 'name': 'SM_MULTASSIGN_FLOAT', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4c420, 'func': pb_mul_assign},
    {'index': 0x118, 'name': 'SM_MULTASSIGN_DOUBLE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d581c0, 'func': pb_mul_assign},
    {'index': 0x119, 'name': 'SM_DUP_STACKED_LVALUE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d46c80, 'func': pb_dup_stack},
    {'index': 0x11a, 'name': 'SM_EQ_ARRAY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d46d90, 'func': pb_compare},
    {'index': 0x11b, 'name': 'SM_NE_ARRAY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c590, 'func': pb_compare},
    {'index': 0x11c, 'name': 'SM_CONV_TO_LVALUE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d55d00, 'func': pb_empty},
    {'index': 0x11d, 'name': 'SM_PUSH_LOCAL_VAR_LV', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55db0, 'func': pb_push},
    {'index': 0x11e, 'name': 'SM_PUSH_SHARED_VAR_LV', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55e60, 'func': pb_push},
    {'index': 0x11f, 'name': 'SM_PUSH_LOCAL_GLOBREF_LV', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55ef0, 'func': pb_push},
    {'index': 0x120, 'name': 'SM_PUSH_LOCAL_ARGREF_LV', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55fc0, 'func': pb_push},
    {'index': 0x121, 'name': 'SM_PUSH_SHARED_GLOBREF_LV', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d59010},
    {'index': 0x122, 'name': 'SM_DOT_LV', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d57200, 'func': pb_dot},
    {'index': 0x123, 'name': 'SM_INDEX_LV', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c590, 'func': pb_array_index},
    {'index': 0x124, 'name': 'SM_NOOP', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5c950},
    {'index': 0x125, 'name': 'SM_POP', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c970},
    {'index': 0x126, 'name': 'SM_FREE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d54250},
    {'index': 0x127, 'name': 'SM_PUSH_RESULT', 'arg_num': 0, 'unknown': 0x1, 'addr': 0x10d5c990, 'func': pb_empty},
    {'index': 0x128, 'name': 'SM_POP_POP', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c9f0, 'func': pb_empty},
    {'index': 0x129, 'name': 'SM_POP_FREE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5ca70, 'func': pb_empty},
    {'index': 0x12a, 'name': 'SM_FREE_POP', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5caf0, 'func': pb_empty},
    {'index': 0x12b, 'name': 'SM_FREE_FREE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d59770, 'func': pb_empty},
    {'index': 0x12c, 'name': 'SM_COPY_ARRAY_INSTANCE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d597a0, 'func': pb_empty},
    {'index': 0x12d, 'name': 'SM_COPY_STRUCTURE_INSTANCE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d597d0, 'func': pb_empty},
    {'index': 0x12e, 'name': 'SM_COPY_CONST_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59870, 'func': pb_empty},
    {'index': 0x12f, 'name': 'SM_COPY_CONST_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d598d0, 'func': pb_empty},
    {'index': 0x130, 'name': 'SM_COPY_CONST_DATE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59930, 'func': pb_empty},
    {'index': 0x131, 'name': 'SM_COPY_CONST_TIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59990, 'func': pb_empty},
    {'index': 0x132, 'name': 'SM_COPY_CONST_DATETIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d599f0, 'func': pb_empty},
    {'index': 0x133, 'name': 'SM_COPY_CONST_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59a40, 'func': pb_empty},
    {'index': 0x134, 'name': 'SM_COPY_LVALUE_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59ae0, 'func': pb_empty},
    {'index': 0x135, 'name': 'SM_COPY_LVALUE_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59b50, 'func': pb_copy},
    {'index': 0x136, 'name': 'SM_COPY_LVALUE_DATE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59bc0, 'func': pb_copy},
    {'index': 0x137, 'name': 'SM_COPY_LVALUE_TIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59c30, 'func': pb_copy},
    {'index': 0x138, 'name': 'SM_COPY_LVALUE_DATETIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59ca0, 'func': pb_copy},
    {'index': 0x139, 'name': 'SM_COPY_LVALUE_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59cf0, 'func': pb_empty},
    {'index': 0x13a, 'name': 'SM_COPY_LVALUE_BINARY', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5cb80, 'func': pb_copy},
    {'index': 0x13b, 'name': 'SM_POP_N_TIMES', 'arg_num': 1, 'unknown': 0x100, 'addr': 0x10d5cbf0, 'func': pb_empty},
    {'index': 0x13c, 'name': 'SM_FREE_NODE_N', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52790, 'func': pb_empty},
    {'index': 0x13d, 'name': 'SM_CONV_DBL_RVALUE_TO_PTR', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59d80, 'func': pb_empty},
    {'index': 0x13e, 'name': 'SM_COPY_EXPR_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5c5b0, 'func': pb_empty},
    {'index': 0x13f, 'name': 'SM_BREAKPOINT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d57330},
    {'index': 0x140, 'name': 'SM_INDEX_ERR_CHK', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d585e0, 'func': pb_array_index},
    {'index': 0x141, 'name': 'SM_DOT_DOUBLE', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d58af0, 'func': pb_dot},
    {'index': 0x142, 'name': 'SM_DOT_DEC', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d56d40, 'func': pb_dot},
    {'index': 0x143, 'name': 'SM_INDEX_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d56f50, 'func': pb_array_index},
    {'index': 0x144, 'name': 'SM_INDEX_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d57450, 'func': pb_array_index},
    {'index': 0x145, 'name': 'SM_INDEX_ERR_CHK_DBL', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d576c0, 'func': pb_array_index},
    {'index': 0x146, 'name': 'SM_INDEX_ERR_CHK_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c590, 'func': pb_array_index},
    {'index': 0x147, 'name': 'SM_GLOBFUNCCALL_DOUBLE', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x148, 'name': 'SM_GLOBFUNCCALL_DEC', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x149, 'name': 'SM_SYSFUNCCALL_DOUBLE', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x14a, 'name': 'SM_SYSFUNCCALL_DEC', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x14b, 'name': 'SM_DLLFUNCCALL_DOUBLE', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x14c, 'name': 'SM_DLLFUNCCALL_DEC', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d59f50},
    {'index': 0x14d, 'name': 'SM_DOTFUNCCALL_DOUBLE', 'arg_num': 4, 'unknown': 0x0, 'addr': 0x10d5a110, 'func': pb_call_func},
    {'index': 0x14e, 'name': 'SM_DOTFUNCCALL_DEC', 'arg_num': 4, 'unknown': 0x0, 'addr': 0x10d54350, 'func': pb_call_func},
    {'index': 0x14f, 'name': 'SM_PUSH_LOCAL_VAR_DOUBLE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d544d0, 'func': pb_push},
    {'index': 0x150, 'name': 'SM_PUSH_LOCAL_VAR_DEC', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54700, 'func': pb_push},
    {'index': 0x151, 'name': 'SM_PUSH_SHARED_VAR_DOUBLE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d548a0, 'func': pb_push},
    {'index': 0x152, 'name': 'SM_PUSH_SHARED_VAR_DEC', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54e00, 'func': pb_push},
    {'index': 0x153, 'name': 'SM_PUSH_LOCAL_GLOBREF_DOUBLE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54f80, 'func': pb_push},
    {'index': 0x154, 'name': 'SM_PUSH_LOCAL_GLOBREF_DEC', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55190, 'func': pb_push},
    {'index': 0x155, 'name': 'SM_PUSH_LOCAL_ARGREF_DOUBLE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55310},
    {'index': 0x156, 'name': 'SM_PUSH_LOCAL_ARGREF_DEC', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55500},
    {'index': 0x157, 'name': 'SM_PUSH_SHARED_GLOBREF_DOUBLE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55680},
    {'index': 0x158, 'name': 'SM_PUSH_SHARED_GLOBREF_DEC', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d4d380},
    {'index': 0x159, 'name': 'SM_ASSIGN_ANY', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d52a40, 'func': pb_assign},
    {'index': 0x15a, 'name': 'SM_CNV_ANY_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52be0, 'func': pb_empty},
    {'index': 0x15b, 'name': 'SM_CNV_ANY_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52f60, 'func': pb_empty},
    {'index': 0x15c, 'name': 'SM_CNV_ANY_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53150, 'func': pb_empty},
    {'index': 0x15d, 'name': 'SM_CNV_ANY_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53340, 'func': pb_empty},
    {'index': 0x15e, 'name': 'SM_CNV_ANY_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d535f0, 'func': pb_empty},
    {'index': 0x15f, 'name': 'SM_CNV_ANY_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d537b0, 'func': pb_empty},
    {'index': 0x160, 'name': 'SM_CNV_ANY_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53b30, 'func': pb_empty},
    {'index': 0x161, 'name': 'SM_CNV_ANY_TO_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53bf0, 'func': pb_empty},
    {'index': 0x162, 'name': 'SM_CNV_ANY_TO_BOOL', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53c60, 'func': pb_in_func},
    {'index': 0x163, 'name': 'SM_CNV_ANY_TO_BINARY', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53d20, 'func': pb_in_func},
    {'index': 0x164, 'name': 'SM_CNV_ANY_TO_DATE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53d90, 'func': pb_in_func},
    {'index': 0x165, 'name': 'SM_CNV_ANY_TO_TIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53e00, 'func': pb_in_func},
    {'index': 0x166, 'name': 'SM_CNV_ANY_TO_DATETIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53e70, 'func': pb_in_func},
    {'index': 0x167, 'name': 'SM_CNV_ANY_TO_CHAR', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53f20, 'func': pb_in_func},
    {'index': 0x168, 'name': 'SM_CNV_ANY_TO_HANDLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d53f90, 'func': pb_in_func},
    {'index': 0x169, 'name': 'SM_CNV_ANY_TO_ENUM', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d540b0, 'func': pb_in_func},
    {'index': 0x16a, 'name': 'SM_CNV_ANY_TO_OBJECT', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d52810, 'func': pb_empty},
    {'index': 0x16b, 'name': 'SM_CONV_DEC_RVALUE_TO_PTR', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59e20},
    {'index': 0x16c, 'name': 'SM_COPY_EXPR_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d59530, 'func': pb_empty},
    {'index': 0x16d, 'name': 'SM_CREATE_EXT_OBJ', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d5c590, 'func': pb_create_obj},
    {'index': 0x16e, 'name': 'SM_GLOBFUNCCALL_ANY', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x16f, 'name': 'SM_SYSFUNCCALL_ANY', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x170, 'name': 'SM_DLLFUNCCALL_ANY', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5a1e0},
    {'index': 0x171, 'name': 'SM_DOTFUNCCALL_ANY', 'arg_num': 4, 'unknown': 0x0, 'addr': 0x10d545c0, 'func': pb_call_func},
    {'index': 0x172, 'name': 'SM_PUSH_LOCAL_VAR_ANY', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d549a0, 'func': pb_push},
    {'index': 0x173, 'name': 'SM_PUSH_SHARED_VAR_ANY', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55070},
    {'index': 0x174, 'name': 'SM_PUSH_LOCAL_GLOBREF_ANY', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55400},
    {'index': 0x175, 'name': 'SM_PUSH_LOCAL_ARGREF_ANY', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55770},
    {'index': 0x176, 'name': 'SM_PUSH_SHARED_GLOBREF_ANY', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d4f0b0},
    {'index': 0x177, 'name': 'SM_ADD_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f6d0, 'func': pb_add},
    {'index': 0x178, 'name': 'SM_SUB_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fd50, 'func': pb_sub},
    {'index': 0x179, 'name': 'SM_MULT_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d501b0, 'func': pb_mul},
    {'index': 0x17a, 'name': 'SM_DIV_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50b00, 'func': pb_div},
    {'index': 0x17b, 'name': 'SM_POWER_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50dd0, 'func': pb_power},
    {'index': 0x17c, 'name': 'SM_NEGATE_ANY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d477d0, 'func': pb_negate},
    {'index': 0x17d, 'name': 'SM_EQ_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48120, 'func': pb_compare},
    {'index': 0x17e, 'name': 'SM_NE_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48a00, 'func': pb_compare},
    {'index': 0x17f, 'name': 'SM_GT_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d492e0, 'func': pb_compare},
    {'index': 0x180, 'name': 'SM_LT_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49bc0, 'func': pb_compare},
    {'index': 0x181, 'name': 'SM_GE_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4a4a0, 'func': pb_compare},
    {'index': 0x182, 'name': 'SM_LE_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5dfe0, 'func': pb_compare},
    {'index': 0x183, 'name': 'SM_AND_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5e020, 'func': pb_compare},
    {'index': 0x184, 'name': 'SM_OR_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5e060, 'func': pb_compare},
    {'index': 0x185, 'name': 'SM_NOT_ANY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d58db0, 'func': pb_not},
    {'index': 0x186, 'name': 'SM_DOT_ANY', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d57080},
    {'index': 0x187, 'name': 'SM_INDEX_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d57830, 'func': pb_array_index},
    {'index': 0x188, 'name': 'SM_INDEX_ERR_CHK_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5ae30, 'func': pb_array_index},
    {'index': 0x189, 'name': 'SM_INT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5aea0, 'func': pb_empty},
    {'index': 0x18a, 'name': 'SM_ABS_LONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5aee0, 'func': pb_in_func},
    {'index': 0x18b, 'name': 'SM_ABS_DOUBLE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b040, 'func': pb_in_func},
    {'index': 0x18c, 'name': 'SM_ASC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b0a0},
    {'index': 0x18d, 'name': 'SM_BLOB', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5b1b0, 'func': pb_in_func},
    {'index': 0x18e, 'name': 'SM_CEILING', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b280, 'func': pb_in_func},
    {'index': 0x18f, 'name': 'SM_COS', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b2a0, 'func': pb_in_func},
    {'index': 0x190, 'name': 'SM_EXP', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b2e0, 'func': pb_in_func},
    {'index': 0x191, 'name': 'SM_FACT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b3e0},
    {'index': 0x192, 'name': 'SM_INTHIGH', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b420},
    {'index': 0x193, 'name': 'SM_INTLOW', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b460},
    {'index': 0x194, 'name': 'SM_ISDATE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b4f0, 'func': pb_in_func},
    {'index': 0x195, 'name': 'SM_ISNULL', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b570, 'func': pb_in_func},
    {'index': 0x196, 'name': 'SM_ISNUMBER', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b5e0, 'func': pb_in_func},
    {'index': 0x197, 'name': 'SM_ISTIME', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b660, 'func': pb_in_func},
    {'index': 0x198, 'name': 'SM_ISVALID', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b6c0, 'func': pb_in_func},
    {'index': 0x199, 'name': 'SM_LEN_STRING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b730, 'func': pb_in_func},
    {'index': 0x19a, 'name': 'SM_LEN_BINARY', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b790, 'func': pb_in_func},
    {'index': 0x19b, 'name': 'SM_LOG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b800, 'func': pb_in_func},
    {'index': 0x19c, 'name': 'SM_LOGTEN', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b880, 'func': pb_in_func},
    {'index': 0x19d, 'name': 'SM_LOWER', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5b900, 'func': pb_in_func},
    {'index': 0x19e, 'name': 'SM_PI', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b9c0, 'func': pb_in_func},
    {'index': 0x19f, 'name': 'SM_RAND_LONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b920, 'func': pb_math},
    {'index': 0x1a0, 'name': 'SM_RAND_DOUBLE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b9f0, 'func': pb_math},
    {'index': 0x1a1, 'name': 'SM_SIN', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5ba10, 'func': pb_in_func},
    {'index': 0x1a2, 'name': 'SM_SQRT', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5ba80, 'func': pb_in_func},
    {'index': 0x1a3, 'name': 'SM_TAN', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5bab0, 'func': pb_in_func},
    {'index': 0x1a4, 'name': 'SM_UPPER', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5c590, 'func': pb_in_func},
    {'index': 0x1a5, 'name': 'SM_CONV_TO_REFPAK', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d561c0},
    {'index': 0x1a6, 'name': 'SM_PUSH_LOCAL_GLOBREF_RP', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d56280, 'func': pb_push},
    {'index': 0x1a7, 'name': 'SM_PUSH_LOCAL_ARGREF_RP', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d56370},
    {'index': 0x1a8, 'name': 'SM_PUSH_SHARED_GLOBREF_RP', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d56050},
    {'index': 0x1a9, 'name': 'SM_PUSH_LOCAL_VAR_RP', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d56100, 'func': pb_push},
    {'index': 0x1aa, 'name': 'SM_PUSH_SHARED_VAR_RP', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d56560, 'func': pb_push},
    {'index': 0x1ab, 'name': 'SM_TRANSFORM_BOUNDED_TO_BOUNDED', 'arg_num': 5, 'unknown': 0x100, 'addr': 0x10d56670, 'func': pb_empty},
    {'index': 0x1ac, 'name': 'SM_TRANSFORM_BOUNDED_TO_UNBOUNDED', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d566c0, 'func': pb_empty},
    {'index': 0x1ad, 'name': 'SM_TRANSFORM_UNBOUNDED_TO_BOUNDED', 'arg_num': 4, 'unknown': 0x100, 'addr': 0x10d567d0, 'func': pb_empty},
    {'index': 0x1ae, 'name': 'SM_TRANSFORM_UNBOUNDED_TO_UNBOUNDED', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d57b00, 'func': pb_empty},
    {'index': 0x1af, 'name': 'SM_CALC_UNBOUNDED_ARRAY_BOUND', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d57ba0, 'func': pb_empty},
    {'index': 0x1b0, 'name': 'SM_CALC_SIMPLE_ARRAY_BOUND', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d57c50, 'func': pb_empty},
    {'index': 0x1b1, 'name': 'SM_CALC_COMPLEX_ARRAY_BOUND', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d56950, 'func': pb_complex_array_index},
    {'index': 0x1b2, 'name': 'SM_BUILD_UNBOUNDED_ARRAYLIST', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d56aa0, 'func': pb_build_array_list},
    {'index': 0x1b3, 'name': 'SM_BUILD_BOUNDED_ARRAYLIST', 'arg_num': 5, 'unknown': 0x100, 'addr': 0x10d5c590},
    {'index': 0x1b4, 'name': 'SM_TRANSFORM_ARRAYLIST_TO_UNBOUNDED', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590, 'func': pb_empty},
    {'index': 0x1b5, 'name': 'SM_TRANSFORM_ARRAYLIST_TO_BOUNDED', 'arg_num': 5, 'unknown': 0x0, 'addr': 0x10d5cc20, 'func': pb_empty},
    {'index': 0x1b6, 'name': 'SM_FREE_REF_PAK_N', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d57d80, 'func': pb_empty},
    {'index': 0x1b7, 'name': 'SM_ARRAY_BOUND_INFO', 'arg_num': 4, 'unknown': 0x2, 'addr': 0x10d57e20},
    {'index': 0x1b8, 'name': 'SM_LOWERBOUND', 'arg_num': 2, 'unknown': 0x100, 'addr': 0x10d57f60, 'func': pb_array_lowerbound},
    {'index': 0x1b9, 'name': 'SM_UPPERBOUND', 'arg_num': 2, 'unknown': 0x100, 'addr': 0x10d4df40, 'func': pb_array_upperbound},
    {'index': 0x1ba, 'name': 'SM_INCR_ANY', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4eb20, 'func': pb_incr},
    {'index': 0x1bb, 'name': 'SM_DECR_ANY', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d56430, 'func': pb_decr},
    {'index': 0x1bc, 'name': 'SM_PUSH_FUNC_CLASS', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d5a450, 'func': pb_call_func},
    {'index': 0x1bd, 'name': 'SM_CLASS_CALL', 'arg_num': 3, 'unknown': 0xffffffff, 'addr': 0x10d5a720, 'func': pb_call_func},
    {'index': 0x1be, 'name': 'SM_CLASS_CALL_DEC', 'arg_num': 3, 'unknown': 0xffffffff, 'addr': 0x10d5a520, 'func': pb_call_func},
    {'index': 0x1bf, 'name': 'SM_CLASS_CALL_DOUBLE', 'arg_num': 3, 'unknown': 0xffffffff, 'addr': 0x10d5a810, 'func': pb_call_func},
    {'index': 0x1c0, 'name': 'SM_CLASS_CALL_ANY', 'arg_num': 3, 'unknown': 0xffffffff, 'addr': 0x10d57a20, 'func': pb_call_func},
    {'index': 0x1c1, 'name': 'SM_INDEX_RP', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5d9b0, 'func': pb_array_index},
    {'index': 0x1c2, 'name': 'SM_DBDELETEWITHCURS', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d5dc60},
    {'index': 0x1c3, 'name': 'SM_DBEXECUTEIMMED', 'arg_num': 0, 'unknown': 0xfffffffe, 'addr': 0x10d5ddb0,'func': pb_db_execute},
    {'index': 0x1c4, 'name': 'SM_DBEXECDYNWITHDESC', 'arg_num': 2, 'unknown': 0xfffffffd, 'addr': 0x10d5d3e0},
    {'index': 0x1c5, 'name': 'SM_DBFETCHWITHDESC', 'arg_num': 2, 'unknown': 0xfffffffd, 'addr': 0x10d5d6b0},
    {'index': 0x1c6, 'name': 'SM_DBOPENDYNWITHDESC', 'arg_num': 2, 'unknown': 0xfffffffd, 'addr': 0x10d5d150},
    {'index': 0x1c7, 'name': 'SM_DBUPDATEWITHCURS', 'arg_num': 3, 'unknown': 0x100, 'addr': 0x10d59680},
    {'index': 0x1c8, 'name': 'SM_CREATE_USING', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d56920},
    {'index': 0x1c9, 'name': 'SM_TRANSFORM_ANY_TO_UNBOUNDED', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d56810},
    {'index': 0x1ca, 'name': 'SM_TRANSFORM_ANY_TO_BOUNDED', 'arg_num': 4, 'unknown': 0x100, 'addr': 0x10d5cc70},
    {'index': 0x1cb, 'name': 'SM_FREE_INV_METH_ARGS', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d54aa0, 'func': pb_empty},
    {'index': 0x1cc, 'name': 'SM_PUSH_NULL', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d59d50},
    {'index': 0x1cd, 'name': 'SM_COPY_LVALUE_ANY', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5ad70, 'func': pb_copy},
    {'index': 0x1ce, 'name': 'SM_ENTER_EMBEDDED', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5adc0, 'func': pb_empty},
    {'index': 0x1cf, 'name': 'SM_EXIT_EMBEDDED', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d592b0, 'func': pb_empty},
    {'index': 0x1d0, 'name': 'SM_DOT_FLD_UPDATE_INDEX_RP', 'arg_num': 0, 'unknown': 0xfffffffe, 'addr': 0x10d52970, 'func': pb_array_index2},
    {'index': 0x1d1, 'name': 'SM_CNV_STRING_TO_BOUNDED_CHARARRAY', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d54c30},
    {'index': 0x1d2, 'name': 'SM_PUSH_NTH_PARENT', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d5bb30},
    {'index': 0x1d3, 'name': 'SM_MOD_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bba0, 'func': pb_mod},
    {'index': 0x1d4, 'name': 'SM_MOD_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bc10, 'func': pb_mod},
    {'index': 0x1d5, 'name': 'SM_MOD_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bcf0, 'func': pb_mod},
    {'index': 0x1d6, 'name': 'SM_MOD_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bdb0, 'func': pb_mod},
    {'index': 0x1d7, 'name': 'SM_MOD_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5af30, 'func': pb_mod},
    {'index': 0x1d8, 'name': 'SM_ABS_DEC', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5afa0, 'func': pb_in_func},
    {'index': 0x1d9, 'name': 'SM_ABS_ANY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b1e0, 'func': pb_in_func},
    {'index': 0x1da, 'name': 'SM_CEILING_ANY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5be50, 'func': pb_in_func},
    {'index': 0x1db, 'name': 'SM_MIN_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5beb0, 'func': pb_math},
    {'index': 0x1dc, 'name': 'SM_MIN_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bf10, 'func': pb_math},
    {'index': 0x1dd, 'name': 'SM_MIN_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bfd0, 'func': pb_math},
    {'index': 0x1de, 'name': 'SM_MIN_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c0a0, 'func': pb_math},
    {'index': 0x1df, 'name': 'SM_MIN_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c140, 'func': pb_math},
    {'index': 0x1e0, 'name': 'SM_MAX_LONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c1a0, 'func': pb_math},
    {'index': 0x1e1, 'name': 'SM_MAX_ULONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c200, 'func': pb_math},
    {'index': 0x1e2, 'name': 'SM_MAX_DOUBLE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c2c0, 'func': pb_math},
    {'index': 0x1e3, 'name': 'SM_MAX_DEC', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c390, 'func': pb_math},
    {'index': 0x1e4, 'name': 'SM_MAX_ANY', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c5c0, 'func': pb_math},
    {'index': 0x1e5, 'name': 'SM_PUSH_TRY', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c5f0},
    {'index': 0x1e6, 'name': 'SM_POP_TRY', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5c610},
    {'index': 0x1e7, 'name': 'SM_CATCH_EXCEPTION', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5c730},
    {'index': 0x1e8, 'name': 'SM_THROW_EXCEPTION', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c8b0},
    {'index': 0x1e9, 'name': 'SM_GOSUB', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5c8f0},
    {'index': 0x1ea, 'name': 'SM_RETURN_SUB', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d51160},
    {'index': 0x1eb, 'name': 'SM_CNV_INT_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d513e0, 'func': pb_empty},
    {'index': 0x1ec, 'name': 'SM_CNV_UINT_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d518c0, 'func': pb_empty},
    {'index': 0x1ed, 'name': 'SM_CNV_LONG_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51b40, 'func': pb_empty},
    {'index': 0x1ee, 'name': 'SM_CNV_ULONG_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51f40, 'func': pb_empty},
    {'index': 0x1ef, 'name': 'SM_CNV_DEC_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d521e0, 'func': pb_in_func},
    {'index': 0x1f0, 'name': 'SM_CNV_FLOAT_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52410, 'func': pb_in_func},
    {'index': 0x1f1, 'name': 'SM_CNV_DOUBLE_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52530, 'func': pb_in_func},
    {'index': 0x1f2, 'name': 'SM_CNV_LONGLONG_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52570, 'func': pb_empty},
    {'index': 0x1f3, 'name': 'SM_CNV_LONGLONG_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d525f0, 'func': pb_empty},
    {'index': 0x1f4, 'name': 'SM_CNV_LONGLONG_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52630, 'func': pb_empty},
    {'index': 0x1f5, 'name': 'SM_CNV_LONGLONG_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52670, 'func': pb_empty},
    {'index': 0x1f6, 'name': 'SM_CNV_LONGLONG_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52710, 'func': pb_empty},
    {'index': 0x1f7, 'name': 'SM_CNV_LONGLONG_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52750, 'func': pb_empty},
    {'index': 0x1f8, 'name': 'SM_CNV_LONGLONG_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d4f000, 'func': pb_empty},
    {'index': 0x1f9, 'name': 'SM_ADD_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f620, 'func': pb_add},
    {'index': 0x1fa, 'name': 'SM_SUB_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fc80, 'func': pb_sub},
    {'index': 0x1fb, 'name': 'SM_MULT_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d501a0, 'func': pb_mul},
    {'index': 0x1fc, 'name': 'SM_DIV_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50a40, 'func': pb_div},
    {'index': 0x1fd, 'name': 'SM_POWER_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50da0, 'func': pb_power},
    {'index': 0x1fe, 'name': 'SM_NEGATE_LONGLONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d55ae0, 'func': pb_negate},
    {'index': 0x1ff, 'name': 'SM_PUSH_CONST_LONGLONG', 'arg_num': 2, 'unknown': 0x1, 'addr': 0x10d54410, 'func': pb_push_const},
    {'index': 0x200, 'name': 'SM_PUSH_LOCAL_VAR_LONGLONG', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d54ec0, 'func': pb_push},
    {'index': 0x201, 'name': 'SM_PUSH_LOCAL_GLOBREF_LONGLONG', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d55250, 'func': pb_push},
    {'index': 0x202, 'name': 'SM_PUSH_LOCAL_ARGREF_LONGLONG', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d547d0, 'func': pb_push},
    {'index': 0x203, 'name': 'SM_PUSH_SHARED_VAR_LONGLONG', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d555c0, 'func': pb_push},
    {'index': 0x204, 'name': 'SM_PUSH_SHARED_GLOBREF_LONGLONG', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d4ce80},
    {'index': 0x205, 'name': 'SM_ASSIGN_LONGLONG', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d59820, 'func': pb_assign},
    {'index': 0x206, 'name': 'SM_COPY_CONST_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d4aeb0, 'func': pb_empty},
    {'index': 0x207, 'name': 'SM_ADDASSIGN_LONGLONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4ba80, 'func': pb_add_assign},
    {'index': 0x208, 'name': 'SM_SUBASSIGN_LONGLONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4c640, 'func': pb_sub_assign},
    {'index': 0x209, 'name': 'SM_MULTASSIGN_LONGLONG', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4dd00, 'func': pb_mul_assign},
    {'index': 0x20a, 'name': 'SM_INCR_LONGLONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e8e0, 'func': pb_incr},
    {'index': 0x20b, 'name': 'SM_DECR_LONGLONG', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d59a90, 'func': pb_decr},
    {'index': 0x20c, 'name': 'SM_COPY_LVALUE_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d5af00, 'func': pb_empty},
    {'index': 0x20d, 'name': 'SM_ABS_LONGLONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d5b970, 'func': pb_in_func},
    {'index': 0x20e, 'name': 'SM_RAND_LONGLONG', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d472c0, 'func': pb_math},
    {'index': 0x20f, 'name': 'SM_EQ_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47bf0, 'func': pb_compare},
    {'index': 0x210, 'name': 'SM_NE_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48550, 'func': pb_compare},
    {'index': 0x211, 'name': 'SM_GT_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48e30, 'func': pb_compare},
    {'index': 0x212, 'name': 'SM_LT_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49710, 'func': pb_compare},
    {'index': 0x213, 'name': 'SM_GE_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49ff0, 'func': pb_compare},
    {'index': 0x214, 'name': 'SM_LE_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bc80, 'func': pb_compare},
    {'index': 0x215, 'name': 'SM_MOD_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5bf70, 'func': pb_mod},
    {'index': 0x216, 'name': 'SM_MIN_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c260, 'func': pb_math},
    {'index': 0x217, 'name': 'SM_MAX_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d5c590, 'func': pb_math},
    {'index': 0x218, 'name': 'SM_GLOBFUNCCALL_LONGLONG', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x219, 'name': 'SM_SYSFUNCCALL_LONGLONG', 'arg_num': 2, 'unknown': 0x0, 'addr': 0x10d5c590},
    {'index': 0x21a, 'name': 'SM_DLLFUNCCALL_LONGLONG', 'arg_num': 3, 'unknown': 0x0, 'addr': 0x10d5a020},
    {'index': 0x21b, 'name': 'SM_DOTFUNCCALL_LONGLONG', 'arg_num': 4, 'unknown': 0x0, 'addr': 0x10d5a610, 'func': pb_call_func},
    {'index': 0x21c, 'name': 'SM_CLASS_CALL_LONGLONG', 'arg_num': 3, 'unknown': 0xffffffff, 'addr': 0x10d59dd0, 'func': pb_call_func},
    {'index': 0x21d, 'name': 'SM_COPY_EXPR_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d58860, 'func': pb_empty},
    {'index': 0x21e, 'name': 'SM_DOT_LONGLONG', 'arg_num': 1, 'unknown': 0xffffffff, 'addr': 0x10d56e40, 'func': pb_dot},
    {'index': 0x21f, 'name': 'SM_INDEX_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d53960, 'func': pb_array_index},
    {'index': 0x220, 'name': 'SM_CNV_ANY_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d527d0, 'func': pb_empty},
    {'index': 0x221, 'name': 'SM_CONV_LONGLONG_RVALUE_TO_PTR', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d57580},
    {'index': 0x222, 'name': 'SM_INDEX_ERR_CHK_LONGLONG', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d558a0},
    {'index': 0x223, 'name': 'SM_PUSH_CONST_BYTE', 'arg_num': 1, 'unknown': 0x1, 'addr': 0x10d50f70, 'func': pb_push_const},
    {'index': 0x224, 'name': 'SM_CNV_INT_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d511f0, 'func': pb_empty},
    {'index': 0x225, 'name': 'SM_CNV_UINT_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51730, 'func': pb_empty},
    {'index': 0x226, 'name': 'SM_CNV_LONG_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51990, 'func': pb_empty},
    {'index': 0x227, 'name': 'SM_CNV_ULONG_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51cb0, 'func': pb_empty},
    {'index': 0x228, 'name': 'SM_CNV_DEC_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52050, 'func': pb_in_func},
    {'index': 0x229, 'name': 'SM_CNV_FLOAT_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52350, 'func': pb_in_func},
    {'index': 0x22a, 'name': 'SM_CNV_DOUBLE_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d52da0, 'func': pb_in_func},
    {'index': 0x22b, 'name': 'SM_CNV_ANY_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d525b0, 'func': pb_empty},
    {'index': 0x22c, 'name': 'SM_CNV_LONGLONG_TO_BYTE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51430, 'func': pb_empty},
    {'index': 0x22d, 'name': 'SM_CNV_BYTE_TO_INT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51470, 'func': pb_empty},
    {'index': 0x22e, 'name': 'SM_CNV_BYTE_TO_UINT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d514b0, 'func': pb_empty},
    {'index': 0x22f, 'name': 'SM_CNV_BYTE_TO_LONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d514f0, 'func': pb_empty},
    {'index': 0x230, 'name': 'SM_CNV_BYTE_TO_ULONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51530, 'func': pb_empty},
    {'index': 0x231, 'name': 'SM_CNV_BYTE_TO_DEC', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d515c0, 'func': pb_empty},
    {'index': 0x232, 'name': 'SM_CNV_BYTE_TO_FLOAT', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51610, 'func': pb_empty},
    {'index': 0x233, 'name': 'SM_CNV_BYTE_TO_DOUBLE', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d51660, 'func': pb_empty},
    {'index': 0x234, 'name': 'SM_CNV_BYTE_TO_LONGLONG', 'arg_num': 1, 'unknown': 0x0, 'addr': 0x10d4ecd0, 'func': pb_empty},
    {'index': 0x235, 'name': 'SM_ADD_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f2f0, 'func': pb_add},
    {'index': 0x236, 'name': 'SM_SUB_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4f910, 'func': pb_sub},
    {'index': 0x237, 'name': 'SM_MULT_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d4fed0, 'func': pb_mul},
    {'index': 0x238, 'name': 'SM_DIV_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50490, 'func': pb_div},
    {'index': 0x239, 'name': 'SM_POWER_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d50ca0, 'func': pb_power},
    {'index': 0x23a, 'name': 'SM_NEGATE_BYTE', 'arg_num': 0, 'unknown': 0x0, 'addr': 0x10d4d5b0, 'func': pb_negate},
    {'index': 0x23b, 'name': 'SM_INCR_BYTE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4e190, 'func': pb_incr},
    {'index': 0x23c, 'name': 'SM_DECR_BYTE', 'arg_num': 2, 'unknown': 0xffffffff, 'addr': 0x10d4ca90, 'func': pb_decr},
    {'index': 0x23d, 'name': 'SM_ASSIGN_BYTE', 'arg_num': 1, 'unknown': 0xfffffffe, 'addr': 0x10d4a6a0, 'func': pb_assign},
    {'index': 0x23e, 'name': 'SM_ADDASSIGN_BYTE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4b270, 'func': pb_add_assign},
    {'index': 0x23f, 'name': 'SM_SUBASSIGN_BYTE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d4be30, 'func': pb_sub_assign},
    {'index': 0x240, 'name': 'SM_MULTASSIGN_BYTE', 'arg_num': 2, 'unknown': 0xfffffffe, 'addr': 0x10d46fc0, 'func': pb_mul_assign},
    {'index': 0x241, 'name': 'SM_EQ_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d47910, 'func': pb_compare},
    {'index': 0x242, 'name': 'SM_NE_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48260, 'func': pb_compare},
    {'index': 0x243, 'name': 'SM_GT_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d48b40, 'func': pb_compare},
    {'index': 0x244, 'name': 'SM_LT_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49420, 'func': pb_compare},
    {'index': 0x245, 'name': 'SM_GE_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x10d49d00, 'func': pb_compare},
    {'index': 0x246, 'name': 'SM_LE_BYTE', 'arg_num': 0, 'unknown': 0xffffffff, 'addr': 0x0, 'func': pb_compare},
]