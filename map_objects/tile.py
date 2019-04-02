class Tile:
    """
    A tile on the map, it may or may not block movement and/or sight
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        # by default, blocked tiles block sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
