##Kakaibang protas

fruitsA = ["nyoging", "nyoging", "mananas", "lambigan", "santol"]
fruitsB = ["gomugomu nomi", "hanahana nomi", "barabara nomi", "awawa nomi", "dorodoro nomi"]
fruitsC = ["karots", "kalamansi", "bawang", "sibuyas", "kalamares"]
# all combined tabulatedd

FruitBasketList = [fruitsA, fruitsB, fruitsC] #list of a list liste
print(FruitBasketList)
##spcfic

print(FruitBasketList[2])
print(FruitBasketList[2][2])
#add, outputs single line list

FruitBasketList_Plus = fruitsA + fruitsB + fruitsC #single list
print(FruitBasketList_Plus)
#extend
fruitsA.extend(fruitsB)
fruitsA.extend(fruitsC)
print(fruitsA)