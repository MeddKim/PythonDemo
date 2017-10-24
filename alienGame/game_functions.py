import sys
import pygame

def check_events(ship):
    """"响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1

def update_screen(ai_settings,screen,ship):
    """"更新屏幕上的图像，并切换到新的屏幕上"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
