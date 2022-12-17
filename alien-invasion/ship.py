import pygame

class Ship:
	"""A class to manage the ship or main player xter"""

	def __init__(self, ai_game): #the ai_game parameter allows us access all attribute associated with the game itself.
		"""Initializes the ship, and set the ship starting position, now the ship speed."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings #To use the ship_speed

		#Load ship image and get rect
		self.image = pygame.image.load('images/ship2.bmp')
		self.rect = self.image.get_rect()
		#Each new ship to start at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store a decimal value for ships horizontal position
		self.x = float(self.rect.x)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Updaet ship's position based on the movement flag from users"""
		#We update the x value of the ship not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right: 
			self.x += self.settings.ship_speed
			#self.rect.x += 1
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			#self.rect.x -= 1

		# Update rect object from self.rect.x to self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
