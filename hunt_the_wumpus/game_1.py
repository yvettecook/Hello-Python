from random import choice


def setup_caves(caves_numbers):
    caves = []
    for cave in cave_numbers:
        caves.append([])
    return caves


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

def link_caves():
    while unvisited_caves != []:
        i = choose_cave(visited_caves)

        next_cave = choice(unvisited_caves)
        create_tunnel(i, next_cave)
        visit_cave(next_cave)

def finish_caves():
    for i in cave_numbers:
        while len(caves[i]) < 3:
            passage_to = choice(cave_numbers)
            caves[i].append(passage_to)

def print_location(player_location):
    print "You are in cave", player_location
    print "You can see caves", caves[player_location]
    if wumpus_location in caves[player_location]:
        print "I can smell a wumpus"


def get_next_location():
    print "What cave next?"
    player_input = raw_input(">")
    if(not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print "?", player_input
        print "That's not a cave I can see (doofus)!"
        return None
    else:
        return int(player_input)

cave_numbers = range(0,20)
caves = setup_caves(cave_numbers)
setup_caves(cave_numbers)

unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0)

link_caves()
print_caves()
finish_caves()
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
    print_location(player_location)
    new_location = get_next_location()
    if new_location is not None:
        player_location = new_location
    if player_location == wumpus_location:
        print "Argh, you got eaten by a wumpus!"
        break
