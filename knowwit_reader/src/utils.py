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

def get_config(config_filename):
    """ maybe handy to keep around, note I haven't used this anywhere """
    try:
        config = configparser.ConfigParser()
        config.read(config_filename)
        if 'credentials' in config:
            config_creds = config['credentials']  # just saving typing by creating config_creds
        else:
            raise Exception('Now \'credentials\' section found in {}'.format(config_filename))

        if 'username' in config_creds:
            username = config_creds['username']
        else:
            raise Exception('Config missing needed option: {}'.format('username'))
        
        if 'password' in config_creds:
            password = config_creds['password']
        else:
            raise Exception('Config missing needed option: {}'.format('password'))
        
        if 'user_agent' in config_creds:
            user_agent = config_creds['user_agent']
        else:
            raise Exception('Config missing needed option: {}'.format('user_agent'))
    except Exception as e:
        raise e
    else:
        ret_tup = praw_tuple(username=username, password=password, user_agent=user_agent)
        return ret_tup
