import copy

game_map = [
    [0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]]

prop_list = []


class Prop:
    def __init__(self, name: str, description: str):
        self._name = name.lower()
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class Room:
    def __init__(self, room_coordinates):
        self._description = ''
        self._props = []
        self._room_coordinates = room_coordinates
        self._walls = {'left': 'closed',
                       'right': 'closed',
                       'top': 'closed',
                       'bottom': 'closed'
                       }

    @property
    def room_coordinates(self):
        return self._room_coordinates

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, value):
        self._props = value

    @property
    def walls(self):
        return self._walls

    @walls.setter
    def walls(self, values: str = 'left, right, top, bottom'):
        self._walls['left'] = values[0]
        self._walls['right'] = values[1]
        self._walls['top'] = values[2]
        self._walls['bottom'] = values[3]


# create a room object for every 1 in the game_rooms list with its coordinates
rooms = []
for x in range(0, 5):
    for i in range(0, 5):
        if game_map[x][i] == 1:
            rooms.append(Room([x, i]))
        else:
            continue

# set up room doors
# room 1 doors
rooms[0].walls['bottom'] = 'open'
rooms[0].walls['right'] = 'open'
# room 2 doors
rooms[1].walls['left'] = 'open'
rooms[1].walls['right'] = 'open'
# room 3 doors
rooms[2].walls['left'] = 'open'
# room 4 doors
rooms[3].walls['bottom'] = 'open'
# room 5 doors
rooms[4].walls['top'] = 'open'
rooms[4].walls['bottom'] = 'open'
# room 6 doors
rooms[5].walls['top'] = 'open'
rooms[5].walls['bottom'] = 'open'
rooms[5].walls['right'] = 'open'
# room 7 doors
rooms[6].walls['left'] = 'open'
rooms[6].walls['right'] = 'open'
# room 8 doors
rooms[7].walls['top'] = 'open'
rooms[7].walls['bottom'] = 'open'
rooms[7].walls['left'] = 'open'
rooms[7].walls['right'] = 'open'
# room 9 doors
rooms[8].walls['left'] = 'open'
rooms[8].walls['right'] = 'open'
# room 10 doors
rooms[9].walls['left'] = 'open'
# room 11 doors
rooms[10].walls['top'] = 'open'
rooms[10].walls['right'] = 'open'
# room 12 doors
rooms[11].walls['left'] = 'open'
rooms[11].walls['right'] = 'open'
# room 13 doors
rooms[12].walls['top'] = 'open'
rooms[12].walls['left'] = 'open'
rooms[12].walls['right'] = 'open'
# room 14 doors
rooms[13].walls['left'] = 'open'
rooms[13].walls['bottom'] = 'open'
# room 15 doors
rooms[14].walls['top'] = 'open'
rooms[14].walls['right'] = 'open'
# room 16 doors
rooms[15].walls['left'] = 'open'


class Player:
    def __init__(self, name, current_room):
        self._name = name
        self._current_room = current_room

    @property
    def name(self):
        return self._name

    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, value: Room(list)):
        self._current_room = value

    def get_room_props(self):
        return ','.join(z.name.capitalize() for z in self._current_room.props)

    def get_prop_description(self, prop_name):
        for prop in self._current_room.props:
            if prop.name == prop_name.lower():
                return prop.description

    @property
    def check_location(self):
        return self._current_room.room_coordinates

    def movement(self, direction):
        temp = self.current_room
        if direction.lower() == 'left':
            for z in rooms:
                if z.room_coordinates == [self.current_room.room_coordinates[0],
                                          self.current_room.room_coordinates[1] - 1]\
                                          and self.current_room.walls['left'] == 'open':
                    self.current_room = z
                    break
        elif direction.lower() == 'right':
            for z in rooms:
                if z.room_coordinates == [self.current_room.room_coordinates[0],
                                          self.current_room.room_coordinates[1] + 1]\
                                          and self.current_room.walls['right'] == 'open':
                    self.current_room = z
                    break
        elif direction.lower() == 'top':
            for z in rooms:
                if z.room_coordinates == [self.current_room.room_coordinates[0] - 1,
                                          self.current_room.room_coordinates[1]]\
                                          and self.current_room.walls['top'] == 'open':
                    self.current_room = z
                    break
        elif direction.lower() == 'bottom':
            for z in rooms:
                if z.room_coordinates == [self.current_room.room_coordinates[0] + 1,
                                          self.current_room.room_coordinates[1]]\
                                          and self.current_room.walls['bottom'] == 'open':
                    self.current_room = z
                    break
        if temp == self.current_room:
            print("\u001b[31mMOVEMENT ERROR: I cannot go that way!\u001b[0m")

# setting up props and adding them to props_list
chest = Prop("Chest", "An old, locked chest. I wonder what's inside...")
torch = Prop("Torch", "A torch on the wall, it illuminates the room.")
wooden_bed = Prop("Wooden Bed", "An old, broken bed with a wood frame."
                                " It looks like no one slept in it in very long time.")
shackles = Prop("Shackles", "A pair of shackles bolted to the wall. Someone was probably imprisoned in this room.")
barrel = Prop("Barrel", "Just an old barred, seems to be empty")
statue = Prop("Gargoyle statue", "A creepy statue of a gargoyle. I don't want to stick around in this room for long...")
table = Prop("Table", "A large table, on it there are all types of writing tools."
                      "and papyrus marked with eerie inscriptions.")
