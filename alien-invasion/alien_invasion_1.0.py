import sys
import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

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
		#Instantiate new alien object
		self.aliens = pygame.sprite.Group() #Alien Group

		#Set game background color
		self.bg_color = self.settings.bg_color

		self._create_fleet()

	def run_game(self): #Method-2
		"""Starts the main loop for the game"""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
					

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

	def _update_aliens(self):
		"""Updates the position of all aliens in fleet"""
		self._check_fleet_edges()
		self.aliens.update()
		#self._check_fleet_edges() #first check fleet edges before we updt aliens
		#self.aliens.update()

	def _create_fleet(self):
		"""Creates the fleet of aliens"""
		# Makes an alien and finds the number of alien in a row
		# Spacing of each alien is equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_alien_x = available_space_x // (2 * alien_width)

		# Determine the number of rows of alien that fits on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)


		# Creates the entire fleet of aliens
		for row_number in range(number_rows):
			for alien_number in range(number_alien_x):
				self._create_alien(alien_number, row_number)


	def _create_alien(self, alien_number, row_number):
		"""Creates an alien and places it in a row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x 
		alien.y = alien_height + 2 * alien.rect.height * row_number
		alien.rect.y = alien.y
		#Adding alien to alien group
		self.aliens.add(alien)


	def _check_fleet_edges(self):
		"""This responds approprietly when or if any alien has reched the edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop down the entire fleet, and chage its direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
			self.settings.fleet_direction *= -1


	def _update_screen(self):
		"""Updates images on the screen ad flip to new one"""
		self.screen.fill(self.settings.bg_color)
		#self.mario.blitme()
		self.ship.blitme() #This allows us draw our image to the screen

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Draw alien to screen
		self.aliens.draw(self.screen)

		#Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ ==	 '__main__':
	#Make an instance for the game and run the game
	ai = AlienInvasion()
	ai.run_game()