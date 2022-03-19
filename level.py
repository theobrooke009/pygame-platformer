from re import X
import pygame
from tiles import Tile
from player import Player
from settings import tile_size, screen_width

class Level:
    def __init__(self, level_data, surface):
        #level setup
        self.display_surface  = surface
        self.setup_level(level_data)

        self.level_scroll = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P':
                    player_sprite = Player((x,y), tile_size)
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.level_scroll = 8
            player.speed = 0

        elif player_x > screen_width -(screen_width / 4) and direction_x > 0:
            self.level_scroll = -8
            player.speed = 0
        
        else:
            self.level_scroll = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        #this checks everything in the level collides w/ the player rectangle
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                #if the player tile collides with a level tile, we check to see if the player is moving left or right
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0





    def run(self):
        #level tiles
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.level_scroll)
        self.scroll_x()

        #player tiles
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)