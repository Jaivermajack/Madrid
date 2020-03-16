a = "abcde1234"
str_count=""
num_count=""
for i in a:
    if i.isalpha():
        str_count += i
    else:
        num_count += i

print("total string:",len(str_count))
print('total number:',len(num_count))








