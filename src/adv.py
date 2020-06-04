from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room["foyer"].items.append(Item(1, "Food", "Bag of old Halloween candy"))
room["overlook"].items.append(Item(2, "Dental Device", "A tooth retainer"))
room["narrow"].items.append(Item(3, "Art", "A small statue of Elvis"))
room["outside"].items.append(Item(4, "Odd Item", "A plactic glove filled with birdseed"))
room["treasure"].items.append(Item(5, "Mysterious Substance", "A glob of something creamy/gray, perhaps oatmeal"))
room["overlook"].items.append(Item(6, "Food", "Watermelon"))
room["outside"].items.append(Item(7, "Food", "Ornate 7 tiered cake"))
room["narrow"].items.append(Item(8, "Clothing", "Sequin cape"))
room["overlook"].items.append(Item(9, "Clothing", "One yellow flip-flop"))
room["outside"].items.append(Item(10, "Food", "Box of Kraft Mac&Cheese"))
room["foyer"].items.append(Item(11, "Electronics", "Walkman with Hall&Oats tape"))
room["treasure"].items.append(Item(12, "Food", "Can of yams"))
room["foyer"].items.append(Item(13, "Animal", "Racoon wearing a fedora"))
room["foyer"].items.append(Item(14, "Musical Instrument", "Grand piano"))
room["outside"].items.append(Item(15, "Plant", "Cactus wearing a bowtie"))
room["outside"].items.append(Item(16, "Electronics", "Box of 90s era cellphones"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player("AngryBaby", room["outside"], [])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#  sentence = f'x is {x}, y is {round(y, 2)}, z is "{z}"'
# If the user enters "q", quit the game.

def loop_items(arr):
    for i in arr:
        print(f'You look around and see: Item #{i.id}, {i.description}')

while True:
    print(new_player)
    choice = input('Are you ready to explore? Please press "y" (or press "q" to quit)')
    if choice == "q":
        break
    if choice == "y":

        choice_1 = input("Would you like to see what items are around? If yes, press 'y'. If no, press 'n'")
        if choice_1 == "y":
            loop_items(new_player.room_location.items)
            choice_2 = input("If you are interested is taking one of these items enter it's item number now, or you can move along without taking anything. Press any key to continue on")
            if choice_2 == new_player.room_location.room.items.id:
                room.itmes.index(id)
                new_player.inventory.append(room.items.index(id))
                room.inventory.pop(index(id))
                print(f'Your backpack now contains: {new_player.inventory.i.description} press any key to move on and keep exploring!'

        choice_3 = input("Which direction do you want to go?")
        if choice_3 == "n":
            if new_player.room_location.n_to:
                new_player.room_location = new_player.room_location.n_to
            else:
                print("There is nothing in that direction, please choose a different direction to go")

        if choice == "s":
            if new_player.room_location.s_to:
                new_player.room_location = new_player.room_location.s_to
            else:
                print("There is nothing in that direction, please choose a different direction to go")


        if choice == "e":
            if new_player.room_location.e_to:
                new_player.room_location = new_player.room_location.e_to
            else:
                print("There is nothing in that direction, please choose a different direction to go")


        if choice == "w":
            if new_player.room_location.w_to:
                new_player.room_location = new_player.room_location.w_to
            else:
                print("There is nothing in that direction, please choose a different direction to go")


        else:
            print("Please choose a cardinal direction or press q to quit")






