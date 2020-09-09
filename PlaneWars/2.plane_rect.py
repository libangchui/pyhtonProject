#Author:BangChui
#encoding:utf-8
_date_ = "2019/12/26 10:37"
import pygame
pygame.init()

hero_rect = pygame.Rect(100,200,125,300)
"""
100代表距离X轴原点的位置
200代表距离Y轴原点的位置
125代表矩形的宽度
300代表矩形的长度
"""
print(f"英雄机矩形的X={hero_rect.x},Y={hero_rect.y}")
print(f"英雄机举行的宽{hero_rect.width}，高{hero_rect.height}")
print(f"英雄机的中心位置{hero_rect.centerx}")
print(f"英雄机的顶部{hero_rect.top}")
print(f"英雄机的底部{hero_rect.bottom}")
print(f"英雄机的左部{hero_rect.left}")
print(f"英雄机的右部{hero_rect.right}")
print(f"英雄机的大小{hero_rect.size}")

print(type(pygame.event.get()))