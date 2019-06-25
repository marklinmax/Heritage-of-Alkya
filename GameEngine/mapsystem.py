#-*-coding: utf-8-*-

#§ Création des variables d'information
__version__ = "1.0.0"
__authors__ = "Lightpearl"

#§ Importation des modules complémentaires nécéssaires
from pygame.locals import HWSURFACE, SRCALPHA
from . import constants as cts
from . import systemComponents as core
import threading
import pygame
import time

#§ Création des variables globales du module
TILESETS = [
	{"A1": "Outside_A1", "A2": "Outside_A2", "A3": "Outside_A3", "A4": "Outside_A4", "A5": "Outside_A5", "B": "Outside_B", "C": "Outside_C"}
]

#§ Création des objets du module
class Tile:
	"""
	Tile définissant une case d'une carte
	"""
	def __init__(self):
		self.hitbox = 0
		self.nb_frames = 0
		self.pictures = [[] for _ in range(48)]
		self.picture_choice_mapping = {
			"00000000": 0,
			"00000001": 0,
			"00000010": 1,
			"00000011": 1,
			"00000100": 0,
			"00000101": 0,
			"00000110": 1,
			"00000111": 1,
			"00001000": 2,
			"00001001": 2,
			"00001010": 3,
			"00001011": 4,
			"00001100": 2,
			"00001101": 2,
			"00001110": 3,
			"00001111": 4,
			"00010000": 5,
			"00010001": 5,
			"00010010": 6,
			"00010011": 6,
			"00010100": 5,
			"00010101": 5,
			"00010110": 7,
			"00010111": 7,
			"00011000": 8,
			"00011001": 8,
			"00011010": 9,
			"00011011": 10,
			"00011100": 8,
			"00011101": 8,
			"00011110": 11,
			"00011111": 12,
			"00100000": 0,
			"00100001": 0,
			"00100010": 1,
			"00100011": 1,
			"00100100": 0,
			"00100101": 0,
			"00100110": 1,
			"00100111": 1,
			"00101000": 2,
			"00101001": 2,
			"00101010": 3,
			"00101011": 4,
			"00101100": 2,
			"00101101": 2,
			"00101110": 3,
			"00101111": 4,
			"00110000": 5,
			"00110001": 5,
			"00110010": 6,
			"00110011": 6,
			"00110100": 5,
			"00110101": 5,
			"00110110": 7,
			"00110111": 7,
			"00111000": 8,
			"00111001": 8,
			"00111010": 9,
			"00111011": 10,
			"00111100": 8,
			"00111101": 8,
			"00111110": 11,
			"00111111": 12,
			"01000000": 13,
			"01000001": 13,
			"01000010": 14,
			"01000011": 14,
			"01000100": 13,
			"01000101": 13,
			"01000110": 14,
			"01000111": 14,
			"01001000": 15,
			"01001001": 15,
			"01001010": 16,
			"01001011": 17,
			"01001100": 15,
			"01001101": 15,
			"01001110": 16,
			"01001111": 17,
			"01010000": 18,
			"01010001": 18,
			"01010010": 19,
			"01010011": 19,
			"01010100": 18,
			"01010101": 18,
			"01010110": 20,
			"01010111": 20,
			"01011000": 21,
			"01011001": 21,
			"01011010": 22,
			"01011011": 23,
			"01011100": 21,
			"01011101": 21,
			"01011110": 24,
			"01011111": 25,
			"01100000": 13,
			"01100001": 13,
			"01100010": 14,
			"01100011": 14,
			"01100100": 13,
			"01100101": 13,
			"01100110": 14,
			"01100111": 14,
			"01101000": 26,
			"01101001": 26,
			"01101010": 27,
			"01101011": 28,
			"01101100": 26,
			"01101101": 26,
			"01101110": 27,
			"01101111": 28,
			"01110000": 18,
			"01110001": 18,
			"01110010": 19,
			"01110011": 19,
			"01110100": 18,
			"01110101": 18,
			"01110110": 20,
			"01110111": 20,
			"01111000": 29,
			"01111001": 29,
			"01111010": 30,
			"01111011": 31,
			"01111100": 29,
			"01111101": 29,
			"01111110": 32,
			"01111111": 33,
			"10000000": 0,
			"10000001": 0,
			"10000010": 1,
			"10000011": 1,
			"10000100": 0,
			"10000101": 0,
			"10000110": 1,
			"10000111": 1,
			"10001000": 2,
			"10001001": 2,
			"10001010": 3,
			"10001011": 4,
			"10001100": 2,
			"10001101": 2,
			"10001110": 3,
			"10001111": 4,
			"10010000": 5,
			"10010001": 5,
			"10010010": 6,
			"10010011": 6,
			"10010100": 5,
			"10010101": 5,
			"10010110": 7,
			"10010111": 7,
			"10011000": 8,
			"10011001": 8,
			"10011010": 9,
			"10011011": 10,
			"10011100": 8,
			"10011101": 8,
			"10011110": 11,
			"10011111": 12,
			"10100000": 0,
			"10100001": 0,
			"10100010": 1,
			"10100011": 1,
			"10100100": 0,
			"10100101": 0,
			"10100110": 1,
			"10100111": 1,
			"10101000": 2,
			"10101001": 2,
			"10101010": 3,
			"10101011": 4,
			"10101100": 2,
			"10101101": 2,
			"10101110": 3,
			"10101111": 4,
			"10110000": 5,
			"10110001": 5,
			"10110010": 6,
			"10110011": 6,
			"10110100": 5,
			"10110101": 5,
			"10110110": 7,
			"10110111": 7,
			"10111000": 8,
			"10111001": 8,
			"10111010": 9,
			"10111011": 10,
			"10111100": 8,
			"10111101": 8,
			"10111110": 11,
			"10111111": 12,
			"11000000": 13,
			"11000001": 13,
			"11000010": 14,
			"11000011": 14,
			"11000100": 13,
			"11000101": 13,
			"11000110": 14,
			"11000111": 14,
			"11001000": 15,
			"11001001": 15,
			"11001010": 16,
			"11001011": 17,
			"11001100": 15,
			"11001101": 15,
			"11001110": 16,
			"11001111": 17,
			"11010000": 35,
			"11010001": 35,
			"11010010": 36,
			"11010011": 36,
			"11010100": 35,
			"11010101": 35,
			"11010110": 37,
			"11010111": 37,
			"11011000": 38,
			"11011001": 38,
			"11011010": 39,
			"11011011": 40,
			"11011100": 38,
			"11011101": 38,
			"11011110": 41,
			"11011111": 42,
			"11100000": 13,
			"11100001": 13,
			"11100010": 14,
			"11100011": 14,
			"11100100": 13,
			"11100101": 13,
			"11100110": 14,
			"11100111": 14,
			"11101000": 26,
			"11101001": 26,
			"11101010": 27,
			"11101011": 28,
			"11101100": 26,
			"11101101": 26,
			"11101110": 27,
			"11101111": 28,
			"11110000": 35,
			"11110001": 35,
			"11110010": 36,
			"11110011": 36,
			"11110100": 35,
			"11110101": 35,
			"11110110": 37,
			"11110111": 37,
			"11111000": 43,
			"11111001": 43,
			"11111010": 44,
			"11111011": 45,
			"11111100": 43,
			"11111101": 43,
			"11111110": 46,
			"11111111": 47}
		self.connected_tile = []

	def set_hitbox(self, hitbox):
		"""
		Change la hitbox du tile
		hitbox : 0 (sous le joueur), 1 (au niveau du joueur) ou 2 (au dessus du joueur)
		"""
		self.hitbox = max(min(hitbox, 2), 0)

	def load_picture(self, image, pos, type="field"):
		"""
		Charge les images du tile
		image : image d'où provient le tile
		pos : position de l'image du tile
		type :
			- field : image de fond pour le terrain
			- fall : image de type cascade
			- wall : image de type mur
			- unique : image seule
		"""
		self.nb_frames += 1

		imagepath = "GameAssets\\Tilesets\\pictures\\{}.png".format(image)

		tiles_pictures = pygame.image.load(imagepath).convert_alpha()
		if type == "field":
			tile1 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE/2), HWSURFACE | SRCALPHA)
			tile2 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE/2), HWSURFACE | SRCALPHA)
			tile3 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE/2), HWSURFACE | SRCALPHA)
			tile4 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE/2), HWSURFACE | SRCALPHA)
			tile = pygame.Surface((cts.TILE_SIZE, cts.TILE_SIZE), HWSURFACE | SRCALPHA)

			# Tile 0
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[0].append(tile.convert_alpha())

			# Tile 1
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[1].append(tile.convert_alpha())

			# Tile 2
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[2].append(tile.convert_alpha())

			# Tile 3
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[3].append(tile.convert_alpha())

			# Tile 4
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[4].append(tile.convert_alpha())

			# Tile 5
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[5].append(tile.convert_alpha())

			# Tile 6
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[6].append(tile.convert_alpha())

			# Tile 7
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[7].append(tile.convert_alpha())

			# Tile 8
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[8].append(tile.convert_alpha())

			# Tile 9
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[9].append(tile.convert_alpha())

			# Tile 10
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[10].append(tile.convert_alpha())

			# Tile 11
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[11].append(tile.convert_alpha())

			# Tile 12
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[12].append(tile.convert_alpha())

			# Tile 13
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[13].append(tile.convert_alpha())

			# Tile 14
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[14].append(tile.convert_alpha())

			# Tile 15
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[15].append(tile.convert_alpha())

			# Tile 16
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[16].append(tile.convert_alpha())

			# Tile 17
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[17].append(tile.convert_alpha())

			# Tile 18
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[18].append(tile.convert_alpha())

			# Tile 19
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[19].append(tile.convert_alpha())

			# Tile 20
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[20].append(tile.convert_alpha())

			# Tile 21
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[21].append(tile.convert_alpha())

			# Tile 22
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[22].append(tile.convert_alpha())

			# Tile 23
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[23].append(tile.convert_alpha())

			# Tile 24
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[24].append(tile.convert_alpha())

			# Tile 25
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[25].append(tile.convert_alpha())

			# Tile 26
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[26].append(tile.convert_alpha())

			# Tile 27
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[27].append(tile.convert_alpha())

			# Tile 28
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[28].append(tile.convert_alpha())

			# Tile 29
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[29].append(tile.convert_alpha())

			# Tile 30
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[30].append(tile.convert_alpha())

			# Tile 31
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[31].append(tile.convert_alpha())

			# Tile 32
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[32].append(tile.convert_alpha())

			# Tile 33
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[33].append(tile.convert_alpha())

			# Tile 34
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0], -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[34].append(tile.convert_alpha())

			# Tile 35
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[35].append(tile.convert_alpha())

			# Tile 36
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[36].append(tile.convert_alpha())

			# Tile 37
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[37].append(tile.convert_alpha())

			# Tile 38
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[38].append(tile.convert_alpha())

			# Tile 39
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[39].append(tile.convert_alpha())

			# Tile 40
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[40].append(tile.convert_alpha())

			# Tile 41
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[41].append(tile.convert_alpha())

			# Tile 42
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[42].append(tile.convert_alpha())

			# Tile 43
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-5*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-5*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[43].append(tile.convert_alpha())

			# Tile 44
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[44].append(tile.convert_alpha())

			# Tile 45
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[45].append(tile.convert_alpha())

			# Tile 46
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]-cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[46].append(tile.convert_alpha())

			# Tile 47
			tile.fill((0, 0, 0, 0))
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile3.fill((0, 0, 0, 0))
			tile4.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-2*cts.TILE_SIZE))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-2*cts.TILE_SIZE))
			tile3.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]-3*cts.TILE_SIZE/2))
			tile4.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]-3*cts.TILE_SIZE/2))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			tile.blit(tile3, (0, cts.TILE_SIZE/2))
			tile.blit(tile4, (cts.TILE_SIZE/2, cts.TILE_SIZE/2))
			self.pictures[47].append(tile.convert_alpha())

		elif type == "fall":
			tile1 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE), HWSURFACE | SRCALPHA)
			tile2 = pygame.Surface((cts.TILE_SIZE/2, cts.TILE_SIZE), HWSURFACE | SRCALPHA)
			tile = pygame.Surface((cts.TILE_SIZE, cts.TILE_SIZE), HWSURFACE | SRCALPHA)

			# Tile 0
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			self.pictures[0].append(tile.convert_alpha())
			self.pictures[1].append(tile.convert_alpha())
			self.pictures[13].append(tile.convert_alpha())
			self.pictures[14].append(tile.convert_alpha())

			# Tile 1
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-3*cts.TILE_SIZE/2, -pos[1]))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			self.pictures[5].append(tile.convert_alpha())
			self.pictures[6].append(tile.convert_alpha())
			self.pictures[7].append(tile.convert_alpha())
			self.pictures[18].append(tile.convert_alpha())
			self.pictures[19].append(tile.convert_alpha())
			self.pictures[20].append(tile.convert_alpha())
			self.pictures[35].append(tile.convert_alpha())
			self.pictures[36].append(tile.convert_alpha())
			self.pictures[37].append(tile.convert_alpha())

			# Tile 2
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0], -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			self.pictures[2].append(tile.convert_alpha())
			self.pictures[3].append(tile.convert_alpha())
			self.pictures[4].append(tile.convert_alpha())
			self.pictures[15].append(tile.convert_alpha())
			self.pictures[16].append(tile.convert_alpha())
			self.pictures[17].append(tile.convert_alpha())
			self.pictures[26].append(tile.convert_alpha())
			self.pictures[27].append(tile.convert_alpha())
			self.pictures[28].append(tile.convert_alpha())
			self.pictures[34].append(tile.convert_alpha())

			# Tile 3
			tile1.fill((0, 0, 0, 0))
			tile2.fill((0, 0, 0, 0))
			tile.fill((0, 0, 0, 0))
			tile1.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE, -pos[1]))
			tile2.blit(tiles_pictures, (-pos[0]-cts.TILE_SIZE/2, -pos[1]))
			tile.blit(tile1, (0, 0))
			tile.blit(tile2, (cts.TILE_SIZE/2, 0))
			self.pictures[8].append(tile.convert_alpha())
			self.pictures[9].append(tile.convert_alpha())
			self.pictures[10].append(tile.convert_alpha())
			self.pictures[11].append(tile.convert_alpha())
			self.pictures[12].append(tile.convert_alpha())
			self.pictures[21].append(tile.convert_alpha())
			self.pictures[22].append(tile.convert_alpha())
			self.pictures[23].append(tile.convert_alpha())
			self.pictures[24].append(tile.convert_alpha())
			self.pictures[25].append(tile.convert_alpha())
			self.pictures[29].append(tile.convert_alpha())
			self.pictures[30].append(tile.convert_alpha())
			self.pictures[31].append(tile.convert_alpha())
			self.pictures[32].append(tile.convert_alpha())
			self.pictures[38].append(tile.convert_alpha())
			self.pictures[39].append(tile.convert_alpha())
			self.pictures[40].append(tile.convert_alpha())
			self.pictures[41].append(tile.convert_alpha())
			self.pictures[42].append(tile.convert_alpha())
			self.pictures[43].append(tile.convert_alpha())
			self.pictures[44].append(tile.convert_alpha())
			self.pictures[45].append(tile.convert_alpha())
			self.pictures[46].append(tile.convert_alpha())
			self.pictures[47].append(tile.convert_alpha())

		elif type == "wall":
			pass

		else:
			tile_picture = pygame.Surface((cts.TILE_SIZE, cts.TILE_SIZE), HWSURFACE | SRCALPHA)
			tile_picture.blit(tiles_pictures, [-e for e in pos])
			tile_picture = tile_picture.convert_alpha()
			for picture_type in self.pictures:
				picture_type.append(tile_picture)

	def connect(self, tile_id):
		self.connected_tile.append(tile_id)

