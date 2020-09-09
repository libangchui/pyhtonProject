import pygame
from pygame.locals import *
import random
import time

class HeroBullet():  # 定义一个战机子弹的类
    def __init__(self, x, y, windows):
        self.x = x
        self.y = y
        self.windows = windows
        self.pic = pygame.image.load('img/bullet.png')

    def draw(self):  # 用来画子弹
        self.windows.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        self.y -= 5

class EnemyBullet():
    def __init__(self, x, y, windows):
        self.x = x
        self.y = y
        self.windows = windows
        self.pic = pygame.image.load('img/bullet1.png')

    def draw(self):
        self.windows.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        self.y += 3

windows = pygame.display.set_mode((480, 650), 0, 32)  # 创建窗口
bg = pygame.image.load('img/background.png')
pygame.display.set_caption('雷电1999')
icon = pygame.image.load('img/icon72x72.png')
pygame.display.set_icon(icon)
heroPlane1 = pygame.image.load('img\\hero1.png')
heroPlane2 = pygame.image.load('img\\hero2.png')
enemyPlane = pygame.image.load('img\\enemy1.png')
enemyBombList = ['img\\enemy1_down1.png',
                 'img\\enemy1_down2.png',
                 'img\\enemy1_down3.png',
                 'img\\enemy1_down4.png', ]
heroIndexShift = 0
direct = '左'
pygame.key.set_repeat(20, 30)  # 重复按键指令
heroPlaneX = 190
heroPlaneY = 526
enemyPlaneX = 480 // 2 - 69 // 2
enemyPlaneY = 0
BiuList = []
EnemyBiulist = []
enemy_isBomb = False  # 敌机爆炸条件
enemy_BombIndex = 0  # 爆炸图片索引
while True:
    windows.blit(bg, (0, 0))  # 把背景图片贴上去！
    if heroIndexShift == 0:
        windows.blit(heroPlane1, (heroPlaneX, heroPlaneY))
        heroIndexShift += 1
    else:
        windows.blit(heroPlane2, (heroPlaneX, heroPlaneY))
        heroIdexShift = 0
    if direct == '左':  # 敌机移动
        enemyPlaneX -= 5
        if enemyPlaneX <= 0:
            direct = '右'
    elif direct == '右':
        enemyPlaneX += 5
        if enemyPlaneX >= 480 - 69:
            direct = '左'
    if enemy_isBomb == False:  # 敌机爆炸
        windows.blit(enemyPlane, (enemyPlaneX, enemyPlaneY))
    else:
        if enemy_BombIndex == len(enemyBombList):
            time.sleep(0.1)
            exit(0)
        pic = pygame.image.load(enemyBombList[enemy_BombIndex])
        windows.blit(pic, (enemyPlaneX, enemyPlaneY))
        enemy_BombIndex = (enemy_BombIndex + 1)
        time.sleep(0.1)

    for biu in BiuList:
        biu.draw()
        BiuList.remove(biu) if biu.y < 0 else ''  # 让子弹到最上边的时候，消失

    for biu in EnemyBiulist:
        biu.draw()
        EnemyBiulist.remove(biu) if biu.y > 640 else ''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('关闭了')
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                heroPlaneX = heroPlaneX - 10 if heroPlaneX >= 5 else 0
                oneBiu = HeroBullet(heroPlaneX + 50 - 11, heroPlaneY - 22, windows)
                BiuList.append(oneBiu)
            elif event.key == pygame.K_RIGHT:
                heroPlaneX = heroPlaneX + 10 if heroPlaneX <= 375 else 380
                oneBiu = HeroBullet(heroPlaneX + 50 - 11, heroPlaneY - 22, windows)
                BiuList.append(oneBiu)
            elif event.key == pygame.K_DOWN:
                heroPlaneY = heroPlaneY + 10 if heroPlaneY <= 521 else 526
            elif event.key == pygame.K_UP:
                heroPlaneY = heroPlaneY - 10 if heroPlaneY >= 5  else 0
            elif event.key == pygame.K_SPACE:
                oneBiu = HeroBullet(heroPlaneX + 50 - 11, heroPlaneY - 22, windows)
                BiuList.append(oneBiu)
    x = random.randint(0, 100)
    if x == 5 or x == 79:
        oneBiu = EnemyBullet(enemyPlaneX + 69 // 2 - 9 // 2, enemyPlaneY + 89, windows)
        EnemyBiulist.append(oneBiu)

    enemyRect = Rect(enemyPlaneX, enemyPlaneY, 69, 89)
    # 控制敌机爆炸
    for biu in BiuList:
        biuRect = Rect(biu.x, biu.y, 22, 22)
        if biuRect.colliderect(enemyRect):  # 当战机子弹和敌机重叠时爆炸
            print('敌机爆炸了')
            # enemy_isBomb = True
            BiuList.remove(biu)
    pygame.display.update()
