from math import pi 
dec_num = raw_input("how many decimal? : ")
dec_str = str(dec_num) 
dec_pi = "{0:." + dec_str + "f}"
formatted_pi = dec_pi.format(pi)
print formatted_pi