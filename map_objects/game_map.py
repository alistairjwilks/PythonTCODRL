from map_objects.tile import Tile
from map_objects.rectangle import Rect
from random import randint

class GameMap:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.h)] for x in range(self.w)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        rooms = []
        n_rooms = 0

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position where room fits inside the whole map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # create the rectangle of the room
            new_room = Rect(x, y, w, h)

            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # if the loop runs through without breaking
                # carve out the room
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if n_rooms == 0:
                    # first room, place the player
                    player.x = new_x
                    player.y = new_y
                else:
                    # otherwise, build a tunnel to connect the room to the previously created one
                    (prev_x, prev_y) = rooms[n_rooms - 1].center()

                    #either start horizontally or start vertically
                    if randint(0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_h_tunnel(prev_x, new_x, new_y)
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                # finally add the room
                rooms.append(new_room)
                n_rooms += 1



    def create_room(self, room: Rect):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                # the room's rectangle includes the outer wall
                self.tiles[x][y] = Tile(False)

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Tile(False)

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Tile(False)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
