import time


class Board:

    def __init__(self):
        self.board = [" " for _ in range(1, 10)]
        self.turn = 1
        self.p1 = "0"
        self.p2 = "X"

    def name_p1(self, player_name):
        self.p1 = player_name.upper()

    def name_p2(self, player_name):
        self.p2 = player_name.upper()

    def play_game(self):
        while self.turn <= 9:

            if self.turn % 2 != 0:
                imp_choice = input(f'Please select where you would like to place your {self.p1} token in\n'
                                   'or type "s" to show the board:\n')
                self.place(imp_choice, self.p1)
            else:
                imp_choice = input(f'Please select where you would like to place your {self.p2} token in\n'
                                   'or type "s" to show the board:\n')
                self.place(imp_choice, self.p2)

    # sets where the token is placed and if it can be placed there
    def place(self, choice, player):

        # does the token placement follow rules
        if choice.isnumeric() and 0 < int(choice) < 10:

            # is it an empty cell
            if self.board[int(choice)-1] == " ":
                print(f'\nplayer {player} puts an "{player}" in cell {choice}')
                self.board[int(choice)-1] = player  # updates the cell with he player token
                self.turn += 1  # updates turn counter
                self.show_board()
                self.win_cond()  # checks win conditions
                self.play_game()  # starts next round

            # the cell is taken
            elif self.board[int(choice)-1] != " ":
                print(f"\ncell {choice} is taken, please pick another cell")

        # show board
        elif choice.casefold() == "s":
            self.show_board("y")

        # return for invalid input
        else:
            input("\nInvalid input, please press enter to continue\n")

    def show_board(self, guide="n"):
        counter = 1
        output = ""

        # with guide showing cell numbers
        if guide.casefold() == "y":
            for position, cells in enumerate(self.board):
                output += f"[{cells}] "
                if position == 2:
                    output += "\t\t [1] [2] [3]\n"
                if position == 5:
                    output += "\t=\t [4] [5] [6]\n"
                if position == 8:
                    output += "\t\t [7] [8] [9]"
                counter += 1
            output += "\n\nGame board\t\t\t\tGuide"

        # without guide
        else:
            for cells in self.board:
                output += f"[{cells}] "
                if counter % 3 == 0 and counter != 9:
                    output += "\n"
                counter += 1

        print(f"{output}\n")

    def win_cond(self):
        diagonal_1_9 = "".join(self.board[::4])
        diagonal_3_7 = "".join(self.board[2:7:2])

        # across or down
        for cell in range(0, 3):
            row = "".join(self.board[cell*3:(cell+1)*3])
            column = "".join(self.board[cell::3])
            if row.count(self.p1) == 3 or column.count(self.p1) == 3:
                print(f'{"*"*16}\n Player {self.p1} wins! \n{"*"*16}')
                self.new_game()
            elif row.count(self.p2) == 3 or column.count(self.p2) == 3:
                print(f'{"*"*16}\n Player {self.p2} wins! \n{"*"*16}')
                self.new_game()

        # diagonal
        if diagonal_1_9.count(self.p1) == 3 or diagonal_3_7.count(self.p1) == 3:
            print(f'{"*"*16}\n Player {self.p1} wins! \n{"*"*16}')
            self.new_game()
        elif diagonal_1_9.count(self.p2) == 3 or diagonal_3_7.count(self.p2) == 3:
            print(f'{"*"*16}\n Player {self.p2} wins! \n{"*"*16}')
            self.new_game()

        # full board but no winner
        if (self.board.count(self.p1)+self.board.count(self.p2)) == 9:
            self.show_board()
            print(f'{"*"*23}\n Full board, no winner \n{"*"*23}')
            self.new_game()
        else:
            pass

    def new_game(self):
        new = input('press enter to start a new game or type "e" to quit:\n')
        if new.casefold() == "e":
            print("\nTic-Tac-Toe game will close in 3 seconds")
            time.sleep(3)
            exit()
        else:
            while True:
                new_names = input("would you like to use new player names? y/n:")
                if new_names.casefold() == "y":
                    main()
                elif new_names.casefold() == "n":
                    time.sleep(1)
                    for sec in range(0, 3):
                        print(3-sec)
                        time.sleep(1)
                    self.board = [" " for _ in range(1, 10)]
                    self.turn = 1
                    print("Board reset\n")
                    self.show_board("y")
                else:
                    print("\n*** Sequence not recognised ***")


def main():
    dash = "-"*40
    # title
    print(f"{dash}\n"
          "\t\t\t  TIC TACK TOE"
          f"\n{dash}")

    ox = Board()
    while True:
        # player one name loop
        p1 = input('Player 1 is "0" as default.\n'
                   'Please choose a letter or number to represent yourself or press enter to keep default:\n')
        # input can only be blank or length 1
        if len(p1) > 1:
            print("\n*** Sequence not recognised ***")
            continue
        elif len(p1) <= 1:
            # if letter entered for player 1, change name to this
            if len(p1) == 1:
                ox.name_p1(p1)
        break

    # player one complete, run player 2 name loop
    while True:
        # player two name
        p2 = input('Player 2 is "X" as default.\n'
                   'Please choose a letter or number to represent yourself or press enter to keep default:\n')
        # input can only be blank or length 1
        if len(p2) > 1:
            print("\n*** Sequence not recognised ***")
        # both players can not be the same unless blank as it goes to default values
        if p2 == p1 and (p1+p2).isalnum():
            print("\nBoth player names can not be the same.")
            time.sleep(1)
        elif len(p2) <= 1:
            # if letter entered for player 2, change name to this
            if len(p2) == 1:
                ox.name_p2(p2)
            # initialise the game
            input('\nFor this game of Tic-Tack-Toe:\n'
                  f'Player 1 will be using {ox.p1} as their token\n'
                  f'Player 2 will be using {ox.p2} as their token\n'
                  'Press enter to start.\n')
            ox.show_board("y")
            ox.play_game()


if __name__ == "__main__":

    main()
