import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
	'''显示得分信息的类'''
	def __init__(self,ai_game):
		'''初始化显示得分涉及的属性'''
		self.ai_game=ai_game
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.settings=ai_game.settings
		self.stats=ai_game.stats
		#显示得分信息时使用的字体设置
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		#准备初始得分图像和等级和飞船数
		self.prep_images()

	def prep_images(self):
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		'''将得分转换为渲染的图像'''
		#将小数位数精确到10的整数倍
		rounded_score=round(self.stats.score,-1)
		#将数值转为字符串时插入逗号
		score_str="{:,}".format(rounded_score)
		self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
		#在右上角显示得分
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20

	def prep_high_score(self):
		'''将最高得分转换为渲染的图像'''
		high_score=round(self.stats.high_score,-1)
		high_score_str="{:,}".format(high_score)
		self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
		#将最高得分放在屏幕顶部中间
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect=self.screen_rect.midtop

	def check_high_score(self):
		if self.stats.score>self.stats.high_score:
			self.stats.high_score=self.stats.score
			self.prep_high_score()

	def prep_level(self):
		'''将等级转为渲染的图像'''
		level_str=str(self.stats.level)
		self.level_image=self.font.render(level_str,True,self.text_color,self.settings.bg_color)
		#将等级放在得分下方
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.score_rect.right
		self.level_rect.top=self.score_rect.bottom+10

	def prep_ships(self):
		'''显示余下飞船数'''
		#创建一个空编组存储飞船实例
		self.ships=Group()
		#给剩下的每艘飞船设置坐标并加入到编组中
		for ship_number in range(self.stats.ships_left):
			ship=Ship(self.ai_game)
			ship.rect.x=10+ship_number*ship.rect.width
			ship.rect.y=10
			self.ships.add(ship)

	def show_score(self):
		'''在屏幕上显示得分和等级，放在score_rect指定的位置，画出飞船数'''
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)