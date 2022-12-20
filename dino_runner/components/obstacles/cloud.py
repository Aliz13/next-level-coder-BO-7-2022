import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.image_width = CLOUD.get_width()
        self.x_pos_cloud = random.randint[600, 1000]
        self.y_pos_cloud = random.randint[60, 100]
        self.game_speed = 40

    def update(self):
        self.x_pos_cloud = self.game_speed
        if self.x_pos_cloud <= -self.image_width:
            self.screen.blit(CLOUD, (self.image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 0
        self.x_pos_cloud -= self.game_speed

    def draw(self,screen):
        screen.blit(self.image,(self.x_pos_cloud, self.y_pos_cloud))