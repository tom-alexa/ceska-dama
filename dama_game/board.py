import pygame
from dama_game.constants import *


class Board():
    def __init__(self):
        self.occupied_places = {}       # at start there are not any occupied_places, right away after creating pieces, it gets current
        for row in range(1, ROWS + 1):
            for column in range(1, COLUMNS + 1):
                self.occupied_places[(row, column)] = None

    def draw_board(self, turn, mouse_pos, number_of_players):
        # fill window black
        screen.fill(BLACK)

        # board fill (mark background on the sides)
        pygame.draw.rect(screen, DARKER_WOOD, (0, GAP, BOARD_SIZE + MARK*2, BOARD_SIZE + MARK*2))


        # menu panel on top
        title_text = pygame.font.Font("dama_game/fonts/varsity_font.ttf", BOARD_SIZE//20).render("dáma".upper(), True, WHITE)   # title

        menu_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", BOARD_SIZE//30)      # menu font


        color = "white".upper() if turn > 0 else "black".upper()
        turn_text = menu_font.render(f"Now playing...      {color}", True, LIGHT_WOOD)
        turn_text_pos = WIDTH - (turn_text.get_width() + WIDTH//20)

        if turn > 0:
            pygame.draw.rect(screen, WHITE, (turn_text_pos + turn_text.get_width()*2//3, GAP//5, turn_text.get_width()//5*2, GAP//5*3), border_radius=GAP//20)
        else:
            pygame.draw.rect(screen, WHITE, (turn_text_pos + turn_text.get_width()*2//3, GAP//5, turn_text.get_width()//5*2, GAP//5*3), GAP//20, GAP//20)


        # menu button
        self.menu_btn = menu_font.render("menu".capitalize(), True, WHITE)

        self.menu_btn_x = title_text.get_width() + WIDTH//8
        self.menu_btn_y = GAP//2 - self.menu_btn.get_height()//2

        # draw menu button background
        self.menu_btn_rect_dim = (self.menu_btn_x - GAP//8, self.menu_btn_y - GAP//16, self.menu_btn.get_width() + GAP//4, self.menu_btn.get_height()+ GAP//8)

        if mouse_pos[0] > self.menu_btn_rect_dim[0] and mouse_pos[0] < self.menu_btn_rect_dim[0] + self.menu_btn_rect_dim[2] and mouse_pos[1] > self.menu_btn_rect_dim[1] and mouse_pos[1] < self.menu_btn_rect_dim[1] + self.menu_btn_rect_dim[3]:
            rect_color = LIGHT_WOOD
        else:
            rect_color = DARK_WOOD

        pygame.draw.rect(screen, rect_color, self.menu_btn_rect_dim)



        # stop button button
        if number_of_players == 0:

            self.stop_btn = menu_font.render("stop".capitalize(), True, WHITE)

            self.stop_btn_x = title_text.get_width() + WIDTH//4
            self.stop_btn_y = GAP//2 - self.stop_btn.get_height()//2

            # draw stop button background
            self.stop_btn_rect_dim = (self.stop_btn_x - GAP//8, self.stop_btn_y - GAP//16, self.stop_btn.get_width() + GAP//4, self.stop_btn.get_height()+ GAP//8)

            if mouse_pos[0] > self.stop_btn_rect_dim[0] and mouse_pos[0] < self.stop_btn_rect_dim[0] + self.stop_btn_rect_dim[2] and mouse_pos[1] > self.stop_btn_rect_dim[1] and mouse_pos[1] < self.stop_btn_rect_dim[1] + self.stop_btn_rect_dim[3]:
                rect_color = LIGHT_WOOD
            else:
                rect_color = DARK_WOOD

            pygame.draw.rect(screen, rect_color, self.stop_btn_rect_dim)


            screen.blit(self.stop_btn, (self.stop_btn_x, self.stop_btn_y))



        # blit on the screen
        screen.blit(title_text, (WIDTH//30, GAP//2 - title_text.get_height()//2))
        screen.blit(turn_text, (turn_text_pos, GAP//2 - turn_text.get_height()//2))
        screen.blit(self.menu_btn, (self.menu_btn_x, self.menu_btn_y))

        # draw squares
        for m in range(ROWS):
            for n in range(COLUMNS):
                # draw dark squares
                if (m+n) % 2 == 1:
                    pygame.draw.rect(screen, DARK_WOOD, (MARK + m*SQUARE_SIZE, GAP + MARK + n*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                # draw light squares
                else:
                    pygame.draw.rect(screen, LIGHT_WOOD, (MARK + m*SQUARE_SIZE, GAP + MARK + n*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


        # mark text
        mark_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", BOARD_SIZE//20)
        for m in range(ROWS):       # (1-8)
            mark_text = mark_font.render(f"{m+1}", True, WHITE)

            screen.blit(mark_text, (MARK + m*SQUARE_SIZE + SQUARE_SIZE//2 - mark_text.get_width()//2, HEIGHT - MARK//2 - mark_text.get_height()//2))
            screen.blit(mark_text, (MARK + m*SQUARE_SIZE + SQUARE_SIZE//2 - mark_text.get_width()//2, GAP + MARK//2 - mark_text.get_height()//2))

        for n in range(COLUMNS):    # (A-H)
            letter = chr(n+65)
            mark_text = mark_font.render(f"{letter}", True, WHITE)

            screen.blit(mark_text, (MARK//2 - mark_text.get_width()//2, GAP + (7-n)*SQUARE_SIZE + MARK + SQUARE_SIZE//2 - mark_text.get_height()//2))
            screen.blit(mark_text, (WIDTH - MARK//2 - mark_text.get_width()//2, GAP + (7-n)*SQUARE_SIZE + MARK + SQUARE_SIZE//2 - mark_text.get_height()//2))


    def btn_hover(self, mouse_pos, number_of_players):
        if (mouse_pos[0] > self.menu_btn_rect_dim[0] and mouse_pos[0] < self.menu_btn_rect_dim[0] + self.menu_btn_rect_dim[2] and mouse_pos[1] > self.menu_btn_rect_dim[1] and mouse_pos[1] < self.menu_btn_rect_dim[1] + self.menu_btn_rect_dim[3]):
            return True
        elif number_of_players == 0:
            if (mouse_pos[0] > self.stop_btn_rect_dim[0] and mouse_pos[0] < self.stop_btn_rect_dim[0] + self.stop_btn_rect_dim[2] and mouse_pos[1] > self.stop_btn_rect_dim[1] and mouse_pos[1] < self.stop_btn_rect_dim[1] + self.stop_btn_rect_dim[3]):
                return True
            else:
                return False


    def menu_btn_click(self, mouse_pos):
        if (mouse_pos[0] > self.menu_btn_rect_dim[0] and mouse_pos[0] < self.menu_btn_rect_dim[0] + self.menu_btn_rect_dim[2] and mouse_pos[1] > self.menu_btn_rect_dim[1] and mouse_pos[1] < self.menu_btn_rect_dim[1] + self.menu_btn_rect_dim[3]):
            return True
        else:
            return False


    def stop_btn_click(self, mouse_pos):
        if (mouse_pos[0] > self.stop_btn_rect_dim[0] and mouse_pos[0] < self.stop_btn_rect_dim[0] + self.stop_btn_rect_dim[2] and mouse_pos[1] > self.stop_btn_rect_dim[1] and mouse_pos[1] < self.stop_btn_rect_dim[1] + self.stop_btn_rect_dim[3]):
            return True
        else:
            return False