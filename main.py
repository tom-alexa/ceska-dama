# Author: Tomáš Alexa
# Program: Dáma

# Czech board game based on american board game checkers. If player jump over enemy piece, enemy piece will be removed.
# Player's goal is to jump over all opponents pieces → player has no other pieces.
# User has many option which he can use in the game,
# e.g. change number of players (2, 1 or AI against AI) or number of pieces in the beginning of the game etc.

# imports
from dama_game.constants import *
from dama_game.board import Board
from dama_game.pieces import Piece
from dama_game.menu import Menu
from dama_game.winner_window import Winner_window
from dama_game.ai_window import AI_window

# pygame initialize
pygame.init()

# set the screen
pygame.display.set_caption("Dáma - Tomáš Alexa")
icon = pygame.image.load("dama_game/img/dama_draw.ico")
pygame.display.set_icon(icon)


def computer_move():
    pieces_list = get_pieces_list()

    possible_moves = []

    for piece in pieces_list:
        if (piece.color == WHITE and turn > 0) or (piece.color == BLACK and turn < 0):
            for possible_move in piece.possible_places:
                possible_moves.append((piece, possible_move))

    comp_move = random.choice(possible_moves)

    chosen_piece = comp_move[0]
    chosen_move = comp_move[1]

    move_function(chosen_piece, chosen_move)


