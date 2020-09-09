# Author:BangChui
# encoding:utf-8
# _date_ = "2019/12/31 10:29"

import pygame
import os
import time
import random


# def text_life():
def get_pic(path):
    """获取图片"""
    # 拼接图片路径
    pic_path = os.path.join("C:\\Users\\fugui\\PycharmProjects\\PlaneWars\\img\\", path)

    # 返回pygame对象
    return pygame.image.load(pic_path)


class HeroBullet:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.pic = get_pic("bullet-3.gif")


    def draw(self):
        """绘制子弹"""
        self.screen.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        """子弹移动"""
        self.y -= 10


class EnemyBullet:
    """敌机子弹"""

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.pic = get_pic("bullet-1.gif")

    def draw(self):
        self.screen.blit(self.pic, (self.x, self.y))
        self.move()

    def move(self):
        self.y += 5


class HeroPlane:
    '''英雄机类'''
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.isBoom = False  # 爆炸条件
        self.normal_image_List = ["hero1.png", "hero.gif"]  # 正常图片
        self.normal_image_index = 0  # 索引
        self.Boom_image_list = ["hero_blowup_n1.png", "hero_blowup_n2.png", "hero_blowup_n3.png", "hero_blowup_n4.png"]
        self.Boom_image_index = 0 # 定义爆炸图片索引
        self.heroBiulist = [] # 定义英雄级子弹列表
        self.heroLife = 10 # 定义英雄机生命值
# 定义一个战斗机绘制
    """"""
    def draw(self):
        """绘制英雄机图"""
        if self.isBoom == False:  # 未爆炸情况
            pic = get_pic(self.normal_image_List[self.normal_image_index])
            self.screen.blit(pic, (self.x, self.y))  # 绘制未爆炸英雄机
            self.normal_image_index = (self.normal_image_index + 1) % len(self.normal_image_List)
        else:
            if self.Boom_image_index == len(self.Boom_image_list):
                time.sleep(0.5) #   定义沉睡时间
                exit(0) # 退出
            """爆炸图片绘制"""
            hero_Boom_image = get_pic(self.Boom_image_list[self.Boom_image_index])
            self.screen.blit(hero_Boom_image, (self.x, self.y))
            self.Boom_image_index += 1  # shunxushuchu
            time.sleep(0.5)

    def deal_event(self):
        # event_list = pygame.event.get() #返回事件的列表
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出事件
                # if event.key ==
                exit(0)
            elif event.type ==  pygame.KEYDOWN: # 获取键盘向下触发事件
                if event.key == pygame.K_LEFT: # 获取键盘向左触发事件
                    self.x = self.x - 20 if self.x >= 7 else 0
                    # one_bullet = HeroBullet(self.x + 50 - 11, self.y - 22, self.screen)
                    # self.heroBiulist.append(one_bullet)
                elif event.key == pygame.K_RIGHT:
                    self.x = self.x + 20 if self.x <= 375 else 380
                    # one_bullet = HeroBullet(self.x + 50 - 11, self.y - 22, self.screen)
                    # self.heroBiulist.append(one_bullet)
                elif event.key == pygame.K_UP:
                    self.y = self.y - 20 if self.y >= 7 else 0
                    # one_bullet = HeroBullet(self.x + 50 - 11, self.y - 22, self.screen)
                    # self.heroBiulist.append(one_bullet)
                elif event.key == pygame.K_DOWN:
                    self.y = self.y + 20 if self.y <= 521 else 526
                    # one_bullet = HeroBullet(self.x + 50 - 11, self.y - 22, self.screen)
                    # self.heroBiulist.append(one_bullet)
                elif event.key == pygame.K_SPACE:
                    one_bullet = HeroBullet(self.x + 50 - 11, self.y - 22, self.screen)
                    self.heroBiulist.append(one_bullet)
        # 绘制子弹
        for bullet in self.heroBiulist:
            bullet.draw()
            self.heroBiulist.remove(bullet) if bullet.y < 0 else ""

    def check_collide(self, EnemyBiulist):
        """
        碰撞检测
        :param enemyBiulist: 敌机子弹别表
        :return:
        """
        # 定义英雄级的rect
        hero_rect = pygame.rect.Rect(self.x, self.y, 100, 124)
        for bullet in EnemyBiulist:  # 遍历敌机子弹
            enemy_bullet_rect = pygame.rect.Rect(bullet.x, bullet.y, 9, 21)
            if enemy_bullet_rect.colliderect(hero_rect):
                self.heroLife -= 1
                if self.heroLife <= 0:
                    self.isBoom = True
                    print("英雄机爆炸")
                # 将英雄机爆炸条件置为true
                EnemyBiulist.remove(bullet)  # 爆炸时的移除敌机子弹


