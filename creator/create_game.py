class Creator:

    def __init__(self):
        self.chess_board = list()
        self.chess_colors = list()
        self.list_pieces = ["king", "queen"]
        self.list_pieces_abreviated = ["K", "Q"]

    '''
Apparently in python, if you define the list with 2 lists and using a for loop with some condition, it seems that when you try to modify a value from the list of lists(matrix), it /
modifies the entire column with that value. In this case we need to put them like below, with individual lists
    '''

    def create_chess_board(self):

        lines_list1 = [" -", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list1 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "8"]
        self.chess_board.append(lines_list1)
        self.chess_board.append(squares_list1)
        lines_list2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list2 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "7"]
        self.chess_board.append(lines_list2)
        self.chess_board.append(squares_list2)
        lines_list3 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list3 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "6"]
        self.chess_board.append(lines_list3)
        self.chess_board.append(squares_list3)
        lines_list4 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list4 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "5"]
        self.chess_board.append(lines_list4)
        self.chess_board.append(squares_list4)
        lines_list4 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list4 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "4"]
        self.chess_board.append(lines_list4)
        self.chess_board.append(squares_list4)
        lines_list5 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list5 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "3"]
        self.chess_board.append(lines_list5)
        self.chess_board.append(squares_list5)
        lines_list6 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list6 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "2"]
        self.chess_board.append(lines_list6)
        self.chess_board.append(squares_list6)
        lines_list7 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list7 = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", "1"]
        self.chess_board.append(lines_list7)
        self.chess_board.append(squares_list7)
        lines_list8 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
        squares_list8 = [" ", "A", " ", "B", " ", "C", " ", "D", " ", "E", " ", "F", " ", "G", " ", "H", " "]
        self.chess_board.append(lines_list8)
        self.chess_board.append(squares_list8)

    def create_color_board(self):
        list_white1 = ["W", "B", "W", "B", "W", "B", "W", "B"]
        list_black1 = ["B", "W", "B", "W", "B", "W", "B", "W"]
        list_white2 = ["W", "B", "W", "B", "W", "B", "W", "B"]
        list_black2 = ["B", "W", "B", "W", "B", "W", "B", "W"]
        list_white3 = ["W", "B", "W", "B", "W", "B", "W", "B"]
        list_black3 = ["B", "W", "B", "W", "B", "W", "B", "W"]
        list_white4 = ["W", "B", "W", "B", "W", "B", "W", "B"]
        list_black4 = ["B", "W", "B", "W", "B", "W", "B", "W"]
        self.chess_colors.append(list_white1);self.chess_colors.append(list_black1)
        self.chess_colors.append(list_white2)
        self.chess_colors.append(list_black2)
        self.chess_colors.append(list_white3)
        self.chess_colors.append(list_black3)
        self.chess_colors.append(list_white4)
        self.chess_colors.append(list_black4)

    def print_board(self):
        for i in range(0, len(self.chess_board)):
            for j in range(0, len(self.chess_board[i])):
                print(self.chess_board[i][j], end="")
            print()

    def check_conditions_of_piece_input(self, piece_position):
        if len(piece_position) > 2:
            return 1
        elif (ord(piece_position[0]) < 65 or ord(piece_position[0]) > 72) or (
                ord(piece_position[1]) < 49 or ord(piece_position[1]) > 56):
            return 2
        else:
            return 0

    def ask_piece_placement(self, piece_name):
        print("Please introduce the {} position".format(piece_name))
        king_position = input("").upper()
        condition_value = self.check_conditions_of_piece_input(king_position)
        while condition_value == 1 or condition_value == 2:
            if condition_value == 1:
                print("Position must contain just 2 characters. Introduce again")
                king_position = input("").upper()
                condition_value = self.check_conditions_of_piece_input(king_position)
            elif condition_value == 2:
                print("Not correct board position. Please introduce a letter through a to h and a digit from 0 to 8")
                king_position = input("").upper()
                condition_value = self.check_conditions_of_piece_input(king_position)
        return king_position

    def check_if_king_queen_same_position(self, king_position, queen_position):
        if king_position == queen_position:
            return True
        return False

    def get_color_of_square(self, piece_position):
        if piece_position[0] == "A":
            if int(piece_position[1]) % 2 == 0:
                return "black"
            else:
                return "white"
        if piece_position[0] == "B":
            if int(piece_position[1]) % 2 == 0:
                return "white"
            else:
                return "black"
        if piece_position[0] == "C":
            if int(piece_position[1]) % 2 == 0:
                return "black"
            else:
                return "white"
        if piece_position[0] == "D":
            if int(piece_position[1]) % 2 == 0:
                return "white"
            else:
                return "black"
        if piece_position[0] == "E":
            if int(piece_position[1]) % 2 == 0:
                return "black"
            else:
                return "white"
        if piece_position[0] == "F":
            if int(piece_position[1]) % 2 == 0:
                return "white"
            else:
                return "black"
        if piece_position[0] == "G":
            if int(piece_position[1]) % 2 == 0:
                return "black"
            else:
                return "white"
        if piece_position[0] == "H":
            if int(piece_position[1]) % 2 == 0:
                return "white"
            else:
                return "black"

    def put_piece_on_board(self, piece_position, piece_name):
        global character
        global new_position
        if piece_name == self.list_pieces[0]:
            character = self.list_pieces_abreviated[0]
        elif piece_name == self.list_pieces[1]:
            character = self.list_pieces_abreviated[1]
        result_position = 0

        # A ROW
        if piece_position == "A1":
            self.chess_board[15][1] = character
            result_position = 1
        elif piece_position == "A2":
            self.chess_board[13][1] = character
            result_position = 9
        elif piece_position == "A3":
            self.chess_board[11][1] = character
            result_position = 17
        elif piece_position == "A4":
            self.chess_board[9][1] = character
            result_position = 25
        elif piece_position == "A5":
            self.chess_board[7][1] = character
            result_position = 33
        elif piece_position == "A6":
            self.chess_board[5][1] = character
            result_position = 41
        elif piece_position == "A7":
            self.chess_board[3][1] = character
            result_position = 49
        elif piece_position == "A8":
            self.chess_board[1][1] = character
            result_position = 57

        # B ROW
        elif piece_position == "B1":
            self.chess_board[15][3] = character
            result_position = 2
        elif piece_position == "B2":
            self.chess_board[13][3] = character
            result_position = 10
        elif piece_position == "B3":
            self.chess_board[11][3] = character
            result_position = 18
        elif piece_position == "B4":
            self.chess_board[9][3] = character
            result_position = 26
        elif piece_position == "B5":
            self.chess_board[7][3] = character
            result_position = 34
        elif piece_position == "B6":
            self.chess_board[5][3] = character
            result_position = 42
        elif piece_position == "B7":
            self.chess_board[3][3] = character
            result_position = 50
        elif piece_position == "B8":
            self.chess_board[1][3] = character
            result_position = 58

        # C ROW
        elif piece_position == "C1":
            self.chess_board[15][5] = character
            result_position = 3
        elif piece_position == "C2":
            self.chess_board[13][5] = character
            result_position = 11
        elif piece_position == "C3":
            self.chess_board[11][5] = character
            result_position = 19
        elif piece_position == "C4":
            self.chess_board[9][5] = character
            result_position = 27
        elif piece_position == "C5":
            self.chess_board[7][5] = character
            result_position = 35
        elif piece_position == "C6":
            self.chess_board[5][5] = character
            result_position = 43
        elif piece_position == "C7":
            self.chess_board[3][5] = character
            result_position = 51
        elif piece_position == "C8":
            self.chess_board[1][5] = character
            result_position = 59

            # D ROW
        elif piece_position == "D1":
            self.chess_board[15][7] = character
            result_position = 4
        elif piece_position == "D2":
            self.chess_board[13][7] = character
            result_position = 12
        elif piece_position == "D3":
            self.chess_board[11][7] = character
            result_position = 20
        elif piece_position == "D4":
            self.chess_board[9][7] = character
            result_position = 28
        elif piece_position == "D5":
            self.chess_board[7][7] = character
            result_position = 36
        elif piece_position == "D6":
            self.chess_board[5][7] = character
            result_position = 44
        elif piece_position == "D7":
            self.chess_board[3][7] = character
            result_position = 52
        elif piece_position == "D8":
            self.chess_board[1][7] = character
            result_position = 60

            # E ROW
        elif piece_position == "E1":
            self.chess_board[15][9] = character
            result_position = 5
        elif piece_position == "E2":
            self.chess_board[13][9] = character
            result_position = 13
        elif piece_position == "E3":
            self.chess_board[11][9] = character
            result_position = 21
        elif piece_position == "E4":
            self.chess_board[9][9] = character
            result_position = 29
        elif piece_position == "E5":
            self.chess_board[7][9] = character
            result_position = 37
        elif piece_position == "E6":
            self.chess_board[5][9] = character
            result_position = 45
        elif piece_position == "E7":
            self.chess_board[3][9] = character
            result_position = 53
        elif piece_position == "E8":
            self.chess_board[1][9] = character
            result_position = 61

            # F ROW
        elif piece_position == "F1":
            self.chess_board[15][11] = character
            result_position = 6
        elif piece_position == "F2":
            self.chess_board[13][11] = character
            result_position = 14
        elif piece_position == "F3":
            self.chess_board[11][11] = character
            result_position = 22
        elif piece_position == "F4":
            self.chess_board[9][11] = character
            result_position = 30
        elif piece_position == "F5":
            self.chess_board[7][11] = character
            result_position = 38
        elif piece_position == "F6":
            self.chess_board[5][11] = character
            result_position = 46
        elif piece_position == "F7":
            self.chess_board[3][11] = character
            result_position = 54
        elif piece_position == "F8":
            self.chess_board[1][11] = character
            result_position = 62

            # G ROW
        elif piece_position == "G1":
            self.chess_board[15][13] = character
            result_position = 7
        elif piece_position == "G2":
            self.chess_board[13][13] = character
            result_position = 15
        elif piece_position == "G3":
            self.chess_board[11][13] = character
            result_position = 23
        elif piece_position == "G4":
            self.chess_board[9][13] = character
            result_position = 31
        elif piece_position == "G5":
            self.chess_board[7][13] = character
            result_position = 39
        elif piece_position == "G6":
            self.chess_board[5][13] = character
            result_position = 47
        elif piece_position == "G7":
            self.chess_board[3][13] = character
            result_position = 55
        elif piece_position == "G8":
            self.chess_board[1][13] = character
            result_position = 63

            # H ROW
        elif piece_position == "H1":
            self.chess_board[15][15] = character
            result_position = 8
        elif piece_position == "H2":
            self.chess_board[13][15] = character
            result_position = 16
        elif piece_position == "H3":
            self.chess_board[11][15] = character
            result_position = 24
        elif piece_position == "H4":
            self.chess_board[9][15] = character
            result_position = 32
        elif piece_position == "H5":
            self.chess_board[7][15] = character
            result_position = 40
        elif piece_position == "H6":
            self.chess_board[5][15] = character
            result_position = 48
        elif piece_position == "H7":
            self.chess_board[3][15] = character
            result_position = 56
        elif piece_position == "H8":
            self.chess_board[1][15] = character
            result_position = 64
        return result_position, self.chess_board
