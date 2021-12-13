from pbd.definitions import FuncInfo, ParamInfo

c_40CF = dict()

item = FuncInfo(name = "abs", footprint = "DD", delegate_name = "fnAbs", 
                    m_10 = 0x46, m_14 = 0x0, m_16 = 0x0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x0] = item


item = FuncInfo(name = "acos", footprint = "DD", delegate_name = "fnArcCos", 
                    m_10 = 0x46, m_14 = 0x1, m_16 = 0x1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x1] = item


item = FuncInfo(name = "asc", footprint = "NXS", delegate_name = "fnAsc", 
                    m_10 = 0x46, m_14 = 0x2, m_16 = 0x2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x9, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x2] = item


item = FuncInfo(name = "asca", footprint = "IXS", delegate_name = "fnAscA", 
                    m_10 = 0x46, m_14 = 0x3, m_16 = 0x3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x3] = item


item = FuncInfo(name = "asin", footprint = "DD", delegate_name = "fnArcSin", 
                    m_10 = 0x46, m_14 = 0x4, m_16 = 0x4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x4] = item


item = FuncInfo(name = "atan", footprint = "DD", delegate_name = "fnArcTan", 
                    m_10 = 0x46, m_14 = 0x5, m_16 = 0x5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x5] = item


item = FuncInfo(name = "beep", footprint = "II", delegate_name = "fnBeep", 
                    m_10 = 0x46, m_14 = 0x6, m_16 = 0x6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "count", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x6] = item


item = FuncInfo(name = "blob", footprint = "OA", delegate_name = "fnBlob", 
                    m_10 = 0x46, m_14 = 0x7, m_16 = 0x7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "stringorbyetarray", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x7] = item


item = FuncInfo(name = "blob", footprint = "OSCencoding.", delegate_name = "fnBlob", 
                    m_10 = 0x46, m_14 = 0x8, m_16 = 0x8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x4015, m_a = 0x8))
c_40CF[0x8] = item


item = FuncInfo(name = "blobedit", footprint = "UROUA", delegate_name = "fnBlobEdit", 
                    m_10 = 0x46, m_14 = 0x9, m_16 = 0x9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xa, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x9] = item


item = FuncInfo(name = "blobedit", footprint = "UROUACencoding.", delegate_name = "fnBlobEdit", 
                    m_10 = 0x46, m_14 = 0xa, m_16 = 0xa, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xa, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x4015, m_a = 0x8))
c_40CF[0xa] = item


item = FuncInfo(name = "blobmid", footprint = "OOU", delegate_name = "fnBlobMid", 
                    m_10 = 0x46, m_14 = 0xb, m_16 = 0xb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0xb] = item


item = FuncInfo(name = "blobmid", footprint = "OOUU", delegate_name = "fnBlobMid", 
                    m_10 = 0x46, m_14 = 0xc, m_16 = 0xc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0xc] = item


item = FuncInfo(name = "byte", footprint = "EA", delegate_name = "fnByte", 
                    m_10 = 0x46, m_14 = 0xd, m_16 = 0xd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x15, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0xd] = item


item = FuncInfo(name = "ceiling", footprint = "DD", delegate_name = "fnCeiling", 
                    m_10 = 0x46, m_14 = 0xe, m_16 = 0xe, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xe] = item


item = FuncInfo(name = "char", footprint = "HA", delegate_name = "fnChar", 
                    m_10 = 0x46, m_14 = 0xf, m_16 = 0xf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x12, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0xf] = item


item = FuncInfo(name = "chara", footprint = "HA", delegate_name = "fnCharA", 
                    m_10 = 0x46, m_14 = 0x10, m_16 = 0x10, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x12, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x10] = item


item = FuncInfo(name = "changedirectory", footprint = "IS", delegate_name = "fnChangeDirectory", 
                    m_10 = 0x46, m_14 = 0x11, m_16 = 0x11, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x11] = item


item = FuncInfo(name = "choosecolor", footprint = "IRL", delegate_name = "fnChooseColor", 
                    m_10 = 0x46, m_14 = 0x12, m_16 = 0x12, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x2))
c_40CF[0x12] = item


item = FuncInfo(name = "choosecolor", footprint = "IRLRL[]", delegate_name = "fnChooseColor", 
                    m_10 = 0x46, m_14 = 0x13, m_16 = 0x13, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xa75c, type_id = 0x2, m_a = 0x3))
c_40CF[0x13] = item


item = FuncInfo(name = "classname", footprint = "SXA", delegate_name = "fnClassName", 
                    m_10 = 0x46, m_14 = 0x14, m_16 = 0x14, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x6))
c_40CF[0x14] = item


item = FuncInfo(name = "clipboard", footprint = "S", delegate_name = "fnClipboardSys", 
                    m_10 = 0x46, m_14 = 0x15, m_16 = 0x15, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x15] = item


item = FuncInfo(name = "clipboard", footprint = "SS", delegate_name = "fnClipboardSys", 
                    m_10 = 0x46, m_14 = 0x16, m_16 = 0x16, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x16] = item


item = FuncInfo(name = "close", footprint = "ICwindow.", delegate_name = "fnCloseWnd", 
                    m_10 = 0x46, m_14 = 0x17, m_16 = 0x17, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0x17] = item


item = FuncInfo(name = "closewithreturn", footprint = "ICwindow.S", delegate_name = "fnCloseWithReturn", 
                    m_10 = 0x46, m_14 = 0x18, m_16 = 0x18, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x18] = item


item = FuncInfo(name = "closewithreturn", footprint = "ICwindow.D", delegate_name = "fnCloseWithReturn", 
                    m_10 = 0x46, m_14 = 0x19, m_16 = 0x19, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x19] = item


item = FuncInfo(name = "closewithreturn", footprint = "ICwindow.Cpowerobject.", delegate_name = "fnCloseWithReturn", 
                    m_10 = 0x46, m_14 = 0x1a, m_16 = 0x1a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x4076, m_a = 0x0))
c_40CF[0x1a] = item


item = FuncInfo(name = "closechannel", footprint = "IL", delegate_name = "fnCloseChannel", 
                    m_10 = 0x46, m_14 = 0x1b, m_16 = 0x1b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1b] = item


item = FuncInfo(name = "closechannel", footprint = "ILL", delegate_name = "fnCloseChannel", 
                    m_10 = 0x46, m_14 = 0x1c, m_16 = 0x1c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1c] = item


item = FuncInfo(name = "commandparm", footprint = "S", delegate_name = "fnCommandParm", 
                    m_10 = 0x46, m_14 = 0x1d, m_16 = 0x1d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x1d] = item


item = FuncInfo(name = "cos", footprint = "DD", delegate_name = "fnCos", 
                    m_10 = 0x46, m_14 = 0x1e, m_16 = 0x1e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x1e] = item


item = FuncInfo(name = "cpu", footprint = "L", delegate_name = "fnCPU", 
                    m_10 = 0x46, m_14 = 0x1f, m_16 = 0x1f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x1f] = item


item = FuncInfo(name = "createdirectory", footprint = "IS", delegate_name = "fnCreateDirectory", 
                    m_10 = 0x46, m_14 = 0x20, m_16 = 0x20, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x20] = item


item = FuncInfo(name = "date", footprint = "YA", delegate_name = "fnDate", 
                    m_10 = 0x46, m_14 = 0x21, m_16 = 0x21, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x21] = item


item = FuncInfo(name = "date", footprint = "YIII", delegate_name = "fnDate", 
                    m_10 = 0x46, m_14 = 0x22, m_16 = 0x22, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x22] = item


item = FuncInfo(name = "datetime", footprint = "WA", delegate_name = "fnDateTime", 
                    m_10 = 0x46, m_14 = 0x23, m_16 = 0x23, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xe, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x23] = item


item = FuncInfo(name = "datetime", footprint = "WYT", delegate_name = "fnDateTime", 
                    m_10 = 0x46, m_14 = 0x24, m_16 = 0x24, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xe, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
c_40CF[0x24] = item


item = FuncInfo(name = "day", footprint = "IY", delegate_name = "fnDay", 
                    m_10 = 0x46, m_14 = 0x25, m_16 = 0x25, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0x25] = item


item = FuncInfo(name = "dayname", footprint = "SY", delegate_name = "fnDayName", 
                    m_10 = 0x46, m_14 = 0x26, m_16 = 0x26, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0x26] = item


item = FuncInfo(name = "daynumber", footprint = "IY", delegate_name = "fnDayNumber", 
                    m_10 = 0x46, m_14 = 0x27, m_16 = 0x27, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0x27] = item


item = FuncInfo(name = "daysafter", footprint = "LYY", delegate_name = "fnDaysAfter", 
                    m_10 = 0x46, m_14 = 0x28, m_16 = 0x28, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d1", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d2", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0x28] = item


item = FuncInfo(name = "debugbreak", footprint = "Q", delegate_name = "rt_debug_break", 
                    m_10 = 0x46, m_14 = 0x29, m_16 = 0x29, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x0, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x29] = item


item = FuncInfo(name = "dec", footprint = "MA", delegate_name = "fnDec", 
                    m_10 = 0x46, m_14 = 0x2a, m_16 = 0x2a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x5, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x2a] = item


item = FuncInfo(name = "directoryexists", footprint = "BS", delegate_name = "fnDirectoryExists", 
                    m_10 = 0x46, m_14 = 0x2b, m_16 = 0x2b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x2b] = item


item = FuncInfo(name = "doscript", footprint = "ISRS", delegate_name = "fnDoScript", 
                    m_10 = 0x46, m_14 = 0x2c, m_16 = 0x2c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x2c] = item


item = FuncInfo(name = "double", footprint = "DA", delegate_name = "fnDouble", 
                    m_10 = 0x46, m_14 = 0x2d, m_16 = 0x2d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x2d] = item


item = FuncInfo(name = "draggedobject", footprint = "Cdragobject.", delegate_name = "fnDraggedObject", 
                    m_10 = 0x46, m_14 = 0x2e, m_16 = 0x2e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x407c, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x2e] = item


item = FuncInfo(name = "execremote", footprint = "ISL", delegate_name = "fnExecRemote", 
                    m_10 = 0x46, m_14 = 0x2f, m_16 = 0x2f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x2f] = item


item = FuncInfo(name = "execremote", footprint = "ISLL", delegate_name = "fnExecRemote", 
                    m_10 = 0x46, m_14 = 0x30, m_16 = 0x30, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x30] = item


item = FuncInfo(name = "execremote", footprint = "ISSS", delegate_name = "fnExecRemote", 
                    m_10 = 0x46, m_14 = 0x31, m_16 = 0x31, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x31] = item


item = FuncInfo(name = "exp", footprint = "DD", delegate_name = "fnExp", 
                    m_10 = 0x46, m_14 = 0x32, m_16 = 0x32, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x32] = item


item = FuncInfo(name = "fact", footprint = "DD", delegate_name = "fnFact", 
                    m_10 = 0x46, m_14 = 0x33, m_16 = 0x33, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x33] = item


item = FuncInfo(name = "fileclose", footprint = "II", delegate_name = "fnFileClose", 
                    m_10 = 0x46, m_14 = 0x34, m_16 = 0x34, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x34] = item


item = FuncInfo(name = "filecopy", footprint = "ISS", delegate_name = "fnFileCopy", 
                    m_10 = 0x46, m_14 = 0x35, m_16 = 0x35, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x35] = item


item = FuncInfo(name = "filecopy", footprint = "ISSB", delegate_name = "fnFileCopy", 
                    m_10 = 0x46, m_14 = 0x36, m_16 = 0x36, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x36] = item


item = FuncInfo(name = "filedelete", footprint = "BS", delegate_name = "fnFileDelete", 
                    m_10 = 0x46, m_14 = 0x37, m_16 = 0x37, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x37] = item


item = FuncInfo(name = "fileencoding", footprint = "Cencoding.S", delegate_name = "fnFileEncoding", 
                    m_10 = 0x46, m_14 = 0x38, m_16 = 0x38, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4015, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x38] = item


item = FuncInfo(name = "fileexists", footprint = "BS", delegate_name = "fnFileExists", 
                    m_10 = 0x46, m_14 = 0x39, m_16 = 0x39, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x39] = item


item = FuncInfo(name = "filelength", footprint = "LS", delegate_name = "fnFileLength", 
                    m_10 = 0x46, m_14 = 0x3a, m_16 = 0x3a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x3a] = item


item = FuncInfo(name = "filelength64", footprint = "KS", delegate_name = "fnFileLength64", 
                    m_10 = 0x46, m_14 = 0x3b, m_16 = 0x3b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x14, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x3b] = item


item = FuncInfo(name = "filemove", footprint = "ISS", delegate_name = "fnFileMove", 
                    m_10 = 0x46, m_14 = 0x3c, m_16 = 0x3c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x3c] = item


item = FuncInfo(name = "fileopen", footprint = "IS", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x3d, m_16 = 0x3d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x3d] = item


item = FuncInfo(name = "fileopen", footprint = "ISCfilemode.", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x3e, m_16 = 0x3e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x4019, m_a = 0x8))
c_40CF[0x3e] = item


