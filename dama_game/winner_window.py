import pygame
from dama_game.constants import *


class Winner_window():
    def draw_winner_window(self, winner, mouse_pos, rows_of_pieces, have_to_jump, current_song, number_of_players, player_color, ai_repeating, show_advanced_settings):
        screen.fill(DARK_WOOD)

        # winner text
        opposite_color = WHITE if winner == BLACK else BLACK
        winner_name = "white".upper() if winner == WHITE else "black".upper()

        self.winner_title = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render("winner is".upper(), True, opposite_color)
        self.winner_name = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render(f"{winner_name}", True, winner)

        self.winner_title_pos_x = WIDTH//2 - self.winner_title.get_width()//2
        self.winner_title_pos_y = WIDTH//10

        self.winner_name_pos_x = WIDTH//2 - self.winner_name.get_width()//2
        self.winner_name_pos_y = WIDTH//5





        # blit on the screen
        screen.blit(self.winner_title, (self.winner_title_pos_x, self.winner_title_pos_y))
        screen.blit(self.winner_name, (self.winner_name_pos_x, self.winner_name_pos_y))



        # play again button
        self.play_again_button = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20).render("play again".upper(), True, WHITE)          # play again button font

        self.play_again_button_pos_x = WIDTH//2 - self.play_again_button.get_width()//2                 # play again button possition
        self.play_again_button_pos_y = HEIGHT//2

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


        # get back to menu button
        self.menu_button = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20).render("menu".upper(), True, BLACK)              # get back to menu button font

        self.menu_button_pos_x = WIDTH//2 - self.menu_button.get_width()//2                 # menu button possition
        self.menu_button_pos_y = HEIGHT//5*2

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


        # settings
        self.setting_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//25)               # setting font

        # define relative possitions
        self.setting_pos_x_middle_width = WIDTH//20
        self.setting_pos_x_middle = WIDTH//5*3
        self.setting_pos_y = HEIGHT//3*2
        self.setting_pos_y_change = HEIGHT//15

        # define colors
        self.setting_text_color = WHITE_DARK
        self.setting_value_color = WHITE

        self.number_of_players_text = self.setting_font.render("Number of players", True, self.setting_text_color)      # number of players
        number_of_players = number_of_players if number_of_players != 0 else "AI"
        self.number_of_players_value = self.setting_font.render(f"{number_of_players}", True, self.setting_value_color)


        self.number_of_pieces_text = self.setting_font.render("Number of pieces", True, self.setting_text_color)      # number of pieces
        number_of_pieces = COLUMNS//2 * rows_of_pieces
        self.number_of_pieces_value = self.setting_font.render(f"{number_of_pieces}", True, self.setting_value_color)


        self.duty_to_jump_text = self.setting_font.render("Duty to jump", True, self.setting_text_color)              # duty to jump
        duty_yes_no = "Yes" if have_to_jump else "No"
        self.duty_to_jump_value = self.setting_font.render(f"{duty_yes_no}", True, self.setting_value_color)


        # value background
        self.value_rect_dimensions = (self.setting_pos_x_middle, self.setting_pos_y, WIDTH//10, self.number_of_pieces_value.get_height())

        self.setting_value_background_color = DARKER_WOOD
        self.setting_value_background_color_hover = LIGHT_WOOD

        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]:
            rect_color_number_of_players = self.setting_value_background_color_hover        # number of players
        else:
            rect_color_number_of_players = self.setting_value_background_color
        pygame.draw.rect(screen, rect_color_number_of_players, ((self.value_rect_dimensions[0], self.value_rect_dimensions[1], self.value_rect_dimensions[2], self.value_rect_dimensions[3])))


        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change + self.value_rect_dimensions[3]:
            rect_color_number_of_pieces = self.setting_value_background_color_hover        # number of pieces
        else:
            rect_color_number_of_pieces = self.setting_value_background_color
        pygame.draw.rect(screen, rect_color_number_of_pieces, ((self.value_rect_dimensions[0], self.value_rect_dimensions[1] + self.setting_pos_y_change, self.value_rect_dimensions[2], self.value_rect_dimensions[3])))



        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change*2 and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change*2 + self.value_rect_dimensions[3]:
            rect_color_duty_to_jump = self.setting_value_background_color_hover        # duty to jump
        else:
            rect_color_duty_to_jump = self.setting_value_background_color
        pygame.draw.rect(screen, rect_color_duty_to_jump, ((self.value_rect_dimensions[0], self.value_rect_dimensions[1] + self.setting_pos_y_change*2, self.value_rect_dimensions[2], self.value_rect_dimensions[3])))




        # secondary settings
        self.setting_pos_x_change = WIDTH//8
        if number_of_players != 2:


            if (mouse_pos[0] > self.value_rect_dimensions[0] + self.setting_pos_x_change and mouse_pos[0] < self.value_rect_dimensions[0] + self.setting_pos_x_change + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) or show_advanced_settings:
                rect_color_number_of_players_secondary = self.setting_value_background_color_hover        # number of players secondary
            else:
                rect_color_number_of_players_secondary = self.setting_value_background_color

            pygame.draw.rect(screen, rect_color_number_of_players_secondary, (self.value_rect_dimensions[0] + self.setting_pos_x_change, self.value_rect_dimensions[1], self.value_rect_dimensions[2], self.value_rect_dimensions[3]))

            if number_of_players == 1:
                pygame.draw.rect(screen, player_color, (self.value_rect_dimensions[0] + self.setting_pos_x_change + WIDTH//40, self.value_rect_dimensions[1] + HEIGHT//80, self.value_rect_dimensions[2] - WIDTH//20, self.value_rect_dimensions[3] - HEIGHT//40))

            elif number_of_players == "AI":
                self.three_dots = self.setting_font.render(". . .", True, WHITE)
                screen.blit(self.three_dots, (self.value_rect_dimensions[0] + self.setting_pos_x_change + WIDTH//35, self.value_rect_dimensions[1]))

                self.tab_key = self.setting_font.render("[TAB]", True, WHITE)
                screen.blit(self.tab_key, (self.value_rect_dimensions[0] + self.setting_pos_x_change*2, self.value_rect_dimensions[1]))



        # screen blit

        # number of players
        screen.blit(self.number_of_players_text, (self.setting_pos_x_middle - self.number_of_players_text.get_width() - self.setting_pos_x_middle_width, self.setting_pos_y))
        screen.blit(self.number_of_players_value, (self.setting_pos_x_middle - self.number_of_players_value.get_width()//2 + self.setting_pos_x_middle_width, self.setting_pos_y))

        # number of pieces
        screen.blit(self.number_of_pieces_text, (self.setting_pos_x_middle - self.number_of_pieces_text.get_width() - self.setting_pos_x_middle_width, self.setting_pos_y + self.setting_pos_y_change))
        screen.blit(self.number_of_pieces_value, (self.setting_pos_x_middle - self.number_of_pieces_value.get_width()//2 + self.setting_pos_x_middle_width, self.setting_pos_y + self.setting_pos_y_change))

        # duty to jump
        screen.blit(self.duty_to_jump_text, (self.setting_pos_x_middle - self.duty_to_jump_text.get_width() - self.setting_pos_x_middle_width, self.setting_pos_y + self.setting_pos_y_change*2))
        screen.blit(self.duty_to_jump_value, (self.setting_pos_x_middle - self.duty_to_jump_value.get_width()//2 + self.setting_pos_x_middle_width, self.setting_pos_y + self.setting_pos_y_change*2))



        # current song
        self.current_song = current_song.split("/")[-1].replace(".mp3", "")
        self.current_song_author = self.current_song.split(" - ")[0]
        self.current_song_name = self.current_song.split(" - ")[1]

        self.current_song_author_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//30).render(self.current_song_author, True, BLACK)
        self.current_song_note = pygame.font.Font("dama_game/fonts/musisync.ttf", WIDTH//30).render(" n ", True, WHITE)
        self.current_song_dash = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//30).render("  -  ", True, WHITE)
        self.current_song_name_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//30).render(self.current_song_name, True, WHITE_DARK)


        self.current_song_left_padding = WIDTH//20
        self.current_song_bottom_padding = HEIGHT//20

        # blit on the screen
        screen.blit(self.current_song_note, (WIDTH - self.current_song_author_font.get_width() - self.current_song_name_font.get_width() - self.current_song_dash.get_width() - self.current_song_left_padding - WIDTH//15, HEIGHT - self.current_song_bottom_padding - HEIGHT//300))
        screen.blit(self.current_song_author_font, (WIDTH - self.current_song_author_font.get_width() - self.current_song_name_font.get_width() - self.current_song_dash.get_width() - self.current_song_left_padding, HEIGHT - self.current_song_bottom_padding))
        screen.blit(self.current_song_dash, (WIDTH - self.current_song_dash.get_width() - self.current_song_name_font.get_width() - self.current_song_left_padding, HEIGHT - self.current_song_bottom_padding))
        screen.blit(self.current_song_name_font, (WIDTH - self.current_song_name_font.get_width() - self.current_song_left_padding, HEIGHT - self.current_song_bottom_padding))







    # change window
    def change_window_to_game(self, mouse_pos):     # to game
        if mouse_pos[0] > self.play_again_button_rect_dimension[0] and mouse_pos[0] < self.play_again_button_rect_dimension[0] + self.play_again_button_rect_dimension[2] and mouse_pos[1] > self.play_again_button_rect_dimension[1] and mouse_pos[1] < self.play_again_button_rect_dimension[1] + self.play_again_button_rect_dimension[3]:
            return True
        else:
            return False

    def change_window_to_menu(self, mouse_pos):         # to menu
        if mouse_pos[0] > self.menu_button_rect_dimensions[0] and mouse_pos[0] < self.menu_button_rect_dimensions[0] + self.menu_button_rect_dimensions[2] and mouse_pos[1] > self.menu_button_rect_dimensions[1] and mouse_pos[1] < self.menu_button_rect_dimensions[1] + self.menu_button_rect_dimensions[3]:
            return True
        else:
            return False


    # change number of players
    def change_number_of_players(self, mouse_pos):
        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]:
            return True
        else:
            return False


    # change number of pieces
    def change_number_of_pieces(self, mouse_pos):
        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change + self.value_rect_dimensions[3]:
            return True
        else:
            return False

    # change duty to jump
    def change_duty_to_jump(self, mouse_pos):
        if mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change*2 and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change*2 + self.value_rect_dimensions[3]:
            return True
        else:
            return False


    # if number of player is one, player can choose color
    def change_color(self, mouse_pos):
        if mouse_pos[0] > self.value_rect_dimensions[0] + self.setting_pos_x_change and mouse_pos[0] < self.value_rect_dimensions[0] + self.setting_pos_x_change + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]:
            return True
        else:
            return False



    # draw cursor icon
    def cursor_draw(self, mouse_pos, number_of_players, show_advanced_settings, menu):
        entire_o = pygame.image.load("dama_game/img/entire_o.png")
        broken_x = pygame.image.load("dama_game/img/broken_x.png")
        half_size = entire_o.get_width()//2

        if (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) or (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change + self.value_rect_dimensions[3]) or (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change*2 and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change*2 + self.value_rect_dimensions[3]):
            screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
        else:
            if (mouse_pos[0] > self.value_rect_dimensions[0] + self.setting_pos_x_change and mouse_pos[0] < self.value_rect_dimensions[0] + self.setting_pos_x_change + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) and number_of_players != 2:

                screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

            elif ((mouse_pos[0] > self.play_again_button_rect_dimension[0] and mouse_pos[0] < self.play_again_button_rect_dimension[0] + self.play_again_button_rect_dimension[2] and mouse_pos[1] > self.play_again_button_rect_dimension[1] and mouse_pos[1] < self.play_again_button_rect_dimension[1] + self.play_again_button_rect_dimension[3]) or (mouse_pos[0] > self.menu_button_rect_dimensions[0] and mouse_pos[0] < self.menu_button_rect_dimensions[0] + self.menu_button_rect_dimensions[2] and mouse_pos[1] > self.menu_button_rect_dimensions[1] and mouse_pos[1] < self.menu_button_rect_dimensions[1] + self.menu_button_rect_dimensions[3])) and not show_advanced_settings:
                screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

            elif show_advanced_settings:
                adv_set_hover = menu.cursor_adv(mouse_pos)
                if adv_set_hover:
                    screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
                else:
                    screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

            else:
                screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))