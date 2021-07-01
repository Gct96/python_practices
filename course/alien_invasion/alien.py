import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	'''表示单个外星人的类'''
	def __init__(self,ai_game):
		'''初始化外星人并设置其起始位置'''
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings
		#加载外星人图像并设置其rect属性
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		#每个外星人初始在屏幕左上角
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#存储外星人的精确水平位置
		self.x=float(self.rect.x)

	def check_edges(self):
		'''如果外星人位于屏幕边缘，就返回True'''
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right or self.rect.left<=0:
			return True

	def update(self):
		'''向左或右移动外星人,self.x可存储小数值'''
		self.x+=(self.settings.alien_speed*self.settings.fleet_direction)
		self.rect.x=self.x

	def _check_fleet_edges(self,ai_game):
		'''检查是否有外星人到达屏幕左右边缘'''
		for alien in ai_game.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction(ai_game)
				break

	def _change_fleet_direction(self,ai_game):
		'''将整群外星人下移并改变方向'''
		for alien in ai_game.aliens.sprites():
			alien.rect.y+=self.settings.fleet_drop_speed
		self.settings.fleet_direction*=-1

	def _check_aliens_bottom(self,ai_game):
		'''检查是否有外星人到达屏幕底端'''
		screen_rect=self.screen.get_rect()
		for alien in ai_game.aliens.sprites():
			if alien.rect.bottom>=screen_rect.bottom:
				#象飞船被撞到一样处理
				ai_game.ship._ship_hit(ai_game)
				break

	def _create_fleet(self,ai_game): 
		'''创建外星人群'''
		#创建第一个外星人
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size
		#计算可用的水平宽度
		available_space_x=self.settings.screen_width-(2*alien_width)
		#计算一行可创建的外星人数
		number_alien_x=available_space_x//(2*alien_width)
		#计算可容纳多少行
		ship_height=ai_game.ship.rect.height
		available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
		number_rows=available_space_y//(2*alien_height)
		#创建外星人群
		for row_number in range(number_rows):
			for alien_number in range(number_alien_x):
				self._create_alien(alien_number,row_number,ai_game)

	def _create_alien(self,alien_number,row_number,ai_game):
		 '''辅助方法，创建一个外星人并将其加入当前行'''
		 alien=Alien(self)
		#size属性是一个元组，包含rect对象的宽度高度
		 alien_width,alien_height=alien.rect.size
		#alien的x坐标在移动时是要用到的，所以另设变量x接收初始x坐标
		 alien.x=alien_width+2*alien_width*alien_number
		 alien.rect.x=alien.x
		 alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
		 ai_game.aliens.add(alien)