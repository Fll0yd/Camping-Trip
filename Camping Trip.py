#fat chunky string
camping_stuff = "tent, sleeping bag, water, raspberry pi, coffee, knife, ethernet cable, flash drive, marshmallows"
print (camping_stuff)

#use a list instead
supplies = ["tent", "sleeping bag", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
print(type(supplies))

#lists can have multiple data types
camp_site = ["Crystal Lake", 404, 95.5, 10, False]
camp_site2 = ["Crystal Lake", 404, 89.9, True]

#whos bringing what?
bernard = supplies[0]
print(bernard)

me = supplies[4]
print(me)

you = supplies[-1]
print(you)

#forgot some important stuff
supplies.append("vape")
supplies.append("vape batteries")

supplies.extend(["phone", "phone charger"])

supplies = supplies + ["toilet paper", "bidet"]

supplies.insert(0, "pillow")
supplies.insert(-2, "vape juice")
supplies.insert(-2, "socks")

print (supplies [-1])
print (supplies)

#it wont all fit in the car, gotta get rid of the non essentials.
#supplies.clear()
#nuclear!

supplies.remove("tent")
supplies.remove("sleeping bag")

print("This item was removed from the list: " + supplies.pop(0))

print (supplies)


