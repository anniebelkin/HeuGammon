# Play backgammon
from random import randint

from board import Board
from colour import Colour


def make_move(board, colour):
    dice_roll = [randint(1, 6), randint(1, 6)]
    if dice_roll[0] == dice_roll[1]:
        dice_roll = [dice_roll[0]] * 4
    print("%s rolled %s" % (colour, dice_roll))
    for die_roll in dice_roll:
        valid_pieces = board.get_pieces(colour)
        for piece in valid_pieces:
            if board.is_move_possible(piece, die_roll):
                board.move_piece(piece, die_roll)
                break


i = randint(0, 1)
print('%s goes first' % Colour(i))

board = Board.create_starting_board()
board.print_board()

while True:
    if i % 2 == 0:
        make_move(board, Colour.WHITE)
    else:
        make_move(board, Colour.BLACK)
    board.print_board()
    i = i + 1
    if board.has_game_ended():
        print('%s has won!' % board.who_won())
        break

