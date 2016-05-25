def to_bytes(bytes_or_str):
    """ return bytes type of bytes_or_str """
    if isinstance(bytes_or_str, str):
        ret_val = bytes_or_str.encode('utf-8')
    else:
        ret_val = bytes_or_str
    return ret_val


def to_str(bytes_or_str):
    """ return str (unicode) type of bytes_or_str """
    if isinstance(bytes_or_str, bytes):
        ret_val = bytes_or_str.decode('utf-8')
    else:
        ret_val = bytes_or_str
    return ret_val


def join_txt(txt_dict):
    ret_txt = ''

    for key in txt_dict.keys():
        ret_txt += '{}\n'.format(key) 
        ret_txt += '{}\n'.format(txt_dict[key])       

    return ret_txt
