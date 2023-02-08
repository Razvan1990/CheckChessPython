import configparser
import os

from creator.create_game import Creator
from valid_checks.ChessChecking import ChessChecking


class BuildResult:

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.creator_game = Creator()
        self.chess_checking = ChessChecking()


    def create_file(self):
        global result
        self.parser.read(r"G:\pycharm\pythonProject\CheckChess\configuration.ini")
        path = self.parser.get("configuration", "output_path")
        name = self.parser.get("configuration", "output_filename")
        (result_check, matrix_updated, position_king, position_queen)\
            = self.chess_checking.check_if_chess_available()
        matrix_updated_string = "".join(str(matrix_updated))
        matrix_updated_string = matrix_updated_string.replace("[", "")
        matrix_updated_string = matrix_updated_string.replace("]", "\n")
        matrix_updated_string = matrix_updated_string.replace(",", "")
        matrix_updated_string = matrix_updated_string.replace("'", "")
        if result_check == 1:
            result = "Check. It is a horizontal check"
        elif result_check == 2:
            result = "Check. It is a vertical check"
        elif result_check == 3:
            result = "Check. It is a diagonal check"
        else:
            result = "It is not check"
        king_string = "KING POSITION: "+position_king
        queen_string = "QUEEN POSITION: "+position_queen
        output_string = matrix_updated_string + king_string+"\n"+queen_string+"\n"+result
        os.chdir(path)
        with open(file=os.path.join(path, name), mode="w", encoding="utf-8") as f:
            f.write(output_string)
        os.system(os.path.join(path, name))




