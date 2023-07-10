import pygame
from dama_game.constants import *


class Menu():
    def __init__(self):
        self.advance_set_surface = pygame.surface.Surface((int(WIDTH//10*6), int(HEIGHT//2)))
        self.advance_set_surface.fill(LIGHT_WOOD)

        self.adv_set_sur_pos = (WIDTH//2 - self.advance_set_surface.get_width()//2, HEIGHT//10)


        # define relative possitions
        self.setting_pos_x_middle_width = WIDTH//20
        self.setting_pos_x_middle = WIDTH//5*3
        self.setting_pos_y = HEIGHT//3*2
        self.setting_pos_y_change = HEIGHT//15

        self.value_rect_dimensions = (self.setting_pos_x_middle, self.setting_pos_y, WIDTH//10, HEIGHT//22)


        self.advance_set_middle = self.advance_set_surface.get_width()//2
        self.advance_set_x_start = self.advance_set_surface.get_width()//10
        self.advance_set_change_x = self.advance_set_surface.get_width()//10*2
        self.advance_set_change_y = self.advance_set_surface.get_height()//10

        self.value_rect_dimension_width_adv = self.value_rect_dimensions[2]
        self.value_rect_dimension_heigh_adv = self.value_rect_dimensions[3]
        self.value_rect_dimension_y = self.advance_set_change_y*2.5
        self.value_rect_dimension_y_sec = self.advance_set_change_y*6.5
        self.value_rect_dimension_x = self.advance_set_x_start - self.value_rect_dimension_width_adv//2
        self.value_rect_dimension_x_change = self.advance_set_change_x


    # draw window
    def draw_menu_window(self, mouse_pos, rows_of_pieces, have_to_jump, current_song, number_of_players, player_color, ai_repeating, show_advanced_settings):
        screen.fill(DARK_WOOD)


        # play button
        self.play_button = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//20).render("play".upper(), True, WHITE)          # play button font

        self.play_button_pos_x = WIDTH//2 - self.play_button.get_width()//2                 # play button possition
        self.play_button_pos_y = HEIGHT//2

        # play button background possition and dimensions
        self.play_button_rect_dimension = (self.play_button_pos_x - WIDTH//20, self.play_button_pos_y - HEIGHT//200, self.play_button.get_width() + WIDTH//10, self.play_button.get_height() + HEIGHT//100)

        # change color if user hover the button
        if mouse_pos[0] > self.play_button_rect_dimension[0] and mouse_pos[0] < self.play_button_rect_dimension[0] + self.play_button_rect_dimension[2] and mouse_pos[1] > self.play_button_rect_dimension[1] and mouse_pos[1] < self.play_button_rect_dimension[1] + self.play_button_rect_dimension[3]:
            rect_color = LIGHT_WOOD

        else:
            rect_color = DARKER_WOOD


        # draw play button background
        pygame.draw.rect(screen, rect_color, self.play_button_rect_dimension)
        # draw play button
        screen.blit(self.play_button, (self.play_button_pos_x, self.play_button_pos_y))


        # title
        self.title_text = pygame.font.Font("dama_game/fonts/varsity_font.ttf", WIDTH//10).render("dáma".upper(), True, BLACK)       # title font

        self.title_text_pos_x = WIDTH//2 - self.title_text.get_width()//2                   # title possition
        self.title_text_pos_y = HEIGHT//5

        self.author_text = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//20).render("by Tomáš Alexa", True, WHITE_DARK)     # author font

        self.author_text_pos_x = WIDTH//2 - self.author_text.get_width()//2                 # author possition
        self.author_text_pos_y = HEIGHT//10*3

        # blit on the screen
        screen.blit(self.title_text, (self.title_text_pos_x, self.title_text_pos_y))
        screen.blit(self.author_text, (self.author_text_pos_x, self.author_text_pos_y))


        # settings
        self.setting_font = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//25)               # setting font



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
    def change_window(self, mouse_pos):
        if mouse_pos[0] > self.play_button_rect_dimension[0] and mouse_pos[0] < self.play_button_rect_dimension[0] + self.play_button_rect_dimension[2] and mouse_pos[1] > self.play_button_rect_dimension[1] and mouse_pos[1] < self.play_button_rect_dimension[1] + self.play_button_rect_dimension[3]:
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
    def cursor_draw(self, mouse_pos, number_of_players, show_advanced_settings):
        entire_o = pygame.image.load("dama_game/img/entire_o.png")
        broken_x = pygame.image.load("dama_game/img/broken_x.png")
        half_size = entire_o.get_width()//2

        if (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) or (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change + self.value_rect_dimensions[3]) or (mouse_pos[0] > self.value_rect_dimensions[0] and mouse_pos[0] < self.value_rect_dimensions[0] + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] + self.setting_pos_y_change*2 and mouse_pos[1] < self.value_rect_dimensions[1] + self.setting_pos_y_change*2 + self.value_rect_dimensions[3]):
            screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
        else:
            if (mouse_pos[0] > self.value_rect_dimensions[0] + self.setting_pos_x_change and mouse_pos[0] < self.value_rect_dimensions[0] + self.setting_pos_x_change + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) and number_of_players != 2:

                screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

            elif (mouse_pos[0] > self.play_button_rect_dimension[0] and mouse_pos[0] < self.play_button_rect_dimension[0] + self.play_button_rect_dimension[2] and mouse_pos[1] > self.play_button_rect_dimension[1] and mouse_pos[1] < self.play_button_rect_dimension[1] + self.play_button_rect_dimension[3]) and not show_advanced_settings:
                screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

            elif show_advanced_settings:
                adv_set_hover = self.cursor_adv(mouse_pos)
                if adv_set_hover:
                    screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
                else:
                    screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))


            else:
                screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))



    def draw_advanced_settings(self, ai_repeating, ai_speed, mouse_pos):

        mouse_pos = (mouse_pos[0] - self.adv_set_sur_pos[0], mouse_pos[1] - self.adv_set_sur_pos[1])



        # fill surface
        self.advance_set_surface.fill(DARK_WOOD)




        self.adv_set_text_color = WHITE_DARK
        self.adv_set_value_color = BLACK
        self.adv_set_value_color_picked = WHITE


        self.setting_font_adv = pygame.font.Font("dama_game/fonts/coolvetica.ttf", WIDTH//30)


        # ai repeating
        self.ai_repeating_text = self.setting_font_adv.render("AI repeating", True, self.adv_set_text_color)

        if ai_repeating == 1:
            self.adv_set_val_rep_one_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_rep_one_col = self.adv_set_value_color

        if ai_repeating == 5:
            self.adv_set_val_rep_five_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_rep_five_col = self.adv_set_value_color

        if ai_repeating == 25:
            self.adv_set_val_rep_two_five_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_rep_two_five_col = self.adv_set_value_color

        if ai_repeating == 100:
            self.adv_set_val_rep_hundred_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_rep_hundred_col = self.adv_set_value_color

        if ai_repeating == "auto":
            self.adv_set_val_rep_auto_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_rep_auto_col = self.adv_set_value_color

        self.ai_repeating_one = self.setting_font_adv.render("1x", True, self.adv_set_val_rep_one_col)
        self.ai_repeating_five = self.setting_font_adv.render("5x", True, self.adv_set_val_rep_five_col)
        self.ai_repeating_two_five = self.setting_font_adv.render("25x", True, self.adv_set_val_rep_two_five_col)
        self.ai_repeating_hundred = self.setting_font_adv.render("100x", True, self.adv_set_val_rep_hundred_col)
        self.ai_repeating_auto = self.setting_font_adv.render("auto", True, self.adv_set_val_rep_auto_col)


        # draw background rectangles


        self.adv_set_rect_color = DARK_WOOD
        self.adv_set_rect_color_picked = DARKER_WOOD

        if ai_repeating == 1 or (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            self.adv_set_rec_rep_one_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rec_rep_one_col = self.adv_set_rect_color

        if ai_repeating == 5 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            self.adv_set_rec_rep_five_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rec_rep_five_col = self.adv_set_rect_color

        if ai_repeating == 25 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            self.adv_set_rec_rep_two_five_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rec_rep_two_five_col = self.adv_set_rect_color

        if ai_repeating == 100 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            self.adv_set_rec_rep_hundred_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rec_rep_hundred_col = self.adv_set_rect_color

        if ai_repeating == "auto" or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            self.adv_set_rec_rep_auto_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rec_rep_auto_col = self.adv_set_rect_color


        pygame.draw.rect(self.advance_set_surface, self.adv_set_rec_rep_one_col, (self.value_rect_dimension_x, self.value_rect_dimension_y, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rec_rep_five_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change, self.value_rect_dimension_y, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rec_rep_two_five_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*2, self.value_rect_dimension_y, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rec_rep_hundred_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*3, self.value_rect_dimension_y, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rec_rep_auto_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*4, self.value_rect_dimension_y, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))



        # ai speed
        self.ai_speed_text = self.setting_font_adv.render("AI speed", True, self.adv_set_text_color)

        if ai_speed == 50:
            self.adv_set_val_spe_fifty_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_spe_fifty_col = self.adv_set_value_color

        if ai_speed == 30:
            self.adv_set_val_spe_thirty_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_spe_thirty_col = self.adv_set_value_color

        if ai_speed == 20:
            self.adv_set_val_spe_twenty_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_spe_twenty_col = self.adv_set_value_color

        if ai_speed == 5:
            self.adv_set_val_spe_five_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_spe_five_col = self.adv_set_value_color

        if ai_speed == 1:
            self.adv_set_val_spe_max_col = self.adv_set_value_color_picked
        else:
            self.adv_set_val_spe_max_col = self.adv_set_value_color


        self.ai_speed_fifty = self.setting_font_adv.render("v slow", True, self.adv_set_val_spe_fifty_col)
        self.ai_speed_thirty = self.setting_font_adv.render("slow", True, self.adv_set_val_spe_thirty_col)
        self.ai_speed_twenty = self.setting_font_adv.render("mid", True, self.adv_set_val_spe_twenty_col)
        self.ai_speed_five = self.setting_font_adv.render("fast", True, self.adv_set_val_spe_five_col)
        self.ai_speed_max = self.setting_font_adv.render("v fast", True, self.adv_set_val_spe_max_col)



        # draw background rectangles

    
        if ai_speed == 50 or (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            self.adv_set_rect_spe_fifty_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rect_spe_fifty_col = self.adv_set_rect_color

        if ai_speed == 30 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            self.adv_set_rect_spe_thirty_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rect_spe_thirty_col = self.adv_set_rect_color

        if ai_speed == 20 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            self.adv_set_rect_spe_twenty_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rect_spe_twenty_col = self.adv_set_rect_color

        if ai_speed == 5 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            self.adv_set_rect_spe_five_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rect_spe_five_col = self.adv_set_rect_color

        if ai_speed == 1 or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            self.adv_set_rect_spe_max_col = self.adv_set_rect_color_picked
        else:
            self.adv_set_rect_spe_max_col = self.adv_set_rect_color

        pygame.draw.rect(self.advance_set_surface, self.adv_set_rect_spe_fifty_col, (self.value_rect_dimension_x, self.value_rect_dimension_y_sec, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rect_spe_thirty_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change, self.value_rect_dimension_y_sec, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rect_spe_twenty_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*2, self.value_rect_dimension_y_sec, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rect_spe_five_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*3, self.value_rect_dimension_y_sec, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))
        pygame.draw.rect(self.advance_set_surface, self.adv_set_rect_spe_max_col, (self.value_rect_dimension_x + self.value_rect_dimension_x_change*4, self.value_rect_dimension_y_sec, self.value_rect_dimension_width_adv, self.value_rect_dimension_heigh_adv))


        # blit advanced settings

        # blit ai repeating
        self.advance_set_surface.blit(self.ai_repeating_text, (self.advance_set_middle - self.ai_repeating_text.get_width()//2, self.advance_set_change_y))

        self.advance_set_surface.blit(self.ai_repeating_one, (self.advance_set_x_start - self.ai_repeating_five.get_width()//2, self.advance_set_change_y*2.5))
        self.advance_set_surface.blit(self.ai_repeating_five, (self.advance_set_x_start + self.advance_set_change_x - self.ai_repeating_one.get_width()//2, self.advance_set_change_y*2.5))
        self.advance_set_surface.blit(self.ai_repeating_two_five, (self.advance_set_x_start + self.advance_set_change_x*2 - self.ai_repeating_two_five.get_width()//2, self.advance_set_change_y*2.5))
        self.advance_set_surface.blit(self.ai_repeating_hundred, (self.advance_set_x_start + self.advance_set_change_x*3 - self.ai_repeating_hundred.get_width()//2, self.advance_set_change_y*2.5))
        self.advance_set_surface.blit(self.ai_repeating_auto, (self.advance_set_x_start + self.advance_set_change_x*4 - self.ai_repeating_auto.get_width()//2, self.advance_set_change_y*2.5))

        # blit ai speed
        self.advance_set_surface.blit(self.ai_speed_text, (self.advance_set_middle - self.ai_speed_text.get_width()//2, self.advance_set_change_y*5))

        self.advance_set_surface.blit(self.ai_speed_fifty, (self.advance_set_x_start - self.ai_speed_fifty.get_width()//2, self.advance_set_change_y*6.5))
        self.advance_set_surface.blit(self.ai_speed_thirty, (self.advance_set_x_start + self.advance_set_change_x - self.ai_speed_thirty.get_width()//2, self.advance_set_change_y*6.5))
        self.advance_set_surface.blit(self.ai_speed_twenty, (self.advance_set_x_start + self.advance_set_change_x*2 - self.ai_speed_twenty.get_width()//2, self.advance_set_change_y*6.5))
        self.advance_set_surface.blit(self.ai_speed_five, (self.advance_set_x_start + self.advance_set_change_x*3 - self.ai_speed_five.get_width()//2, self.advance_set_change_y*6.5))
        self.advance_set_surface.blit(self.ai_speed_max, (self.advance_set_x_start + self.advance_set_change_x*4 - self.ai_speed_max.get_width()//2, self.advance_set_change_y*6.5))

        # blit advanced settings surface
        screen.blit(self.advance_set_surface, (self.adv_set_sur_pos[0], self.adv_set_sur_pos[1]))





    def check_click_in_box(self, mouse_pos):
        if mouse_pos[0] > WIDTH//2 - self.advance_set_surface.get_width()//2 and mouse_pos[0] < WIDTH//2 - self.advance_set_surface.get_width()//2 + int(WIDTH//10*6) and mouse_pos[1] > HEIGHT//10 and mouse_pos[1] < HEIGHT//10 + int(HEIGHT//2):
            return True
        else:
            return False

    def check_click_on_dots(self, mouse_pos, number_of_players):
        if (mouse_pos[0] > self.value_rect_dimensions[0] + self.setting_pos_x_change and mouse_pos[0] < self.value_rect_dimensions[0] + self.setting_pos_x_change + self.value_rect_dimensions[2] and mouse_pos[1] > self.value_rect_dimensions[1] and mouse_pos[1] < self.value_rect_dimensions[1] + self.value_rect_dimensions[3]) and number_of_players == 0:
            return True
        else:
            return False

    def return_adv_settings(self, mouse_pos, ai_repeating, ai_speed):
        mouse_pos = (mouse_pos[0] - self.adv_set_sur_pos[0], mouse_pos[1] - self.adv_set_sur_pos[1])

        if (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            ai_repeating = 1
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            ai_repeating = 5
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            ai_repeating = 25
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            ai_repeating = 100
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv):
            ai_repeating = "auto"

        elif (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            ai_speed = 50
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            ai_speed = 30
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            ai_speed = 20
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            ai_speed = 5
        elif (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            ai_speed = 1
        return ai_repeating, ai_speed

    def cursor_adv(self, mouse_pos):
        mouse_pos = (mouse_pos[0] - self.adv_set_sur_pos[0], mouse_pos[1] - self.adv_set_sur_pos[1])

        if (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y and mouse_pos[1] < self.value_rect_dimension_y + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x and mouse_pos[0] < self.value_rect_dimension_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*2 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*2 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*3 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*3 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv) or (mouse_pos[0] > self.value_rect_dimension_x + self.advance_set_change_x*4 and mouse_pos[0] < self.value_rect_dimension_x + self.advance_set_change_x*4 + self.value_rect_dimension_width_adv and mouse_pos[1] > self.value_rect_dimension_y_sec and mouse_pos[1] < self.value_rect_dimension_y_sec + self.value_rect_dimension_heigh_adv):
            return True
        else:
            return False