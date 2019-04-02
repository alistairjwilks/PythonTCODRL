import tcod as tcod
import tcod.event as tc_event


def handle_keys(key: tc_event.KeyboardEvent):
    # returns special player command dicts
    # movement
    if key.sym == tc_event.K_LEFT:
        return{'move': (-1, 0)}
    elif key.sym == tc_event.K_RIGHT:
        return{'move': (1, 0)}
    elif key.sym == tc_event.K_UP:
        return{'move': (0, -1)}
    elif key.sym == tc_event.K_DOWN:
        return{'move': (0, 1)}

    if key.sym == tc_event.K_F4:
        return {'fullscreen': True}
    elif key.sym == tc_event.K_ESCAPE:
        return {'exit': True}

    return {}

