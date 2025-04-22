import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/info/tp_regulation/src/tp_turtle_regulation_nadine_shoaib/turtle_regulation2/install/turtle_regulation2'
