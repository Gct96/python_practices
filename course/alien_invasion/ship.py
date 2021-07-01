import pygame
from time import sleep
from pygame.sprite import Sprite
class Ship(Sprite):
	#接收一个参数，AlienInvasion的实例对象
	def __init__(self,ai_game):   
		'''初始化飞船并设置其初始位置'''
		super().__init__()
		self.screen=ai_game.screen #将屏幕赋给Ship的一个属性
		self.settings=ai_game.settings
		self.screen_rect=ai_game.screen.get_rect() 
		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		#使用get_rect()方法获取相应surface的属性rect，用来指定飞船的位置
		self.rect=self.image.get_rect() 
		#每艘新飞船都放在底部中央
		self.rect.midbottom=self.screen_rect.midbottom
		#在飞船属性x中存储小数
		self.x=float(self.rect.x)
		#移动标志
		self.moving_right=False
		self.moving_left=False

	def update(self):
		'''根据移动标志调整飞船位置'''
		#更新飞船而不是rect对象的x值. self.rect.right返回飞船外接矩形右边缘的x坐标
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.x+=self.settings.ship_speed
		if self.moving_left and self.rect.left>0:
			self.x-=self.settings.ship_speed
		#根据self.x更新rect对象
		self.rect.x=self.x
		
	def blitme(self):
		'''在rect指定位置绘制飞船image'''
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		'''让飞船在屏幕底端居中'''
		self.rect.midbottom=self.screen_rect.midbottom
		#重置跟踪飞船确切位置的属性
		self.x=float(self.rect.x)

	def _ship_hit(self,ai_game):
		'''响应飞船被撞'''
		if (ai_game.stats.ships_left-1)>0:
			#将余下飞船数减1并更新计数 
			ai_game.stats.ships_left-=1
			ai_game.sb.prep_ships()
			#清空余下的外星人和子弹
			ai_game.aliens.empty()
			ai_game.bullets.empty()
			#创建一群新的外星人，飞船放到屏幕底端中间
			ai_game.alien0._create_fleet(ai_game)
			self.center_ship()
			#暂停
			sleep(0.5)
		else:
			ai_game.stats.game_active=False
			pygame.mouse.set_visible(True)