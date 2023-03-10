from object.intangible import Player, Monster
from object.tangible import Metallic_wall, Destructible_wall
from sprites.all_sprites_groups import sprites_group

wall_size = 64


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'w':
                Metallic_wall('Unbr_walls.jpg', x * wall_size, y * wall_size, sprites_group)
            elif level[y][x] == 'b':
                Destructible_wall('wall.jpg', x * wall_size, y * wall_size, sprites_group)
            elif level[y][x] == 'm':
                Monster('monster_left.png', 'monster_right.png', x * wall_size, y * wall_size, sprites_group)

    player = Player('Bomberman_up.png', 'Bomberman_right.png', 'Bomberman_down.png',
                    'Bomberman_left.png',
                    wall_size, wall_size * 2, sprites_group)
    return player
