import tcod
import tcod.event as tc_event
from input_handlers import handle_keys
from entity import Entity
from map_objects.game_map import GameMap
from render_functions import render_all, clear_all


def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    colors = {
        'dark_wall': tcod.Color(0, 0, 100),
        'dark_ground': tcod.Color(50, 50, 150),
    }

    player = Entity(int(screen_width/2), int(screen_height/2), '@', tcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', tcod.yellow)
    entities = [npc, player]

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)

    con = tcod.console_init_root(screen_width, screen_height, 'tcod tutorial revised', False, tcod.RENDERER_SDL2)

    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    tcod.console_set_char_background(con, 6, 6, tcod.red, flag=tcod.BKGND_NONE )
    while True:   # Main loop

        render_all(con, entities, game_map, screen_width, screen_height, colors)
        tcod.console_flush()
        clear_all(con, entities)

        for event in tc_event.wait():
            if event.type == "QUIT":
                print(event)
                raise SystemExit()
            elif event.type == "KEYDOWN":
                action = handle_keys(event)

                move = action.get('move')
                exit = action.get('exit')
                fullscreen = action.get('fullscreen')

                if move:
                    dx, dy = move
                    if not game_map.is_blocked(player.x + dx, player.y + dy):
                        player.move(dx, dy)

                if exit:
                    raise SystemExit()

                if fullscreen:
                    tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()

