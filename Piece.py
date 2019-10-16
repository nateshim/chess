import sys, pygame
from Board import Board
class Piece:
	
	def __init__(self,image, x,y, isSelected, isBeginning, color):
		self.image = image
		self.x = x
		self.y = y
		self.isSelected = isSelected
		self.isBeginning = isBeginning
		self.color = color

	def getColor(self):
		return self.color
	def getImage(self):
		return self.image

	def getPosition(self, x, y):
		board = Board()
		return board.get(x, y)
	def select(self):
		if self.isSelected == False:
			self.isSelected = True
		else:
			self.isSelected = False
	def eat(self, enemyPiece):
		self.x = enemyPiece.x
		self.y = enemyPiece.y
		enemyPiece = None
		self.isSelected = False
		self.isBeginning = False
		return enemyPiece

class Pawn(Piece):
	def move(self, newPos, board): #newPos = (x,y)
		curr = self.getPosition(self.x, self.y)
		if self.image == "blackpawn.png":
			if self.isValid(newPos):
				if self.isBeginning: 
					if newPos[1] >= curr.get('y') + 2*curr.get('h') and newPos[1] <= curr.get('y') + 3*curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
						if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y):
							self.isSelected = False
							return 
						self.x +=2
						self.isBeginning = False
						self.isSelected = False
						board.rePosition(self.x - 2, self.y, self.x, self.y)
						return 
					else:
						if newPos[1] >= curr.get('y') + curr.get('h') and newPos[1] <= curr.get('y') + 2*curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
							if board.isOccupied(self.x + 1, self.y):
								self.isSelected = False
								return 
							self.x += 1
							self.isBeginning = False
							self.isSelected = False
							board.rePosition(self.x - 1, self.y, self.x, self.y)
							return 
				else:
					if newPos[1] >= curr.get('y') + curr.get('h') and newPos[1] <= curr.get('y') + 2*curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
						if board.isOccupied(self.x + 1, self.y):
							self.isSelected = False
							return 
						self.x += 1
						self.isSelected = False
						board.rePosition(self.x - 1, self.y, self.x, self.y)
						return 
			else:
				return 
		elif self.image == "whitepawn.png":
			if self.isValid(newPos):
				if self.isBeginning: 
					if newPos[1] <= curr.get('y') - curr.get('h') and newPos[1] >= curr.get('y') - 2*curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
						if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y):
							self.isSelected = False
							return 
						self.x -=2
						self.isBeginning = False
						self.isSelected = False
						board.rePosition(self.x + 2, self.y, self.x, self.y)
						return 
					else:
						if newPos[1] <= curr.get('y') and newPos[1] >= curr.get('y') - curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
							if board.isOccupied(self.x - 1, self.y):
								self.isSelected = False
								return 
							self.x -=1
							self.isBeginning = False
							self.isSelected = False
							board.rePosition(self.x + 1, self.y, self.x, self.y)
							return 
				else:
					if newPos[1] <= curr.get('y') and newPos[1] >= curr.get('y') - curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
						if board.isOccupied(self.x - 1, self.y):
							self.isSelected = False
							return 
						self.x -= 1
						self.isSelected = False
						board.rePosition(self.x + 1, self.y, self.x, self.y)
						return
			else:
				return 
		else:
			print("Your code is broken")
			return False
	def isValid(self, newPos):
		if not self.isSelected:
			print(newPos)
			return False
		#add case where pawn can move up to two spaces in front if its in starting position
		else:
			return True
	def canEat(self, piece, board):
		if piece.image == "blackking.png" or piece.image == "whiteking.png":
			return False
		if self.getColor() == "black":
			pos = self.getPosition(self.x + 1, self.y - 1)
			pos2 = self.getPosition(self.x + 1, self.y + 1)
			piecePos = self.getPosition(piece.x, piece.y)
			if pos == piecePos or pos2 == piecePos:
				return True
			else:
				return False
		else:
			pos = self.getPosition(self.x - 1, self.y + 1)
			pos2 = self.getPosition(self.x - 1, self.y - 1)
			piecePos = self.getPosition(piece.x, piece.y)
			if pos == piecePos or pos2 == piecePos:
				return True
			else:
				return False
