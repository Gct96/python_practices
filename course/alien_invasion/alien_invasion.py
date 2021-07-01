import sys
#sleep在飞船被撞到后让游戏暂停片刻
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
class AlienInvasion:
	'''管理游戏资源和行为的类'''
	def __init__(self):
		'''初始化游戏并创建游戏资源'''
		pygame.init()
		#他类对象作本类属性
		self.settings=Settings()   
		#元组实参
		self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) 
		pygame.display.set_caption('Alien Invasion')
		self.stats=GameStats(self)
		self.sb=Scoreboard(self)
		#self指向当前AlienInvasion实例
		self.ship=Ship(self) 
		self.bullet=Bullet(self)
		self.alien0=Alien(self)
		#创建一个Group类的实例对象-bullets编组
		self.bullets=pygame.sprite.Group()
		#创建一个Group类的实例对象-aliens编组
		self.aliens=pygame.sprite.Group()
		self.alien0._create_fleet(self)
		#创建play按钮
		self.play_button=Button(self,'play')

	def run_game(self):
		'''开始游戏主循环'''
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self.bullet._update_bullets(self)
				self.start_new_level()
				self._update_aliens()
			self._update_screen()
	
	def _check_events(self):
		'''监视键盘和鼠标事件'''
		for event in pygame.event.get():
            #监听活动类型（退出、按下、松开）
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type==pygame.MOUSEBUTTONDOWN:
				#此方法返回一个元组，包含单机鼠标时的x坐标和y坐标
				mouse_pos=pygame.mouse.get_pos()
				#将获取到的单击坐标传给这方法
				self._check_play_button(mouse_pos)

	def _check_play_button(self,mouse_pos):
		'''在玩家单击play时开始游戏'''
		#检查单击坐标是否在play按钮的rect内
		button_clicked=self.play_button.rect.collidepoint(mouse_pos)
		#只有单击play且游戏处于非活动态才开始新游戏
		if button_clicked and not self.stats.game_active:
			#重置游戏统计信息,给3艘船，并初始化动态设置
			self.settings.initialize_dynamic_settings()
			#先重置统计信息再调用prep_score和level和ships
			self.stats.reset_stats()
			self.stats.game_active=True
			self.sb.prep_images()
			#清空余下的外星人和子弹
			self.bullets.empty()
			#创建一群新的外星人，让飞船居中
			self.alien0._create_fleet(self)
			self.ship.center_ship()
			pygame.mouse.set_visible(False)

	def _check_keydown_events(self,event):
		'''辅助方法，响应按下'''
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=True
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=True
		elif event.key==pygame.K_SPACE:
			self.bullet._fire_bullet(self)
		#当活动是按下键盘的q键时退出
		elif event.key==pygame.K_q:
			sys.exit()

	def _check_keyup_events(self,event):
		'''辅助方法，响应松开'''
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=False
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False

	def _check_bullet_alien_collisions(self):
		'''响应子弹和外星人的碰撞'''
		#检查是否有子弹击中了外星人,groupcollide添加重叠的子弹和外星人(列表)键值对，两个true删除碰撞的外星人和子弹
		collisons=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
		#如果字典存在就遍历其中的值，每个值都是列表
		if collisons:
			for aliens in collisons.values():
				self.stats.score+=self.settings.alien_points*len(aliens)
			#创建一幅最新得分的新图像
			self.sb.prep_score()
			self.sb.check_high_score()

	def start_new_level(self):
		if not self.aliens:
			#删除现有的子弹并新建一群外星人，同时加快游戏节奏
			self.bullets.empty()
			self.alien0._create_fleet(self)
			self.settings.increase_speed()
			#提高游戏等级
			self.stats.level+=1
			self.sb.prep_level()

	def _update_aliens(self):
		self.alien0._check_fleet_edges(self)
		self.aliens.update()
		#检查外星人和飞船之间的碰撞
		#spritecollideany接收一个精灵和一个编组，返回第一个与飞船发生碰撞的外星人
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self.ship._ship_hit(self)
		#检查是否有外星人到达屏幕底端，并作出响应
		self.alien0._check_aliens_bottom(self)

	def _update_screen(self):
		'''更新屏幕上的图像，并切换到新屏幕'''
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		#方法bullets.sprites()返回一个列表，遍历列表的所有精灵，每个都调用draw_bullet
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		#对编组调用draw,参数指定了元素alien绘制在哪个surface上
		self.aliens.draw(self.screen)
		#显示得分、等级和飞船数
		self.sb.show_score()
		#如果游戏非活动状态就绘制play按钮
		if not self.stats.game_active:
			self.play_button.draw_button()
		#让最近绘制的屏幕可见
		pygame.display.flip()

if __name__ == '__main__':
	ai=AlienInvasion()
	ai.run_game()