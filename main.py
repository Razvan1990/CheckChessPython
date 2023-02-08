# This is a sample Python script.
from creator.create_game import Creator
from computation.builder import BuildResult

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def run_app():
    #creator_game = Creator()
    # creator_game.create_chess_board()
    # creator_game.print_board()
    # piece_position = creator_game.ask_piece_placement("king")
    # (result1, result2) = creator_game. put_piece_on_board(piece_position,"king")
    # creator_game.print_board()
    # matrix_updated_string = "".join(str(result2))
    # matrix_updated_string = matrix_updated_string.replace("[", "")
    # matrix_updated_string = matrix_updated_string.replace("]", "\n")
    # matrix_updated_string = matrix_updated_string.replace(",", "")
    # print(matrix_updated_string)
    builder = BuildResult()
    builder.create_file()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_app()



    lista = [[2, 3, 4, 5], [" "," "," "]]
    lista[1][1] = 100
    print(lista)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
