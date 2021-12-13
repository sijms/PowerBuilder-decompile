from pbd.definitions import EnumInfo
# 26 1E 00 00 02 00 2A 00 
# FC 1D 00 00 00 00 2A 00
# 50 1E 00 00 04 00 2A 00 
# 3E 1E 00 00 03 00 2A 00
# 14 1E 00 00 01 00 2A 00
e_4007 = dict()
e_4007[0] = EnumInfo('ok', 0, 0x2a)
e_4007[1] = EnumInfo('okcancel', 1, 0x2a)
e_4007[2] = EnumInfo('retrycancel', 2, 0x2a)
e_4007[3] = EnumInfo('abortretryignore', 3, 0x2a)
e_4007[4] = EnumInfo('yesno', 4, 0x2a)
e_4007[5] = EnumInfo('yesnocancel', 5, 0x2a)

e_4021 = dict()
e_4021[0] = EnumInfo('encodingansi', 0, 0x2a)
e_4021[1] = EnumInfo('encodingutf16le', 1, 0x2a)
e_4021[2] = EnumInfo('encodingutf8', 2, 0x2a)
e_4021[3] = EnumInfo('encodingutf16be', 3, 0x2a)

e_402F = dict()
e_402F[0] = EnumInfo('information', 0, 0x2a)
e_402F[1] = EnumInfo('stopsign', 1, 0x2a)
e_402F[2] = EnumInfo('exclamation', 2, 0x2a)
e_402F[3] = EnumInfo('question', 3, 0x2a)
e_402F[4] = EnumInfo('none', 4, 0x2a)

e_4038 = dict()
e_4038[0] = EnumInfo("keynull", 0, 0)

{ "m_0": 0x0, "m_4": 0xffff, "name": "keyleftbutton", "class_index": 0x1 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyrightbutton", "class_index": 0x2 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keymiddlebutton", "class_index": 0x4 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyback", "class_index": 0x8 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keytab", "class_index": 0x9 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyenter", "class_index": 0xd },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyshift", "class_index": 0x10 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keycontrol", "class_index": 0x11 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyalt", "class_index": 0x12 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keypause", "class_index": 0x13 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keycapslock", "class_index": 0x14 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyescape", "class_index": 0x1b },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyspacebar", "class_index": 0x20 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keypageup", "class_index": 0x21 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keypagedown", "class_index": 0x22 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyend", "class_index": 0x23 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyhome", "class_index": 0x24 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyleftarrow", "class_index": 0x25 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyuparrow", "class_index": 0x26 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyrightarrow", "class_index": 0x27 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keydownarrow", "class_index": 0x28 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyprintscreen", "class_index": 0x2c },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyinsert", "class_index": 0x2d },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keydelete", "class_index": 0x2e },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key0", "class_index": 0x30 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key1", "class_index": 0x31 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key2", "class_index": 0x32 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key3", "class_index": 0x33 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key4", "class_index": 0x34 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key5", "class_index": 0x35 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key6", "class_index": 0x36 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key7", "class_index": 0x37 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key8", "class_index": 0x38 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "key9", "class_index": 0x39 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keya", "class_index": 0x41 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyb", "class_index": 0x42 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyc", "class_index": 0x43 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyd", "class_index": 0x44 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keye", "class_index": 0x45 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf", "class_index": 0x46 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyg", "class_index": 0x47 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyh", "class_index": 0x48 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyi", "class_index": 0x49 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyj", "class_index": 0x4a },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyk", "class_index": 0x4b },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyl", "class_index": 0x4c },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keym", "class_index": 0x4d },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyn", "class_index": 0x4e },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyo", "class_index": 0x4f },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyp", "class_index": 0x50 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyq", "class_index": 0x51 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyr", "class_index": 0x52 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keys", "class_index": 0x53 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyt", "class_index": 0x54 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyu", "class_index": 0x55 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyv", "class_index": 0x56 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyw", "class_index": 0x57 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyx", "class_index": 0x58 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyy", "class_index": 0x59 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyz", "class_index": 0x5a },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyleftwindows", "class_index": 0x5b },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyrightwindows", "class_index": 0x5c },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyapps", "class_index": 0x5d },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad0", "class_index": 0x60 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad1", "class_index": 0x61 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad2", "class_index": 0x62 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad3", "class_index": 0x63 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad4", "class_index": 0x64 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad5", "class_index": 0x65 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad6", "class_index": 0x66 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad7", "class_index": 0x67 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad8", "class_index": 0x68 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumpad9", "class_index": 0x69 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keymultiply", "class_index": 0x6a },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyadd", "class_index": 0x6b },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keysubtract", "class_index": 0x6d },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keydecimal", "class_index": 0x6e },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keydivide", "class_index": 0x6f },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf1", "class_index": 0x70 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf2", "class_index": 0x71 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf3", "class_index": 0x72 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf4", "class_index": 0x73 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf5", "class_index": 0x74 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf6", "class_index": 0x75 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf7", "class_index": 0x76 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf8", "class_index": 0x77 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf9", "class_index": 0x78 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf10", "class_index": 0x79 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf11", "class_index": 0x7a },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyf12", "class_index": 0x7b },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keynumlock", "class_index": 0x90 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyscrolllock", "class_index": 0x91 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keysemicolon", "class_index": 0xba },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyequal", "class_index": 0xbb },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keycomma", "class_index": 0xbc },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keydash", "class_index": 0xbd },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyperiod", "class_index": 0xbe },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyslash", "class_index": 0xbf },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keybackquote", "class_index": 0xc0 },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyleftbracket", "class_index": 0xdb },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keybackslash", "class_index": 0xdc },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyrightbracket", "class_index": 0xdd },
{ "m_0": 0x0, "m_4": 0xffff, "name": "keyquote", "class_index": 0xde },


