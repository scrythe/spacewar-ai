import pygame
from .utils import scale_image
from .laser import Laser


class Ship(pygame.sprite.Sprite):
    MAX_AMMO = 2
    SHOT_DELAY = 300

    def __init__(self, screen_rect: pygame.Rect, x):
        super().__init__()
        image = pygame.image.load('assets/spaceship.png').convert_alpha()
        self.image = scale_image(image, 1/4)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_rect = screen_rect
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = x
        self.lasers = pygame.sprite.Group()
        self.speed = 5
        self.ammo = self.MAX_AMMO
        self.last_shot = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left

    def shoot_laser(self, frames):
        if self.ammo >= 1 and self.last_shot + self.SHOT_DELAY < frames:
            self.last_shot = frames
            self.lasers.add(Laser(self.rect, self.screen_rect))
            self.ammo -= 1
            return True
        return False

    # def inputs(self, keys):
    #     if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    #         self.move_right()
    #     if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    #         self.move_left()

    def update(self):
        # keys = pygame.key.get_pressed()
        # self.inputs(keys)
        self.lasers.update()
