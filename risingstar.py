try:
    five = int(input("how many 5※ do you have:"))
except:
    five = 0
try:
    four = int(input("how many 4※ do you have:"))
except:
    four = 0
try: 
    three = int(input("how many 3※ do you have:"))
except:
    three = 0
try:
    two = int(input("how many 2※ but mix leavl do you have:"))
except:
    two = 0

total = 6*5*4 - 24
#white eges and ssr been excluded
n_two = total - five*16 - four*3 - three - two
n_n = n_two * 3 + two * 2
n_w = 30 - five*5 - four


if n_n < 0 or n_w < 0:
    print("Error")
else:
    if n_two >= 0:
        print("You still need lv1 N cards:",n_n)
    else:
        print("You just need rise 2※:",two+n_two)
    print("You still need lv20 N cards:",n_two)
    print("You still need 4※ white eges:",n_w)