item = FuncInfo(name = "fileopen", footprint = "ISCfilemode.Cfileaccess.", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x3f, m_16 = 0x3f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x4019, m_a = 0x8))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4017, m_a = 0x8))
c_40CF[0x3f] = item


item = FuncInfo(name = "fileopen", footprint = "ISCfilemode.Cfileaccess.Cfilelock.", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x40, m_16 = 0x40, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x4019, m_a = 0x8))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4017, m_a = 0x8))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x4018, m_a = 0x8))
c_40CF[0x40] = item


item = FuncInfo(name = "fileopen", footprint = "ISCfilemode.Cfileaccess.Cfilelock.Cwritemode.", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x41, m_16 = 0x41, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x4019, m_a = 0x8))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4017, m_a = 0x8))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x4018, m_a = 0x8))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x4070, m_a = 0x8))
c_40CF[0x41] = item


item = FuncInfo(name = "fileopen", footprint = "ISCfilemode.Cfileaccess.Cfilelock.Cwritemode.Cencoding.", delegate_name = "fnFileOpen", 
                    m_10 = 0x46, m_14 = 0x42, m_16 = 0x42, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x4019, m_a = 0x8))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4017, m_a = 0x8))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x4018, m_a = 0x8))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x4070, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x4015, m_a = 0x8))
c_40CF[0x42] = item


item = FuncInfo(name = "fileread", footprint = "IIRO", delegate_name = "fnFileRead", 
                    m_10 = 0x46, m_14 = 0x43, m_16 = 0x43, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
c_40CF[0x43] = item


item = FuncInfo(name = "fileread", footprint = "IIRS", delegate_name = "fnFileRead", 
                    m_10 = 0x46, m_14 = 0x44, m_16 = 0x44, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x44] = item


item = FuncInfo(name = "filereadex", footprint = "LIRO", delegate_name = "fnFileReadEx", 
                    m_10 = 0x46, m_14 = 0x45, m_16 = 0x45, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
c_40CF[0x45] = item


item = FuncInfo(name = "filereadex", footprint = "LIRS", delegate_name = "fnFileReadEx", 
                    m_10 = 0x46, m_14 = 0x46, m_16 = 0x46, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x46] = item


item = FuncInfo(name = "filereadex", footprint = "LIROU", delegate_name = "fnFileReadEx", 
                    m_10 = 0x46, m_14 = 0x47, m_16 = 0x47, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x47] = item


item = FuncInfo(name = "fileseek", footprint = "LIL", delegate_name = "fnFileSeek", 
                    m_10 = 0x46, m_14 = 0x48, m_16 = 0x48, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x48] = item


item = FuncInfo(name = "fileseek64", footprint = "KIK", delegate_name = "fnFileSeek64", 
                    m_10 = 0x46, m_14 = 0x49, m_16 = 0x49, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x14, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
c_40CF[0x49] = item


item = FuncInfo(name = "fileseek", footprint = "LILCseektype.", delegate_name = "fnFileSeek", 
                    m_10 = 0x46, m_14 = 0x4a, m_16 = 0x4a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x405b, m_a = 0x8))
c_40CF[0x4a] = item


item = FuncInfo(name = "fileseek64", footprint = "KIKCseektype.", delegate_name = "fnFileSeek64", 
                    m_10 = 0x46, m_14 = 0x4b, m_16 = 0x4b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x14, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x405b, m_a = 0x8))
c_40CF[0x4b] = item


item = FuncInfo(name = "filewrite", footprint = "IIO", delegate_name = "fnFileWrite", 
                    m_10 = 0x46, m_14 = 0x4c, m_16 = 0x4c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x4c] = item


item = FuncInfo(name = "filewrite", footprint = "IIS", delegate_name = "fnFileWrite", 
                    m_10 = 0x46, m_14 = 0x4d, m_16 = 0x4d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x4d] = item


item = FuncInfo(name = "filewriteex", footprint = "LIO", delegate_name = "fnFileWriteEx", 
                    m_10 = 0x46, m_14 = 0x4e, m_16 = 0x4e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x4e] = item


item = FuncInfo(name = "filewriteex", footprint = "LIS", delegate_name = "fnFileWriteEx", 
                    m_10 = 0x46, m_14 = 0x4f, m_16 = 0x4f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x4f] = item


item = FuncInfo(name = "filewriteex", footprint = "LIOU", delegate_name = "fnFileWriteEx", 
                    m_10 = 0x46, m_14 = 0x50, m_16 = 0x50, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x50] = item


item = FuncInfo(name = "fill", footprint = "SXSL", delegate_name = "fnFill", 
                    m_10 = 0x46, m_14 = 0x51, m_16 = 0x51, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x51] = item


item = FuncInfo(name = "garbagecollect", footprint = "Q", delegate_name = "ot_GarbageCollect", 
                    m_10 = 0x46, m_14 = 0x52, m_16 = 0x52, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x0, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x52] = item


item = FuncInfo(name = "garbagecollectgettimelimit", footprint = "L", delegate_name = "ot_GarbageCollectGetTimeLimit", 
                    m_10 = 0x46, m_14 = 0x53, m_16 = 0x53, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x53] = item


item = FuncInfo(name = "garbagecollectsettimelimit", footprint = "LL", delegate_name = "ot_GarbageCollectSetTimeLimit", 
                    m_10 = 0x46, m_14 = 0x54, m_16 = 0x54, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "newtimeinmilliseconds", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x54] = item


item = FuncInfo(name = "getapplication", footprint = "Capplication.", delegate_name = "fnGetApplication", 
                    m_10 = 0x46, m_14 = 0x55, m_16 = 0x55, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4080, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x55] = item


item = FuncInfo(name = "getbyte", footprint = "IOURE", delegate_name = "fnGetByte", 
                    m_10 = 0x46, m_14 = 0x56, m_16 = 0x56, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x15, m_a = 0x2))
c_40CF[0x56] = item


item = FuncInfo(name = "getbytearray", footprint = "AO", delegate_name = "fnGetByteArray", 
                    m_10 = 0x46, m_14 = 0x57, m_16 = 0x57, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "input", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x57] = item


item = FuncInfo(name = "getcommanddde", footprint = "IRS", delegate_name = "fnGetCommandDDE", 
                    m_10 = 0x46, m_14 = 0x58, m_16 = 0x58, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x58] = item


item = FuncInfo(name = "getcommandddeorigin", footprint = "IRS", delegate_name = "fnGetCommandDDEOrigin", 
                    m_10 = 0x46, m_14 = 0x59, m_16 = 0x59, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x59] = item


item = FuncInfo(name = "getcurrentdirectory", footprint = "S", delegate_name = "fnGetCurrentDirectory", 
                    m_10 = 0x46, m_14 = 0x5a, m_16 = 0x5a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x5a] = item


item = FuncInfo(name = "getdatadde", footprint = "IRS", delegate_name = "fnGetDataDDE", 
                    m_10 = 0x46, m_14 = 0x5b, m_16 = 0x5b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x5b] = item


item = FuncInfo(name = "getdataddeorigin", footprint = "IRSRSRS", delegate_name = "fnGetDataDDEOrigin", 
                    m_10 = 0x46, m_14 = 0x5c, m_16 = 0x5c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x5c] = item


item = FuncInfo(name = "getenvironment", footprint = "IRCenvironment.", delegate_name = "fnGetEnvironment", 
                    m_10 = 0x46, m_14 = 0x5d, m_16 = 0x5d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x4085, m_a = 0x12))
c_40CF[0x5d] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x5e, m_16 = 0x5e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x5e] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRSS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x5f, m_16 = 0x5f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x5f] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRSSS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x60, m_16 = 0x60, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x60] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRSSSS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x61, m_16 = 0x61, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x61] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRSSSSU", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x62, m_16 = 0x62, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x62] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS[]", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x63, m_16 = 0x63, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb114, type_id = 0x6, m_a = 0x3))
c_40CF[0x63] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS[]S", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x64, m_16 = 0x64, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb120, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x64] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS[]SS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x65, m_16 = 0x65, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb12c, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x65] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS[]SSS", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x66, m_16 = 0x66, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb138, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x66] = item


item = FuncInfo(name = "getfileopenname", footprint = "ISRSRS[]SSSU", delegate_name = "fnGetFileOpenName", 
                    m_10 = 0x46, m_14 = 0x67, m_16 = 0x67, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb144, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x67] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x68, m_16 = 0x68, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x68] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRSS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x69, m_16 = 0x69, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x69] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRSSS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6a, m_16 = 0x6a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x6a] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRSSSS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6b, m_16 = 0x6b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x6b] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRSSSSU", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6c, m_16 = 0x6c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x6c] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS[]", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6d, m_16 = 0x6d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb194, type_id = 0x6, m_a = 0x3))
c_40CF[0x6d] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS[]S", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6e, m_16 = 0x6e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb1a0, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x6e] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS[]SS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x6f, m_16 = 0x6f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb1ac, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x6f] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS[]SSS", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x70, m_16 = 0x70, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb1b8, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x70] = item


item = FuncInfo(name = "getfilesavename", footprint = "ISRSRS[]SSSU", delegate_name = "fnGetFileSaveName", 
                    m_10 = 0x46, m_14 = 0x71, m_16 = 0x71, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xb1c4, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x71] = item