def get_board_position(pos):
    """get position on the board (mouse click) ({1-8}, {1-8})"""
    pos_x = pos[0] - MARK
    pos_y = pos[1] - GAP - MARK

    board_pos_x = pos_x // SQUARE_SIZE + 1
    board_pos_y = ROWS -  (pos_y // SQUARE_SIZE)

    board_pos = (board_pos_x, board_pos_y)

    return board_pos


def move_function(piece, possible_place):
    """Make the move"""
    global turn

    # if piece became queen last move, this property disappears now
    for queen in pieces:
        queen.just_became_queen = False

    piece.move(possible_place, board, pieces)

    # update possible positions
    piece.get_update_possible_places(board)

    # change turn if player can not do double jump
    if (piece.jump and (piece.just_became_queen or not piece.possible_jump)) or (not piece.jump):
        turn *= -1
    
    # if piece can do double jump, select the piece
    if piece.jump and piece.possible_jump and not piece.just_became_queen and number_of_players != 0:
        piece.is_clicked = True
        piece.possible_places = []
        for place in piece.possible_jump:
            piece.possible_places.append(place)


def get_pieces_list():
    """get to know if player has to jump and get pieces list"""

    # variable, it can change
    have_to_jump = False

    # check if there is any piece jumps, if so player has to jump
    for piece in pieces:
        if (piece.color == WHITE and turn > 0) or (piece.color == BLACK and turn < 0):

            # update possible places for piece
            piece.get_update_possible_places(board)

            if piece.possible_jump and not piece.just_became_queen:
                have_to_jump = True

    # create piece list if there is jump available
    pieces_list = []
    for piece in pieces:
        if (piece.color == WHITE and turn > 0) or (piece.color == BLACK and turn < 0):
            if have_to_jump and duty_to_jump:
                for piece in pieces:
                    if piece.possible_jump and not piece.just_became_queen:
                        pieces_list.append(piece)

                        piece.possible_places = []
                        for place in piece.possible_jump:
                            piece.possible_places.append(place)

            # create all possible player moves if there is not any jumps available
            else:
                for piece in pieces:
                    if (piece.color == WHITE and turn > 0) or (piece.color == BLACK and turn < 0):
                        piece.get_update_possible_places(board)
                        if piece.possible_places:
                            pieces_list.append(piece)


    return pieces_list




# when click on board
def board_click(board_mouse_pos):

    pieces_list = get_pieces_list()


    # each piece
    for piece in pieces_list:

        # variable, it can change
        move = False


        # if piece was already picked and mouse possition is equal to one of possible place possitions -> piece makes move
        if piece.is_clicked:
            for possible_place in piece.possible_places:
                if possible_place == board_mouse_pos:
                    
                    # make move
                    move = True
                    move_function(piece, possible_place)



        # if piece did not make move and piece possition is equel to mouse possition -> piece became picked
        if not move:
            if number_of_players == 2 or (number_of_players == 1 and piece.color == player_color):
                if piece.pos == board_mouse_pos:
                    if turn > 0:
                        if piece.color == WHITE:
                            piece.is_clicked = True
                    else:
                        if piece.color == BLACK:
                            piece.is_clicked = True
                else:
                    piece.is_clicked = False






# mouse click when we are in menu
def menu_click(mouse_pos):
    global menu_running, game_running, winner_running, rows_of_pieces, duty_to_jump, number_of_players, player_color, show_advanced_settings, ai_repeating, ai_speed

    change_window = menu.change_window(mouse_pos)
    change_number_of_pieces = menu.change_number_of_pieces(mouse_pos)
    change_duty_to_jump = menu.change_duty_to_jump(mouse_pos)
    change_number_of_players = menu.change_number_of_players(mouse_pos)

    change_color = menu.change_color(mouse_pos)

    if change_window and not show_advanced_settings:

        start_game()            # reset stats
    
        menu_running = False
        winner_running = False
        game_running = True

    elif change_number_of_players:
        number_of_players = number_of_players + 1 if number_of_players < 2 else 0

    elif change_number_of_pieces:
        rows_of_pieces = rows_of_pieces + 1 if rows_of_pieces < 3 else 1

    elif change_duty_to_jump:
        duty_to_jump = not duty_to_jump


    if number_of_players == 1:
        if change_color:
            player_color = WHITE if player_color == BLACK else BLACK


    click_on_dots = menu.check_click_on_dots(mouse_pos, number_of_players)
    if click_on_dots:
        menu_tab(True)
    else:
        menu_tab(False)

    if show_advanced_settings:
        ai_repeating, ai_speed = menu.return_adv_settings(mouse_pos, ai_repeating, ai_speed)


# advance settings for AI
def menu_tab(click):
    global show_advanced_settings

    mouse_pos = pygame.mouse.get_pos()

    if click:
        show_advanced_settings = not show_advanced_settings
    else:
        click_in_box = menu.check_click_in_box(mouse_pos)
        if not click_in_box:
            show_advanced_settings = False




# mouse click when we are in after game window
def winner_click(mouse_pos):
    global menu_running, game_running, winner_running, rows_of_pieces, duty_to_jump, number_of_players, player_color, show_advanced_settings, ai_repeating, ai_speed

    change_window_to_game = winner_window.change_window_to_game(mouse_pos)
    change_window_to_menu = winner_window.change_window_to_menu(mouse_pos)
    change_number_of_pieces = winner_window.change_number_of_pieces(mouse_pos)
    change_duty_to_jump = winner_window.change_duty_to_jump(mouse_pos)
    change_number_of_players = winner_window.change_number_of_players(mouse_pos)

    change_color = winner_window.change_color(mouse_pos)

    if change_window_to_game and not show_advanced_settings:

        start_game()            # reset stats
    
        menu_running = False
        winner_running = False
        game_running = True

    elif change_window_to_menu and not show_advanced_settings:

        menu_running = True
        winner_running = False
        game_running = False

    elif change_number_of_players:
        number_of_players = number_of_players + 1 if number_of_players < 2 else 0

    elif change_number_of_pieces:
        rows_of_pieces = rows_of_pieces + 1 if rows_of_pieces < 3 else 1

    elif change_duty_to_jump:
        duty_to_jump = not duty_to_jump


    if change_color:
        player_color = WHITE if player_color == BLACK else BLACK


    click_on_dots = menu.check_click_on_dots(mouse_pos, number_of_players)
    if click_on_dots:
        menu_tab(True)
    else:
        menu_tab(False)

    if show_advanced_settings:
        ai_repeating, ai_speed = menu.return_adv_settings(mouse_pos, ai_repeating, ai_speed)



# after ai finish its sequence
def ai_window_click(mouse_pos):
    global game_running, ai_window_running, menu_running, white_wins, black_wins

    change_window_to_menu = ai_window.change_window_to_menu(mouse_pos)
    change_again_to_play = ai_window.change_again_to_play(mouse_pos)

    if change_window_to_menu:
        ai_window_running = False
        menu_running = True

        reset_ai()

    elif change_again_to_play:
        start_game()

        ai_window_running = False
        game_running = True




def reset_ai():
    global white_wins, black_wins, current_game_count_ai

    white_wins = 0
    black_wins = 0

    current_game_count_ai = 0





# in game if menu button is clicked
def menu_click_change(mouse_pos):
    global game_running, menu_running, winner_running

    reset_ai()

    game_running = False
    menu_running = True
    winner_running = False

# in game if stop button is clicked
def stop_btn_change(mouse_pos):
    global game_running, ai_window_running

    game_running = False
    ai_window_running = True



# check if there is a winner
def check_winner():
    white_pieces = 0
    black_pieces = 0


    for piece in pieces:
        if piece.color == WHITE:
            white_pieces += 1
        else:
            black_pieces += 1

    possible_moves_list = get_pieces_list()

    winner = None
    if white_pieces == 0:
        winner = BLACK
    elif black_pieces == 0:
        winner = WHITE

    elif not possible_moves_list:
        winner = WHITE if turn < 0 else BLACK


    return winner



# reset stats
def start_game():
    global board, pieces, turn

    board = Board()                     # create board

    pieces = []                         # all pieces

    for i in range(rows_of_pieces):     # create pieces
        for m in range(COLUMNS//2):

            if i % 2 == 0:      # odd line
                piece_white = Piece(WHITE, (1+m*2, i+1), board)
                piece_black = Piece(BLACK, (2+m*2, ROWS-i), board)

            else:               # even line
                piece_white = Piece(WHITE, (2+m*2, i+1), board)
                piece_black = Piece(BLACK, (1+m*2, ROWS-i), board)

            pieces.append(piece_white)      # add to pieces list
            pieces.append(piece_black)

    turn = 1            # white start




# draw cursor
def cursor_draw(mouse_pos):

    entire_o = pygame.image.load("dama_game/img/entire_o.png")
    broken_x = pygame.image.load("dama_game/img/broken_x.png")
    half_size = entire_o.get_width()//2

    if game_running:
        hover_piece = False
        hover_btn = False

        if MARK < mouse_pos[0] < WIDTH - MARK and GAP + MARK < mouse_pos[1] < HEIGHT - MARK:
            board_click_pos = get_board_position(mouse_pos)
            
            for piece in pieces:
                if piece.pos == board_click_pos:
                    hover_piece = True
                    break
        else:
            hover_btn = board.btn_hover(mouse_pos, number_of_players)

        if hover_piece or hover_btn:
            screen.blit(broken_x, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))
        else:
            screen.blit(entire_o, (mouse_pos[0] - half_size, mouse_pos[1] - half_size))

    elif menu_running:
        menu.cursor_draw(mouse_pos, number_of_players, show_advanced_settings)

    elif winner_running:
        winner_window.cursor_draw(mouse_pos, number_of_players, show_advanced_settings, menu)

    elif ai_window_running:
        ai_window.cursor_draw(mouse_pos)


def renew_window():
    """Update view"""

    mouse_pos = pygame.mouse.get_pos()

    if game_running:
        board.draw_board(turn, mouse_pos, number_of_players)          # draw board

        for piece in pieces:            # draw all pieces
            piece.draw_piece()

    elif menu_running:
        menu.draw_menu_window(mouse_pos, rows_of_pieces, duty_to_jump, current_song, number_of_players, player_color, ai_repeating, show_advanced_settings)

    elif winner_running:
        winner_window.draw_winner_window(winner, mouse_pos, rows_of_pieces, duty_to_jump, current_song, number_of_players, player_color, ai_repeating, show_advanced_settings)

    elif ai_window_running:
        ai_window.draw_window(white_wins, black_wins, mouse_pos)



    if show_advanced_settings:
        menu.draw_advanced_settings(ai_repeating, ai_speed, mouse_pos)


    cursor_draw(mouse_pos)


    pygame.display.update()


# main
def main():
    global volume, rows_of_pieces, game_running, menu_running, winner_running, menu, winner_window, winner, rows_of_pieces, duty_to_jump, current_song, number_of_players, player_color, ai_repeating, show_advanced_settings, ai_speed, white_wins, black_wins, ai_window, ai_window_running, current_game_count_ai

    clock = pygame.time.Clock()
    FPS = 60                    # loop replays 60 times in one seconds +-


    # number of rows of pieces in the beginning
    rows_of_pieces = 2      # (1-3)
    duty_to_jump = True
    number_of_players = 1

    # all pages
    game_running = False
    menu_running = True
    winner_running = False
    ai_window_running = False

    ai_window = AI_window()

    winner = WHITE
    player_color = WHITE

    # AI
    ai_repeating = 5
    current_count_ai = 0
    current_game_count_ai = 0
    ai_speed = 5
    ai_speed_one_player = 5

    white_wins = 0
    black_wins = 0


    show_advanced_settings = False

    menu = Menu()
    winner_window = Winner_window()

    volume_change = None    # change by clicking UP key or DOWN key

    pygame.mouse.set_visible(False)     # mouse cursor gets invisible


    # main loop
    running = True
    while running:
        clock.tick(FPS)         # loop replays 60 times in one seconds +-

        # checking each event
        for event in pygame.event.get():

            # close window
            if event.type == pygame.QUIT:
                running = False

            # volume change
            if event.type == pygame.KEYDOWN:
                # volume down
                if event.key == pygame.K_DOWN:
                    volume_change = "down"
                # volume up
                elif event.key == pygame.K_UP:
                    volume_change = "up"

            # volume stops changing
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    volume_change = None

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if game_running:
                        if mouse_pos[0] > MARK and mouse_pos[0] < WIDTH - MARK and mouse_pos[1] > GAP + MARK and mouse_pos[1] < HEIGHT - MARK:
                            board_mouse_pos = get_board_position(mouse_pos)
                            board_click(board_mouse_pos)
                        else:
                            click_on_menu = board.menu_btn_click(mouse_pos)
                            click_on_stop = False
                            if number_of_players == 0:
                                click_on_stop = board.stop_btn_click(mouse_pos)
    
                            if click_on_menu:
                                menu_click_change(mouse_pos)
                            elif click_on_stop:
                                stop_btn_change(mouse_pos)

                    elif menu_running:
                        menu_click(mouse_pos)

                    elif winner_running:
                        winner_click(mouse_pos)

                    elif ai_window_running:
                        ai_window_click(mouse_pos)

            # advanced AI settings
            if event.type == pygame.KEYDOWN:
                if menu_running or winner_running:
                    if event.key == pygame.K_TAB:
                        if number_of_players == 0:
                            menu_tab(True)
                        elif number_of_players == 1:
                            player_color = WHITE if player_color == BLACK else BLACK


            # change song after one is finished
            if event.type == song_finished:
                # randomly choose song from list
                current_song = random.choice(music_list)
                # play the song
                music.load(current_song)
                music.play(0)


        # volume change
        if volume_change == "down":
            volume -= volume_change_number
            music.set_volume(volume)
            if volume < 0:
                volume = 0
        elif volume_change == "up":
            volume += volume_change_number
            music.set_volume(volume)
            if volume > 1:
                volume = 1



        # check if there is a winner
        if game_running:
            winner = check_winner()
            if winner != None:
                if number_of_players != 0:
                    game_running = False
                    menu_running = False
                    winner_running = True
                else:

                    if winner == WHITE:
                        white_wins += 1
                    else:
                        black_wins += 1



                    if ai_repeating == "auto":
                        start_game()


                    elif current_game_count_ai + 1 < ai_repeating:

                        current_game_count_ai += 1


                        start_game()


                    else:

                        game_running = False
                        menu_running = False
                        winner_running = False
                        ai_window_running = True

                        current_game_count_ai = 0


        # if it is computer move -> computer does the move
        if game_running:
            if number_of_players == 1:
                if (player_color == WHITE and turn < 0) or (player_color == BLACK and turn > 0):
    
                    current_count_ai += 1
                    if current_count_ai >= ai_speed_one_player:
                        computer_move()
                        current_count_ai = 0


            elif number_of_players == 0:
                current_count_ai += 1
                if current_count_ai >= ai_speed:
                    computer_move()
                    current_count_ai = 0


        # after each loop get new current screen
        renew_window()

# if the file is not imported to another it calls main part of the program
if __name__ == "__main__":
    main()