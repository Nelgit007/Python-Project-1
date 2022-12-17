class Settings:
	"""A class to store all settings for our game, Alien Invasion'. """
	
	def __init__(self):
		"""Initialize the games settings"""
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 244, 203)

		# Ship settings
		self.ship_speed = 1.5  #Ship will now move by 1.5 pixel
		
		#Bullet Settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		#Set the number of allowed bullets per time to 4
		self.bullets_allowed = 3

		#Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 1
		#fleet_direction of 1 represents right direction, and -1 rep left dirctn
		self.fleet_direction = 1
