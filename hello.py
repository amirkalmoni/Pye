name = input("what is your name? ")
print(f"hello, {name}")

numb = int(input("what number did you pick? "))
if numb < 0:
    print(f"{numb} is negative")
elif numb > 0:
    print(f"{numb} is positive")
else: 
    print("number is zero")