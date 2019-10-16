#Author: Nathanael Shim
#The board will be reduced to a matrix (double array) with each element holding a dict which maps 
#coordinates to their respective values (ex. {x: 0, y: 0, w: 0, h: 0})

###MATRIX###
# [[{A8}, {B8}, {C8}, {D8}, {E8}, {F8}, {G8}, {H8}],
#  [{A7}, {B7}, {C7}, {D7}, {E7}, {F7}, {G7}, {H7}],
#  [{A6}, {B6}, {C6}, {D6}, {E6}, {F6}, {G6}, {H6}],
#  [{A5}, {B5}, {C5}, {D5}, {E5}, {F5}, {G5}, {H5}],
#  [{A4}, {B4}, {C4}, {D4}, {E4}, {F4}, {G4}, {H4}],
#  [{A3}, {B3}, {C3}, {D3}, {E3}, {F3}, {G3}, {H3}],
#  [{A2}, {B2}, {C2}, {D2}, {E2}, {F2}, {G2}, {H2}],
#  [{A1}, {B1}, {C1}, {D1}, {E1}, {F1}, {G1}, {H1}]]
import sys, pygame
from Piece import Piece,Pawn, King, Queen, Bishop, Knight, Rook
from Board import Board
pygame.init()
size = width, height = 500, 500
black = 0, 255, 255
screen = pygame.display.set_mode(size)
board = Board()
board_img = pygame.image.load("board.gif")
board_img = pygame.transform.scale(board_img, (500, 500))

blackPawn0 = Pawn("blackpawn.png", 1, 0, False, True, "black")
pawnImage0 = pygame.image.load(blackPawn0.getImage())
pawnImage0 = pygame.transform.scale(pawnImage0, (50,50))
board.update(1,0,True)

blackPawn1 = Pawn("blackpawn.png", 1, 1, False, True, "black")
pawnImage1 = pygame.image.load(blackPawn1.getImage())
pawnImage1 = pygame.transform.scale(pawnImage1, (50,50))
board.update(1,1,True)

blackPawn2 = Pawn("blackpawn.png", 1, 2, False, True, "black")
pawnImage2 = pygame.image.load(blackPawn2.getImage())
pawnImage2 = pygame.transform.scale(pawnImage2, (50,50))
board.update(1,2,True)

blackPawn3 = Pawn("blackpawn.png", 1, 3, False, True, "black")
pawnImage3 = pygame.image.load(blackPawn3.getImage())
pawnImage3 = pygame.transform.scale(pawnImage3, (50,50))
board.update(1,3,True)

blackPawn4 = Pawn("blackpawn.png", 1, 4, False, True, "black")
pawnImage4 = pygame.image.load(blackPawn4.getImage())
pawnImage4 = pygame.transform.scale(pawnImage4, (50,50))
board.update(1,4,True)

blackPawn5 = Pawn("blackpawn.png", 1, 5, False, True, "black")
pawnImage5 = pygame.image.load(blackPawn5.getImage())
pawnImage5 = pygame.transform.scale(pawnImage5, (50,50))
board.update(1,5,True)

blackPawn6 = Pawn("blackpawn.png", 1, 6, False, True, "black")
pawnImage6 = pygame.image.load(blackPawn6.getImage())
pawnImage6 = pygame.transform.scale(pawnImage6, (50,50))
board.update(1,6,True)

blackPawn7 = Pawn("blackpawn.png", 1, 7, False, True, "black")
pawnImage7 = pygame.image.load(blackPawn7.getImage())
pawnImage7 = pygame.transform.scale(pawnImage7, (50,50))
board.update(1,7,True)

whitePawn0 = Pawn("whitepawn.png", 6, 0, False, True, "white")
whitePawnImage0 = pygame.image.load(whitePawn0.getImage())
whitePawnImage0 = pygame.transform.scale(whitePawnImage0, (50,50))
board.update(6,0,True)

whitePawn1 = Pawn("whitepawn.png", 6, 1, False, True, "white")
whitePawnImage1 = pygame.image.load(whitePawn1.getImage())
whitePawnImage1 = pygame.transform.scale(whitePawnImage1, (50,50))
board.update(6,1,True)

whitePawn2 = Pawn("whitepawn.png", 6, 2, False, True, "white")
whitePawnImage2 = pygame.image.load(whitePawn2.getImage())
whitePawnImage2 = pygame.transform.scale(whitePawnImage2, (50,50))
board.update(6,2,True)

whitePawn3 = Pawn("whitepawn.png", 6, 3, False, True, "white")
whitePawnImage3 = pygame.image.load(whitePawn3.getImage())
whitePawnImage3 = pygame.transform.scale(whitePawnImage3, (50,50))
board.update(6,3,True)

whitePawn4 = Pawn("whitepawn.png", 6, 4, False, True, "white")
whitePawnImage4 = pygame.image.load(whitePawn4.getImage())
whitePawnImage4 = pygame.transform.scale(whitePawnImage4, (50,50))
board.update(6,4,True)

