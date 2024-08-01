# step 1
beatles =[]
print("Step 1:", beatles)
# step 2
beatles.extend(["John Lennon" , "Paul McCartney" , "George Harrison"])
print("Step 2:", beatles)

# step 3
for i in beatles:
    i = str(input(' Enter a name if done type done: '))
    if i == "done":
        break
    else:
        beatles.append(i)
print("Step 3:", beatles)

# step 4
del beatles[3:5]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