item = FuncInfo(name = "getfocus", footprint = "Cgraphicobject.", delegate_name = "fnGetFocus", 
                    m_10 = 0x46, m_14 = 0x72, m_16 = 0x72, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x407a, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x72] = item


item = FuncInfo(name = "getfolder", footprint = "ISRS", delegate_name = "fnGetFolder", 
                    m_10 = 0x46, m_14 = 0x73, m_16 = 0x73, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x73] = item


item = FuncInfo(name = "getremote", footprint = "ISRSL", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x74, m_16 = 0x74, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x74] = item


item = FuncInfo(name = "getremote", footprint = "ISRSLB", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x75, m_16 = 0x75, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x75] = item


item = FuncInfo(name = "getremote", footprint = "ISRSLL", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x76, m_16 = 0x76, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x76] = item


item = FuncInfo(name = "getremote", footprint = "ISRSLLB", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x77, m_16 = 0x77, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x77] = item


item = FuncInfo(name = "getremote", footprint = "ISRSSS", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x78, m_16 = 0x78, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x78] = item


item = FuncInfo(name = "getremote", footprint = "ISRSSSB", delegate_name = "fnGetRemote", 
                    m_10 = 0x46, m_14 = 0x79, m_16 = 0x79, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x79] = item


item = FuncInfo(name = "handle", footprint = "LCapplication.B", delegate_name = "fnHandle", 
                    m_10 = 0x46, m_14 = 0x7a, m_16 = 0x7a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4080, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x7a] = item


item = FuncInfo(name = "handle", footprint = "LCpowerobject.", delegate_name = "fnHandle", 
                    m_10 = 0x46, m_14 = 0x7b, m_16 = 0x7b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4076, m_a = 0x0))
c_40CF[0x7b] = item


item = FuncInfo(name = "hour", footprint = "IT", delegate_name = "fnHour", 
                    m_10 = 0x46, m_14 = 0x7c, m_16 = 0x7c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
c_40CF[0x7c] = item


item = FuncInfo(name = "idle", footprint = "II", delegate_name = "fnIdle", 
                    m_10 = 0x46, m_14 = 0x7d, m_16 = 0x7d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x7d] = item


item = FuncInfo(name = "int", footprint = "ID", delegate_name = "fnInt", 
                    m_10 = 0x46, m_14 = 0x7e, m_16 = 0x7e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x7e] = item


item = FuncInfo(name = "inthigh", footprint = "IL", delegate_name = "fnIntHigh", 
                    m_10 = 0x46, m_14 = 0x7f, m_16 = 0x7f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x7f] = item


item = FuncInfo(name = "intlow", footprint = "IL", delegate_name = "fnIntLow", 
                    m_10 = 0x46, m_14 = 0x80, m_16 = 0x80, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x80] = item


item = FuncInfo(name = "integer", footprint = "IA", delegate_name = "fnInteger", 
                    m_10 = 0x46, m_14 = 0x81, m_16 = 0x81, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x81] = item


item = FuncInfo(name = "isdate", footprint = "BS", delegate_name = "fnIsDate", 
                    m_10 = 0x46, m_14 = 0x82, m_16 = 0x82, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x82] = item


item = FuncInfo(name = "isnull", footprint = "BXA", delegate_name = "fnIsNull", 
                    m_10 = 0x46, m_14 = 0x83, m_16 = 0x83, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x8, m_a = 0x6))
c_40CF[0x83] = item


item = FuncInfo(name = "isnumber", footprint = "BS", delegate_name = "fnIsNumber", 
                    m_10 = 0x46, m_14 = 0x84, m_16 = 0x84, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x84] = item


item = FuncInfo(name = "istime", footprint = "BS", delegate_name = "fnIsTime", 
                    m_10 = 0x46, m_14 = 0x85, m_16 = 0x85, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x85] = item


item = FuncInfo(name = "isvalid", footprint = "BCpowerobject.", delegate_name = "fnIsValid", 
                    m_10 = 0x46, m_14 = 0x86, m_16 = 0x86, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4076, m_a = 0x0))
c_40CF[0x86] = item


item = FuncInfo(name = "keydown", footprint = "BI", delegate_name = "fnKeyDown", 
                    m_10 = 0x46, m_14 = 0x87, m_16 = 0x87, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x87] = item


item = FuncInfo(name = "keydown", footprint = "BCkeycode.", delegate_name = "fnKeyDown", 
                    m_10 = 0x46, m_14 = 0x88, m_16 = 0x88, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x4038, m_a = 0x8))
c_40CF[0x88] = item


item = FuncInfo(name = "lastpos", footprint = "LXSXS", delegate_name = "fnLastPos", 
                    m_10 = 0x46, m_14 = 0x89, m_16 = 0x89, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x89] = item


item = FuncInfo(name = "lastpos", footprint = "LXSXSL", delegate_name = "fnLastPos", 
                    m_10 = 0x46, m_14 = 0x8a, m_16 = 0x8a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x8a] = item


item = FuncInfo(name = "left", footprint = "SXSL", delegate_name = "fnLeft", 
                    m_10 = 0x46, m_14 = 0x8b, m_16 = 0x8b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x8b] = item


item = FuncInfo(name = "lefttrim", footprint = "SXS", delegate_name = "fnLeftTrim", 
                    m_10 = 0x46, m_14 = 0x8c, m_16 = 0x8c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x8c] = item


item = FuncInfo(name = "lefttrim", footprint = "SXSB", delegate_name = "fnLeftTrim", 
                    m_10 = 0x46, m_14 = 0x8d, m_16 = 0x8d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "removealltypespaces", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x8d] = item


item = FuncInfo(name = "len", footprint = "LO", delegate_name = "fnLen", 
                    m_10 = 0x46, m_14 = 0x8e, m_16 = 0x8e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x8e] = item


item = FuncInfo(name = "len", footprint = "LS", delegate_name = "fnLen", 
                    m_10 = 0x46, m_14 = 0x8f, m_16 = 0x8f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x8f] = item


item = FuncInfo(name = "librarycreate", footprint = "IS", delegate_name = "fnLibraryCreate", 
                    m_10 = 0x46, m_14 = 0x90, m_16 = 0x90, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x90] = item


item = FuncInfo(name = "librarycreate", footprint = "ISS", delegate_name = "fnLibraryCreate", 
                    m_10 = 0x46, m_14 = 0x91, m_16 = 0x91, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x91] = item


item = FuncInfo(name = "librarydelete", footprint = "IS", delegate_name = "fnLibraryDelete", 
                    m_10 = 0x46, m_14 = 0x92, m_16 = 0x92, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x92] = item


item = FuncInfo(name = "librarydelete", footprint = "ISSClibimporttype.", delegate_name = "fnLibraryDelete", 
                    m_10 = 0x46, m_14 = 0x93, m_16 = 0x93, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403c, m_a = 0x8))
c_40CF[0x93] = item


item = FuncInfo(name = "librarydirectory", footprint = "SSClibdirtype.", delegate_name = "fnLibraryDirectory", 
                    m_10 = 0x46, m_14 = 0x94, m_16 = 0x94, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403d, m_a = 0x8))
c_40CF[0x94] = item


item = FuncInfo(name = "librarydirectoryex", footprint = "SSClibdirtype.", delegate_name = "fnLibraryDirectoryEx", 
                    m_10 = 0x46, m_14 = 0x95, m_16 = 0x95, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403d, m_a = 0x8))
c_40CF[0x95] = item


item = FuncInfo(name = "libraryexport", footprint = "SSSClibexporttype.", delegate_name = "fnLibraryExport", 
                    m_10 = 0x46, m_14 = 0x96, m_16 = 0x96, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403b, m_a = 0x8))
c_40CF[0x96] = item


item = FuncInfo(name = "libraryimport", footprint = "ISSClibimporttype.SRS", delegate_name = "fnLibraryImport", 
                    m_10 = 0x46, m_14 = 0x97, m_16 = 0x97, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403c, m_a = 0x8))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x97] = item


item = FuncInfo(name = "libraryimport", footprint = "ISSClibimporttype.SRSS", delegate_name = "fnLibraryImport", 
                    m_10 = 0x46, m_14 = 0x98, m_16 = 0x98, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x403c, m_a = 0x8))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x98] = item


item = FuncInfo(name = "log", footprint = "DD", delegate_name = "fnLog", 
                    m_10 = 0x46, m_14 = 0x99, m_16 = 0x99, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x99] = item


item = FuncInfo(name = "logten", footprint = "DD", delegate_name = "fnLogTen", 
                    m_10 = 0x46, m_14 = 0x9a, m_16 = 0x9a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x9a] = item


item = FuncInfo(name = "long", footprint = "LA", delegate_name = "fnLong", 
                    m_10 = 0x46, m_14 = 0x9b, m_16 = 0x9b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x9b] = item


item = FuncInfo(name = "long", footprint = "LII", delegate_name = "fnLong2", 
                    m_10 = 0x46, m_14 = 0x9c, m_16 = 0x9c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x9c] = item


item = FuncInfo(name = "longlong", footprint = "KA", delegate_name = "fnLonglong", 
                    m_10 = 0x46, m_14 = 0x9d, m_16 = 0x9d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x14, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x9d] = item


item = FuncInfo(name = "longlong", footprint = "KLL", delegate_name = "fnLonglong2", 
                    m_10 = 0x46, m_14 = 0x9e, m_16 = 0x9e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x14, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x9e] = item


item = FuncInfo(name = "lower", footprint = "SXS", delegate_name = "fnLower", 
                    m_10 = 0x46, m_14 = 0x9f, m_16 = 0x9f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x9f] = item


item = FuncInfo(name = "lowerbound", footprint = "LRA[]", delegate_name = "fnLowerBound", 
                    m_10 = 0x46, m_14 = 0xa0, m_16 = 0xa0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xb6bc, type_id = 0x8, m_a = 0x3))
c_40CF[0xa0] = item


item = FuncInfo(name = "lowerbound", footprint = "LRA[]I", delegate_name = "fnLowerBound", 
                    m_10 = 0x46, m_14 = 0xa1, m_16 = 0xa1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xb6f8, type_id = 0x8, m_a = 0x3))