class King(Piece):
	def move(self, newPos, board):
		if self.isValid(newPos):
			curr = self.getPosition(self.x, self.y)
			if newPos[1] >= curr.get('y') + curr.get('h') and newPos[1] <= curr.get('y') + 2*curr.get('h') and newPos[0] >= curr.get('x') + curr.get('w') and newPos[0] <= curr.get('x') + 2*curr.get('w'):
				if board.isOccupied(self.x + 1, self.y + 1):
					self.isSelected = False
					return
				self.x +=1
				self.y += 1
				board.rePosition(self.x - 1, self.y - 1, self.x, self.y)
				self.isSelected = False
				return
			if newPos[1] >= curr.get('y') + curr.get('h') and newPos[1] <= curr.get('y') + 2*curr.get('h') and newPos[0] <= curr.get('x') and newPos[0] >= curr.get('x') - curr.get('w'):
				if board.isOccupied(self.x + 1, self.y - 1):
					self.isSelected = False
					return
				self.x +=1
				self.y -= 1
				board.rePosition(self.x - 1, self.y + 1, self.x, self.y)
				self.isSelected = False
				return
			if newPos[1] <= curr.get('y') and newPos[1] >= curr.get('y') - curr.get('h') and newPos[0] >= curr.get('x') + curr.get('w') and newPos[0] <= curr.get('x') + 2*curr.get('w'):
				if board.isOccupied(self.x - 1, self.y + 1):
					self.isSelected = False
					return
				self.x -=1
				self.y += 1
				board.rePosition(self.x + 1, self.y - 1, self.x, self.y)
				self.isSelected = False
				return
			if newPos[1] <= curr.get('y') and newPos[1] >= curr.get('y') - curr.get('h') and newPos[0] <= curr.get('x') and newPos[0] >= curr.get('x') - curr.get('w'):
				if board.isOccupied(self.x - 1, self.y - 1):
					self.isSelected = False
					return
				self.x -=1
				self.y -= 1
				board.rePosition(self.x + 1, self.y + 1, self.x, self.y)
				self.isSelected = False
				return
			if newPos[1] >= curr.get('y') + curr.get('h') and newPos[1] <= curr.get('y') + 2*curr.get('h'):
				if board.isOccupied(self.x + 1, self.y):
					self.isSelected = False
					return 
				self.x +=1
				board.rePosition(self.x - 1, self.y, self.x, self.y)
			if newPos[1] <= curr.get('y') and newPos[1] >= curr.get('y') - curr.get('h'):
				if board.isOccupied(self.x - 1, self.y):
					self.isSelected = False
					return 
				self.x -=1
				board.rePosition(self.x + 1, self.y, self.x, self.y)
			if newPos[0] >= curr.get('x') + curr.get('w') and newPos[0] <= curr.get('x') + 2*curr.get('w'):
				if board.isOccupied(self.x, self.y + 1):
					self.isSelected = False
					return 
				self.y += 1
				board.rePosition(self.x, self.y - 1, self.x, self.y)
			if newPos[0] <= curr.get('x') and newPos[0] >= curr.get('x') - curr.get('w'):
				if board.isOccupied(self.x, self.y - 1):
					self.isSelected = False
					return
				self.y -=1
				board.rePosition(self.x, self.y + 1, self.x, self.y)

		self.isSelected = False
		return 
	def isValid(self, newPos):
		return True
	def canEat(self, piece, board):
		if piece.image == "blackking.png" or piece.image == "whiteking.png":
			return False
		newPos = self.getPosition(piece.x, piece.y)
		curr = self.getPosition(self.x, self.y)
		if newPos.get('y') >= curr.get('y') + curr.get('h') and newPos.get('y') <= curr.get('y') + 2*curr.get('h'):
			return True
		if newPos.get('y') <= curr.get('y') and newPos.get('y') >= curr.get('y') - curr.get('h'):
			return True
		if newPos.get('x') >= curr.get('x') + curr.get('w') and newPos.get('x') <= curr.get('x') + 2*curr.get('w'):
			return True
		if newPos.get('x') <= curr.get('x') and newPos.get('x') >= curr.get('x') - curr.get('w'):
			return True
		return False
class Queen(Piece):
	def move(self, newPos, board):
		return
	def isValid(self, newPos):
		return True 
	def canEat(self, piece, board):
		if piece.image == "blackking.png" or piece.image == "whiteking.png":
			return False
		return True
