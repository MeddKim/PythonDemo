import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)
    bullets = Group()
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()