item.parameters.append(ParamInfo(name = "dim", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xa1] = item


item = FuncInfo(name = "match", footprint = "BXSXS", delegate_name = "fnMatch", 
                    m_10 = 0x46, m_14 = 0xa2, m_16 = 0xa2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0xa2] = item


item = FuncInfo(name = "max", footprint = "DDD", delegate_name = "fnMax", 
                    m_10 = 0x46, m_14 = 0xa3, m_16 = 0xa3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xa3] = item


item = FuncInfo(name = "messagebox", footprint = "ISB", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa4, m_16 = 0xa4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0xa4] = item


item = FuncInfo(name = "messagebox", footprint = "ISBCicon.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa5, m_16 = 0xa5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
c_40CF[0xa5] = item


item = FuncInfo(name = "messagebox", footprint = "ISBCicon.Cbutton.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa6, m_16 = 0xa6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
c_40CF[0xa6] = item


item = FuncInfo(name = "messagebox", footprint = "ISBCicon.Cbutton.I", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa7, m_16 = 0xa7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xa7] = item


item = FuncInfo(name = "messagebox", footprint = "ISD", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa8, m_16 = 0xa8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xa8] = item


item = FuncInfo(name = "messagebox", footprint = "ISDCicon.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xa9, m_16 = 0xa9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
c_40CF[0xa9] = item


item = FuncInfo(name = "messagebox", footprint = "ISDCicon.Cbutton.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xaa, m_16 = 0xaa, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
c_40CF[0xaa] = item


item = FuncInfo(name = "messagebox", footprint = "ISDCicon.Cbutton.I", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xab, m_16 = 0xab, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xab] = item


item = FuncInfo(name = "messagebox", footprint = "ISK", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xac, m_16 = 0xac, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
c_40CF[0xac] = item


item = FuncInfo(name = "messagebox", footprint = "ISKCicon.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xad, m_16 = 0xad, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
c_40CF[0xad] = item


item = FuncInfo(name = "messagebox", footprint = "ISKCicon.Cbutton.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xae, m_16 = 0xae, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
c_40CF[0xae] = item


item = FuncInfo(name = "messagebox", footprint = "ISKCicon.Cbutton.I", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xaf, m_16 = 0xaf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x14, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xaf] = item


item = FuncInfo(name = "messagebox", footprint = "ISS", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xb0, m_16 = 0xb0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xb0] = item


item = FuncInfo(name = "messagebox", footprint = "ISSCicon.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xb1, m_16 = 0xb1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
c_40CF[0xb1] = item


item = FuncInfo(name = "messagebox", footprint = "ISSCicon.Cbutton.", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xb2, m_16 = 0xb2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
c_40CF[0xb2] = item


item = FuncInfo(name = "messagebox", footprint = "ISSCicon.Cbutton.I", delegate_name = "fnMessageBox", 
                    m_10 = 0x46, m_14 = 0xb3, m_16 = 0xb3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x402f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x4007, m_a = 0x8))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xb3] = item


item = FuncInfo(name = "mid", footprint = "SXSL", delegate_name = "fnMid", 
                    m_10 = 0x46, m_14 = 0xb4, m_16 = 0xb4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xb4] = item


item = FuncInfo(name = "mid", footprint = "SXSLL", delegate_name = "fnMid", 
                    m_10 = 0x46, m_14 = 0xb5, m_16 = 0xb5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xb5] = item


item = FuncInfo(name = "min", footprint = "DDD", delegate_name = "fnMin", 
                    m_10 = 0x46, m_14 = 0xb6, m_16 = 0xb6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xb6] = item


item = FuncInfo(name = "minute", footprint = "IT", delegate_name = "fnMinute", 
                    m_10 = 0x46, m_14 = 0xb7, m_16 = 0xb7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
c_40CF[0xb7] = item


item = FuncInfo(name = "mod", footprint = "DDD", delegate_name = "fnMod", 
                    m_10 = 0x46, m_14 = 0xb8, m_16 = 0xb8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xb8] = item


item = FuncInfo(name = "month", footprint = "IY", delegate_name = "fnMonth", 
                    m_10 = 0x46, m_14 = 0xb9, m_16 = 0xb9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0xb9] = item


item = FuncInfo(name = "now", footprint = "T", delegate_name = "fnNow", 
                    m_10 = 0x46, m_14 = 0xba, m_16 = 0xba, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0xba] = item


item = FuncInfo(name = "open", footprint = "IRCwindow.", delegate_name = "fnOpenWnd", 
                    m_10 = 0x46, m_14 = 0xbb, m_16 = 0xbb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
c_40CF[0xbb] = item


item = FuncInfo(name = "open", footprint = "IRCwindow.Cwindow.", delegate_name = "fnOpenWnd", 
                    m_10 = 0x46, m_14 = 0xbc, m_16 = 0xbc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xbc] = item


item = FuncInfo(name = "open", footprint = "IRCwindow.S", delegate_name = "fnOpenWnd", 
                    m_10 = 0x46, m_14 = 0xbd, m_16 = 0xbd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xbd] = item


item = FuncInfo(name = "open", footprint = "IRCwindow.SCwindow.", delegate_name = "fnOpenWnd", 
                    m_10 = 0x46, m_14 = 0xbe, m_16 = 0xbe, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xbe] = item


item = FuncInfo(name = "openchannel", footprint = "LSS", delegate_name = "fnOpenChannel", 
                    m_10 = 0x46, m_14 = 0xbf, m_16 = 0xbf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xbf] = item


item = FuncInfo(name = "openchannel", footprint = "LSSL", delegate_name = "fnOpenChannel", 
                    m_10 = 0x46, m_14 = 0xc0, m_16 = 0xc0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xc0] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.Cwindow.", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc1, m_16 = 0xc1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xc1] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.Cwindow.I", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc2, m_16 = 0xc2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xc2] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.Cwindow.ICarrangeopen.", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc3, m_16 = 0xc3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xc3] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.SCwindow.", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc4, m_16 = 0xc4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xc4] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.SCwindow.I", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc5, m_16 = 0xc5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xc5] = item


item = FuncInfo(name = "opensheet", footprint = "IRCwindow.SCwindow.ICarrangeopen.", delegate_name = "fnOpenSheet", 
                    m_10 = 0x46, m_14 = 0xc6, m_16 = 0xc6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xc6] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSCwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xc7, m_16 = 0xc7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xc7] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDCwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xc8, m_16 = 0xc8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xc8] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.Cwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xc9, m_16 = 0xc9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xc9] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSCwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xca, m_16 = 0xca, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xca] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDCwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xcb, m_16 = 0xcb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xcb] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.Cwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xcc, m_16 = 0xcc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xcc] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSCwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xcd, m_16 = 0xcd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xcd] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDCwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xce, m_16 = 0xce, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xce] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.Cwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xcf, m_16 = 0xcf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xcf] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSSCwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd0, m_16 = 0xd0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xd0] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDSCwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd1, m_16 = 0xd1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xd1] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.SCwindow.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd2, m_16 = 0xd2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xd2] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSSCwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd3, m_16 = 0xd3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xd3] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDSCwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd4, m_16 = 0xd4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xd4] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.SCwindow.I", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd5, m_16 = 0xd5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xd5] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XSSCwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd6, m_16 = 0xd6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xd6] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XDSCwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd7, m_16 = 0xd7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xd7] = item


item = FuncInfo(name = "opensheetwithparm", footprint = "IRCwindow.XCpowerobject.SCwindow.ICarrangeopen.", delegate_name = "fnOpenSheetWithParm", 
                    m_10 = 0x46, m_14 = 0xd8, m_16 = 0xd8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4002, m_a = 0x8))
c_40CF[0xd8] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XS", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xd9, m_16 = 0xd9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0xd9] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XD", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xda, m_16 = 0xda, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
c_40CF[0xda] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XCpowerobject.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xdb, m_16 = 0xdb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
c_40CF[0xdb] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XSCwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xdc, m_16 = 0xdc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xdc] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XDCwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xdd, m_16 = 0xdd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xdd] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XCpowerobject.Cwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xde, m_16 = 0xde, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xde] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XSS", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xdf, m_16 = 0xdf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xdf] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XDS", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xe0, m_16 = 0xe0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xe0] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XCpowerobject.S", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xe1, m_16 = 0xe1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xe1] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XSSCwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xe2, m_16 = 0xe2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xe2] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XDSCwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xe3, m_16 = 0xe3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xe3] = item


item = FuncInfo(name = "openwithparm", footprint = "IRCwindow.XCpowerobject.SCwindow.", delegate_name = "fnOpenWithParm", 
                    m_10 = 0x46, m_14 = 0xe4, m_16 = 0xe4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x2))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x4076, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0xe4] = item


item = FuncInfo(name = "pi", footprint = "DD", delegate_name = "fnPi", 
                    m_10 = 0x46, m_14 = 0xe5, m_16 = 0xe5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0xe5] = item


item = FuncInfo(name = "pixelstounits", footprint = "IICconverttype.", delegate_name = "fnPixelsToUnits", 
                    m_10 = 0x46, m_14 = 0xe6, m_16 = 0xe6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "u", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x400b, m_a = 0x8))
c_40CF[0xe6] = item


item = FuncInfo(name = "pos", footprint = "LXSXS", delegate_name = "fnPos", 
                    m_10 = 0x46, m_14 = 0xe7, m_16 = 0xe7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0xe7] = item


item = FuncInfo(name = "pos", footprint = "LXSXSL", delegate_name = "fnPos", 
                    m_10 = 0x46, m_14 = 0xe8, m_16 = 0xe8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xe8] = item


item = FuncInfo(name = "post", footprint = "BLNLL", delegate_name = "fnPost", 
                    m_10 = 0x46, m_14 = 0xe9, m_16 = 0xe9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x9, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xe9] = item


item = FuncInfo(name = "post", footprint = "BLNLS", delegate_name = "fnPost", 
                    m_10 = 0x46, m_14 = 0xea, m_16 = 0xea, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x9, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xea] = item


item = FuncInfo(name = "print", footprint = "ILS", delegate_name = "fnPrint", 
                    m_10 = 0x46, m_14 = 0xeb, m_16 = 0xeb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xeb] = item


item = FuncInfo(name = "print", footprint = "ILSI", delegate_name = "fnPrint", 
                    m_10 = 0x46, m_14 = 0xec, m_16 = 0xec, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xec] = item


item = FuncInfo(name = "print", footprint = "ILIS", delegate_name = "fnPrint", 
                    m_10 = 0x46, m_14 = 0xed, m_16 = 0xed, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xed] = item


item = FuncInfo(name = "print", footprint = "ILISI", delegate_name = "fnPrint", 
                    m_10 = 0x46, m_14 = 0xee, m_16 = 0xee, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t1", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t2", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xee] = item


item = FuncInfo(name = "printbitmap", footprint = "ILSIIII", delegate_name = "fnPrintBitmap", 
                    m_10 = 0x46, m_14 = 0xef, m_16 = 0xef, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xef] = item


item = FuncInfo(name = "printcancel", footprint = "IL", delegate_name = "fnPrintCancel", 
                    m_10 = 0x46, m_14 = 0xf0, m_16 = 0xf0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xf0] = item


item = FuncInfo(name = "printclose", footprint = "IL", delegate_name = "fnPrintClose", 
                    m_10 = 0x46, m_14 = 0xf1, m_16 = 0xf1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0xf1] = item


item = FuncInfo(name = "printdatawindow", footprint = "ILCdatastore.", delegate_name = "fnPrintDataWindow", 
                    m_10 = 0x46, m_14 = 0xf2, m_16 = 0xf2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x408a, m_a = 0x0))
c_40CF[0xf2] = item


item = FuncInfo(name = "printdatawindow", footprint = "ILCdatawindow.", delegate_name = "fnPrintDataWindow", 
                    m_10 = 0x46, m_14 = 0xf3, m_16 = 0xf3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x4089, m_a = 0x0))
c_40CF[0xf3] = item


item = FuncInfo(name = "printdatawindow", footprint = "ILCdatawindowchild.", delegate_name = "fnPrintDataWindow", 
                    m_10 = 0x46, m_14 = 0xf4, m_16 = 0xf4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x409a, m_a = 0x10))
c_40CF[0xf4] = item


