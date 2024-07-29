blocks = int(input("Enter the number of blocks: "))
i = 1
height = 0
#
# Write your code here.
#	
while blocks > 0:
    blocks = blocks - i
    i += 1
    height += 1
    if blocks < 0:
        height -= 1
print("The height of the pyramid:", height)