# 9C 08 00 00 03 00 2A 00 
# 6C 08 00 00 00 00 2A 00
# 72 08 00 00 01 00 2A 00 
# 84 08 00 00 02 00 2A 00
# BE 08 00 00 04 00 2A 00 
# CA 08 00 00 05 00 2A 00

e_404A = dict()
e_404A[0] = EnumInfo("adoresultset", 0, 42)
e_404A[1] = EnumInfo("animation", 1, 42)
e_404A[2] = EnumInfo("application", 2, 42)
e_404A[3] = EnumInfo("arraybounds", 3, 42)
e_404A[4] = EnumInfo("checkbox", 4, 42)
e_404A[5] = EnumInfo("classdefinition", 5, 42)
e_404A[6] = EnumInfo("classdefinitionobject", 6, 42)
e_404A[7] = EnumInfo("commandbutton", 7, 42)
e_404A[8] = EnumInfo("connection", 8, 0)
e_404A[9] = EnumInfo("connectioninfo", 9, 0)
e_404A[10] = EnumInfo("connectobject", 10, 0)
e_404A[11] = EnumInfo("contextinformation", 11, 0)
e_404A[12] = EnumInfo("contextkeyword", 12, 0)
e_404A[13] = EnumInfo("corbacurrent", 13, 0)
e_404A[14] = EnumInfo("corbaobject", 14, 0)
e_404A[15] = EnumInfo("corbaunion", 15, 0)
e_404A[16] = EnumInfo("cplusplus", 16, 0)
e_404A[17] = EnumInfo("datastore", 17, 0)
e_404A[18] = EnumInfo("datawindow", 18, 0)
e_404A[19] = EnumInfo("datawindowchild", 19, 0)
e_404A[20] = EnumInfo("datepicker", 20, 0)
e_404A[21] = EnumInfo("dragobject", 21, 0)
e_404A[22] = EnumInfo("drawobject", 22, 0)
e_404A[23] = EnumInfo("dropdownlistbox", 23, 0)
e_404A[24] = EnumInfo("dropdownpicturelistbox", 24, 97)
e_404A[25] = EnumInfo("dwobject", 25, 116)
e_404A[26] = EnumInfo("dynamicdescriptionarea", 26, 101)
e_404A[27] = EnumInfo("dynamicstagingarea", 27, 0)
e_404A[28] = EnumInfo("editmask", 28, 0)
e_404A[29] = EnumInfo("enumerationdefinition", 29, 0)
e_404A[30] = EnumInfo("enumerationitemdefinition", 30, 0)
e_404A[31] = EnumInfo("environment", 31, 0)
e_404A[32] = EnumInfo("error", 32, 0)
e_404A[33] = EnumInfo("errorlogging", 33, 0)
e_404A[34] = EnumInfo("extobject", 34, 0)
e_404A[35] = EnumInfo("functionobject", 35, 0)
e_404A[36] = EnumInfo("graph", 36, 0)
e_404A[37] = EnumInfo("graphicobject", 37, 0)
e_404A[38] = EnumInfo("graxis", 38, 0)
e_404A[39] = EnumInfo("grdispattr", 39, 0)
e_404A[40] = EnumInfo("groupbox", 40, 0)
e_404A[41] = EnumInfo("hprogressbar", 41, 0)
e_404A[42] = EnumInfo("hscrollbar", 42, 0)
e_404A[43] = EnumInfo("htrackbar", 43, 0)
e_404A[44] = EnumInfo("inet", 44, 0)
e_404A[45] = EnumInfo("inkedit", 45, 0)
e_404A[46] = EnumInfo("inkpicture", 46, 0)
e_404A[47] = EnumInfo("internetresult", 47, 0)
e_404A[48] = EnumInfo("jaguarorb", 48, 0)
e_404A[49] = EnumInfo("line", 49, 16384)
e_404A[50] = EnumInfo("listbox", 50, 0)
e_404A[51] = EnumInfo("listview", 51, 0)
e_404A[52] = EnumInfo("listviewitem", 52, 0)
e_404A[53] = EnumInfo("mailfiledescription", 53, 0)
e_404A[54] = EnumInfo("mailmessage", 54, 0)
e_404A[55] = EnumInfo("mailrecipient", 55, 0)
e_404A[56] = EnumInfo("mailsession", 56, 0)
e_404A[57] = EnumInfo("mdiclient", 57, 0)
e_404A[58] = EnumInfo("menu", 58, 0)
e_404A[59] = EnumInfo("menucascade", 59, 0)
e_404A[60] = EnumInfo("message", 60, 0)
e_404A[61] = EnumInfo("mlsync", 61, 0)
e_404A[62] = EnumInfo("mlsynchronization", 62, 0)
e_404A[63] = EnumInfo("monthcalendar", 63, 0)
e_404A[64] = EnumInfo("multilineedit", 64, 116)
e_404A[65] = EnumInfo("nonvisualobject", 65, 111)
e_404A[66] = EnumInfo("olecontrol", 66, 116)
e_404A[67] = EnumInfo("olecustomcontrol", 67, 98)
e_404A[68] = EnumInfo("oleobject", 68, 111)
e_404A[69] = EnumInfo("olestorage", 69, 115)
e_404A[70] = EnumInfo("olestream", 70, 117)
e_404A[71] = EnumInfo("oletxnobject", 71, 114)
e_404A[72] = EnumInfo("omcontrol", 72, 101)
e_404A[73] = EnumInfo("omcustomcontrol", 73, 98)
e_404A[74] = EnumInfo("omembeddedcontrol", 74, 111)
e_404A[75] = EnumInfo("omobject", 75, 99)
e_404A[76] = EnumInfo("omstorage", 76, 109)
e_404A[77] = EnumInfo("omstream", 77, 97)
e_404A[78] = EnumInfo("orb", 78, 114)
e_404A[79] = EnumInfo("oval", 79, 0)
e_404A[80] = EnumInfo("pbtocppobject", 80, 104)
e_404A[81] = EnumInfo("picture", 81, 101)
e_404A[82] = EnumInfo("picturebutton", 82, 108)
e_404A[83] = EnumInfo("picturehyperlink", 83, 111)
e_404A[84] = EnumInfo("picturelistbox", 84, 110)
e_404A[85] = EnumInfo("pipeline", 85, 101)
e_404A[86] = EnumInfo("powerobject", 86, 119)
e_404A[87] = EnumInfo("profilecall", 87, 101)
e_404A[88] = EnumInfo("profileclass", 88, 0)
e_404A[89] = EnumInfo("profileline", 89, 0)
e_404A[90] = EnumInfo("profileroutine", 90, 0)
e_404A[91] = EnumInfo("profiling", 91, 0)
e_404A[92] = EnumInfo("radiobutton", 92, 0)
e_404A[93] = EnumInfo("rectangle", 93, 0)
e_404A[94] = EnumInfo("remoteobject", 94, 0)
e_404A[95] = EnumInfo("resultset", 95, 0)
e_404A[96] = EnumInfo("resultsets", 96, 0)
e_404A[97] = EnumInfo("richtextedit", 97, 0)
e_404A[98] = EnumInfo("roundrectangle", 98, 0)
e_404A[99] = EnumInfo("scriptdefinition", 99, 0)
e_404A[100] = EnumInfo("service", 100, 0)
e_404A[101] = EnumInfo("simpletypedefinition", 101, 0)
e_404A[102] = EnumInfo("singlelineedit", 102, 0)
e_404A[103] = EnumInfo("sslcallback", 103, 0)
e_404A[104] = EnumInfo("sslserviceprovider", 104, 0)
e_404A[105] = EnumInfo("statichyperlink", 105, 0)
e_404A[106] = EnumInfo("statictext", 106, 0)
e_404A[107] = EnumInfo("structure", 107, 0)
e_404A[108] = EnumInfo("syncparm", 108, 0)
e_404A[109] = EnumInfo("systemfunctions", 109, 0)
e_404A[110] = EnumInfo("tab", 110, 0)
e_404A[111] = EnumInfo("timing", 111, 0)
e_404A[112] = EnumInfo("traceactivitynode", 112, 0)
e_404A[113] = EnumInfo("tracebeginend", 113, 0)
e_404A[114] = EnumInfo("traceerror", 114, 0)
e_404A[115] = EnumInfo("traceesql", 115, 0)
e_404A[116] = EnumInfo("tracefile", 116, 0)
e_404A[117] = EnumInfo("tracegarbagecollect", 117, 0)
e_404A[118] = EnumInfo("traceline", 118, 0)
e_404A[119] = EnumInfo("traceobject", 119, 0)
e_404A[120] = EnumInfo("traceroutine", 120, 0)
e_404A[121] = EnumInfo("tracetree", 121, 0)
e_404A[122] = EnumInfo("tracetreeerror", 122, 0)
e_404A[123] = EnumInfo("tracetreeesql", 123, 0)
e_404A[124] = EnumInfo("tracetreegarbagecollect", 124, 0)
e_404A[125] = EnumInfo("tracetreeline", 125, 0)
e_404A[126] = EnumInfo("tracetreenode", 126, 0)
e_404A[127] = EnumInfo("tracetreeobject", 127, 0)
e_404A[128] = EnumInfo("tracetreeroutine", 128, 0)
e_404A[129] = EnumInfo("tracetreeuser", 129, 0)
e_404A[130] = EnumInfo("traceuser", 130, 0)
e_404A[131] = EnumInfo("transaction", 131, 0)
e_404A[132] = EnumInfo("transactionserver", 132, 0)
e_404A[133] = EnumInfo("treeview", 133, 0)
e_404A[134] = EnumInfo("treeviewitem", 134, 0)
e_404A[135] = EnumInfo("typedefinition", 135, 0)
e_404A[136] = EnumInfo("ulsync", 136, 0)
e_404A[137] = EnumInfo("userobject", 137, 0)
e_404A[138] = EnumInfo("variablecardinalitydefinition", 138, 0)
e_404A[139] = EnumInfo("variabledefinition", 139, 0)
e_404A[140] = EnumInfo("vprogressbar", 140, 0)
e_404A[141] = EnumInfo("vscrollbar", 141, 0)
e_404A[142] = EnumInfo("vtrackbar", 142, 0)
e_404A[143] = EnumInfo("window", 143, 0)
e_404A[144] = EnumInfo("windowobject", 144, 0)
e_404A[145] = EnumInfo("wsconnection", 145, 0)
e_404A[146] = EnumInfo("blob", 146, 0)
e_404A[147] = EnumInfo("boolean", 147, 0)
e_404A[148] = EnumInfo("character", 148, 0)
e_404A[149] = EnumInfo("date", 149, 0)
e_404A[150] = EnumInfo("datetime", 150, 0)
e_404A[151] = EnumInfo("decimal", 151, 0)
e_404A[152] = EnumInfo("double", 152, 0)
e_404A[153] = EnumInfo("notype", 153, 0)
e_404A[154] = EnumInfo("integer", 154, 0)
e_404A[155] = EnumInfo("long", 155, 0)
e_404A[156] = EnumInfo("objhandle", 156, 0)
e_404A[157] = EnumInfo("real", 157, 0)
e_404A[158] = EnumInfo("string", 158, 0)
e_404A[159] = EnumInfo("time", 159, 0)
e_404A[160] = EnumInfo("unsignedinteger", 160, 0)
e_404A[161] = EnumInfo("unsignedlong", 161, 0)
e_404A[162] = EnumInfo("any", 162, 0)

