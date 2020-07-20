names = ["amir","tj","rohit"]

print(names)

names.append("ken")

print(names)
names.sort()
print(names)
names.append("ken")
print(names)
names.sort()
print(names[0],names[2])

sets = set()
sets.add("1")
sets.add("2")
sets.add("3")
print(sets)

namez = "amir"
i=0
length =len(namez)
for character in namez:
    i=i+1
    print(f"letter {i} of {length } is {character}")

house ={"tj":"friend", "rohit":"rommie"}
print(house["tj"])
print(house["rohit"])
house["tony"]="replacement rommie"
print(house)
print(house["tony"])

from functions import square

print(square(5))



