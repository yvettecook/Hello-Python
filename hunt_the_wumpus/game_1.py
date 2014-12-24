def create_tunnel(cave_from, cave_to):
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)

def visit_cave(cave_number):
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)


def choose_cave(cave_list):
  cave_number = choice(cave_list)
  while len(caves[cave_number]) >= 3:
    cave_number = choice(cave_list)
  return cave_number

def print_caves():
    for number in cave_numbers:
        print number, ":", caves[number]
    print "---------"


from random import choice

cave_numbers = range(0,20)
caves = []

for i in cave_numbers:
    caves.append([])

unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves != []:
    i = choose_cave(visited_caves)

    next_cave = choice(unvisited_caves)
    create_tunnel(i, next_cave)
    visit_cave(next_cave)

    print_caves()

for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)

    print_caves()

wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)

while (player_location == wumpus_location or
    player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"

while True:
    print "You are in cave", player_location
    print "You can see caves", caves[player_location]
    if (player_location == wumpus_location - 1 or
    player_location == wumpus_location + 1):
        print "I can smell a wumpus"
    if (player_location == wumpus_friend_location - 1 or
    player_location == wumpus_friend_location + 1):
        print "I can hear something noisy next door"

    print "What cave next?"
    player_input = raw_input(">")
    if(not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print "?", player_input
        print "That's not a cave I can see (doofus)!"
        continue

    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Argh, you got eaten by a wumpus!"
            break

        if player_location == wumpus_friend_location:
            print "Argh, you got eaten by the wumpus' cunning friend!"
            break
