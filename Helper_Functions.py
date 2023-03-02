import random
quit = False
def roomgen():
   
    chance = random.randrange(0, 100)
    if chance < 25:
        return 2
    elif chance < 50:
        return 3
    elif chance < 75:
        return 4
    elif chance < 100:
        return 5

    
def roomdescription(bruh):
    if bruh == 2:
        print("You are in a crew cabin. You see several bunk beds on both sides of the room, neatly made with tighly tucked-in wool blankets. A folding table with several chairs sits in the middle of the room, covered with cards, empty cups, and bubblegum wrappers. It appears that nobody has been in this room for quite some time")
    elif bruh == 3:
        print("You are in the engine room. The smell of rusting metal and oil hits you by surprise. There are tools randomly scattered around the room. Wrenches, hammers, bolts, and nails. As you go a littel further, there are assortements of several broken down engines of every kind.")
    elif bruh == 4:
        print("You are in the storage room. The are many shelves around you with a random assortment of things on them such as boxes, equipment, and some body parts. You search through the boxes but you notice that they are all filled with packing peanuts with nothing else inside. You look at the body parts but not touch them because if you do you could get arested because of finger prints.")
    elif bruh == 5:
        print("You are now in the kitchen. In this room you notice many knives on the floor with most of them being covered in blood. The kitchen smells weird to the fact that you could notice that a murder must've happened earlier if the blood wasn't already obvious.")
while quit != True:
    user = (input("Go into the rooms?"))
    if user == 'yes':
        if roomgen() == 2:
            roomdescription(2)
        elif roomgen() == 3:
            roomdescription(3)
        elif roomgen() == 4:
            roomdescription(4)
        elif roomgen() == 5:
            roomdescription(5)
    else:
        quit = True
    