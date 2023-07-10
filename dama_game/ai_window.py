import pygame
from dama_game.constants import *


class AI_window():
    def draw_window(self, white_wins, black_wins, mouse_pos):
        
        self.winner = self.get_winner(white_wins, black_wins)

        screen.fill(DARK_WOOD)

        # winner text
        opposite_color = WHITE if self.winner == BLACK else BLACK
        winner_name = "white".upper() if self.winner == WHITE else "black".upper()

        # title text
        
        if self.winner != None:
            self.winner_title = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render("winner is".upper(), True, opposite_color)
            self.winner_name = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render(f"{winner_name}", True, self.winner)
        else:
            self.winner_title = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render("the game".upper(), True, BLACK)
            self.winner_name = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render("is tie".upper(), True, WHITE)


        # possitions

        # title
        self.winner_title_pos_x = WIDTH//2 - self.winner_title.get_width()//2
        self.winner_title_pos_y = WIDTH//10

        self.winner_name_pos_x = WIDTH//2 - self.winner_name.get_width()//2
        self.winner_name_pos_y = WIDTH//5

        # colors text
        self.middle_width = WIDTH//20
        self.col_x_start = WIDTH//20*11
        self.col_y_start = HEIGHT//10*4
        self.col_y_change = HEIGHT//10

        self.color_font = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20)

        self.white_text = self.color_font.render("white".upper(), True, WHITE)
        self.black_text = self.color_font.render("black".upper(), True, BLACK)


        # colors scores
        self.white_score_font = self.color_font.render(f"{white_wins}", True, WHITE)
        self.black_score_font = self.color_font.render(f"{black_wins}", True, BLACK)




        # blit on the screen

        # title
        screen.blit(self.winner_title, (self.winner_title_pos_x, self.winner_title_pos_y))
        screen.blit(self.winner_name, (self.winner_name_pos_x, self.winner_name_pos_y))

        # color text
        screen.blit(self.white_text, (self.col_x_start - self.white_text.get_width() - self.middle_width, self.col_y_start))
        screen.blit(self.black_text, (self.col_x_start - self.black_text.get_width() - self.middle_width, self.col_y_start + self.col_y_change))

        # color score
        screen.blit(self.white_score_font, (self.col_x_start + self.middle_width, self.col_y_start))
        screen.blit(self.black_score_font, (self.col_x_start + self.middle_width, self.col_y_start + self.col_y_change))





        # buttons

        # play again button

        self.play_again_button = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20).render("play again".upper(), True, WHITE)          # play again button font

        self.play_again_button_pos_x = WIDTH//2 - self.play_again_button.get_width()//2                 # play again button possition
        self.play_again_button_pos_y = HEIGHT//4*3

        # play button background possition and dimensions
        self.play_again_button_rect_dimension = (self.play_again_button_pos_x - WIDTH//20, self.play_again_button_pos_y - HEIGHT//200, self.play_again_button.get_width() + WIDTH//10, self.play_again_button.get_height() + HEIGHT//100)

        # change color if user hover the button
        if mouse_pos[0] > self.play_again_button_rect_dimension[0] and mouse_pos[0] < self.play_again_button_rect_dimension[0] + self.play_again_button_rect_dimension[2] and mouse_pos[1] > self.play_again_button_rect_dimension[1] and mouse_pos[1] < self.play_again_button_rect_dimension[1] + self.play_again_button_rect_dimension[3]:
            rect_color = LIGHT_WOOD

        else:
            rect_color = DARKER_WOOD


        # draw play button background
        pygame.draw.rect(screen, rect_color, self.play_again_button_rect_dimension)
        # draw play button
        screen.blit(self.play_again_button, (self.play_again_button_pos_x, self.play_again_button_pos_y))


        # menu button

        self.menu_button = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20).render("menu".upper(), True, BLACK)              # get back to menu button font

        self.menu_button_pos_x = WIDTH//2 - self.menu_button.get_width()//2                 # menu button possition
        self.menu_button_pos_y = HEIGHT//3*2

        # menu button dimensions
        self.menu_button_rect_dimensions = (self.menu_button_pos_x - WIDTH//20, self.menu_button_pos_y - HEIGHT//200, self.menu_button.get_width() + WIDTH//10, self.menu_button.get_height() + HEIGHT//100)

        if mouse_pos[0] > self.menu_button_rect_dimensions[0] and mouse_pos[0] < self.menu_button_rect_dimensions[0] + self.menu_button_rect_dimensions[2] and mouse_pos[1] > self.menu_button_rect_dimensions[1] and mouse_pos[1] < self.menu_button_rect_dimensions[1] + self.menu_button_rect_dimensions[3]:
            rect_menu_color = LIGHT_WOOD
        else:
            rect_menu_color = DARKER_WOOD


        # draw menu button background
        pygame.draw.rect(screen, rect_menu_color, self.menu_button_rect_dimensions)
        # draw menu button
        screen.blit(self.menu_button, (self.menu_button_pos_x, self.menu_button_pos_y))







    def get_winner(self, white_wins, black_wins):
        if white_wins > black_wins:
            return WHITE
        elif black_wins > white_wins:
            return BLACK
        else:
            return None


    def cursor_draw(self, mouse_pos):
        entire_o = pygame.image.load("dama_game/img/entire_o.png")
        broken_x = pygame.image.load("dama_game/img/broken_x.png")
        half_size = entire_o.get_width()//2

        if (mouse_pos[0] > self.play_again_button_rect_dimension[0] and mouse_pos[0] < self.play_again_button_rect_dimension[0] + self.play_again_button_rect_dimension[2] and mouse_pos[1] > self.play_again_button_rect_dimension[1] and mouse_pos[1] < self.play_again_button_rect_dimension[1] + self.play_again_button_rect_dimension[3]) or (mouse_pos[0] > self.menu_button_rect_dimensions[0] and mouse_pos[0] < self.menu_button_rect_dimensions[0] + self.menu_button_rect_dimensions[2] and mouse_pos[1] > self.menu_button_rect_dimensions[1] and mouse_pos[1] < self.menu_button_rect_dimensions[1] + self.menu_button_rect_dimensions[3]):
            screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
        else:
            screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))


    def change_again_to_play(self, mouse_pos):
        if (mouse_pos[0] > self.play_again_button_rect_dimension[0] and mouse_pos[0] < self.play_again_button_rect_dimension[0] + self.play_again_button_rect_dimension[2] and mouse_pos[1] > self.play_again_button_rect_dimension[1] and mouse_pos[1] < self.play_again_button_rect_dimension[1] + self.play_again_button_rect_dimension[3]):
            return True
        else:
            return False


    def change_window_to_menu(self, mouse_pos):
        if (mouse_pos[0] > self.menu_button_rect_dimensions[0] and mouse_pos[0] < self.menu_button_rect_dimensions[0] + self.menu_button_rect_dimensions[2] and mouse_pos[1] > self.menu_button_rect_dimensions[1] and mouse_pos[1] < self.menu_button_rect_dimensions[1] + self.menu_button_rect_dimensions[3]):
            return True
        else:
            return False
