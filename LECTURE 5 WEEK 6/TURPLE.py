#TURPLE #IMMUTABLE
fruitsA = ("nyoging", "nyoging", "mananas", "lambigan", "santol")
print(fruitsA)
print(fruitsA.index("nyoging"))
print(fruitsA.count("santol"))
print(fruitsA[4])

# print(fruitsA[4])
fruitsB = ("lambutan", "patatashaha", "langkasama", "pinyagong")
fruitsBasket = (fruitsA, fruitsB)
print(fruitsBasket)
mytuple = (
    (1, 2, 3, "A"),
    (4, 5, 6, "B"),
    (7, 8, 9, "C"),
    (0, "*", "#", "D")
)

print(mytuple[3][2])