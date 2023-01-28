from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction

pygame.init()

pygame.display.set_caption("ZomStrike")
pygame.display.set_icon(pygame.image.load("ico/icon.png"))

sc = pygame.display.set_mode((WIDTH, HEIGHT))

sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, player, clock)
interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
interaction.play_music()

while True:

    player.movement()
    drawing.background(player.angle)
    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    drawing.player_weapon([wall_shot, sprites.sprite_shot])

    interaction.interaction_objects()
    interaction.npc_action()
    interaction.clear_world()
    interaction.check_win()

    pygame.display.flip()
    clock.tick()
