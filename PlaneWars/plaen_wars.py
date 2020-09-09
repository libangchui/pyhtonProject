#Author:BangChui
#encoding:utf-8
_date_ = "2019/12/26 14:15"
import pygame
import random
import time
class HeroBullet:
    """英雄机子弹"""
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.pic = pygame.image.load("img/bullet-3.gif")
    def draw(self):
        """绘制英雄机子弹"""
        self.screen.blit(self.pic,(self.x,self.y))
        self.move()
    def move(self):
        self.y -=5
class Enemybullet:
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.pic = pygame.image.load("img/bullet-1.gif")
    def draw(self):
        """绘制子弹"""
        self.screen.blit(self.pic,(self.x,self.y))
        self.move()
    def move(self):
        self.y+=12

# class hero_daodan:
# """定义战机跟踪导弹"""
#     def __init__(self,x,y,screen):
#         self.x = x
#         self.y = y
#         self.screen = screen
#         self.hero_daodan = pygame.image.load("img/zidan1.png")
#     def draw(self):
#         self.screen.blit(self.hero_daodan,(self.x,self.y))
#         self.move
#     def move(self):
#         self.x = enemy_plaenX
#         self.y = enemy_plaenY
pygame.init()
# 9*104   130*104




# 设置窗口大小
screen = pygame.display.set_mode((480,650), pygame.DOUBLEBUF,32)#pygame.DOUBLEBUF,pygame.FULLSCREEN
#修改游戏名称
pygame.display.set_caption("雷电1949","华文隶书")

# 修改游戏图标
icon = pygame.image.load("img/icon72x72.png")
pygame.display.set_icon(icon)
#加载背景图片，和英雄机图片
bg_image = pygame.image.load("img/background.png")
hero_image1 = pygame.image.load("img/hero.gif")# 英雄机1
hero_image2 = pygame.image.load("img/hero2.png") # 英雄机2

