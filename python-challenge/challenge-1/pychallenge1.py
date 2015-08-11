def decode(char_list):
    for i in range(len(char_list)-2):
        yield char_list[i], char_list[i+2]

def char_table():
    ascii_code = [x for x in range(0,127)] #32 to 127 codes are printable ASCII char
    char_list = [chr(c) for c in ascii_code] #convert every ASCII code to character
    return char_list

def decode_key(char_list):
    decode_dict = {}
    for key,val in decode(char_list):
        decode_dict[key] = val
    return decode_dict

if __name__ == "__main__":
    cryptic = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print cryptic.split(' ')
    char_list = char_table()
    msg_dict = decode_key(char_list)
    #print msg_dict
    new_msg = ''
    for msg_c in cryptic:
        new_msg = new_msg + msg_dict[msg_c]
    print new_msg
