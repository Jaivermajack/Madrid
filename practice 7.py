input=20
div=5
inc=1
fact=1
while inc<=div:
    for i in range(1,inc+1):
        fact = fact * i
    print("divide",input/fact)
    print("factorila",fact)
    fact = 1
    inc +=1


