import sys
import pygame
from bullet import  Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """按键响应"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    """发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """"响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    """"更新屏幕上的图像，并切换到新的屏幕上"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()
