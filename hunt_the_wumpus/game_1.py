from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"

while True:
    print "You are in cave", player_location
    if (player_location == wumpus_location - 1 or
    player_location == wumpus_location + 1):
        print "I can smell a wumpus"

    print "What cave next?"
    player_input = raw_input(">")
    if(not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print player_input, "is not a cave, doofus!"

    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Argh, you got eaten by a wumpus!"
            break