item = FuncInfo(name = "printdefinefont", footprint = "ILISIICfontpitch.Cfontfamily.BB", delegate_name = "fnPrintDefineFont", 
                    m_10 = 0x46, m_14 = 0xf5, m_16 = 0xf5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x401f, m_a = 0x8))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x401e, m_a = 0x8))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "u", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0xf5] = item


item = FuncInfo(name = "printgetprinter", footprint = "S", delegate_name = "fnGetPrinter", 
                    m_10 = 0x46, m_14 = 0xf6, m_16 = 0xf6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0xf6] = item


item = FuncInfo(name = "printgetprinters", footprint = "S", delegate_name = "fnGetPrinters", 
                    m_10 = 0x46, m_14 = 0xf7, m_16 = 0xf7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0xf7] = item


item = FuncInfo(name = "printscreen", footprint = "ILII", delegate_name = "fnPrintScreen", 
                    m_10 = 0x46, m_14 = 0xf8, m_16 = 0xf8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xf8] = item


item = FuncInfo(name = "printscreen", footprint = "ILIIII", delegate_name = "fnPrintScreen", 
                    m_10 = 0x46, m_14 = 0xf9, m_16 = 0xf9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xf9] = item


item = FuncInfo(name = "printsend", footprint = "ILS", delegate_name = "fnPrintSend", 
                    m_10 = 0x46, m_14 = 0xfa, m_16 = 0xfa, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xfa] = item


item = FuncInfo(name = "printsend", footprint = "ILSI", delegate_name = "fnPrintSend", 
                    m_10 = 0x46, m_14 = 0xfb, m_16 = 0xfb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xfb] = item


item = FuncInfo(name = "printsetfont", footprint = "ILI", delegate_name = "fnPrintSetFont", 
                    m_10 = 0x46, m_14 = 0xfc, m_16 = 0xfc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0xfc] = item


item = FuncInfo(name = "printsetprinter", footprint = "IS", delegate_name = "fnSetPrinter", 
                    m_10 = 0x46, m_14 = 0xfd, m_16 = 0xfd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0xfd] = item


item = FuncInfo(name = "printsetspacing", footprint = "ILF", delegate_name = "fnPrintSetSpacing", 
                    m_10 = 0x46, m_14 = 0xfe, m_16 = 0xfe, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x3, m_a = 0x0))
c_40CF[0xfe] = item


item = FuncInfo(name = "printsetup", footprint = "I", delegate_name = "fnPrintSetup", 
                    m_10 = 0x46, m_14 = 0xff, m_16 = 0xff, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0xff] = item


item = FuncInfo(name = "printsetupprinter", footprint = "I", delegate_name = "fnSetupPrinter", 
                    m_10 = 0x46, m_14 = 0x100, m_16 = 0x100, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x100] = item


item = FuncInfo(name = "printline", footprint = "ILIIIII", delegate_name = "fnPrintLine", 
                    m_10 = 0x46, m_14 = 0x101, m_16 = 0x101, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x1", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y1", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x2", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y2", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x101] = item


item = FuncInfo(name = "printopen", footprint = "L", delegate_name = "fnPrintOpen", 
                    m_10 = 0x46, m_14 = 0x102, m_16 = 0x102, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x102] = item


item = FuncInfo(name = "printopen", footprint = "LS", delegate_name = "fnPrintOpen", 
                    m_10 = 0x46, m_14 = 0x103, m_16 = 0x103, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x103] = item


item = FuncInfo(name = "printopen", footprint = "LSB", delegate_name = "fnPrintOpen", 
                    m_10 = 0x46, m_14 = 0x104, m_16 = 0x104, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "showprintdlg", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x104] = item


item = FuncInfo(name = "printoval", footprint = "ILIIIII", delegate_name = "fnPrintOval", 
                    m_10 = 0x46, m_14 = 0x105, m_16 = 0x105, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x105] = item


item = FuncInfo(name = "printpage", footprint = "IL", delegate_name = "fnPrintPage", 
                    m_10 = 0x46, m_14 = 0x106, m_16 = 0x106, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x106] = item


item = FuncInfo(name = "printrect", footprint = "ILIIIII", delegate_name = "fnPrintRect", 
                    m_10 = 0x46, m_14 = 0x107, m_16 = 0x107, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x107] = item


item = FuncInfo(name = "printroundrect", footprint = "ILIIIIIII", delegate_name = "fnPrintRoundRect", 
                    m_10 = 0x46, m_14 = 0x108, m_16 = 0x108, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x108] = item


item = FuncInfo(name = "printtext", footprint = "ILSII", delegate_name = "fnPrintText", 
                    m_10 = 0x46, m_14 = 0x109, m_16 = 0x109, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x109] = item


item = FuncInfo(name = "printtext", footprint = "ILSIII", delegate_name = "fnPrintText", 
                    m_10 = 0x46, m_14 = 0x10a, m_16 = 0x10a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x10a] = item


item = FuncInfo(name = "printwidth", footprint = "ILS", delegate_name = "fnPrintWidth", 
                    m_10 = 0x46, m_14 = 0x10b, m_16 = 0x10b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x10b] = item


item = FuncInfo(name = "printx", footprint = "IL", delegate_name = "fnPrintX", 
                    m_10 = 0x46, m_14 = 0x10c, m_16 = 0x10c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x10c] = item


item = FuncInfo(name = "printy", footprint = "IL", delegate_name = "fnPrintY", 
                    m_10 = 0x46, m_14 = 0x10d, m_16 = 0x10d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "j", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x10d] = item


item = FuncInfo(name = "profileint", footprint = "ISSSI", delegate_name = "fnProfileInt", 
                    m_10 = 0x46, m_14 = 0x10e, m_16 = 0x10e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x10e] = item


item = FuncInfo(name = "profilestring", footprint = "SSSSS", delegate_name = "fnProfileString", 
                    m_10 = 0x46, m_14 = 0x10f, m_16 = 0x10f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x10f] = item


item = FuncInfo(name = "rand", footprint = "LL", delegate_name = "fnRand", 
                    m_10 = 0x46, m_14 = 0x110, m_16 = 0x110, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x110] = item


item = FuncInfo(name = "randomize", footprint = "IL", delegate_name = "fnRandomize", 
                    m_10 = 0x46, m_14 = 0x111, m_16 = 0x111, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x111] = item


item = FuncInfo(name = "real", footprint = "FA", delegate_name = "fnReal", 
                    m_10 = 0x46, m_14 = 0x112, m_16 = 0x112, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x3, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x112] = item


item = FuncInfo(name = "registryget", footprint = "ISSRS", delegate_name = "fnRegistryGet", 
                    m_10 = 0x46, m_14 = 0x113, m_16 = 0x113, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x113] = item


item = FuncInfo(name = "registryget", footprint = "ISSCregistryvaluetype.RS", delegate_name = "fnRegistryGet2", 
                    m_10 = 0x46, m_14 = 0x114, m_16 = 0x114, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x114] = item


item = FuncInfo(name = "registryget", footprint = "ISSCregistryvaluetype.RS[]", delegate_name = "fnRegistryGet2", 
                    m_10 = 0x46, m_14 = 0x115, m_16 = 0x115, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xbf50, type_id = 0x6, m_a = 0x3))
c_40CF[0x115] = item


item = FuncInfo(name = "registryget", footprint = "ISSCregistryvaluetype.RU", delegate_name = "fnRegistryGet2", 
                    m_10 = 0x46, m_14 = 0x116, m_16 = 0x116, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0xa, m_a = 0x2))
c_40CF[0x116] = item


item = FuncInfo(name = "registryget", footprint = "ISSCregistryvaluetype.RO", delegate_name = "fnRegistryGet2", 
                    m_10 = 0x46, m_14 = 0x117, m_16 = 0x117, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
c_40CF[0x117] = item


item = FuncInfo(name = "registryset", footprint = "ISSCregistryvaluetype.S", delegate_name = "fnRegistrySet2", 
                    m_10 = 0x46, m_14 = 0x118, m_16 = 0x118, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x118] = item


item = FuncInfo(name = "registryset", footprint = "ISSCregistryvaluetype.S[]", delegate_name = "fnRegistrySet2", 
                    m_10 = 0x46, m_14 = 0x119, m_16 = 0x119, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xbf94, type_id = 0x6, m_a = 0x1))
c_40CF[0x119] = item


item = FuncInfo(name = "registryset", footprint = "ISSCregistryvaluetype.U", delegate_name = "fnRegistrySet2", 
                    m_10 = 0x46, m_14 = 0x11a, m_16 = 0x11a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
c_40CF[0x11a] = item


item = FuncInfo(name = "registryset", footprint = "ISSCregistryvaluetype.O", delegate_name = "fnRegistrySet2", 
                    m_10 = 0x46, m_14 = 0x11b, m_16 = 0x11b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x4056, m_a = 0x8))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x11b] = item


item = FuncInfo(name = "registryset", footprint = "ISSS", delegate_name = "fnRegistrySet", 
                    m_10 = 0x46, m_14 = 0x11c, m_16 = 0x11c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x11c] = item


item = FuncInfo(name = "registrydelete", footprint = "ISS", delegate_name = "fnRegistryDelete", 
                    m_10 = 0x46, m_14 = 0x11d, m_16 = 0x11d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x11d] = item


item = FuncInfo(name = "registrykeys", footprint = "ISRS[]", delegate_name = "fnRegistryKeys", 
                    m_10 = 0x46, m_14 = 0x11e, m_16 = 0x11e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xbffc, type_id = 0x6, m_a = 0x3))
c_40CF[0x11e] = item


item = FuncInfo(name = "registryvalues", footprint = "ISRS[]", delegate_name = "fnRegistryValues", 
                    m_10 = 0x46, m_14 = 0x11f, m_16 = 0x11f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xc040, type_id = 0x6, m_a = 0x3))
c_40CF[0x11f] = item


item = FuncInfo(name = "relativedate", footprint = "YYI", delegate_name = "fnRelativeDate", 
                    m_10 = 0x46, m_14 = 0x120, m_16 = 0x120, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x120] = item


item = FuncInfo(name = "relativetime", footprint = "TTL", delegate_name = "fnRelativeTime", 
                    m_10 = 0x46, m_14 = 0x121, m_16 = 0x121, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x121] = item


item = FuncInfo(name = "removedirectory", footprint = "IS", delegate_name = "fnRemoveDirectory", 
                    m_10 = 0x46, m_14 = 0x122, m_16 = 0x122, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x122] = item


item = FuncInfo(name = "replace", footprint = "SXSLLXS", delegate_name = "fnReplace", 
                    m_10 = 0x46, m_14 = 0x123, m_16 = 0x123, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x123] = item


item = FuncInfo(name = "respondremote", footprint = "IB", delegate_name = "fnRespondRemote", 
                    m_10 = 0x46, m_14 = 0x124, m_16 = 0x124, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x124] = item


item = FuncInfo(name = "restart", footprint = "I", delegate_name = "fnRestart", 
                    m_10 = 0x46, m_14 = 0x125, m_16 = 0x125, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x125] = item


item = FuncInfo(name = "rgb", footprint = "LIII", delegate_name = "fnRgb", 
                    m_10 = 0x46, m_14 = 0x126, m_16 = 0x126, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "g", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x126] = item