# 加载英雄机2号
hero2_image1 = pygame.image.load("img/hero2_image.png")
hero2_image2 = pygame.image.load("img/hero_image2.png")
# 加载敌机图片
enemy_image1 = pygame.image.load("img/enemy1.png")
enemy_image2 = pygame.image.load("img/enemy-2.gif")
# 加载导弹图片
# hero_daodan = pygame.image.load("img/zidan1.png")
# 加载敌机爆炸图片
enemy_booooom_list = ["img/enemy1_down1.png","img/enemy1_down2.png","img/enemy1_down3.png","img/enemy1_down4.png"]
# 加载英雄机爆炸图片
hero_booooom_list = ["img/hero_blowup_n1.png","img/hero_blowup_n2.png","img/hero_blowup_n3.png","img/hero_blowup_n4.png"]
# 加载游戏结束图片
game_over = pygame.image.load("img/quit_nor.png")
# 定义敌机rect
enemy_rect = pygame.rect.Rect(480//2-68//2,0,68,89)
# 定义英雄机图片切换索引
heroindexshif = 0
# 定义敌机图片切换索引
enemyindexshif = 0
# 定义英雄机1的rect
hero_rect =pygame.rect.Rect(190,526,100,124)
# 定义英雄机2的rect
hero_rect1 = pygame.rect.Rect(190,650,69,89)
# 敌机的x，y坐标
enemy_plaenX = enemy_rect.x
enemy_plaenY = enemy_rect.y
# 创建时钟
clock  = pygame.time.Clock()
#  创建英雄机1的xy轴
hero_planeX = hero_rect.x
hero_planeY = hero_rect.y
# 创建英雄机2的xy轴
hero2_planeX = hero_rect1.x
hero2_planeY = hero_rect1.y

# 创建英雄机的子弹列表
heroBiulist = []
# 创建敌机的子弹列表
EnemyBiulist1 = []
# 敌机爆炸条件
enemy_booooom = False
#英雄机爆炸条件
hero_booooom = False
# 英雄机爆炸图片索引
hero_boom_index = 0
# 敌机爆炸图片索引
enemy_boom_index = 0
# 定义敌机初始移动方向
direct = "左"
#按键灵敏度设置
pygame.key.set_repeat(20,30)
# 游戏循环
# 敌机血量
EnemyLife = 10000
HeroLife = 100
# 定义信息显示的形式
text = pygame.font.SysFont("华文隶书", 26)# Blackadder ITC
if hero_rect.bottom<= 0:
    hero_rect.y = 650
while True:
    clock.tick(60)# 表示每秒刷新120次
    """把背景图片添加到游戏界面，从（0,0）开始，表示背景图片放到远点位置"""
    screen.blit(bg_image, (0, 0))
    # 绘制生命值提示信息
    text_enemy = text.render(f"EnemyLife:{EnemyLife}",1,(242,72,27))
    text_hero = text.render(f"HeroLife:{HeroLife}",1,(39,117,182))
    # 绘制飞机生命值显示位置
    screen.blit(text_enemy,(0,0))
    screen.blit(text_hero, (360,620))
    #控制敌机移动
    if direct == "左":
        enemy_plaenX -=6
        if enemy_plaenX<=0:
            direct = "右"
    elif direct == "右":
        enemy_plaenX+=6
        if enemy_plaenX>= 480-68:
            direct = "左"
    # 绘制英雄机子弹
    for bullethero in heroBiulist:
        bullethero.draw()
        # 让子弹上升到最上面消失
        heroBiulist.remove(bullethero) if bullethero.y < 0 else ""
        # 定义战机子弹的rectangle
        hero_bullet_rect = pygame.rect.Rect(bullethero.x,bullethero.y,22,22)
        # 检测战机子弹是否和敌机相交
        # while enemy_left == 10:
        enemy_rect1 = pygame.rect.Rect(enemy_plaenX,enemy_plaenY,68,89)
        if hero_bullet_rect.colliderect(enemy_rect1):
            EnemyLife-=2
            try:
                heroBiulist.remove(bullethero)
            except Exception:
                pass
            if EnemyLife < 0:
                print("敌机爆炸")
                enemy_booooom = True

    if enemy_booooom == False:
        # 未爆炸图片
        # 让它从底部飞出
        if enemyindexshif == 0:
            screen.blit(enemy_image1, (enemy_plaenX, enemy_plaenY))
            enemyindexshif += 1
        else:
            screen.blit(enemy_image2, (enemy_plaenX, enemy_plaenY))
            enemyindexshif = 0
        # 绘制敌机爆炸图片
    else:
        if enemy_boom_index == len(enemy_booooom_list):# 当爆炸图片索引和爆炸图片总数相同时
            time.sleep(0.2)
            screen.blit(game_over,(230,320))
            exit(0)
        enemy_bobm_image = pygame.image.load(enemy_booooom_list[enemy_boom_index])
        screen.blit(enemy_bobm_image,(enemy_plaenX,enemy_plaenY))# 绘制图片
        enemy_boom_index +=1
        time.sleep(0.5)

    x = random.randint(1,100)
    if x == 5 or x == 50:
        enemy_bullet1 = Enemybullet(enemy_plaenX + 9, enemy_plaenY + 104, screen)
        EnemyBiulist1.append(enemy_bullet1)
    for bullet in EnemyBiulist1:
        bullet.draw()  # 绘制子弹
        # 子弹消失
        EnemyBiulist1.remove(bullet) if bullet.y >= 650else ""
        # 定义敌机子弹rect
        enemy_bullet_rect = pygame.rect.Rect(bullet.x, bullet.y, 9, 21)
        hero_rect2 = pygame.rect.Rect(hero_planeX, hero_planeY, 100, 124)

        # 碰撞检测
        enemy_rect_d = pygame.rect.Rect(enemy_plaenX,enemy_plaenY,68,89)
        hero_rect_y = pygame.rect.Rect(hero_planeX, hero_planeY, 100, 124)
        if enemy_rect_d.colliderect(hero_rect_y):
            EnemyLife-=2
            HeroLife-=1
            print("飞机碰撞...")
            if HeroLife < 0:
                # 英雄机爆炸绘制
                if hero_boom_index == len(hero_booooom_list):  # 当爆炸图片索引和爆炸图片总数相同时
                    print("英雄机阵亡")
                    time.sleep(0.5)
                    screen.blit(game_over, (230, 320))
                    exit(0)
                hero_bobm_image = pygame.image.load(hero_booooom_list[hero_boom_index])
                screen.blit(hero_bobm_image, (hero_planeX, hero_planeY))  # 绘制图片
                hero_boom_index += 1
                time.sleep(0.5)
            elif EnemyLife < 0:
                # 敌机爆炸绘制
                if enemy_boom_index == len(enemy_booooom_list):  # 当爆炸图片索引和爆炸图片总数相同时
                    print("敌机死亡")
                    time.sleep(0.5)
                    screen.blit(game_over, (230, 320))
                    exit(0)
                enemy_bobm_image = pygame.image.load(enemy_booooom_list[enemy_boom_index])
                screen.blit(enemy_bobm_image, (enemy_plaenX, enemy_plaenY))  # 绘制图片
                enemy_boom_index += 1
                time.sleep(0.5)

            if hero_boom_index == len(hero_booooom_list):  # 当爆炸图片索引和爆炸图片总数相同时
                time.sleep(0.2)
                screen.blit(game_over, (230, 320))
                exit(0)
                print("游戏结束")
        if enemy_bullet_rect.colliderect(hero_rect2):
            HeroLife-=1
            if HeroLife < 0:
                print("英雄机爆炸")
                hero_booooom = True
                # 移除敌机子弹
            EnemyBiulist1.remove(bullet)
    if hero_booooom == False:
        # 绘制英雄机1
        if heroindexshif == 0:
            screen.blit(hero_image1, (hero_planeX, hero_planeY))
            screen.blit(hero2_image1, (hero2_planeX, hero2_planeY))
            heroindexshif += 1
        else:
            screen.blit(hero_image2, (hero_planeX, hero_planeY))
            screen.blit(hero_image2, (hero2_planeX, hero2_planeY))
            heroindexshif = 0
            # 修改英雄机的y值，实现自动飞行
            hero_rect.y -= 3
    else:
        if hero_boom_index == len(hero_booooom_list):# 当爆炸图片索引和爆炸图片总数相同时
            time.sleep(0.2)
            screen.blit(game_over, (230, 320))
            exit(0)
        hero_bobm_image = pygame.image.load(hero_booooom_list[hero_boom_index])
        screen.blit(hero_bobm_image,(hero_planeX,hero_planeY))# 绘制图片
        hero_boom_index +=1
        time.sleep(0.5)
    # for enemy_diji in EnemyBiulist1:
    #     for hero_yx in heroBiulist:
    #         enemy_bullet_rect = pygame.rect.Rect(bullet.x, bullet.y, 9, 21)
    #         hero_bullet_rect = pygame.rect.Rect(bullethero.x, bullethero.y, 22, 22)
    #         flag = enemy_bullet_rect.colliderect(hero_bullet_rect)
    #         if flag:
    #             EnemyBiulist1.remove(bullet)
    #             heroBiulist.remove(bullethero)
    # 获取所有事件
    event_list = pygame.event.get()
    #print(event_list) 打印所有事件
    for event in event_list:
        # 捕获窗口退出事件
        if event.type == pygame.QUIT:
            print("游戏结束...")
            pygame.quit()
            exit(0)# 终止python程序
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_planeX = hero_planeX - 20 if hero_planeX>=7 else 0
                hero_bullet = HeroBullet(hero_planeX + 50 - 11, hero_planeY - 22, screen)
                heroBiulist.append(hero_bullet)
            elif event.key == pygame.K_RIGHT:
                hero_planeX = hero_planeX+20 if hero_planeX <=375 else 380
                hero_bullet = HeroBullet(hero_planeX + 50 - 11, hero_planeY - 22, screen)
                heroBiulist.append(hero_bullet)
            elif event.key == pygame.K_UP:
                hero_planeY = hero_planeY - 20 if hero_planeY>=7 else 0
                hero_bullet = HeroBullet(hero_planeX + 50 - 11, hero_planeY - 22, screen)
                heroBiulist.append(hero_bullet)
            elif event.key == pygame.K_DOWN:
                hero_planeY = hero_planeY+20 if hero_planeY<=521 else 526
                hero_bullet = HeroBullet(hero_planeX + 50 - 11, hero_planeY - 22, screen)
                heroBiulist.append(hero_bullet)
            elif event.key == pygame.K_SPACE:
                # 实例化子弹对象
                hero_bullet = HeroBullet(hero_planeX+50-11,hero_planeY-22,screen)
                # 子弹添加到列表
                heroBiulist.append(hero_bullet)
            elif event.key == pygame.K_4:
                HeroLife = HeroLife+10
                EnemyLife = EnemyLife-100
                '''----------------'''
            # elif event.key == pygame.K_a:
            #     hero_dd = hero_daodan(hero_planeX + 50 - 11, hero_planeY - 22, screen)
            #     heroBiulist.append(hero_bullet)
                '''-----------------'''
    # 实现自动射击
    hero_bullet = HeroBullet(hero_planeX + 50 - 11, hero_planeY - 22, screen)
    heroBiulist.append(hero_bullet)
            # hero2_planeY = hero2_planeY+7 if hero2_planeY <= 521 else 590
    pygame.display.update() # 循环更新页面
    time.sleep(0.01)
pygame.quit()