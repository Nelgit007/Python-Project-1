import sys
import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

class AlienInvasion:
	"""Overall class to manage game properties/methods and behavior."""

	def __init__(self): #Method-1
		"""Initializes game and creates game resources."""
		pygame.init()
		#Instantiate the new class
		self.settings = Settings()

		#Setting the game to display in full screen
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height


		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		#Instantiating a new ship object
		self.bullets = pygame.sprite.Group()

		#Set game background color
		self.bg_color = self.settings.bg_color

	def run_game(self): #Method-2
		"""Starts the main loop for the game"""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
					

	def _check_events(self):
		"""Detects vand responds to keyboard presses and mouse events, "user inputs"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN: #Chek for keydown event
				self._check_keydown_events(event)
			
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respnd to key presses"""
		if event.key == pygame.K_RIGHT:
			#Move ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullets()

	def _check_keyup_events(self, event):
		"""Respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _fire_bullets(self):
		"""Creates a new bullets and adds it to bullet Group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Updates the position of bullets as wel as get rid of old bullets"""
		# To updte bullets position
		self.bullets.update()

		# Getting rid of bullets that have gone past our game screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
				print(len(self.bullets))




	def _update_screen(self):
		"""Updates images on the screen ad flip to new one"""
		self.screen.fill(self.settings.bg_color)
		#self.mario.blitme()
		self.ship.blitme() #This allows us draw our image to the screen

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		#Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ ==	 '__main__':
	#Make an instance for the game and run the game
	ai = AlienInvasion()
	ai.run_game()