item = FuncInfo(name = "right", footprint = "SXSL", delegate_name = "fnRight", 
                    m_10 = 0x46, m_14 = 0x127, m_16 = 0x127, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x127] = item


item = FuncInfo(name = "righttrim", footprint = "SXS", delegate_name = "fnRightTrim", 
                    m_10 = 0x46, m_14 = 0x128, m_16 = 0x128, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x128] = item


item = FuncInfo(name = "righttrim", footprint = "SXSB", delegate_name = "fnRightTrim", 
                    m_10 = 0x46, m_14 = 0x129, m_16 = 0x129, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "removealltypespaces", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x129] = item


item = FuncInfo(name = "round", footprint = "MMI", delegate_name = "fnRound", 
                    m_10 = 0x46, m_14 = 0x12a, m_16 = 0x12a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x5, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x5, m_a = 0xf8))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x12a] = item


item = FuncInfo(name = "run", footprint = "IS", delegate_name = "fnRun", 
                    m_10 = 0x46, m_14 = 0x12b, m_16 = 0x12b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x12b] = item


item = FuncInfo(name = "run", footprint = "ISCwindowstate.", delegate_name = "fnRun", 
                    m_10 = 0x46, m_14 = 0x12c, m_16 = 0x12c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x406e, m_a = 0x8))
c_40CF[0x12c] = item


item = FuncInfo(name = "second", footprint = "IT", delegate_name = "fnSecond", 
                    m_10 = 0x46, m_14 = 0x12d, m_16 = 0x12d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
c_40CF[0x12d] = item


item = FuncInfo(name = "secondsafter", footprint = "LTT", delegate_name = "fnSecondsAfter", 
                    m_10 = 0x46, m_14 = 0x12e, m_16 = 0x12e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "t1", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t2", m_4 = 0xffff, type_id = 0xd, m_a = 0x0))
c_40CF[0x12e] = item


item = FuncInfo(name = "send", footprint = "LLNLL", delegate_name = "fnSend", 
                    m_10 = 0x46, m_14 = 0x12f, m_16 = 0x12f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x9, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x12f] = item


item = FuncInfo(name = "send", footprint = "LLNLS", delegate_name = "fnSend", 
                    m_10 = 0x46, m_14 = 0x130, m_16 = 0x130, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x9, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x130] = item


item = FuncInfo(name = "setbyte", footprint = "IROUE", delegate_name = "fnSetByte", 
                    m_10 = 0x46, m_14 = 0x131, m_16 = 0x131, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x2))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0xa, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x15, m_a = 0x0))
c_40CF[0x131] = item


item = FuncInfo(name = "setdatadde", footprint = "IS", delegate_name = "fnSetDataDDE", 
                    m_10 = 0x46, m_14 = 0x132, m_16 = 0x132, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x132] = item


item = FuncInfo(name = "setdatadde", footprint = "ISSSS", delegate_name = "fnSetDataDDE", 
                    m_10 = 0x46, m_14 = 0x133, m_16 = 0x133, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x133] = item


item = FuncInfo(name = "setnull", footprint = "IRA", delegate_name = "fnSetNull", 
                    m_10 = 0x46, m_14 = 0x134, m_16 = 0x134, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x8, m_a = 0x2))
c_40CF[0x134] = item


item = FuncInfo(name = "setpointer", footprint = "Cpointer.Cpointer.", delegate_name = "fnSetPointer", 
                    m_10 = 0x46, m_14 = 0x135, m_16 = 0x135, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4055, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x4055, m_a = 0x8))
c_40CF[0x135] = item


item = FuncInfo(name = "setprofilestring", footprint = "ISSSS", delegate_name = "fnSetProfileString", 
                    m_10 = 0x46, m_14 = 0x136, m_16 = 0x136, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x136] = item


item = FuncInfo(name = "setremote", footprint = "ISSL", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x137, m_16 = 0x137, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x137] = item


item = FuncInfo(name = "setremote", footprint = "ISSLB", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x138, m_16 = 0x138, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x138] = item


item = FuncInfo(name = "setremote", footprint = "ISSLL", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x139, m_16 = 0x139, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x139] = item


item = FuncInfo(name = "setremote", footprint = "ISSLLB", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x13a, m_16 = 0x13a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "w", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x13a] = item


item = FuncInfo(name = "setremote", footprint = "ISSSS", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x13b, m_16 = 0x13b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x13b] = item


item = FuncInfo(name = "setremote", footprint = "ISSSSB", delegate_name = "fnSetRemote", 
                    m_10 = 0x46, m_14 = 0x13c, m_16 = 0x13c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "r", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x13c] = item


item = FuncInfo(name = "sharedobjectdirectory", footprint = "Cerrorreturn.RS[]", delegate_name = "ob_SharedObjectDirectory", 
                    m_10 = 0x46, m_14 = 0x13d, m_16 = 0x13d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "instancenames", m_4 = 0xc39c, type_id = 0x6, m_a = 0x3))
c_40CF[0x13d] = item


item = FuncInfo(name = "sharedobjectdirectory", footprint = "Cerrorreturn.RS[]RS[]", delegate_name = "ob_SharedObjectDirectory", 
                    m_10 = 0x46, m_14 = 0x13e, m_16 = 0x13e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "instancenames", m_4 = 0xc424, type_id = 0x6, m_a = 0x3))
item.parameters.append(ParamInfo(name = "classnames", m_4 = 0xc430, type_id = 0x6, m_a = 0x3))
c_40CF[0x13e] = item


item = FuncInfo(name = "sharedobjectregister", footprint = "Cerrorreturn.XSXS", delegate_name = "ob_SharedObjectRegister", 
                    m_10 = 0x46, m_14 = 0x13f, m_16 = 0x13f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "classname", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "instancename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x13f] = item


item = FuncInfo(name = "sharedobjectunregister", footprint = "Cerrorreturn.XS", delegate_name = "ob_SharedObjectUnregister", 
                    m_10 = 0x46, m_14 = 0x140, m_16 = 0x140, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "instancename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x140] = item


item = FuncInfo(name = "sharedobjectget", footprint = "Cerrorreturn.XSRCpowerobject.", delegate_name = "ob_SharedObjectGet", 
                    m_10 = 0x46, m_14 = 0x141, m_16 = 0x141, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "instancename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "objectinstance", m_4 = 0xffff, type_id = 0x4076, m_a = 0x2))
c_40CF[0x141] = item


item = FuncInfo(name = "showhelp", footprint = "ISChelpcommand.", delegate_name = "fnShowHelp", 
                    m_10 = 0x46, m_14 = 0x142, m_16 = 0x142, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x402d, m_a = 0x8))
c_40CF[0x142] = item


item = FuncInfo(name = "showhelp", footprint = "ISChelpcommand.L", delegate_name = "fnShowHelp", 
                    m_10 = 0x46, m_14 = 0x143, m_16 = 0x143, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x402d, m_a = 0x8))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x143] = item


item = FuncInfo(name = "showhelp", footprint = "ISChelpcommand.S", delegate_name = "fnShowHelp", 
                    m_10 = 0x46, m_14 = 0x144, m_16 = 0x144, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x402d, m_a = 0x8))
item.parameters.append(ParamInfo(name = "k", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x144] = item


item = FuncInfo(name = "showpopuphelp", footprint = "ISCdragobject.L", delegate_name = "fnShowPopupHelp", 
                    m_10 = 0x46, m_14 = 0x145, m_16 = 0x145, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x407c, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x145] = item


item = FuncInfo(name = "sign", footprint = "ID", delegate_name = "fnSign", 
                    m_10 = 0x46, m_14 = 0x146, m_16 = 0x146, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x146] = item


item = FuncInfo(name = "sin", footprint = "DD", delegate_name = "fnSin", 
                    m_10 = 0x46, m_14 = 0x147, m_16 = 0x147, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x147] = item


item = FuncInfo(name = "sleep", footprint = "IL", delegate_name = "fnSleep", 
                    m_10 = 0x46, m_14 = 0x148, m_16 = 0x148, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x148] = item


item = FuncInfo(name = "space", footprint = "SL", delegate_name = "fnSpace", 
                    m_10 = 0x46, m_14 = 0x149, m_16 = 0x149, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x149] = item


item = FuncInfo(name = "sqrt", footprint = "DD", delegate_name = "fnSqrt", 
                    m_10 = 0x46, m_14 = 0x14a, m_16 = 0x14a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x14a] = item


item = FuncInfo(name = "starthotlink", footprint = "ISSS", delegate_name = "fnStartHotLink", 
                    m_10 = 0x46, m_14 = 0x14b, m_16 = 0x14b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x14b] = item


item = FuncInfo(name = "starthotlink", footprint = "ISSSB", delegate_name = "fnStartHotLink", 
                    m_10 = 0x46, m_14 = 0x14c, m_16 = 0x14c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x14c] = item


item = FuncInfo(name = "startserverdde", footprint = "ISSV", delegate_name = "fnStartServerDDE", 
                    m_10 = 0x46, m_14 = 0x14d, m_16 = 0x14d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "...", m_4 = 0xffff, type_id = 0x8, m_a = 0x4))
c_40CF[0x14d] = item


item = FuncInfo(name = "startserverdde", footprint = "ICwindow.SSV", delegate_name = "fnStartServerDDE", 
                    m_10 = 0x46, m_14 = 0x14e, m_16 = 0x14e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "...", m_4 = 0xffff, type_id = 0x8, m_a = 0x4))
c_40CF[0x14e] = item


item = FuncInfo(name = "stophotlink", footprint = "ISSS", delegate_name = "fnStopHotLink", 
                    m_10 = 0x46, m_14 = 0x14f, m_16 = 0x14f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x14f] = item


item = FuncInfo(name = "stopserverdde", footprint = "ISS", delegate_name = "fnStopServerDDE", 
                    m_10 = 0x46, m_14 = 0x150, m_16 = 0x150, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x150] = item


item = FuncInfo(name = "stopserverdde", footprint = "ICwindow.SS", delegate_name = "fnStopServerDDE", 
                    m_10 = 0x46, m_14 = 0x151, m_16 = 0x151, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
item.parameters.append(ParamInfo(name = "a", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x151] = item


item = FuncInfo(name = "string", footprint = "SA", delegate_name = "fnString", 
                    m_10 = 0x46, m_14 = 0x152, m_16 = 0x152, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x152] = item


item = FuncInfo(name = "string", footprint = "SAS", delegate_name = "fnString", 
                    m_10 = 0x46, m_14 = 0x153, m_16 = 0x153, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x153] = item


item = FuncInfo(name = "string", footprint = "SOCencoding.", delegate_name = "fnString", 
                    m_10 = 0x46, m_14 = 0x154, m_16 = 0x154, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x4015, m_a = 0x8))
c_40CF[0x154] = item


item = FuncInfo(name = "signalerror", footprint = "I", delegate_name = "fnSignalError", 
                    m_10 = 0x46, m_14 = 0x155, m_16 = 0x155, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x155] = item


item = FuncInfo(name = "signalerror", footprint = "IIS", delegate_name = "fnSignalErrorMsg", 
                    m_10 = 0x46, m_14 = 0x156, m_16 = 0x156, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x156] = item


item = FuncInfo(name = "populateerror", footprint = "IIS", delegate_name = "fnPopulateError", 
                    m_10 = 0x46, m_14 = 0x157, m_16 = 0x157, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x157] = item


item = FuncInfo(name = "tan", footprint = "DD", delegate_name = "fnTan", 
                    m_10 = 0x46, m_14 = 0x158, m_16 = 0x158, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x4, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x158] = item


item = FuncInfo(name = "time", footprint = "TA", delegate_name = "fnTime", 
                    m_10 = 0x46, m_14 = 0x159, m_16 = 0x159, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x8, m_a = 0x0))