whitePawn5 = Pawn("whitepawn.png", 6, 5, False, True, "white")
whitePawnImage5 = pygame.image.load(whitePawn5.getImage())
whitePawnImage5 = pygame.transform.scale(whitePawnImage5, (50,50))
board.update(6,5,True)

whitePawn6 = Pawn("whitepawn.png", 6, 6, False, True, "white")
whitePawnImage6 = pygame.image.load(whitePawn6.getImage())
whitePawnImage6 = pygame.transform.scale(whitePawnImage6, (50,50))
board.update(6,6,True)

whitePawn7 = Pawn("whitepawn.png", 6, 7, False, True, "white")
whitePawnImage7 = pygame.image.load(whitePawn7.getImage())
whitePawnImage7 = pygame.transform.scale(whitePawnImage7, (50,50))
board.update(6,7,True)

blackKing = King("blackking.png",0, 4, False, True, "black")
blackKingImage = pygame.image.load(blackKing.getImage())
blackKingImage = pygame.transform.scale(blackKingImage, (50,50))
board.update(0,4,True)

blackQueen = Queen("blackqueen.png", 0, 3, False, True, "black")
blackQueenImage = pygame.image.load(blackQueen.getImage())
blackQueenImage = pygame.transform.scale(blackQueenImage, (50, 50))
board.update(0,3,True)

whiteKing = King("whiteking.png",7, 4, False, True, "white")
whiteKingImage = pygame.image.load(whiteKing.getImage())
whiteKingImage = pygame.transform.scale(whiteKingImage, (50,50))
board.update(7,4,True)

whiteQueen = Queen("whitequeen.png", 7, 3, False, True, "white")
whiteQueenImage = pygame.image.load(whiteQueen.getImage())
whiteQueenImage = pygame.transform.scale(whiteQueenImage, (50, 50))
board.update(7,3,True)

blackBishopL = Bishop("blackbishop.png",0, 2, False, True, "black")
blackBishopLImage = pygame.image.load(blackBishopL.getImage())
blackBishopLImage = pygame.transform.scale(blackBishopLImage, (50,50))
board.update(0,2,True)

blackBishopR = Bishop("blackbishop.png", 0,5,False,True,"black")
blackBishopRImage = pygame.image.load(blackBishopR.getImage())
blackBishopRImage = pygame.transform.scale(blackBishopRImage, (50,50))
board.update(0,5,True)

blackKnightL = Knight("blackknight.png", 0,1,False,True,"black")
blackKnightLImage = pygame.image.load(blackKnightL.getImage())
blackKnightLImage = pygame.transform.scale(blackKnightLImage, (50,50))
board.update(0,1,True)

blackKnightR = Knight("blackknight.png", 0,6,False,True,"black")
blackKnightRImage = pygame.image.load(blackKnightR.getImage())
blackKnightRImage = pygame.transform.scale(blackKnightRImage, (50,50))
board.update(0,6,True)

blackRookL = Rook("blackrook.png", 0,0,False,True,"black")
blackRookLImage = pygame.image.load(blackRookL.getImage())
blackRookLImage = pygame.transform.scale(blackRookLImage, (50,50))
board.update(0,0,True)

blackRookR = Rook("blackrook.png", 0,7,False,True,"black")
blackRookRImage = pygame.image.load(blackRookR.getImage())
blackRookRImage = pygame.transform.scale(blackRookRImage, (50,50))
board.update(0,7,True)

whiteBishopL = Bishop("whitebishop.png",7, 2, False, True, "white")
whiteBishopLImage = pygame.image.load(whiteBishopL.getImage())
whiteBishopLImage = pygame.transform.scale(whiteBishopLImage, (50,50))
board.update(7,2,True)

whiteBishopR = Bishop("whitebishop.png", 7,5,False,True,"white")
whiteBishopRImage = pygame.image.load(whiteBishopR.getImage())
whiteBishopRImage = pygame.transform.scale(whiteBishopRImage, (50,50))
board.update(7,5,True)

whiteKnightL = Knight("whiteknight.png", 7,1,False,True,"white")
whiteKnightLImage = pygame.image.load(whiteKnightL.getImage())
whiteKnightLImage = pygame.transform.scale(whiteKnightLImage, (50,50))
board.update(7,1,True)

whiteKnightR = Knight("whiteknight.png", 7,6,False,True,"white")
whiteKnightRImage = pygame.image.load(whiteKnightR.getImage())
whiteKnightRImage = pygame.transform.scale(whiteKnightRImage, (50,50))
board.update(7,6,True)

whiteRookL = Rook("whiterook.png", 7,0,False,True,"white")
whiteRookLImage = pygame.image.load(whiteRookL.getImage())
whiteRookLImage = pygame.transform.scale(whiteRookLImage, (50,50))
board.update(7,0,True)

whiteRookR = Rook("whiterook.png", 7,7,False,True,"white")
whiteRookRImage = pygame.image.load(whiteRookR.getImage())
whiteRookRImage = pygame.transform.scale(whiteRookRImage, (50,50))
board.update(7,7,True)


