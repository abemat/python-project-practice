import string
import re
import urllib2

def char_table():
    ascii_code = [x for x in range(97,123)] #32 to 127 codes are printable ASCII char
    ascii_code.extend([x for x in range(65,91)])
    from_str = [chr(c) for c in ascii_code] #convert every ASCII code to character
    ascii_crypt = [x+2 for x in ascii_code]
    to_str = [chr(c) for c in ascii_crypt] #convert every ASCII code to character
    fro = ''.join(from_str)
    to = ''.join(to_str)
    return fro, to

if __name__ == "__main__":
    fro, to = char_table()
    to = re.sub(r'{','a',to)
    to = re.sub(r'\|','b',to)
    #print fro
    trans = string.maketrans(fro,to)
    #cryptic = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    cryptic = 'map'
    decrypt = cryptic.translate(trans)
    nexturl = 'http://www.pythonchallenge.com/pc/def/'+decrypt+'.html'
    print urllib2.urlopen(nexturl).getcode()
