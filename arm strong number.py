In=input("enter your number")
a = len(In)
l = []
inct = 1
for i in In:
    get_val = int(i)
    get_mul = get_val**a
    l.append(get_mul)

add_val = 0
for i in l:
    add_val = add_val + i

add_val = str(add_val)
if add_val == In:
    print("Armstrong No:, ",add_val)
else:
    print("Not Armstrong No:", add_val)
