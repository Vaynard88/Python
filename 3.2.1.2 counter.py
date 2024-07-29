counter = 0
while counter != 1000:
    print("Inside the loop.", counter)
    counter += 1
print("Outside the loop.", counter)

counter = 1000
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

