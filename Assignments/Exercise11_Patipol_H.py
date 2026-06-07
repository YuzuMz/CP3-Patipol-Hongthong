starNum = int(input("Star Pyramid : "))
for x in range(starNum):
    print(" "*(starNum-x)+"* "*(x+1))
print("Your Pyramid.")