selectedPiece = None
gameDisplay = pygame.display.set_mode((width, height))
def select(piece, selectedPiece):
	piece.select()
	if piece.isSelected:
		selectedPiece = piece
	else:
		selectedPiece = None
	print(selectedPiece)
	return selectedPiece

while 1:
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.MOUSEBUTTONUP: 
			pos = pygame.mouse.get_pos()
			pawn0Rect = None
			if blackPawn0:
				pawn0Rect = pawnImage0.get_rect()
				pawn0Rect.x = board.get(blackPawn0.x, blackPawn0.y).get('x')
				pawn0Rect.y = board.get(blackPawn0.x,blackPawn0.y).get('y')
				pawn0Rect.width = board.get(blackPawn0.x,blackPawn0.y).get('w')
				pawn0Rect.height = board.get(blackPawn0.x,blackPawn0.y).get('h')
			pawn1Rect = None
			if blackPawn1:	
				pawn1Rect = pawnImage1.get_rect()
				pawn1Rect.x = board.get(blackPawn1.x, blackPawn1.y).get('x')
				pawn1Rect.y = board.get(blackPawn1.x,blackPawn1.y).get('y')
				pawn1Rect.width = board.get(blackPawn1.x,blackPawn1.y).get('w')
				pawn1Rect.height = board.get(blackPawn1.x,blackPawn1.y).get('h')
			pawn2Rect = None
			if blackPawn2:
				pawn2Rect = pawnImage2.get_rect()
				pawn2Rect.x = board.get(blackPawn2.x, blackPawn2.y).get('x')
				pawn2Rect.y = board.get(blackPawn2.x,blackPawn2.y).get('y')
				pawn2Rect.width = board.get(blackPawn2.x,blackPawn2.y).get('w')
				pawn2Rect.height = board.get(blackPawn2.x,blackPawn2.y).get('h')
			pawn3Rect = None
			if blackPawn3:
				pawn3Rect = pawnImage3.get_rect()
				pawn3Rect.x = board.get(blackPawn3.x, blackPawn3.y).get('x')
				pawn3Rect.y = board.get(blackPawn3.x,blackPawn3.y).get('y')
				pawn3Rect.width = board.get(blackPawn3.x,blackPawn3.y).get('w')
				pawn3Rect.height = board.get(blackPawn3.x,blackPawn3.y).get('h')
			pawn4Rect = None
			if blackPawn4:
				pawn4Rect = pawnImage4.get_rect()
				pawn4Rect.x = board.get(blackPawn4.x, blackPawn4.y).get('x')
				pawn4Rect.y = board.get(blackPawn4.x,blackPawn4.y).get('y')
				pawn4Rect.width = board.get(blackPawn4.x,blackPawn4.y).get('w')
				pawn4Rect.height = board.get(blackPawn4.x,blackPawn4.y).get('h')
			pawn5Rect = None
			if blackPawn5:
				pawn5Rect = pawnImage5.get_rect()
				pawn5Rect.x = board.get(blackPawn5.x, blackPawn5.y).get('x')
				pawn5Rect.y = board.get(blackPawn5.x,blackPawn5.y).get('y')
				pawn5Rect.width = board.get(blackPawn5.x,blackPawn5.y).get('w')
				pawn5Rect.height = board.get(blackPawn5.x,blackPawn5.y).get('h')
			pawn6Rect = None
			if blackPawn6:
				pawn6Rect = pawnImage6.get_rect()
				pawn6Rect.x = board.get(blackPawn6.x, blackPawn6.y).get('x')
				pawn6Rect.y = board.get(blackPawn6.x,blackPawn6.y).get('y')
				pawn6Rect.width = board.get(blackPawn6.x,blackPawn6.y).get('w')
				pawn6Rect.height = board.get(blackPawn6.x,blackPawn6.y).get('h')
			pawn7Rect = None
			if blackPawn7:
				pawn7Rect = pawnImage7.get_rect()
				pawn7Rect.x = board.get(blackPawn7.x, blackPawn7.y).get('x')
				pawn7Rect.y = board.get(blackPawn7.x,blackPawn7.y).get('y')
				pawn7Rect.width = board.get(blackPawn7.x,blackPawn7.y).get('w')
				pawn7Rect.height = board.get(blackPawn7.x,blackPawn7.y).get('h')
			wpawn0Rect = None
			if whitePawn0:
				wpawn0Rect = whitePawnImage0.get_rect()
				wpawn0Rect.x = board.get(whitePawn0.x, whitePawn0.y).get('x')
				wpawn0Rect.y = board.get(whitePawn0.x,whitePawn0.y).get('y')
				wpawn0Rect.width = board.get(whitePawn0.x,whitePawn0.y).get('w')
				wpawn0Rect.height = board.get(whitePawn0.x,whitePawn0.y).get('h')
			wpawn1Rect = None
			if whitePawn1:
				wpawn1Rect = whitePawnImage1.get_rect()
				wpawn1Rect.x = board.get(whitePawn1.x, whitePawn1.y).get('x')
				wpawn1Rect.y = board.get(whitePawn1.x,whitePawn1.y).get('y')
				wpawn1Rect.width = board.get(whitePawn1.x,whitePawn1.y).get('w')
				wpawn1Rect.height = board.get(whitePawn1.x,whitePawn1.y).get('h')
			wpawn2Rect = None
			if whitePawn2:
				wpawn2Rect = whitePawnImage2.get_rect()
				wpawn2Rect.x = board.get(whitePawn2.x, whitePawn2.y).get('x')
				wpawn2Rect.y = board.get(whitePawn2.x,whitePawn2.y).get('y')
				wpawn2Rect.width = board.get(whitePawn2.x,whitePawn2.y).get('w')
				wpawn2Rect.height = board.get(whitePawn2.x,whitePawn2.y).get('h')
			wpawn3Rect = None
			if whitePawn3:
				wpawn3Rect = whitePawnImage3.get_rect()
				wpawn3Rect.x = board.get(whitePawn3.x, whitePawn3.y).get('x')
				wpawn3Rect.y = board.get(whitePawn3.x,whitePawn3.y).get('y')
				wpawn3Rect.width = board.get(whitePawn3.x,whitePawn3.y).get('w')
				wpawn3Rect.height = board.get(whitePawn3.x,whitePawn3.y).get('h')
			wpawn4Rect = None
			if whitePawn4:
				wpawn4Rect = whitePawnImage4.get_rect()
				wpawn4Rect.x = board.get(whitePawn4.x, whitePawn4.y).get('x')
				wpawn4Rect.y = board.get(whitePawn4.x,whitePawn4.y).get('y')
				wpawn4Rect.width = board.get(whitePawn4.x,whitePawn4.y).get('w')
				wpawn4Rect.height = board.get(whitePawn4.x,whitePawn4.y).get('h')
			wpawn5Rect = None
			if whitePawn5:
				wpawn5Rect = whitePawnImage5.get_rect()
				wpawn5Rect.x = board.get(whitePawn5.x, whitePawn5.y).get('x')
				wpawn5Rect.y = board.get(whitePawn5.x,whitePawn5.y).get('y')
				wpawn5Rect.width = board.get(whitePawn5.x,whitePawn5.y).get('w')
				wpawn5Rect.height = board.get(whitePawn5.x,whitePawn5.y).get('h')
			wpawn6Rect = None
			if whitePawn6:
				wpawn6Rect = whitePawnImage6.get_rect()
				wpawn6Rect.x = board.get(whitePawn6.x, whitePawn6.y).get('x')
				wpawn6Rect.y = board.get(whitePawn6.x,whitePawn6.y).get('y')
				wpawn6Rect.width = board.get(whitePawn6.x,whitePawn6.y).get('w')
				wpawn6Rect.height = board.get(whitePawn6.x,whitePawn6.y).get('h')
			wpawn7Rect = None
			if whitePawn7:
				wpawn7Rect = whitePawnImage7.get_rect()
				wpawn7Rect.x = board.get(whitePawn7.x, whitePawn7.y).get('x')
				wpawn7Rect.y = board.get(whitePawn7.x,whitePawn7.y).get('y')
				wpawn7Rect.width = board.get(whitePawn7.x,whitePawn7.y).get('w')
				wpawn7Rect.height = board.get(whitePawn7.x,whitePawn7.y).get('h')

			blackKingRect = blackKingImage.get_rect()
			blackKingRect.x = board.get(blackKing.x, blackKing.y).get('x')
			blackKingRect.y = board.get(blackKing.x, blackKing.y).get('y')
			blackKingRect.width = board.get(blackKing.x, blackKing.y).get('w')
			blackKingRect.height = board.get(blackKing.x, blackKing.y).get('h')

			whiteKingRect = whiteKingImage.get_rect()
			whiteKingRect.x = board.get(whiteKing.x, whiteKing.y).get('x')
			whiteKingRect.y = board.get(whiteKing.x, whiteKing.y).get('y')
			whiteKingRect.width = board.get(whiteKing.x, whiteKing.y).get('w')
			whiteKingRect.height = board.get(whiteKing.x, whiteKing.y).get('h')
			blackRookLRect = None
			if blackRookL:	
				blackRookLRect = blackRookLImage.get_rect()
				blackRookLRect.x = board.get(blackRookL.x, blackRookL.y).get('x')
				blackRookLRect.y = board.get(blackRookL.x, blackRookL.y).get('y')
				blackRookLRect.width = board.get(blackRookL.x, blackRookL.y).get('w')
				blackRookLRect.height = board.get(blackRookL.x, blackRookL.y).get('h')	
			blackRookRRect = None
			if blackRookR:
				blackRookRRect = blackRookRImage.get_rect()
				blackRookRRect.x = board.get(blackRookR.x, blackRookR.y).get('x')
				blackRookRRect.y = board.get(blackRookR.x, blackRookR.y).get('y')
				blackRookRRect.width = board.get(blackRookR.x, blackRookR.y).get('w')
				blackRookRRect.height = board.get(blackRookR.x, blackRookR.y).get('h')
			if whiteRookL:	
				whiteRookLRect = whiteRookLImage.get_rect()
				whiteRookLRect.x = board.get(whiteRookL.x, whiteRookL.y).get('x')
				whiteRookLRect.y = board.get(whiteRookL.x, whiteRookL.y).get('y')
				whiteRookLRect.width = board.get(whiteRookL.x, whiteRookL.y).get('w')
				whiteRookLRect.height = board.get(whiteRookL.x, whiteRookL.y).get('h')	
			if whiteRookR:
				whiteRookRRect = whiteRookRImage.get_rect()
				whiteRookRRect.x = board.get(whiteRookR.x, whiteRookR.y).get('x')
				whiteRookRRect.y = board.get(whiteRookR.x, whiteRookR.y).get('y')
				whiteRookRRect.width = board.get(whiteRookR.x, whiteRookR.y).get('w')
				whiteRookRRect.height = board.get(whiteRookR.x, whiteRookR.y).get('h')
			if blackQueen:
				blackQueenRect = blackQueenImage.get_rect()
				blackQueenRect.x = board.get(blackQueen.x, blackQueen.y).get('x')
				blackQueenRect.y = board.get(blackQueen.x, blackQueen.y).get('y')
				blackQueenRect.width = board.get(blackQueen.x, blackQueen.y).get('w')
				blackQueenRect.height = board.get(blackQueen.x, blackQueen.y).get('h')
			if whiteQueen:
				whiteQueenRect = whiteQueenImage.get_rect()
				whiteQueenRect.x = board.get(whiteQueen.x, whiteQueen.y).get('x')
				whiteQueenRect.y = board.get(whiteQueen.x, whiteQueen.y).get('y')
				whiteQueenRect.width = board.get(whiteQueen.x, whiteQueen.y).get('w')
				whiteQueenRect.height = board.get(whiteQueen.x, whiteQueen.y).get('h')
			if blackBishopL:	
				blackBishopLRect = blackBishopLImage.get_rect()
				blackBishopLRect.x = board.get(blackBishopL.x, blackBishopL.y).get('x')
				blackBishopLRect.y = board.get(blackBishopL.x, blackBishopL.y).get('y')
				blackBishopLRect.width = board.get(blackBishopL.x, blackBishopL.y).get('w')
				blackBishopLRect.height = board.get(blackBishopL.x, blackBishopL.y).get('h')	
			if blackBishopR:
				blackBishopRRect = blackBishopRImage.get_rect()
				blackBishopRRect.x = board.get(blackBishopR.x, blackBishopR.y).get('x')
				blackBishopRRect.y = board.get(blackBishopR.x, blackBishopR.y).get('y')
				blackBishopRRect.width = board.get(blackBishopR.x, blackBishopR.y).get('w')
				blackBishopRRect.height = board.get(blackBishopR.x, blackBishopR.y).get('h')
			if whiteBishopL:	
				whiteBishopLRect = whiteBishopLImage.get_rect()
				whiteBishopLRect.x = board.get(whiteBishopL.x, whiteBishopL.y).get('x')
				whiteBishopLRect.y = board.get(whiteBishopL.x, whiteBishopL.y).get('y')
				whiteBishopLRect.width = board.get(whiteBishopL.x, whiteBishopL.y).get('w')
				whiteBishopLRect.height = board.get(whiteBishopL.x, whiteBishopL.y).get('h')	
			if whiteBishopR:
				whiteBishopRRect = whiteBishopRImage.get_rect()
				whiteBishopRRect.x = board.get(whiteBishopR.x, whiteBishopR.y).get('x')
				whiteBishopRRect.y = board.get(whiteBishopR.x, whiteBishopR.y).get('y')
				whiteBishopRRect.width = board.get(whiteBishopR.x, whiteBishopR.y).get('w')
				whiteBishopRRect.height = board.get(whiteBishopR.x, whiteBishopR.y).get('h')
			if blackKnightL:	
				blackKnightLRect = blackKnightLImage.get_rect()
				blackKnightLRect.x = board.get(blackKnightL.x, blackKnightL.y).get('x')
				blackKnightLRect.y = board.get(blackKnightL.x, blackKnightL.y).get('y')
				blackKnightLRect.width = board.get(blackKnightL.x, blackKnightL.y).get('w')
				blackKnightLRect.height = board.get(blackKnightL.x, blackKnightL.y).get('h')	
			if blackKnightR:	
				blackKnightRRect = blackKnightRImage.get_rect()
				blackKnightRRect.x = board.get(blackKnightR.x, blackKnightR.y).get('x')
				blackKnightRRect.y = board.get(blackKnightR.x, blackKnightR.y).get('y')
				blackKnightRRect.width = board.get(blackKnightR.x, blackKnightR.y).get('w')
				blackKnightRRect.height = board.get(blackKnightR.x, blackKnightR.y).get('h')
			if whiteKnightL:	
				whiteKnightLRect = whiteKnightLImage.get_rect()
				whiteKnightLRect.x = board.get(whiteKnightL.x, whiteKnightL.y).get('x')
				whiteKnightLRect.y = board.get(whiteKnightL.x, whiteKnightL.y).get('y')
				whiteKnightLRect.width = board.get(whiteKnightL.x, whiteKnightL.y).get('w')
				whiteKnightLRect.height = board.get(whiteKnightL.x, whiteKnightL.y).get('h')	
			if whiteKnightR:	
				whiteKnightRRect = whiteKnightRImage.get_rect()
				whiteKnightRRect.x = board.get(whiteKnightR.x, whiteKnightR.y).get('x')
				whiteKnightRRect.y = board.get(whiteKnightR.x, whiteKnightR.y).get('y')
				whiteKnightRRect.width = board.get(whiteKnightR.x, whiteKnightR.y).get('w')
				whiteKnightRRect.height = board.get(whiteKnightR.x, whiteKnightR.y).get('h')

			###BLACK PAWNS###
			if pawn0Rect and pawn0Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn0.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn0, board):
						blackPawn0 = selectedPiece.eat(blackPawn0)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn0, selectedPiece)
			#if blank space, move selectedPiece if the move is valid
			elif pawn1Rect and pawn1Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn1.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn1, board):
						blackPawn1 = selectedPiece.eat(blackPawn1)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn1, selectedPiece)
			elif pawn2Rect and pawn2Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn2.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn2, board):
						blackPawn2 = selectedPiece.eat(blackPawn2)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn2, selectedPiece)
			elif pawn3Rect and pawn3Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn3.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn3, board):
						blackPawn3 = selectedPiece.eat(blackPawn3)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn3, selectedPiece)
			elif pawn4Rect and pawn4Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn4.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn4, board):
						blackPawn4 = selectedPiece.eat(blackPawn4)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn4, selectedPiece)
			elif pawn5Rect and pawn5Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn5.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn5, board):
						blackPawn5 = selectedPiece.eat(blackPawn5)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn5, selectedPiece)
			elif pawn6Rect and pawn6Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn6.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn6, board):
						blackPawn6 = selectedPiece.eat(blackPawn6)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn6, selectedPiece)
			elif pawn7Rect and pawn7Rect.collidepoint(pos):
				if selectedPiece != None:
					if blackPawn7.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackPawn7, board):
						blackPawn7 = selectedPiece.eat(blackPawn7)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackPawn7, selectedPiece)
			###WHITE PAWNS###
			elif wpawn0Rect and wpawn0Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn0.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn0, board):
						whitePawn0 = selectedPiece.eat(whitePawn0)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn0, selectedPiece)
			elif wpawn1Rect and wpawn1Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn1.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn1, board):
						whitePawn1 = selectedPiece.eat(whitePawn1)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn1, selectedPiece)
			elif wpawn2Rect and wpawn2Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn2.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn2, board):
						whitePawn2 = selectedPiece.eat(whitePawn2)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn2, selectedPiece)
			elif wpawn3Rect and wpawn3Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn3.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn3, board):
						whitePawn3 = selectedPiece.eat(whitePawn3)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn3, selectedPiece)
			elif whitePawn4 and wpawn4Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn4.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn4, board):
						whitePawn4 = selectedPiece.eat(whitePawn4)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn4, selectedPiece)
			elif wpawn5Rect and wpawn5Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn5.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn5, board):
						whitePawn5 = selectedPiece.eat(whitePawn5)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn5, selectedPiece)
			elif wpawn6Rect and wpawn6Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn6.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn6, board):
						whitePawn6 = selectedPiece.eat(whitePawn6)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn6, selectedPiece)
			elif wpawn7Rect and wpawn7Rect.collidepoint(pos):
				if selectedPiece != None:
					if whitePawn7.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whitePawn7, board):
						whitePawn7 = selectedPiece.eat(whitePawn7)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whitePawn7, selectedPiece)
			###BLACK KING###
			elif blackKingRect.collidepoint(pos):
				selectedPiece = select(blackKing, selectedPiece)
			###WHITE KING###
			elif whiteKingRect.collidepoint(pos):
				selectedPiece = select(whiteKing, selectedPiece)
			###BLACK ROOK###
			elif blackRookLRect.collidepoint(pos):
				if selectedPiece != None:
					if blackRookL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackRookL, board):
						blackRookL = selectedPiece.eat(blackRookL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackRookL, selectedPiece)
			elif blackRookRRect.collidepoint(pos):
				if selectedPiece != None:
					if blackRookR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackRookR, board):
						blackRookR = selectedPiece.eat(blackRookR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackRookR, selectedPiece)
			###WHITE ROOK###
			elif whiteRookLRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteRookL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteRookL, board):
						whiteRookL = selectedPiece.eat(whiteRookL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteRookL, selectedPiece)
			elif whiteRookRRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteRookR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteRookR, board):
						whiteRookR = selectedPiece.eat(whiteRookR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteRookR, selectedPiece)
			###BLACK BISHOP###
			elif blackBishopLRect.collidepoint(pos):
				if selectedPiece != None:
					if blackBishopL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackBishopL, board):
						blackBishopL = selectedPiece.eat(blackBishopL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackBishopL, selectedPiece)
			elif blackBishopRRect.collidepoint(pos):
				if selectedPiece != None:
					if blackBishopR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackBishopR, board):
						blackBishopR = selectedPiece.eat(blackBishopR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackBishopR, selectedPiece)
			###WHITE BISHOP###
			elif whiteBishopLRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteBishopL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteBishopL, board):
						whiteBishopL = selectedPiece.eat(whiteBishopL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteBishopL, selectedPiece)
			elif whiteBishopRRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteBishopR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteBishopR, board):
						whiteBishopR = selectedPiece.eat(whiteBishopR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteBishopR, selectedPiece)
			###BLACK QUEEN###
			elif blackQueenRect.collidepoint(pos):
				if selectedPiece != None:
					if blackQueen.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackQueen, board):
						blackQueen = selectedPiece.eat(blackQueen)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackQueen, selectedPiece)
			###WHITE QUEEN###
			elif whiteQueenRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteQueen.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteQueen, board):
						whiteQueen = selectedPiece.eat(whiteQueen)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteQueen, selectedPiece)
			###BLACK KNIGHT###
			elif blackKnightLRect.collidepoint(pos):
				if selectedPiece != None:
					if blackKnightL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackKnightL, board):
						blackKnightL = selectedPiece.eat(blackKnightL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackKnightL, selectedPiece)
			elif blackKnightRRect.collidepoint(pos):
				if selectedPiece != None:
					if blackKnightR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(blackKnightR, board):
						blackKnightR = selectedPiece.eat(blackKnightR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(blackKnightR, selectedPiece)
			###WHITE KNIGHT###
			elif whiteKnightLRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteKnightL.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteKnightL, board):
						whiteKnightL = selectedPiece.eat(whiteKnightL)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteKnightL, selectedPiece)
			elif whiteKnightRRect.collidepoint(pos):
				if selectedPiece != None:
					if whiteKnightR.getColor() != selectedPiece.getColor() and selectedPiece.canEat(whiteKnightR, board):
						whiteKnightR = selectedPiece.eat(whiteKnightR)
						board.update(selectedPiece.x, selectedPiece.y, False)
						selectedPiece = None
				else:
					selectedPiece = select(whiteKnightR, selectedPiece)
			else:
				if selectedPiece == None:
					print("select piece")
				else:
					selectedPiece.move(pos, board)
					selectedPiece = None
	###DISPLAY BOARD###
	screen.fill(black)
	gameDisplay.blit(board_img, (0,0))
	###DISPLAY BLACK PAWNS###
	if blackPawn0: gameDisplay.blit(pawnImage0, (board.get(blackPawn0.x, blackPawn0.y).get('x') + 5, board.get(blackPawn0.x,blackPawn0.y).get('y')))
	if blackPawn1: gameDisplay.blit(pawnImage1, (board.get(blackPawn1.x, blackPawn1.y).get('x') + 5, board.get(blackPawn1.x,blackPawn1.y).get('y')))
	if blackPawn2: gameDisplay.blit(pawnImage2, (board.get(blackPawn2.x, blackPawn2.y).get('x') + 5, board.get(blackPawn2.x,blackPawn2.y).get('y')))
	if blackPawn3: gameDisplay.blit(pawnImage3, (board.get(blackPawn3.x, blackPawn3.y).get('x') + 5, board.get(blackPawn3.x,blackPawn3.y).get('y')))
	if blackPawn4: gameDisplay.blit(pawnImage4, (board.get(blackPawn4.x, blackPawn4.y).get('x') + 5, board.get(blackPawn4.x,blackPawn4.y).get('y')))
	if blackPawn5: gameDisplay.blit(pawnImage5, (board.get(blackPawn5.x, blackPawn5.y).get('x') + 5, board.get(blackPawn5.x,blackPawn5.y).get('y')))
	if blackPawn6: gameDisplay.blit(pawnImage6, (board.get(blackPawn6.x, blackPawn6.y).get('x') + 5, board.get(blackPawn6.x,blackPawn6.y).get('y')))
	if blackPawn7: gameDisplay.blit(pawnImage7, (board.get(blackPawn7.x, blackPawn7.y).get('x') + 5, board.get(blackPawn7.x,blackPawn7.y).get('y')))
	###DISPLAY WHITE PAWNS###
	if whitePawn0: gameDisplay.blit(whitePawnImage0, (board.get(whitePawn0.x, whitePawn0.y).get('x') + 5, board.get(whitePawn0.x,whitePawn0.y).get('y')))
	if whitePawn1: gameDisplay.blit(whitePawnImage1, (board.get(whitePawn1.x, whitePawn1.y).get('x') + 5, board.get(whitePawn1.x,whitePawn1.y).get('y')))
	if whitePawn2: gameDisplay.blit(whitePawnImage2, (board.get(whitePawn2.x, whitePawn2.y).get('x') + 5, board.get(whitePawn2.x,whitePawn2.y).get('y')))
	if whitePawn3: gameDisplay.blit(whitePawnImage3, (board.get(whitePawn3.x, whitePawn3.y).get('x') + 5, board.get(whitePawn3.x,whitePawn3.y).get('y')))
	if whitePawn4: gameDisplay.blit(whitePawnImage4, (board.get(whitePawn4.x, whitePawn4.y).get('x') + 5, board.get(whitePawn4.x,whitePawn4.y).get('y')))
	if whitePawn5: gameDisplay.blit(whitePawnImage5, (board.get(whitePawn5.x, whitePawn5.y).get('x') + 5, board.get(whitePawn5.x,whitePawn5.y).get('y')))
	if whitePawn6: gameDisplay.blit(whitePawnImage6, (board.get(whitePawn6.x, whitePawn6.y).get('x') + 5, board.get(whitePawn6.x,whitePawn6.y).get('y')))
	if whitePawn7: gameDisplay.blit(whitePawnImage7, (board.get(whitePawn7.x, whitePawn7.y).get('x') + 5, board.get(whitePawn7.x,whitePawn7.y).get('y')))
	###DISPLAY BLACK KING###
	gameDisplay.blit(blackKingImage, (board.get(blackKing.x, blackKing.y).get('x') + 5, board.get(blackKing.x, blackKing.y).get('y')))
	###DISPLAY WHITE KING###
	gameDisplay.blit(whiteKingImage, (board.get(whiteKing.x, whiteKing.y).get('x') + 5, board.get(whiteKing.x,whiteKing.y).get('y')))

	###DISPLAY BLACK QUEEN###
	if blackQueen: gameDisplay.blit(blackQueenImage, (board.get(blackQueen.x, blackQueen.y).get('x') + 5, board.get(blackQueen.x, blackQueen.y).get('y')))
	###DISPLAY WHITE QUEEN###
	if whiteQueen: gameDisplay.blit(whiteQueenImage, (board.get(whiteQueen.x, whiteQueen.y).get('x') + 5, board.get(whiteQueen.x, whiteQueen.y).get('y')))
	###DISPLAY BLACK KNIGHTS###
	if blackKnightL: gameDisplay.blit(blackKnightLImage, (board.get(blackKnightL.x, blackKnightL.y).get('x') + 5, board.get(blackKnightL.x, blackKnightL.y).get('y')))
	if blackKnightR: gameDisplay.blit(blackKnightRImage, (board.get(blackKnightR.x, blackKnightR.y).get('x') + 5, board.get(blackKnightR.x, blackKnightR.y).get('y')))
	###DISPLAY WHITE KNIGHTS###
	if whiteKnightL: gameDisplay.blit(whiteKnightLImage, (board.get(whiteKnightL.x, whiteKnightL.y).get('x') + 5, board.get(whiteKnightL.x, whiteKnightL.y).get('y')))
	if whiteKnightR: gameDisplay.blit(whiteKnightRImage, (board.get(whiteKnightR.x, whiteKnightR.y).get('x') + 5, board.get(whiteKnightR.x, whiteKnightR.y).get('y')))
	###DISPLAY BLACK BISHOPS###
	if blackBishopL: gameDisplay.blit(blackBishopLImage, (board.get(blackBishopL.x, blackBishopL.y).get('x') + 5, board.get(blackBishopL.x, blackBishopL.y).get('y')))
	if blackBishopR: gameDisplay.blit(blackBishopRImage, (board.get(blackBishopR.x, blackBishopR.y).get('x') + 5, board.get(blackBishopR.x, blackBishopR.y).get('y')))	
	###DISPLAY WHITE BISHOPS###
	if whiteBishopL: gameDisplay.blit(whiteBishopLImage, (board.get(whiteBishopL.x, whiteBishopL.y).get('x') + 5, board.get(whiteBishopL.x, whiteBishopL.y).get('y')))
	if whiteBishopR: gameDisplay.blit(whiteBishopRImage, (board.get(whiteBishopR.x, whiteBishopR.y).get('x') + 5, board.get(whiteBishopR.x, whiteBishopR.y).get('y')))	
	###DISPLAY BLACK ROOKS###
	if blackRookL: gameDisplay.blit(blackRookLImage, (board.get(blackRookL.x, blackRookL.y).get('x') + 5, board.get(blackRookL.x, blackRookL.y).get('y')))
	if blackRookR: gameDisplay.blit(blackRookRImage, (board.get(blackRookR.x, blackRookR.y).get('x') + 5, board.get(blackRookR.x, blackRookR.y).get('y')))
	###DISPLAY WHITE ROOKS###
	if whiteRookL: gameDisplay.blit(whiteRookLImage, (board.get(whiteRookL.x, whiteRookL.y).get('x') + 5, board.get(whiteRookL.x, whiteRookL.y).get('y')))
	if whiteRookR: gameDisplay.blit(whiteRookRImage, (board.get(whiteRookR.x, whiteRookR.y).get('x') + 5, board.get(whiteRookR.x, whiteRookR.y).get('y')))
	
	pygame.display.update()