bookshelf = Prop("Bookshelf", "A bookshelf containing a few ruined books.")
books = Prop("Books", "A pile of dusty books, they don't seem very interesting.")
potion = Prop("Potion", "A flask filled with a strange, glowing liquid. I'd better not touch that.")
prop_list.extend([chest, torch, wooden_bed, shackles, barrel, statue, table, bookshelf, books, potion])

# adding props to rooms
rooms[0].props = [barrel, torch, torch]
rooms[1].props = [torch, torch, torch, torch]
rooms[2].props = [torch, torch, torch, bookshelf, bookshelf, bookshelf, books]
rooms[3].props = [bookshelf, books, table, torch, torch, torch, torch, potion, barrel]
rooms[4].props = [torch, torch, barrel]
rooms[5].props = [torch, torch, torch, chest]
rooms[6].props = [torch, barrel]
rooms[7].props = [torch, torch, torch, torch, wooden_bed, potion, books]
rooms[8].props = [barrel, barrel, barrel, barrel, barrel, barrel, barrel, barrel]
rooms[9].props = [torch, torch]
rooms[10].props = [torch, torch, bookshelf]
rooms[11].props = [torch, torch, torch]
rooms[12].props = [statue, torch, torch]
rooms[13].props = [potion, potion, potion, potion, potion, potion, barrel, barrel, barrel, barrel, barrel,
                   chest, chest, chest, chest, chest, chest, chest, chest, chest, ]
rooms[14].props = [torch]
rooms[15].props = [shackles, shackles, shackles, shackles, potion, potion, potion]


# setting up room descriptions
rooms[0].description = 'This rooms is made out of stone and looks pretty empty.' \
                       ' I can see a large wooden door to the right and a smaller one to the bottom.'
rooms[1].description = 'This room looks more like a corridor, besides the torches on the wall,' \
                       ' it is completely empty. It has a door to the left and one to the right'
rooms[2].description = 'Hmm, seems like came to a dead end, the only door is to the left, back where I came from.' \
                       'I do see a few bookshelves though, I wonder if they have any interesting books.'
rooms[3].description = 'It seems like I came to a dead end. The only way back is through the door at the bottom.' \
                       'I see a table in the middle of the room and an interesting potion finds itself on top of it.'
rooms[4].description = 'This room has doors both at the top and bottom, I wonder where it will lead me.'
rooms[5].description = 'This room has doors leading everywhere besides to the left. That wall seems to be empty,' \
                       'but I can see a chest in the corner'
rooms[6].description = 'A very dark room, one lowly torch spotlights the wall and the barrel next to it.' \
                       ' You can barely make out a door to the left and one to the right.'
rooms[7].description = 'This is the room you woke up in, there is a wooden bed in although you remember' \
                       ' waking up on the floor. There is a pile of books next to the bed as well as a potion.' \
                       'There are doors to all sides of the room.'
rooms[8].description = 'This rooms has barrels all along two walls of the walls of the room, could\'ve been some' \
                       ' sort of storage room.'
rooms[9].description = 'Looks like a dead end. The only door is back where I came from. On the left.'
rooms[10].description = 'A dusty room,  there is a bookshelf in the corner but I' \
                        ' don\'t think it will help me much. Doors can be found on the top and right'
rooms[11].description = 'A corridor looking room, looks pretty empty to me. There are doors on the left and right'
rooms[12].description = 'This room seems to connect back to the origin room. Does it make a loop? There is a statue' \
                        ' of a strange creature in the middle, I better not stay around for long. Doors are found at' \
                        ' the top, left and right.'
rooms[13].description = 'This room is filled with chests, barrels and potions, could\'ve been the room of an' \
                        ' alchemist doors are found on the left and the bottom.'
rooms[14].description = 'This room is very eerie. There are doors to the left and right, but not much else.'
rooms[15].description = 'Another dead end. There are many shackles bolted to the wall and broken, empty flasks on the' \
                        ' floor. Looks like a torture room. There is a door to the left, back where I came from.'


player_name = input("What is your name? ")
player = Player("Jon", rooms[7])
print(f"\u001b[37mHello \u001b[37;1m{player_name}\u001b[37m! Enjoy your stay.\u001b[0m")
help_me = "\u001b[36mHELP: Type 'q' to quit the game.\nHELP: Type 'left', 'right', 'top' or 'bottom' to move.\n" \
          "HELP: Type the name of a prop to interact with it.\n"\
          "HELP: Type 'location' to show your location.\nHELP: Type 'help' to see this message again.\nGood luck!\u001b[0m"
print(help_me)
print(f"\u001b[33m{player.current_room.description}\u001b[0m")
print(f"\u001b[32mProps: {', '.join([t.name.capitalize() for t in player.current_room.props])}\u001b[0m")
while True:
    user_input = input("What would you like to do? (Type 'q' to leave the game) ").lower()
    if user_input == 'q':
        print("The game has ended. I hope you enjoyed it!")
        break
    if user_input == 'help':
        print(help_me)
        continue
    if user_input == 'left' or user_input == 'right' or user_input == 'top' or user_input == 'bottom':
        player.movement(user_input)
        print(f"\u001b[33m{player.current_room.description}\u001b[0m")
        print(f"\u001b[32mProps: {', '.join([z.name.capitalize() for z in player.current_room.props])}\u001b[0m")
        continue
    if user_input == 'location':
        new_map = copy.deepcopy(game_map)
        new_map[player.check_location[0]][player.check_location[1]] = '^'
        for z in range(0, 5):
            print(new_map[z])
        continue

    for z in player.current_room.props:
        if user_input == z.name.lower():
            print(f"\u001b[34m{z.description}\u001b[0m")
            break
    else:
        print("\u001b[31mThis doesn't seem to do anything... Try again!\u001b[0m")

# done