class Tileset:
	"""
	Ensemble de tiles
	"""
	def __init__(self, tileset_id):
		self.tileset_id = tileset_id
		self.tiles = {
			"A1": [],
			"A2": [],
			"A3": [],
			"A4": [],
			"A5": [],
			"B": [],
			"C": []}
		self.load_A1()
		self.load_A2()
		self.load_A3()
		self.load_A4()
		self.load_A5()
		self.load_B()
		self.load_C()

	def load_A1(self):
		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (0, 0))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (2*cts.TILE_SIZE, 0))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (4*cts.TILE_SIZE, 0))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 0))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (8*cts.TILE_SIZE, 0))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (10*cts.TILE_SIZE, 0))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (12*cts.TILE_SIZE, 0))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 0), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 2*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (0, 3*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (2*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (4*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (8*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (10*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (12*cts.TILE_SIZE, 3*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 3*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 4*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 5*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (0, 6*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (2*cts.TILE_SIZE, 6*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (4*cts.TILE_SIZE, 6*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 6*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 7*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 8*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (8*cts.TILE_SIZE, 6*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (10*cts.TILE_SIZE, 6*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (12*cts.TILE_SIZE, 6*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 6*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 7*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 8*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (0, 9*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (2*cts.TILE_SIZE, 9*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (4*cts.TILE_SIZE, 9*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 9*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 10*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (6*cts.TILE_SIZE, 11*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (8*cts.TILE_SIZE, 9*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (10*cts.TILE_SIZE, 9*cts.TILE_SIZE))
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (12*cts.TILE_SIZE, 9*cts.TILE_SIZE))
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

		tile = Tile()
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 9*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 10*cts.TILE_SIZE), type="fall")
		tile.load_picture(TILESETS[self.tileset_id]["A1"], (14*cts.TILE_SIZE, 11*cts.TILE_SIZE), type="fall")
		tile.set_hitbox(1)
		self.tiles["A1"].append(tile)

	def load_A2(self):
		for y in range(4):
			for x in range(8):
				tile = Tile()
				tile.load_picture(TILESETS[self.tileset_id]["A2"], (x*2*cts.TILE_SIZE, 3*y*cts.TILE_SIZE))
				if x == 6:
					tile.set_hitbox(1)
				elif x == 7:
					if y == 3:
						tile.set_hitbox(1)
					else:
						tile.set_hitbox(0)
				else:
					tile.set_hitbox(0)
				self.tiles["A2"].append(tile)

	def load_A3(self):
		pass

	def load_A4(self):
		pass

	def load_A5(self):
		pass

	def load_B(self):
		tileset_picture = pygame.image.load("GameAssets\\Tilesets\\pictures\\{}.png".format(TILESETS[self.tileset_id]["B"])).convert_alpha()
		nb_tile_x = tileset_picture.get_width()//48
		nb_tile_y = tileset_picture.get_height()//48
		for j in range(nb_tile_y):
			for i in range(nb_tile_x//2):
				tile = Tile()
				tile.load_picture(TILESETS[self.tileset_id]["B"], (i*cts.TILE_SIZE, j*cts.TILE_SIZE), type="unique")
				self.tiles["B"].append(tile)

		for j in range(nb_tile_y):
			for i in range(nb_tile_x//2):
				tile = Tile()
				tile.load_picture(TILESETS[self.tileset_id]["B"], ((i+nb_tile_x//2)*cts.TILE_SIZE, j*cts.TILE_SIZE), type="unique")
				self.tiles["B"].append(tile)

	def load_C(self):
		tileset_picture = pygame.image.load("GameAssets\\Tilesets\\pictures\\{}.png".format(TILESETS[self.tileset_id]["C"])).convert_alpha()
		nb_tile_x = tileset_picture.get_width()//48
		nb_tile_y = tileset_picture.get_height()//48
		for j in range(nb_tile_y):
			for i in range(nb_tile_x//2):
				tile = Tile()
				tile.load_picture(TILESETS[self.tileset_id]["C"], (i*cts.TILE_SIZE, j*cts.TILE_SIZE), type="unique")
				self.tiles["C"].append(tile)

		for j in range(nb_tile_y):
			for i in range(nb_tile_x//2):
				tile = Tile()
				tile.load_picture(TILESETS[self.tileset_id]["C"], ((i+nb_tile_x//2)*cts.TILE_SIZE, j*cts.TILE_SIZE), type="unique")
				self.tiles["C"].append(tile)

	def __getitem__(self, index):
		picture, pos = index
		return self.tiles[picture][pos]

TILESETS_OBJECTS = [Tileset(i) for i in range(len(TILESETS))]

class Map:
	"""
	Objet définissant la carte sur laquelle se déplacent les entitées et le joueur
	"""
	def __init__(self, size, tileset_id, tiles=[]):
		self.size = size
		self.tileset = TILESETS_OBJECTS[tileset_id]
		self.tile_map = [[[[] for _ in range(self.size[1])] for _ in range(self.size[0])] for _ in range(3)]
		self.load_tiles(tiles)

		self.layouts = [pygame.Surface(cts.WINDOW_SIZE, HWSURFACE | SRCALPHA) for _ in range(3)]

		self.current_frame = 0

	def load_tiles(self, tiles):
		for tile_infos in tiles:
			tile_id, tile_pos = tile_infos
			tile_x, tile_y = tile_pos
			tile = self.tileset[tile_id]
			self.tile_map[tile.hitbox][tile_x][tile_y].append(tile_id)

	def render(self, level, fps, camera_pos):
		self.layouts[level].fill((0, 0, 0, 0))
		camera_x, camera_y = camera_pos

		min_x = camera_x//cts.TILE_SIZE
		min_y = camera_y//cts.TILE_SIZE

		for x in range(min_x, min(self.size[0], min_x+cts.TILE_NUMBER_X+1)):
			for y in range(min_y, min(self.size[1], min_y+cts.TILE_NUMBER_Y+1)):
				for tile_id in self.tile_map[level][x][y]:
					tile = self.tileset[tile_id]
					real_x = (x-min_x)*cts.TILE_SIZE - (camera_x%cts.TILE_SIZE)
					real_y = (y-min_y)*cts.TILE_SIZE - (camera_y%cts.TILE_SIZE)
					n1 = int(tile_id in self.tile_map[level][max(0, x-1)][max(0, y-1)])
					n2 = int(tile_id in self.tile_map[level][x][max(0, y-1)])
					n3 = int(tile_id in self.tile_map[level][min(self.size[0]-1, x+1)][max(0, y-1)])
					n4 = int(tile_id in self.tile_map[level][max(0, x-1)][y])
					n5 = int(tile_id in self.tile_map[level][min(self.size[0]-1, x+1)][y])
					n6 = int(tile_id in self.tile_map[level][max(0, x-1)][min(self.size[1]-1, y+1)])
					n7 = int(tile_id in self.tile_map[level][x][min(self.size[1]-1, y+1)])
					n8 = int(tile_id in self.tile_map[level][min(self.size[0]-1, x+1)][min(self.size[1]-1, y+1)])
					neighborhood = str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)
					picture = tile.pictures[tile.picture_choice_mapping[neighborhood]][self.current_frame//int(fps*cts.TILE_ANIMATION_PERIOD)%tile.nb_frames]
					self.layouts[level].blit(picture, (real_x, real_y))


	def update(self, fps, camera_pos):
		workers = []
		for x in range(3):
			worker = threading.Thread(target=self.render, args=(x, fps, camera_pos))
			workers.append(worker)
			worker.start()

		for worker in workers:
			worker.join()

		self.current_frame += 1
