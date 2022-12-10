import pygame

from pygame.sprite import Sprite 

class Bullet(Sprite):
	"""A class to manage bullets fired from ship"""

	def __init__(self, ai_game):
		"""Creates a bullets object at current position of our ship"""
		super().__init__() #This is to reference the Sprite class we are calling.
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#Create a bullet with rect at (0, 0) and set its correct position
		self.rect = pygame.rect.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#Store the bullets positions as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen"""
		# Update the decimal position of the bullet
		self.y -= self.settings.bullet_speed #Define y co-ordinate
		# Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
