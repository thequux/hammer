import ctypes

# conversions:
# str -> uint8_t* str, size_t len

def _bytes(arg):
    strbuf = ctypes.create_string_buffer(arg)
    return (strbuf, ctypes.c_size_t(ctypes.sizeof(arg) - 1))

_bool = ctypes.c_bool
_size_t = ctypes.c_size_t
_uint8 = ctypes.c_uint8
_int64 = ctypes.c_int64
def _Parser(arg):
    if type(arg) != Parser:
        raise TypeError("Expected parser, got %s" % (type(arg),), arg)
    return arg._raw



_API_DESC = {
    'token': (_bytes,),
    'ch': (_uint8,),
    'ch_range': (_uint8, _uint8),
    'int_range': (_Parser, _int64, _int64),
    'bits': (_size_t, _bool),
    'int64': (),
    'int32': (),
    'int16': (),
    'int8': (),
    'uint64': (),
    'uint32': (),
    'uint16': (),
    'uint8': (),
    'whitespace': (_Parser,),
    'left': (_Parser, _Parser),
    'right': (_Parser, _Parser),
    'middle': (_Parser, _Parser, _Parser),
    'action': (_Parser, _Action),
    'in': (_charset,),
    # leave out not_in; that should be handled at a higher level.
    'end_p', (),
    'nothing_p': (),
    'sequence': (_NullTerm(_Parser),),
    'choice': (_NullTerm(_Parser),),
    'butnot': (_Parser, _Parser),
    'difference': (_Parser, _Parser),
    'xor': (_Parser, _Parser),
    'many': (_Parser,),
    'many1': (_Parser,),
    'repeat_n': (_Parser, _size_t),
    'optional': (_Parser,),
    'ignore': (_Parser,),
    'sepBy': (_Parser, _Parser),
    'sepBy1': (_Parser, _Parser),
    'epsilon_p': (),
    'length_value': (_Parser, _Parser),
    'attr_bool': (_Parser, _Predicate),
    'and': (_Parser,),
    'not': (_Parser,),
    'indirect': (),
    'bind_indirect': (_Parser, _Parser)
}

# missing: parse_result_free, write_result_unamb, pprint, compile, bitwriter*
# Also, actions, benchmark
    