e_4055 = dict()
e_4055[12] = EnumInfo("appstarting", 12, 0)
e_4055[0] = EnumInfo("arrow", 0, 42)
e_4055[2] = EnumInfo("beam", 2, 42)
e_4055[1] = EnumInfo("cross", 1, 42)
e_4055[13] = EnumInfo("help", 13, 0)
e_4055[8] = EnumInfo("hourglass", 8, 0)
e_4055[14] = EnumInfo("hyperlink", 14, 0)
e_4055[9] = EnumInfo("icon", 9, 0)
e_4055[11] = EnumInfo("nopointer", 11, 0)
e_4055[10] = EnumInfo("size", 10, 0)
e_4055[3] = EnumInfo("sizenesw", 3, 42)
e_4055[4] = EnumInfo("sizens", 4, 42)
e_4055[5] = EnumInfo("sizenwse", 5, 42)
e_4055[6] = EnumInfo("sizewe", 6, 42)
e_4055[7] = EnumInfo("uparrow", 7, 42)

e_4056 = dict()
e_4056[1] = EnumInfo("regstring", 1, 0)
e_4056[2] = EnumInfo("regexpandstring", 2, 0)
e_4056[3] = EnumInfo("regbinary", 3, 0)
e_4056[4] = EnumInfo("regulong", 4, 0)
e_4056[5] = EnumInfo("regulongbigendian", 5, 0)
e_4056[6] = EnumInfo("reglink", 6, 0)
e_4056[7] = EnumInfo("regmultistring", 7, 0)

e_4072 = dict()
e_4072[3] = EnumInfo("dtfcustom", 3, 42)
e_4072[0] = EnumInfo("dtflongdate", 0, 42)
e_4072[1] = EnumInfo("dtfshortdate", 1, 42)
e_4072[2] = EnumInfo("dtftime", 2, 42)

enum_main = dict()
enum_main[0x4007] = e_4007
enum_main[0x4021] = e_4021
enum_main[0x402f] = e_402F
enum_main[0x404a] = e_404A
enum_main[0x4055] = e_4055
enum_main[0x4056] = e_4056
enum_main[0x4072] = e_4072