c_40CF[0x159] = item


item = FuncInfo(name = "time", footprint = "TIII", delegate_name = "fnTime", 
                    m_10 = 0x46, m_14 = 0x15a, m_16 = 0x15a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x15a] = item


item = FuncInfo(name = "time", footprint = "TIIII", delegate_name = "fnTime", 
                    m_10 = 0x46, m_14 = 0x15b, m_16 = 0x15b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "u", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x15b] = item


item = FuncInfo(name = "timer", footprint = "ID", delegate_name = "fnTimer", 
                    m_10 = 0x46, m_14 = 0x15c, m_16 = 0x15c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
c_40CF[0x15c] = item


item = FuncInfo(name = "timer", footprint = "IDCwindow.", delegate_name = "fnTimer", 
                    m_10 = 0x46, m_14 = 0x15d, m_16 = 0x15d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4, m_a = 0x0))
item.parameters.append(ParamInfo(name = "o", m_4 = 0xffff, type_id = 0x4084, m_a = 0x0))
c_40CF[0x15d] = item


item = FuncInfo(name = "today", footprint = "Y", delegate_name = "fnToday", 
                    m_10 = 0x46, m_14 = 0x15e, m_16 = 0x15e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x15e] = item


item = FuncInfo(name = "tracebegin", footprint = "Cerrorreturn.XS", delegate_name = "FN_BeginTrace", 
                    m_10 = 0x46, m_14 = 0x15f, m_16 = 0x15f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "identifier", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x15f] = item


item = FuncInfo(name = "traceclose", footprint = "Cerrorreturn.", delegate_name = "FN_CloseTrace", 
                    m_10 = 0x46, m_14 = 0x160, m_16 = 0x160, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x160] = item


item = FuncInfo(name = "tracedisableactivity", footprint = "Cerrorreturn.Ctraceactivity.", delegate_name = "FN_DisableEventTrace", 
                    m_10 = 0x46, m_14 = 0x161, m_16 = 0x161, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "activity", m_4 = 0xffff, type_id = 0x40c7, m_a = 0x8))
c_40CF[0x161] = item


item = FuncInfo(name = "tracedump", footprint = "Cerrorreturn.XSXS", delegate_name = "FN_DumpTrace", 
                    m_10 = 0x46, m_14 = 0x162, m_16 = 0x162, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x3, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "infilename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "outfilename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x162] = item


item = FuncInfo(name = "traceenableactivity", footprint = "Cerrorreturn.Ctraceactivity.", delegate_name = "FN_EnableEventTrace", 
                    m_10 = 0x46, m_14 = 0x163, m_16 = 0x163, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "activity", m_4 = 0xffff, type_id = 0x40c7, m_a = 0x8))
c_40CF[0x163] = item


item = FuncInfo(name = "traceend", footprint = "Cerrorreturn.", delegate_name = "FN_EndTrace", 
                    m_10 = 0x46, m_14 = 0x164, m_16 = 0x164, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x164] = item


item = FuncInfo(name = "traceerror", footprint = "Cerrorreturn.LXS", delegate_name = "FN_TraceErrorEvent", 
                    m_10 = 0x46, m_14 = 0x165, m_16 = 0x165, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "severity", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "message", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x165] = item


item = FuncInfo(name = "traceopen", footprint = "Cerrorreturn.XSCtimerkind.", delegate_name = "FN_OpenTrace", 
                    m_10 = 0x46, m_14 = 0x166, m_16 = 0x166, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "filename", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "timer", m_4 = 0xffff, type_id = 0x40c6, m_a = 0x8))
c_40CF[0x166] = item


item = FuncInfo(name = "traceuser", footprint = "Cerrorreturn.LXS", delegate_name = "FN_TraceUserEvent", 
                    m_10 = 0x46, m_14 = 0x167, m_16 = 0x167, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40c8, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "info", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "message", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x167] = item


item = FuncInfo(name = "trim", footprint = "SXS", delegate_name = "fnTrim", 
                    m_10 = 0x46, m_14 = 0x168, m_16 = 0x168, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x168] = item


item = FuncInfo(name = "trim", footprint = "SXSB", delegate_name = "fnTrim", 
                    m_10 = 0x46, m_14 = 0x169, m_16 = 0x169, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "removealltypespaces", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x169] = item


item = FuncInfo(name = "truncate", footprint = "MMI", delegate_name = "fnTruncate", 
                    m_10 = 0x46, m_14 = 0x16a, m_16 = 0x16a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x5, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x5, m_a = 0xf8))
item.parameters.append(ParamInfo(name = "p", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x16a] = item


item = FuncInfo(name = "unitstopixels", footprint = "IICconverttype.", delegate_name = "fnUnitsToPixels", 
                    m_10 = 0x46, m_14 = 0x16b, m_16 = 0x16b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "u", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x400b, m_a = 0x8))
c_40CF[0x16b] = item


item = FuncInfo(name = "upper", footprint = "SXS", delegate_name = "fnUpper", 
                    m_10 = 0x46, m_14 = 0x16c, m_16 = 0x16c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x16c] = item


item = FuncInfo(name = "upperbound", footprint = "LRA[]", delegate_name = "fnUpperBound", 
                    m_10 = 0x46, m_14 = 0x16d, m_16 = 0x16d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xcb1c, type_id = 0x8, m_a = 0x3))
c_40CF[0x16d] = item


item = FuncInfo(name = "upperbound", footprint = "LRA[]I", delegate_name = "fnUpperBound", 
                    m_10 = 0x46, m_14 = 0x16e, m_16 = 0x16e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "a", m_4 = 0xcb58, type_id = 0x8, m_a = 0x3))
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x16e] = item


item = FuncInfo(name = "year", footprint = "IY", delegate_name = "fnYear", 
                    m_10 = 0x46, m_14 = 0x16f, m_16 = 0x16f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "d", m_4 = 0xffff, type_id = 0xc, m_a = 0x0))
c_40CF[0x16f] = item


item = FuncInfo(name = "yield", footprint = "B", delegate_name = "fnYield", 
                    m_10 = 0x46, m_14 = 0x170, m_16 = 0x170, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x170] = item


item = FuncInfo(name = "wordcap", footprint = "SS", delegate_name = "fnWordCap", 
                    m_10 = 0x46, m_14 = 0x171, m_16 = 0x171, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x171] = item


item = FuncInfo(name = "reverse", footprint = "SXS", delegate_name = "fnReverse", 
                    m_10 = 0x46, m_14 = 0x172, m_16 = 0x172, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x172] = item


item = FuncInfo(name = "ishebrew", footprint = "BXH", delegate_name = "fnIsHebrew", 
                    m_10 = 0x46, m_14 = 0x173, m_16 = 0x173, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x12, m_a = 0x6))
c_40CF[0x173] = item


item = FuncInfo(name = "isallhebrew", footprint = "BXS", delegate_name = "fnIsAllHebrew", 
                    m_10 = 0x46, m_14 = 0x174, m_16 = 0x174, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x174] = item


item = FuncInfo(name = "isanyhebrew", footprint = "BXS", delegate_name = "fnAnyHebrew", 
                    m_10 = 0x46, m_14 = 0x175, m_16 = 0x175, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x175] = item


item = FuncInfo(name = "ishebrewandnumbers", footprint = "BXS", delegate_name = "fnIsHebrewAndNumbers", 
                    m_10 = 0x46, m_14 = 0x176, m_16 = 0x176, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x176] = item


item = FuncInfo(name = "isarabic", footprint = "BXH", delegate_name = "fnIsArabic", 
                    m_10 = 0x46, m_14 = 0x177, m_16 = 0x177, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "c", m_4 = 0xffff, type_id = 0x12, m_a = 0x6))
c_40CF[0x177] = item


item = FuncInfo(name = "isallarabic", footprint = "BXS", delegate_name = "fnIsAllArabic", 
                    m_10 = 0x46, m_14 = 0x178, m_16 = 0x178, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x178] = item


item = FuncInfo(name = "isanyarabic", footprint = "BXS", delegate_name = "fnAnyArabic", 
                    m_10 = 0x46, m_14 = 0x179, m_16 = 0x179, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x179] = item


item = FuncInfo(name = "isarabicandnumbers", footprint = "BXS", delegate_name = "fnIsArabicAndNumbers", 
                    m_10 = 0x46, m_14 = 0x17a, m_16 = 0x17a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x17a] = item


item = FuncInfo(name = "toansi", footprint = "OS", delegate_name = "fnToAnsi", 
                    m_10 = 0x46, m_14 = 0x17b, m_16 = 0x17b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x17b] = item


item = FuncInfo(name = "fromansi", footprint = "SO", delegate_name = "fnFromAnsi", 
                    m_10 = 0x46, m_14 = 0x17c, m_16 = 0x17c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x17c] = item


item = FuncInfo(name = "tounicode", footprint = "OS", delegate_name = "fnToUnicode", 
                    m_10 = 0x46, m_14 = 0x17d, m_16 = 0x17d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x17d] = item


item = FuncInfo(name = "fromunicode", footprint = "SO", delegate_name = "fnFromUnicode", 
                    m_10 = 0x46, m_14 = 0x17e, m_16 = 0x17e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x17e] = item


item = FuncInfo(name = "toutf8", footprint = "OS", delegate_name = "fnToUTF8", 
                    m_10 = 0x46, m_14 = 0x17f, m_16 = 0x17f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0xb, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x17f] = item


item = FuncInfo(name = "fromutf8", footprint = "SO", delegate_name = "fnFromUTF8", 
                    m_10 = 0x46, m_14 = 0x180, m_16 = 0x180, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x180] = item


item = FuncInfo(name = "fillw", footprint = "SXSL", delegate_name = "fnFillW", 
                    m_10 = 0x46, m_14 = 0x181, m_16 = 0x181, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x181] = item


item = FuncInfo(name = "leftw", footprint = "SXSL", delegate_name = "fnLeftW", 
                    m_10 = 0x46, m_14 = 0x182, m_16 = 0x182, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x182] = item


item = FuncInfo(name = "lefttrimw", footprint = "SXS", delegate_name = "fnLeftTrimW", 
                    m_10 = 0x46, m_14 = 0x183, m_16 = 0x183, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x183] = item


item = FuncInfo(name = "lenw", footprint = "LO", delegate_name = "fnLenW", 
                    m_10 = 0x46, m_14 = 0x184, m_16 = 0x184, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x184] = item


item = FuncInfo(name = "lenw", footprint = "LS", delegate_name = "fnLenW", 
                    m_10 = 0x46, m_14 = 0x185, m_16 = 0x185, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x185] = item


