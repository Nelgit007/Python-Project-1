import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A singl alien in the fleet"""

	def __init__(self, ai_game):
		"""Initiazes the alien, and also set alien starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings #referenced settings

		#Loading alien image and set its rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Starting each alien near the top left end of screen
		self.rect.x = self.rect.width #Away from x-axis
		self.rect.y = self.rect.height #Away from the heogh of image

		# Store alien exact horizontal position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Checks and return True if alien is at edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True

		elif self.rect.left <= 0:
			return True

	def update(self):
		"""This moves the alien position to the right"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x
		#self.x += self.settings.alien_speed
		#self.rect.x = self.x

