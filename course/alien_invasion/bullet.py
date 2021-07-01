import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''管理飞船发射子弹的类Bullet继承父类Sprite'''
	def __init__(self,ai_game):
		'''在飞船当前位置创建一个子弹对象'''
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings
		self.color=self.settings.bullet_color
		#在0，0处创建一个表示子弹的矩形，再设置位置为飞船矩形的中间顶部
		self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		self.rect.midtop=ai_game.ship.rect.midtop
		#存储用小数表示的子弹位置
		self.y=float(self.rect.y)
		
	def update(self):
		'''向上移动子弹'''
		#更新表示子弹位置的小数值
		self.y-=self.settings.bullet_speed
		#更新表示子弹的矩形的位置
		self.rect.y=self.y

	def draw_bullet(self):
		'''绘制子弹'''
		#rect函数使用color的颜色填充表示子弹的rect占据screen的部分
		pygame.draw.rect(self.screen,self.color,self.rect)

	def _fire_bullet(self,ai_game):
		'''创建一颗子弹并加到编组bullets中'''
		if len(ai_game.bullets)<self.settings.bullets_allowed :
		#创建Bullet类的实例对象并赋给变量new_bullet
			new_bullet=Bullet(ai_game)
		#add方法类似append，专为pygame编写
			ai_game.bullets.add(new_bullet)

	def _update_bullets(self,ai_game):
		'''更新子弹位置并删除消失的子弹'''
		#为编组bullets中的每颗子弹调用bullet.update()
		ai_game.bullets.update()
		#删除消失的子弹
		for bullet in ai_game.bullets.copy():
			if bullet.rect.bottom<=0:
				ai_game.bullets.remove(bullet)
		ai_game._check_bullet_alien_collisions()