item = FuncInfo(name = "matchw", footprint = "BXSXS", delegate_name = "fnMatchW", 
                    m_10 = 0x46, m_14 = 0x186, m_16 = 0x186, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x7, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x186] = item


item = FuncInfo(name = "midw", footprint = "SXSL", delegate_name = "fnMidW", 
                    m_10 = 0x46, m_14 = 0x187, m_16 = 0x187, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x187] = item


item = FuncInfo(name = "midw", footprint = "SXSLL", delegate_name = "fnMidW", 
                    m_10 = 0x46, m_14 = 0x188, m_16 = 0x188, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x188] = item


item = FuncInfo(name = "posw", footprint = "LXSXS", delegate_name = "fnPosW", 
                    m_10 = 0x46, m_14 = 0x189, m_16 = 0x189, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x189] = item


item = FuncInfo(name = "posw", footprint = "LXSXSL", delegate_name = "fnPosW", 
                    m_10 = 0x46, m_14 = 0x18a, m_16 = 0x18a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x18a] = item


item = FuncInfo(name = "replacew", footprint = "SXSLLXS", delegate_name = "fnReplaceW", 
                    m_10 = 0x46, m_14 = 0x18b, m_16 = 0x18b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x18b] = item


item = FuncInfo(name = "rightw", footprint = "SXSL", delegate_name = "fnRightW", 
                    m_10 = 0x46, m_14 = 0x18c, m_16 = 0x18c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x18c] = item


item = FuncInfo(name = "righttrimw", footprint = "SXS", delegate_name = "fnRightTrimW", 
                    m_10 = 0x46, m_14 = 0x18d, m_16 = 0x18d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x18d] = item


item = FuncInfo(name = "trimw", footprint = "SXS", delegate_name = "fnTrimW", 
                    m_10 = 0x46, m_14 = 0x18e, m_16 = 0x18e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x18e] = item


item = FuncInfo(name = "imesetmode", footprint = "ILI", delegate_name = "fnIMESetMode", 
                    m_10 = 0x46, m_14 = 0x18f, m_16 = 0x18f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "m", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x18f] = item


item = FuncInfo(name = "imegetmode", footprint = "IL", delegate_name = "fnIMEGetMode", 
                    m_10 = 0x46, m_14 = 0x190, m_16 = 0x190, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x190] = item


item = FuncInfo(name = "imegetcompositiontext", footprint = "SL", delegate_name = "fnIMEGetCompositionText", 
                    m_10 = 0x46, m_14 = 0x191, m_16 = 0x191, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x191] = item


item = FuncInfo(name = "findclassdefinition", footprint = "Cclassdefinition.S", delegate_name = "fnFindClass", 
                    m_10 = 0x46, m_14 = 0x192, m_16 = 0x192, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40ce, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x192] = item


item = FuncInfo(name = "findclassdefinition", footprint = "Cclassdefinition.SS[]", delegate_name = "fnFindClass", 
                    m_10 = 0x46, m_14 = 0x193, m_16 = 0x193, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40ce, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xd0e4, type_id = 0x6, m_a = 0x1))
c_40CF[0x193] = item


item = FuncInfo(name = "findtypedefinition", footprint = "Ctypedefinition.S", delegate_name = "fnFindType", 
                    m_10 = 0x46, m_14 = 0x194, m_16 = 0x194, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40cd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x194] = item


item = FuncInfo(name = "findtypedefinition", footprint = "Ctypedefinition.SS[]", delegate_name = "fnFindType", 
                    m_10 = 0x46, m_14 = 0x195, m_16 = 0x195, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40cd, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xd12c, type_id = 0x6, m_a = 0x1))
c_40CF[0x195] = item


item = FuncInfo(name = "findfunctiondefinition", footprint = "Cscriptdefinition.S", delegate_name = "fnFindFunctionDefinition", 
                    m_10 = 0x46, m_14 = 0x196, m_16 = 0x196, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40cc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x196] = item


item = FuncInfo(name = "findfunctiondefinition", footprint = "Cscriptdefinition.SS[]", delegate_name = "fnFindFunctionDefinition", 
                    m_10 = 0x46, m_14 = 0x197, m_16 = 0x197, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x40cc, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "l", m_4 = 0xd198, type_id = 0x6, m_a = 0x1))
c_40CF[0x197] = item


item = FuncInfo(name = "gpf", footprint = "L", delegate_name = "ot_cause_gpf", 
                    m_10 = 0x46, m_14 = 0x198, m_16 = 0x198, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x3, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x198] = item


item = FuncInfo(name = "setlibrarylist", footprint = "IS", delegate_name = "fnSetLibraryList", 
                    m_10 = 0x46, m_14 = 0x199, m_16 = 0x199, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x199] = item


item = FuncInfo(name = "getlibrarylist", footprint = "S", delegate_name = "fnGetLibraryList", 
                    m_10 = 0x46, m_14 = 0x19a, m_16 = 0x19a, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
c_40CF[0x19a] = item


item = FuncInfo(name = "addtolibrarylist", footprint = "IS", delegate_name = "fnAddToLibraryList", 
                    m_10 = 0x46, m_14 = 0x19b, m_16 = 0x19b, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x1, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "l", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x19b] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LS", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x19c, m_16 = 0x19c, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x19c] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x19d, m_16 = 0x19d, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
c_40CF[0x19d] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.RS", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x19e, m_16 = 0x19e, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x19e] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.RSB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x19f, m_16 = 0x19f, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x19f] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.RSBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a0, m_16 = 0x1a0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a0] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.RSBBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a1, m_16 = 0x1a1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a1] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.B", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a2, m_16 = 0x1a2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a2] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.BB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a3, m_16 = 0x1a3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a3] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSCvalschemetype.BBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a4, m_16 = 0x1a4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a4] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSRS", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a5, m_16 = 0x1a5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x1a5] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSRSB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a6, m_16 = 0x1a6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a6] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSRSBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a7, m_16 = 0x1a7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a7] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSRSBBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a8, m_16 = 0x1a8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a8] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1a9, m_16 = 0x1a9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1a9] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1aa, m_16 = 0x1aa, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1aa] = item


item = FuncInfo(name = "xmlparsefile", footprint = "LSBBB", delegate_name = "fnXMLParseFile", 
                    m_10 = 0x46, m_14 = 0x1ab, m_16 = 0x1ab, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1ab] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LS", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1ac, m_16 = 0x1ac, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x1ac] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1ad, m_16 = 0x1ad, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
c_40CF[0x1ad] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.RS", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1ae, m_16 = 0x1ae, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x1ae] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.RSB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1af, m_16 = 0x1af, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1af] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.RSBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b0, m_16 = 0x1b0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b0] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.RSBBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b1, m_16 = 0x1b1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b1] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.B", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b2, m_16 = 0x1b2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b2] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.BB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b3, m_16 = 0x1b3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b3] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSCvalschemetype.BBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b4, m_16 = 0x1b4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "v", m_4 = 0xffff, type_id = 0x4071, m_a = 0x8))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b4] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSRS", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b5, m_16 = 0x1b5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
c_40CF[0x1b5] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSRSB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b6, m_16 = 0x1b6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b6] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSRSBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b7, m_16 = 0x1b7, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b7] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSRSBBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b8, m_16 = 0x1b8, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "e", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b8] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1b9, m_16 = 0x1b9, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1b9] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1ba, m_16 = 0x1ba, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1ba] = item


item = FuncInfo(name = "xmlparsestring", footprint = "LSBBB", delegate_name = "fnXMLParseString", 
                    m_10 = 0x46, m_14 = 0x1bb, m_16 = 0x1bb, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
item.parameters.append(ParamInfo(name = "ns", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
item.parameters.append(ParamInfo(name = "sf", m_4 = 0xffff, type_id = 0x7, m_a = 0x0))
c_40CF[0x1bb] = item


item = FuncInfo(name = "filla", footprint = "SXSL", delegate_name = "fnFillA", 
                    m_10 = 0x46, m_14 = 0x1bc, m_16 = 0x1bc, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "f", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1bc] = item


item = FuncInfo(name = "lefta", footprint = "SXSL", delegate_name = "fnLeftA", 
                    m_10 = 0x46, m_14 = 0x1bd, m_16 = 0x1bd, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1bd] = item


item = FuncInfo(name = "lena", footprint = "LO", delegate_name = "fnLenA", 
                    m_10 = 0x46, m_14 = 0x1be, m_16 = 0x1be, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "b", m_4 = 0xffff, type_id = 0xb, m_a = 0x0))
c_40CF[0x1be] = item


item = FuncInfo(name = "lena", footprint = "LS", delegate_name = "fnLenA", 
                    m_10 = 0x46, m_14 = 0x1bf, m_16 = 0x1bf, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x0))
c_40CF[0x1bf] = item


item = FuncInfo(name = "mida", footprint = "SXSL", delegate_name = "fnMidA", 
                    m_10 = 0x46, m_14 = 0x1c0, m_16 = 0x1c0, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1c0] = item


item = FuncInfo(name = "mida", footprint = "SXSLL", delegate_name = "fnMidA", 
                    m_10 = 0x46, m_14 = 0x1c1, m_16 = 0x1c1, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1c1] = item


item = FuncInfo(name = "posa", footprint = "LXSXS", delegate_name = "fnPosA", 
                    m_10 = 0x46, m_14 = 0x1c2, m_16 = 0x1c2, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x1c2] = item


item = FuncInfo(name = "posa", footprint = "LXSXSL", delegate_name = "fnPosA", 
                    m_10 = 0x46, m_14 = 0x1c3, m_16 = 0x1c3, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1c3] = item


item = FuncInfo(name = "replacea", footprint = "SXSLLXS", delegate_name = "fnReplaceA", 
                    m_10 = 0x46, m_14 = 0x1c4, m_16 = 0x1c4, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s1", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "y", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "s2", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
c_40CF[0x1c4] = item


item = FuncInfo(name = "righta", footprint = "SXSL", delegate_name = "fnRightA", 
                    m_10 = 0x46, m_14 = 0x1c5, m_16 = 0x1c5, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x6, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "s", m_4 = 0xffff, type_id = 0x6, m_a = 0x6))
item.parameters.append(ParamInfo(name = "x", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
c_40CF[0x1c5] = item


item = FuncInfo(name = "pbgetmenustring", footprint = "LLIRSI", delegate_name = "fnGetMenuString", 
                    m_10 = 0x46, m_14 = 0x1c6, m_16 = 0x1c6, m_18 = 0xffff, m_1a = 0x0, 
                    return_type_id = 0x2, m_1f = 0xa, m_20 = 0xffff, m_22 = 0x2, 
                    m_24 = 0x0, m_28 = 0x0, m_2c = 0xffff, m_2e = 0x0)
item.parameters.append(ParamInfo(name = "h", m_4 = 0xffff, type_id = 0x2, m_a = 0x0))
item.parameters.append(ParamInfo(name = "i", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
item.parameters.append(ParamInfo(name = "t", m_4 = 0xffff, type_id = 0x6, m_a = 0x2))
item.parameters.append(ParamInfo(name = "n", m_4 = 0xffff, type_id = 0x1, m_a = 0x0))
c_40CF[0x1c6] = item

