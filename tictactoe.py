class TicTacToe(object):
    """Implement a command line version of Tic-Tac-Toe

    This was the question for the angellist "A-list" interview.
    """

    def play(self):
        current_player = 'X'
        winner = False

        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        while winner is False:
            self.print_board(board)

            board = self.get_user_input(current_player, board)

            winner = self.test_board(board)
            if winner is not False:
                print('%s is the winner!' % winner)
                break

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

    def print_board(self, board):
        for row in board:
            print '|',
            for col in row:
                print '%s ' % col,
            print '|'

    def get_user_input(self, player, board):
        print('It is "%s" turn.' % player)

        while True:
            row = int(raw_input('Select Row'))
            col = int(raw_input('Select Col'))

            if board[row][col] is None:
                board[row][col] = player
                return board
            else:
                print('You cant pick [%s,%s]' % (row, col))

    def test_board(self, board):
        '''Decide if the given board is won

        XXX

        X
        X
        X

        X
         X
          X
        '''
        
    
        for row in board:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] is not None:
                    return row[0]
        
        # test a col
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] is not None:
                    return row[0][col]
        
        # test diagonal
        if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] is not None:
            return board[1][1]

        return False
    
if __name__ == '__main__':
    game = TicTacToe()
    game.play()