class Bishop(Piece):
    def move(self, newPos, board):
    	if self.isValid(newPos):
    		tempx = self.x
    		tempy = self.y
    		possiblex = list()
    		possibley = list()
    		while tempx < 7 and tempy < 7:
    			possiblex.append(tempx + 1)
    			possibley.append(tempy + 1)
    			tempx+=1
    			tempy+=1
    		tempx = self.x
    		tempy = self.y
    		while tempx > 0 and tempy < 7:
    			possiblex.append(tempx - 1)
    			possibley.append(tempy + 1)
    			tempx-=1
    			tempy +=1
    		tempx = self.x
    		tempy = self.y
    		while tempx > 0 and tempy > 0:
    			possiblex.append(tempx - 1)
    			possibley.append(tempy - 1)
    			tempx -=1
    			tempy -=1
    		tempx = self.x
    		tempy = self.y
    		while tempx < 7 and tempy > 0:
    			possiblex.append(tempx + 1)
    			possibley.append(tempy - 1)
    			tempx +=1
    			tempy -=1
    		for x,y in zip(possiblex, possibley):
    			curr = self.getPosition(x, y)
    			if newPos[0] <= curr.get('x') + curr.get('w') and newPos[0] >= curr.get('x') and newPos[1] <= curr.get('y') + curr.get('h') and newPos[1] >= curr.get('y'):
    				self.x = x
    				self.y = y
    	self.isSelected = False
    	return 
    def isValid(self, newPos):
    	return True
    def canEat(self, piece, board):
    	if piece.image == "blackking.png" or piece.image == "whiteking.png":
    		return False
    	newPos = self.getPosition(piece.x, piece.y)
    	tempx = self.x
    	tempy = self.y
    	possiblex = list()
    	possibley = list()
    	while tempx < 7 and tempy < 7:
    		possiblex.append(tempx + 1)
    		possibley.append(tempy + 1)
    		tempx+=1
    		tempy+=1
    	tempx = self.x
    	tempy = self.y
    	while tempx > 0 and tempy < 7:
    		possiblex.append(tempx - 1)
    		possibley.append(tempy + 1)
    		tempx-=1
    		tempy +=1
    	tempx = self.x
    	tempy = self.y
    	while tempx > 0 and tempy > 0:
    		possiblex.append(tempx - 1)
    		possibley.append(tempy - 1)
    		tempx -=1
    		tempy -=1
    	tempx = self.x
    	tempy = self.y
    	while tempx < 7 and tempy > 0:
    		possiblex.append(tempx + 1)
    		possibley.append(tempy - 1)
    		tempx +=1
    		tempy -=1
    	for x,y in zip(possiblex, possibley):
    		curr = self.getPosition(x, y)
    		if newPos.get('x') <= curr.get('x') + curr.get('w') and newPos.get('x') >= curr.get('x') and newPos.get('y') <= curr.get('y') + curr.get('h') and newPos.get('y') >= curr.get('y'):
    			return True
    	return False
class Knight(Piece):
	def move(self, newPos, board):
		if self.isValid(newPos):
			possiblex = list()
			possibley = list()
			if not self.x + 2 > 7 and not self.y + 1 > 7:
				possiblex.append(self.x + 2)
				possibley.append(self.y + 1)
			if not self.x + 2 > 7 and not self.y - 1 < 0:
				possiblex.append(self.x + 2)
				possibley.append(self.y - 1)
			if not self.x - 2 < 0 and not self.y + 1 > 7:
				possiblex.append(self.x - 2)
				possibley.append(self.y + 1)
			if not self.x - 2 < 0 and not self.y - 1 < 0:
				possiblex.append(self.x - 2)
				possibley.append(self.y - 1)
			if not self.y + 2 > 7 and not self.x + 1 > 7:
				possiblex.append(self.x + 1)
				possibley.append(self.y + 2)
			if not self.y + 2 > 7 and not self.x - 1 < 0:
				possiblex.append(self.x - 1)
				possibley.append(self.y + 2)
			if not self.y - 2 < 0 and not self.x + 1 > 7:
				possiblex.append(self.x + 1)
				possibley.append(self.y - 2)
			if not self.y - 2 < 0 and not self.x - 1 < 0:
				possiblex.append(self.x - 1)
				possibley.append(self.y - 2)
			for x,y in zip(possiblex, possibley):
				curr = self.getPosition(x,y)
				if newPos[0] <= curr.get('x') + curr.get('w') and newPos[0] >= curr.get('x') and newPos[1] <= curr.get('y') + curr.get('h') and newPos[1] >= curr.get('y'):
					self.x = x
					self.y = y
			self.isSelected = False
			return 
	def isValid(self, newPos):
		return True
	def canEat(self, piece, board):
		if piece.image == "blackking.png" or piece.image == "whiteking.png":
			return False
		return True
