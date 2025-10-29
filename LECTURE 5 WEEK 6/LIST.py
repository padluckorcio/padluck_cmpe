#LIST
##LIST

fruitsA = ["nyoging", "nyoging", "mananas", "lambigan", "santol"]
print(fruitsA)
print(fruitsA)
print(fruitsA)
#check the specific item based on its order

print(fruitsA[3])
#check the position

print(fruitsA.index("santol"))
#boolean checking

isThere = "guyababao" in fruitsA

##Random list ex

randomMixLs = ["guyababao", True, 23]
print(randomMixLs)
print(randomMixLs[2])

##List Functions

#add ito sa dolo

fruitsA.append("Pech")
print(fruitsA)
#specific add, position mentioned

fruitsA.insert(2, "Potatu")
print(fruitsA)
#length to know positioning using index

print(len(fruitsA))
#counting stated items

print(fruitsA.count("nyoging"))
#removal first match value

fruitsA.remove("nyoging")
print(fruitsA)

#know the position

print(fruitsA.index("lambigan"))
#revalue
fruitsA[1] = "pinyagongi"
print(fruitsA)