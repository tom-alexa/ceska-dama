# imports
import os
import random
from pathlib import Path

import pygame

# pygame initialize
pygame.init()

# board
BOARD_SIZE = 800

# gap on top ; mark on each side
GAP = BOARD_SIZE // 10
MARK = BOARD_SIZE // 16

# width, height
WIDTH, HEIGHT = BOARD_SIZE + MARK * 2, BOARD_SIZE + GAP + MARK * 2

# set position of the window on the screen (ideal would be in center)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{500},{50}"

# creating screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK_LIGHT = (50, 50, 50)
WHITE_DARK = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (150, 0, 0)
DARK_BLUE = (0, 0, 150)
LIGHT_WOOD = (180, 120, 70)
DARK_WOOD = (70, 30, 6)
DARKER_WOOD = (40, 20, 6)
MOST_DARK_WOOD = (20, 10, 3)
YELLOW = (255, 255, 0)

# rows, columns, square size, piece radius
ROWS, COLUMNS = 8, 8

SQUARE_SIZE = BOARD_SIZE // ROWS
CIRCLE_RADIUS = SQUARE_SIZE // 3
QUEEN_RECTANGLE_WIDTH = SQUARE_SIZE // 8 * 7
QUEEN_RECTANGLE_HEIGHT = SQUARE_SIZE // 6

# sounds
cwd = Path(__file__).parent / "sounds"
move_path = cwd / "move.wav"
capture_path = cwd / "capture.wav"
sound_move = pygame.mixer.Sound(move_path.absolute().as_posix())
sound_capture = pygame.mixer.Sound(capture_path.absolute().as_posix())

# --- background song ---

# create event when song ends
song_finished = pygame.USEREVENT + 1

# when song ends it call this event
music = pygame.mixer.music
music.set_endevent(song_finished)

# list of background songs
seven = cwd / "background" / "Tobu - Seven.mp3"
flares = cwd / "background" / "NIVIRO - Flares.mp3"
arrow = cwd / "background" / "Jim Yosef - Arrow.mp3"
fire = cwd / "background" / "Elektronomia - Fire.mp3"
music_list = [
    seven.absolute().as_posix(),
    flares.absolute().as_posix(),
    arrow.absolute().as_posix(),
    fire.absolute().as_posix()
]

# volume
volume = .3  # set volume in the beginning
volume_change_number = .01  # how much volume will change after clicking UP key or DOWN key

# start first song
current_song = random.choice(music_list)  # randomly choose
music.load(current_song)  # load song
music.set_volume(volume)  # set volume
music.play(0)  # start playing
