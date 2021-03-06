import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""

    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen

        #在(0,0)处创建子弹，再设置正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

