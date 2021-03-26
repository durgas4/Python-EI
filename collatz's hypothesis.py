steps=0
c0=int(input("Input any integer"))
while c0!=1:
    if c0%2==0:
        c0=int(c0/2)
        steps=steps+1
        print(c0)


    else:
        c0=int(3*c0+1)
        steps=steps+1
        print(c0)

print("Steps:",steps)



