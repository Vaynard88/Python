number = int(input("Please chose a number to start the count down from: "))

while number > -1:
    print (number)
    number -= 1
    if number > 9:
        print("Number is to big try later!")
        break
12