class Rook(Piece):
	def move(self, newPos, board):
		if self.isValid(newPos):
			curr = self.getPosition(self.x, self.y)
			if newPos[1] >= curr.get('y') + curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
				if newPos[1] <= curr.get('y') + 2*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y):
						self.isSelected = False
						return
					self.x +=1
					board.rePosition(self.x - 1, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 3*curr.get('h'):
					if board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 1, self.y):
						self.isSelected = False
						return
					self.x += 2
					board.rePosition(self.x - 2, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 4*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y):
						self.isSelected = False
						return
					self.x += 3
					board.rePosition(self.x - 3, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 5*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y):
						self.isSelected = False
						return
					self.x += 4
					board.rePosition(self.x - 4, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 6*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y):
						self.isSelected = False
						return 
					self.x += 5
					board.rePosition(self.x - 5, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 7*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y) or board.isOccupied(self.x + 6, self.y):
						self.isSelected = False
						return 
					self.x += 6
					board.rePosition(self.x - 6, self.y, self.x, self.y)
				elif newPos[1] <= curr.get('y') + 8*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y) or board.isOccupied(self.x + 6, self.y) or board.isOccupied(self.x + 7, self.y):
						self.isSelected = False
						return 
					self.x += 7	
					board.rePosition(self.x - 7, self.y, self.x, self.y)
			elif newPos[1] <= curr.get('y') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
				if newPos[1] >= curr.get('y') - curr.get('h'):
					if board.isOccupied(self.x - 1, self.y):
						self.isSelected = False
						return
					self.x -=1
					board.rePosition(self.x + 1, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 2*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y):
						self.isSelected = False
						return
					self.x -=2
					board.rePosition(self.x + 2, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 3*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y):
						self.isSelected = False
						return
					self.x -=3
					board.rePosition(self.x + 3, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 4*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y):
						self.isSelected = False
						return
					self.x -=4
					board.rePosition(self.x + 4, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 5*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y):
						self.isSelected = False
						return
					self.x -=5
					board.rePosition(self.x + 5, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 6*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y) or board.isOccupied(self.x - 6, self.y):
						return
					self.x -=6
					board.rePosition(self.x + 6, self.y, self.x, self.y)
				elif newPos[1] >= curr.get('y') - 7*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y) or board.isOccupied(self.x - 6, self.y) or board.isOccupied(self.x - 7, self.y):
						return
					self.x -=7
					board.rePosition(self.x + 7, self.y, self.x, self.y)
			elif newPos[0] <= curr.get('x') and not newPos[1] <= curr.get('y') and not newPos[1] >= curr.get('y') + curr.get('h'):
				if newPos[0] >= curr.get('x') - curr.get('w'):
					if board.isOccupied(self.x, self.y - 1):
						self.isSelected = False
						return
					self.y -=1
					board.rePosition(self.x, self.y + 1, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 2*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2):
						self.isSelected = False
						return
					self.y -=2
					board.rePosition(self.x, self.y + 2, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 3*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3):
						self.isSelected = False
						return
					self.y -=3
					board.rePosition(self.x, self.y + 3, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 4*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4):
						self.isSelected = False
						return
					self.y -=4
					board.rePosition(self.x, self.y + 4, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 5*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5):
						self.isSelected = False
						return
					self.y -=5
					board.rePosition(self.x, self.y + 5, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 6*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5) or board.isOccupied(self.x, self.y - 6):
						self.isSelected = False
						return
					self.y -=6
					board.rePosition(self.x, self.y + 6, self.x, self.y)
				elif newPos[0] >= curr.get('x') - 7*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5) or board.isOccupied(self.x, self.y - 6) or board.isOccupied(self.x, self.y - 7):
						self.isSelected = False
						return
					self.y -=7
					board.rePosition(self.x, self.y + 7, self.x, self.y)
			elif newPos[0] >= curr.get('x') + curr.get('w') and not newPos[1] <= curr.get('y') and not newPos[1] >= curr.get('y') + curr.get('h'):
				if newPos[0] <= curr.get('x') + 2*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1):
						self.isSelected = False
						return
					self.y +=1
					board.rePosition(self.x, self.y - 1, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 3*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2):
						self.isSelected = False
						return
					self.y +=2
					board.rePosition(self.x, self.y - 2, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 4*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3):
						self.isSelected = False
						return
					self.y +=3
					board.rePosition(self.x, self.y - 3, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 5*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4):
						self.isSelected = False
						return
					self.y +=4
					board.rePosition(self.x, self.y - 4, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 6*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5):
						self.isSelected = False
						return
					self.y +=5
					board.rePosition(self.x, self.y - 5, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 7*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5) or board.isOccupied(self.x, self.y + 6):
						self.isSelected = False
						return
					self.y +=6
					board.rePosition(self.x, self.y - 6, self.x, self.y)
				elif newPos[0] <= curr.get('x') + 8*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5) or board.isOccupied(self.x, self.y + 6) or board.isOccupied(self.x, self.y + 7):
						self.isSelected = False
						return
					self.y +=7
					board.rePosition(self.x, self.y - 7, self.x, self.y)
		self.isSelected = False
		return 
	def isValid(self, newPos):
		return True
	def canEat(self, piece, board):
		curr = self.getPosition(self.x, self.y)	
		newPos = self.getPosition(piece.x, piece.y)
		if piece.image == "blackking.png" or piece.image == "whiteking.png":
			return False
		else:
			if newPos[1] >= curr.get('y') + curr.get('h') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
				if newPos[1] <= curr.get('y') + 2*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] <= curr.get('y') + 3*curr.get('h'):
					if board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 1, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] <= curr.get('y') + 4*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] <= curr.get('y') + 5*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] <= curr.get('y') + 6*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y):
						self.isSelected = False
						return  False
					return True
				elif newPos[1] <= curr.get('y') + 7*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y) or board.isOccupied(self.x + 6, self.y):
						self.isSelected = False
						return  False
					return True
				elif newPos[1] <= curr.get('y') + 8*curr.get('h'):
					if board.isOccupied(self.x + 1, self.y) or board.isOccupied(self.x + 2, self.y) or board.isOccupied(self.x + 3, self.y) or board.isOccupied(self.x + 4, self.y) or board.isOccupied(self.x + 5, self.y) or board.isOccupied(self.x + 6, self.y) or board.isOccupied(self.x + 7, self.y):
						self.isSelected = False
						return  False
					return True	
			elif newPos[1] <= curr.get('y') and not newPos[0] <= curr.get('x') and not newPos[0] >= curr.get('x') + curr.get('w'):
				if newPos[1] >= curr.get('y') - curr.get('h'):
					if board.isOccupied(self.x - 1, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] >= curr.get('y') - 2*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] >= curr.get('y') - 3*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] >= curr.get('y') - 4*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] >= curr.get('y') - 5*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y):
						self.isSelected = False
						return False
					return True
				elif newPos[1] >= curr.get('y') - 6*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y) or board.isOccupied(self.x - 6, self.y):
						return
					return True
				elif newPos[1] >= curr.get('y') - 7*curr.get('h'):
					if board.isOccupied(self.x - 1, self.y) or board.isOccupied(self.x - 2, self.y) or board.isOccupied(self.x - 3, self.y) or board.isOccupied(self.x - 4, self.y) or board.isOccupied(self.x - 5, self.y) or board.isOccupied(self.x - 6, self.y) or board.isOccupied(self.x - 7, self.y):
						return
					return True
			elif newPos[0] <= curr.get('x') and not newPos[1] <= curr.get('y') and not newPos[1] >= curr.get('y') + curr.get('h'):
				if newPos[0] >= curr.get('x') - curr.get('w'):
					if board.isOccupied(self.x, self.y - 1):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 2*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 3*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 4*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 5*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 6*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5) or board.isOccupied(self.x, self.y - 6):
						self.isSelected = False
						return False
					return True
				elif newPos[0] >= curr.get('x') - 7*curr.get('w'):
					if board.isOccupied(self.x, self.y - 1) or board.isOccupied(self.x, self.y - 2) or board.isOccupied(self.x, self.y - 3) or board.isOccupied(self.x, self.y - 4) or board.isOccupied(self.x, self.y - 5) or board.isOccupied(self.x, self.y - 6) or board.isOccupied(self.x, self.y - 7):
						self.isSelected = False
						return False
					return True
			elif newPos[0] >= curr.get('x') + curr.get('w') and not newPos[1] <= curr.get('y') and not newPos[1] >= curr.get('y') + curr.get('h'):
				if newPos[0] <= curr.get('x') + 2*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 3*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 4*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 5*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 6*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 7*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5) or board.isOccupied(self.x, self.y + 6):
						self.isSelected = False
						return False
					return True
				elif newPos[0] <= curr.get('x') + 8*curr.get('w'):
					if board.isOccupied(self.x, self.y + 1) or board.isOccupied(self.x, self.y + 2) or board.isOccupied(self.x, self.y + 3) or board.isOccupied(self.x, self.y + 4) or board.isOccupied(self.x, self.y + 5) or board.isOccupied(self.x, self.y + 6) or board.isOccupied(self.x, self.y + 7):
						self.isSelected = False
						return False
					return True