class EnemyPlane:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.isBoom = False  # 爆炸条件
        self.normal_image_List = ["enemy1.png", "enemy-2.gif"]  # 正常图片
        self.normal_image_index = 0  # 索引
        self.Boom_image_list = ["enemy1_down1.png", "enemy1_down2.png", "enemy1_down3.png", "enemy1_down4.png"]
        self.Boom_image_index = 0
        self.EnemyBiulist = []
        self.direct = "左"
        self.enemyLife = 100

    def draw(self):
        """绘制敌机"""
        if self.isBoom == False:
            """绘制未爆炸图片"""
            pic = get_pic(self.normal_image_List[self.normal_image_index])
            self.screen.blit(pic, (self.x, self.y))
            self.normal_image_index = (self.normal_image_index + 1) % len(self.normal_image_List)
        else:
            """绘制敌机爆炸图片"""
            if self.Boom_image_index == len(self.Boom_image_list):
                time.sleep(0.5)
                exit(0)
            enemy_boom_image = get_pic(self.Boom_image_list[self.Boom_image_index])
            self.screen.blit(enemy_boom_image, (self.x, self.y))
            self.Boom_image_index += 1
            time.sleep(0.5)
        # 控制敌机移动
        self.move()
        self.fire()
    def move(self):
        """控制敌机移动"""
        if self.direct == "左":
            self.x -= 5
            if self.x <= 0:
                self.direct = "右"
        if self.direct == "右":
            self.x += 5
            if self.x >= 480 - 68:
                self.direct = "左"

    def fire(self):
        """敌机开火"""
        # 产生随机数
        x = random.randint(1, 100)
        if x == 5 or x == 50:
            # 实例化一个敌机子弹
            one_bullet = EnemyBullet(self.x + 9, self.y + 104, self.screen)
            self.EnemyBiulist.append(one_bullet)
        for bullet in self.EnemyBiulist:
            bullet.draw()
            # 让子弹最下面消失
            self.EnemyBiulist.remove(bullet) if bullet.y > 650  else ""

    def check_dollide(self, heroBiulist, ):
        """
        碰撞检测
        :param heroBiulist: 战机子弹列表
        :return:
         """
        # 定义敌机rect
        enemy_rect = pygame.rect.Rect(self.x, self.y, 69, 89)
        for bullet in heroBiulist:
            hero_bullet_rect = pygame.rect.Rect(bullet.x, bullet.y, 22, 22)
            if hero_bullet_rect.colliderect(enemy_rect):
                if self.enemyLife <= 0:
                    print("敌机爆炸")
                    # 移除英雄机子弹
                    self.isBoom = True
                self.enemyLife -= 1
                heroBiulist.remove(bullet)


if __name__ == '__main__':
    # 初始化游戏
    pygame.init()
    # 设置背景
    screen = pygame.display.set_mode((480, 650), 0, 32)
    #  设置标题
    pygame.display.set_caption("雷霆战机")
    # 设置图标
    pygame.display.set_icon(get_pic("icon72x72.png"))
    # 实例化英雄机对象
    hero_plane = HeroPlane(190, 526, screen)
    # 实例化敌机对象
    enemy_plane = EnemyPlane(480 // 2 - 68 // 2, 0, screen)
    pygame.key.set_repeat(20, 30)
    while True:
        # 绘制背景图片
        # clock.tick(60)
        bg = get_pic("background.png")
        screen.blit(bg, (0, 0))
        # 敌机碰撞检测
        enemy_plane.check_dollide(hero_plane.heroBiulist)
        # 英雄机碰撞检测
        hero_plane.check_collide(enemy_plane.EnemyBiulist)
        # 绘制英雄机
        hero_plane.draw()
        # 绘制敌机
        enemy_plane.draw()
        #  血量文本显示
        text = pygame.font.SysFont("华文隶书", 26)  # Blackadder ITC
        # 敌机血量提示
        text_enemy = text.render(f'EnemyLife:{enemy_plane.enemyLife}', 1, (242, 72, 27))
        screen.blit(text_enemy, (0, 0))
        # 英雄机血量提示
        text_hero = text.render(f"HeroLife:{hero_plane.heroLife}", 1, (39, 117, 182))
        screen.blit(text_hero, (360, 620))
        hero_plane.deal_event()
        pygame.display.update()
        time.sleep(0.02)