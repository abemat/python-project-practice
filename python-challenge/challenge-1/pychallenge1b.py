def char_table():
    ascii_code = [x for x in range(97,123)] #32 to 127 codes are printable ASCII char
    ascii_code.extend([x for x in range(65,91)])
    char_list = [chr(c) for c in ascii_code] #convert every ASCII code to character
    return char_list

if __name__ == "__main__":
    cryptic = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    #cryptic = 'map'
    new_msg = ' '
    for ch in cryptic:
        if ch is not (' ' or '\n' or '\t' or '.'):
            ch = chr(ord(ch)+2)
        new_msg = new_msg + ch
    print new_msg
