##SETS - no duplicate and no order
fruitsA = {"bahay", "kubo", "kahit", "munti", "ang", "halaman"}
fruitsB = {"dito", "ay", "sarisari", "singkamas", "attalong"}
fruitsA.add("bomb") #Add
print(fruitsA)
YunYonFruits = fruitsA.union(fruitsB)
print(YunYonFruits)
InterseksyonFruits = fruitsA.intersection(fruitsB)
print(InterseksyonFruits)
FruitDiff = fruitsA.difference(fruitsB)
print(FruitDiff)
FruitDiff = fruitsB.difference(fruitsA)
print(FruitDiff)