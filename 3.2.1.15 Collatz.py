c0 = int(input("Enter any non-negative and non-zero integer: "))
steps = 0
while c0 != 1:
    if c0 % 2 != 0:
        c0 = 3 * c0 + 1
        c0 = int(c0)
        print (c0)
        steps += 1
    else:
       c0 = c0 / 2
       c0 = int(c0)
       print (c0)
       steps += 1
print("Steps:",steps)