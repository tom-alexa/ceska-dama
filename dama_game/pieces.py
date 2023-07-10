import pygame
from dama_game.constants import *


class Piece():
    def __init__(self, color, pos, board):
        self.color = color                          # piece color
        
        if self.color == WHITE:
            self.opposite_color = BLACK             # piece opposite color
            self.filter_color = WHITE_DARK
            self.filter_opposite_color = BLACK_LIGHT
        else:
            self.opposite_color = WHITE
            self.filter_color = BLACK_LIGHT
            self.filter_opposite_color = WHITE_DARK
        
        self.pos = pos                                  # possition ( {1-8}, {1-8} )
        self.queen = False                          # no queen in the beginning
        self.just_became_queen = False

        self.possible_places = []                   # after calling function it will gets possible current places
        self.__update_possible_places(board)        # this updates possible places

        self.is_clicked = False                     # tells us if piece is clicked
        self.jump = False                           # tells us if piece can jump over another piece
        self.possible_jump = False

        board.occupied_places[self.pos] = self.color    # writes itself in occupied places


    # draw piece
    def draw_piece(self):

        if self.is_clicked:

            # draw possible places
            for possible_place in self.possible_places:
                possible_place_pos_x, possible_place_pos_y =  self.__get_pos_xy(possible_place)

                pygame.draw.circle(screen, DARKER_WOOD, (possible_place_pos_x, possible_place_pos_y), CIRCLE_RADIUS*4//5)       # draw smaller circle

            # get darker if is picked
            pygame.draw.rect(screen, MOST_DARK_WOOD, (self.pos_x - SQUARE_SIZE//2, self.pos_y - SQUARE_SIZE//2, SQUARE_SIZE, SQUARE_SIZE))


        # draw piece
        self.pos_x, self.pos_y = self.__get_pos_xy(self.pos)        # get real possitions (x,y)


        # if piece is queen
        if self.queen:

        # horizontally
            # border queen rectangle
            pygame.draw.rect(screen, self.color, (self.pos_x - QUEEN_RECTANGLE_WIDTH//2, self.pos_y - QUEEN_RECTANGLE_HEIGHT//2, QUEEN_RECTANGLE_WIDTH, QUEEN_RECTANGLE_HEIGHT))
            # queen rectangle
            pygame.draw.rect(screen, self.opposite_color, (self.pos_x - QUEEN_RECTANGLE_WIDTH//2, self.pos_y - QUEEN_RECTANGLE_HEIGHT//2, QUEEN_RECTANGLE_WIDTH, QUEEN_RECTANGLE_HEIGHT), SQUARE_SIZE//40)

        # vertically
            # border queen rectangle
            pygame.draw.rect(screen, self.color, (self.pos_x - QUEEN_RECTANGLE_HEIGHT//2, self.pos_y - QUEEN_RECTANGLE_WIDTH//2, QUEEN_RECTANGLE_HEIGHT, QUEEN_RECTANGLE_WIDTH))
            # queen rectangle
            pygame.draw.rect(screen, self.opposite_color, (self.pos_x - QUEEN_RECTANGLE_HEIGHT//2, self.pos_y - QUEEN_RECTANGLE_WIDTH//2, QUEEN_RECTANGLE_HEIGHT, QUEEN_RECTANGLE_WIDTH), SQUARE_SIZE//40)

        # draw piece body
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), CIRCLE_RADIUS)                                 # circle (piece)
        pygame.draw.circle(screen, self.opposite_color, (self.pos_x, self.pos_y), CIRCLE_RADIUS, SQUARE_SIZE//25)       # border circle (opposite color)
        pygame.draw.circle(screen, self.filter_opposite_color, (self.pos_x, self.pos_y), CIRCLE_RADIUS//3*2, SQUARE_SIZE//25)       # border smaller circle (opposite color)

        # if piece is queen
        if self.queen:
            pygame.draw.circle(screen, self.filter_color, (self.pos_x, self.pos_y), CIRCLE_RADIUS//2)




    # piece move
    def move(self, possible_place, board, pieces):
        # remove old piece possition from occupied places
        board.occupied_places[self.pos] = None

        # after move piece becomes not picked
        self.is_clicked = False

        # variable if jumped
        self.jump = False

        # check if piece jump over another
        for i in range(abs(self.pos[1] - possible_place[1]) - 1):

            between_place_x = self.pos[0] + (i + 1) if self.pos[0] < possible_place[0] else self.pos[0] - (i + 1)
            between_place_y = self.pos[1] + (i + 1) if self.pos[1] < possible_place[1] else self.pos[1] - (i + 1)

            between_place = (between_place_x, between_place_y)

            for piece in pieces:
                if piece.pos == between_place:
                    piece.was_jumped(board, pieces)
                    self.jump = True

        # get new piece possition
        self.pos = possible_place

        # add new piece possition in occupied places
        board.occupied_places[self.pos] = self.color


        # if piece reach last line -> it becomes queen
        if self.color == WHITE:
            if not self.queen and self.pos[1] == ROWS:
                self.queen = True
                self.just_became_queen = True
        else:
            if not self.queen and self.pos[1] == 1:
                self.queen = True
                self.just_became_queen = True




    # function call function below, it is here to call the function from other file -> it is public function
    def get_update_possible_places(self, board):
        self.__update_possible_places(board)


    # get possible places -> it is private function
    def __update_possible_places(self, board):
        self.possible_places = []
        self.possible_jump = []

        # if not queen
        if not self.queen:

            possible_y = (self.pos[1] + 1) if self.color == WHITE else (self.pos[1] - 1)    # get next line


            # get all board places in next line
            for m in range(COLUMNS//2):

                if self.pos[1] % 2 == 1:
                    possible_x = m*2+2
                else:
                    possible_x = m*2+1

                # get possible possition to tuple
                possible_pos = (possible_x, possible_y)


                # if on possible possition is not standing same color as itself and x possition is right next to current possition and is inside the board (not outside)
                if board.occupied_places[possible_pos] != self.color and abs(self.pos[0]-possible_x) == 1:

                    if board.occupied_places[possible_pos] == None:     # if possible possition is free it can be written in possible places
                        self.possible_places.append(possible_pos)


                    else:       # if possible possition is occupied by opponent -> check if possition behind is free for jump
                        possible_x_jump = possible_x + (possible_x - self.pos[0])
                        possible_y_jump = possible_y + 1 if self.color == WHITE else possible_y - 1

                        possible_pos = (possible_x_jump, possible_y_jump)

                        # if next possible possition is free it can be written in possible places
                        if possible_x_jump != 0 and possible_x_jump != 9 and possible_y_jump != 0 and possible_y_jump != 9:
                            if board.occupied_places[possible_pos] == None:
                                self.possible_places.append(possible_pos)
                                self.possible_jump.append(possible_pos)



        # if queen
        else:
            
            # max steps to each direction
            north_east_max = (COLUMNS - self.pos[0]) if (COLUMNS - self.pos[0]) < (ROWS - self.pos[1]) else (ROWS - self.pos[1])
            south_east_max = (COLUMNS - self.pos[0]) if (COLUMNS - self.pos[0]) < (self.pos[1] - 1) else (self.pos[1] - 1)
            south_west_max = (self.pos[0] - 1) if (self.pos[0] - 1) < (self.pos[1] - 1) else (self.pos[1] - 1)
            north_west_max = (self.pos[0] - 1) if (self.pos[0] - 1) < (ROWS - self.pos[1]) else (ROWS - self.pos[1])

            # count how many opponent pieces are in diagonal
            count_north_east, count_south_east, count_south_west, count_north_west = 0, 0, 0, 0

            for i in range(1, north_east_max + 1):
                if count_north_east < 2:
                    possible_pos = (self.pos[0] + i, self.pos[1] + i)

                    count_north_east, same_color = self.__possible_move_queen(possible_pos, count_north_east, board)

                    if same_color:
                        break


            for i in range(1, south_east_max + 1):
                if count_south_east < 2:
                    possible_pos = (self.pos[0] + i, self.pos[1] - i)
                    count_south_east, same_color = self.__possible_move_queen(possible_pos, count_south_east, board)

                    if same_color:
                        break


            for i in range(1, south_west_max + 1):
                if count_south_west < 2:
                    possible_pos = (self.pos[0] - i, self.pos[1] - i)
                    count_south_west, same_color =  self.__possible_move_queen(possible_pos, count_south_west, board)

                    if same_color:
                        break


            for i in range(1, north_west_max + 1):
                if count_north_west < 2:
                    possible_pos = (self.pos[0] - i, self.pos[1] + i)
                    count_north_west, same_color = self.__possible_move_queen(possible_pos, count_north_west, board)

                    if same_color:
                        break


    def __possible_move_queen(self, possible_pos, count, board):
        # if possible possition is free
        is_valid = True if board.occupied_places[possible_pos] == None else False

        # if same color piece is standing on possible possition
        same_color = True if board.occupied_places[possible_pos] == self.color else False

        # if opponent is standing on possible possition
        count += 1 if board.occupied_places[possible_pos] == self.opposite_color else 0

        if count == 1 and is_valid:
            self.possible_jump.append(possible_pos)

        if is_valid:
            self.possible_places.append(possible_pos)

        return count, same_color






    # get real possition for draw
    def __get_pos_xy(self, pos):
        pos_x = (pos[0]-1)*SQUARE_SIZE + MARK + SQUARE_SIZE//2
        pos_y = (ROWS - pos[1])*SQUARE_SIZE + GAP + MARK + SQUARE_SIZE//2

        return pos_x, pos_y


    # piece was jumped, now is dead
    def was_jumped(self, board, pieces):
        board.occupied_places[self.pos] = None
        pieces.remove(self)