from creator.create_game import Creator


class ChessChecking:

    def __init__(self):
        self.list_extremities_left = [1, 9, 17, 25, 33, 41, 49, 57]
        self.list_extremities_right = [8, 16, 24, 32, 40, 48, 56, 64]
        self.creator_game = Creator()

    def check_if_chess_available(self):
        self.creator_game.create_chess_board()
        position_king = self.creator_game.ask_piece_placement(self.creator_game.list_pieces[0])
        position_queen = self.creator_game.ask_piece_placement(self.creator_game.list_pieces[1])
        while self.creator_game.check_if_king_queen_same_position(position_king, position_queen):
            print("King and queen cannot be on same position")
            position_queen = self.creator_game.ask_piece_placement("queen")
            self.creator_game.check_if_king_queen_same_position(position_king, position_queen)
        king_int_position = self.creator_game.put_piece_on_board(position_king, self.creator_game.list_pieces[0])[0]
        queen_int_position = self.creator_game.put_piece_on_board(position_queen, self.creator_game.list_pieces[1])[0]
        matrix_updated = self.creator_game.put_piece_on_board(position_queen, self.creator_game.list_pieces[1])[1]
        if (
                king_int_position in self.list_extremities_left and queen_int_position in self.list_extremities_right) and abs(
            king_int_position - queen_int_position) == 7:
            check_type = 1
            return check_type, matrix_updated, position_king, position_queen
        if (
                king_int_position in self.list_extremities_right and queen_int_position in self.list_extremities_left) and abs(
            king_int_position - queen_int_position) == 7:
            check_type = 1
            return check_type, matrix_updated, position_king, position_queen
        if abs(king_int_position - queen_int_position) < 7:
            check_type = 1
            return check_type, matrix_updated, position_king, position_queen
        # check vertically
        elif abs(king_int_position - queen_int_position) % 8 == 0:
            check_type = 2
            return check_type, matrix_updated, position_king, position_queen
        # check diagonally
        square_color_king = self.creator_game.get_color_of_square(position_king)
        square_color_queen = self.creator_game.get_color_of_square(position_queen)
        if abs(king_int_position - queen_int_position) % 9 == 0 and (square_color_king == square_color_king) and\
            (king_int_position not in self.list_extremities_left and queen_int_position not in self.list_extremities_left ):
            check_type = 3
            return check_type, matrix_updated, position_king, position_queen
        if abs(king_int_position - queen_int_position) % 7 == 0 and (square_color_king == square_color_queen):
            check_type = 3
            return check_type, matrix_updated, position_king, position_queen
        else:
            check_type = 0
        return check_type, matrix_updated, position_king, position_queen
