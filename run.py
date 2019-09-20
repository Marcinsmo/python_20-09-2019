
flowerName = "Olive tree"
mainComunication = "Hello, this is your: " + flowerName + "!"
print(mainComunication)

watering = input("Do you want to water her?")
print(watering)

if watering == "yes":
    print("Your " + flowerName + " is growing!")
elif watering == "no":
    print("Your " + flowerName + " is dying!")
else:
    print("I don't understand")
