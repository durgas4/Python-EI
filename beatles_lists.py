# step 1
beatles=[]
print("Step 1:", beatles)

# step 2
beatles.append('John Lennon ,Paul McCartney, George Harrison')
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Member names "))
print("Step 3:", beatles)

# step 4
del beatles[-1]
print("Step 4(1):", beatles)
del beatles[-1]
print("Step 4 (2):", beatles)
# step 5
beatles.insert(0,"Ringo starr")
print("Step 5:", beatles)
# testing list legth
print("The Fab", len(beatles))