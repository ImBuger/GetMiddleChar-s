def get_middle(s):
    length = len(s)
    a1= int((length / 2) - 1)
    a2 = int(length / 2)
    if(length % 2 == 0):
        st = s[a1] + s[a2]
        print(st)
    if(length % 2 == 1):
        print(s[a2])
get_middle("utku")
get_middle("bugra")