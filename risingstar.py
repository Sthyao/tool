five = int(input("how many 5※ do you have:"))
four = int(input("how many 4※ do you have:"))
three = int(input("how many 3※ do you have:"))
two = int(input("how many 2※ but mix leavl do you have:"))

total = 6*5*4 - 26
#white eges and ssr been excluded
n_two = total - five*20 - four*4 - three - two

if n_two >= 0:
    n_n = n_two * 3 + two * 2
    n_w = 25 - five*5 - four
    print("You still need lv1 N cards:",n_n)
    print("You still need lv20 N cards:",n_two)
    print("You still need 4※ white eges:",n_w)
else:
    n_n = (n_two + two) * 2
    n_w = 25 - five*5 - four
    print("You have adequate lv.20 N cards, but:")
    print("You still need lv1 N cards:",n_n)
    print("You still need 4※ white eges:",n_w)





