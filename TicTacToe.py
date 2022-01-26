import sys, pygame
import numpy as np
    
class TicTacToe:

	def __init__(self, size=(600, 600)):

		self.size = self.width, self.height = size

		# Colors
		self.BACKGROUND_COLOR = (20, 70, 100)
		self.WHITE_COLOR = (255, 255, 255)
		self.CIRCLE_COLOR = (140, 146, 172)
		self.CROSS_COLOR = (140, 146, 172)

		pygame.init()
		self.restart_game()


	def draw_game(self):
		offset = self.width / 100 * 7
		pygame.draw.line(self.screen, self.WHITE_COLOR, (self.width // 3, 0 + offset), (self.width // 3, self.width - offset), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (2 * self.width // 3, 0 + offset), (2 * self.width // 3, self.width - offset), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (0 + offset, self.width // 3), (self.width - offset, self.width // 3), width=4)
		pygame.draw.line(self.screen, self.WHITE_COLOR, (0 + offset, 2 * self.width // 3), (self.width - offset, 2 * self.width // 3), width=4)


	def draw_circle(self, x, y):
		radius = self.width / 100 * 8
		pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (self.width // 6 + self.width // 3 * y, self.width // 6 + self.width // 3 * x), radius, width=8)
		pygame.display.update()

	def draw_cross(self, x, y):
		radius = self.width / 100 * 8
		centre_pos = (self.width // 6 + self.width // 3 * y, self.width // 6 + self.width // 3 * x)
		pygame.draw.line(self.screen, self.CROSS_COLOR, (centre_pos[0] - radius, centre_pos[1] - radius), (centre_pos[0] + radius, centre_pos[1] + radius), width=8)
		pygame.draw.line(self.screen, self.CROSS_COLOR, (centre_pos[0] - radius, centre_pos[1] + radius), (centre_pos[0] + radius, centre_pos[1] - radius), width=8)
		pygame.display.update()

	def position_to_index(self, x, y):
		return y // (self.width / 3), x // (self.width / 3)


	def change_turn(self):

		self.turn_O = not self.turn_O

		if(self.turn_O):
			pygame.display.set_caption("Tic Tac Toe - O's turn")
		else:
			pygame.display.set_caption("Tic Tac Toe - X's turn")


	def is_game_over(self):
		
		if(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == 3) or
		   ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == 3) or
		   ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == 3) or
		   ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == 3) or
		   ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == 3)):
				
				pygame.display.set_caption("Game over - O won")
				return True

		elif(((self.board_state[0, 0] + self.board_state[0, 1] + self.board_state[0, 2]) == -3) or
		     ((self.board_state[1, 0] + self.board_state[1, 1] + self.board_state[1, 2]) == -3) or
		     ((self.board_state[2, 0] + self.board_state[2, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 0] + self.board_state[2, 0]) == -3) or
		     ((self.board_state[0, 1] + self.board_state[1, 1] + self.board_state[2, 1]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 2] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == -3) or
		     ((self.board_state[0, 2] + self.board_state[1, 1] + self.board_state[2, 0]) == -3)):
			
				pygame.display.set_caption("Game over - X won")
				return True

		is_there_free_cell = False
		for x in range(3):
			for y in range(3):
				if self.board_state[x, y] == 0:
					is_there_free_cell = True
		if (is_there_free_cell == False):
			pygame.display.set_caption("Draw")
			return True
		else:
			return False


	def restart_game(self):

		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Tic Tac Toe - O's turn")
		self.screen.fill(self.BACKGROUND_COLOR)

		self.draw_game()

		self.turn_O = True

		self.board_state = np.zeros((3, 3))
		pygame.display.update()


	def get_score(self, x, y):

		# Winning movement
		if(((self.board_state[x, 0] + self.board_state[x, 1] + self.board_state[x, 2]) == -2) or
		   ((self.board_state[0, y] + self.board_state[1, y] + self.board_state[2, y]) == -2)):
			return 3 
		elif(x == y): # Main diagonal
			if((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == -2):
				return 3
		elif(((x, y) == (2, 0)) or ((x, y) == (1, 1)) or ((x, y) == (0, 2))): # Other diagonal
			if((self.board_state[2, 0] + self.board_state[1, 1] + self.board_state[0, 2]) == -2):
				return 3


		# Blocking the enemy
		if(((self.board_state[x, 0] + self.board_state[x, 1] + self.board_state[x, 2]) == 2) or
		   ((self.board_state[0, y] + self.board_state[1, y] + self.board_state[2, y]) == 2)):
			return 2
		elif(x == y): # Main diagonal
			if((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == 2):
				return 2
		elif(((x, y) == (2, 0)) or ((x, y) == (1, 1)) or ((x, y) == (0, 2))): # Other diagonal
			if((self.board_state[2, 0] + self.board_state[1, 1] + self.board_state[0, 2]) == 2):
				return 2

		# Align pawns
		if(((self.board_state[x, 0] + self.board_state[x, 1] + self.board_state[x, 2]) == -1) or
		   ((self.board_state[0, y] + self.board_state[1, y] + self.board_state[2, y]) == -1)):
			return 1
		elif(x == y): # Main diagonal
			if((self.board_state[0, 0] + self.board_state[1, 1] + self.board_state[2, 2]) == -1):
				return 1
		elif(((x, y) == (2, 0)) or ((x, y) == (1, 1)) or ((x, y) == (0, 2))): # Other diagonal
			if((self.board_state[2, 0] + self.board_state[1, 1] + self.board_state[0, 2]) == -1):
				return 1

		return 0


	def play_ai(self):

		
		best_movement = []
		best_score = -1
		for x in range(3):
			for y in range(3):
				if self.board_state[x, y] == 0:

					if self.get_score(x, y) > best_score:
						best_movement = (x, y)
						best_score = self.get_score(x, y)

		#idx = np.random.randint(len(free_cells))
		x = best_movement[0]
		y = best_movement[1]
		self.draw_cross(x, y)
		self.board_state[int(x), int(y)] = -1

		self.change_turn()
		self.is_game_over()
		pygame.display.update()


	def play(self, mode='player_vs_player'):
		"""
		:param: mode a mode in ['player_vs_player', 'player_vs_ai']
		"""
		while 1:

		    for event in pygame.event.get():

		    	if event.type == pygame.QUIT:
		    		sys.exit()

		    	if self.is_game_over():

		    		if event.type == pygame.MOUSEBUTTONUP:
		    			self.restart_game()
		    		continue

		    	if event.type == pygame.MOUSEBUTTONUP:
		    		x, y = self.position_to_index(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		    		if self.turn_O:

		    			if self.board_state[int(x), int(y)] == 0:
		    				self.draw_circle(x, y)
		    				self.board_state[int(x), int(y)] = 1
		    				self.change_turn()

		    				if mode == 'player_vs_ai':
		    					if not self.is_game_over():
		    						self.play_ai()

		    		else:

		    			if mode == 'player_vs_player':

			    			if self.board_state[int(x), int(y)] == 0:
			    				self.draw_cross(x, y)
			    				self.board_state[int(x), int(y)] = -1
			    				self.change_turn()

		    		

		    pygame.display.update()


game = TicTacToe()
game.play(mode='player_vs_ai')
