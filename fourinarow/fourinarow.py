import numpy as np

class FPR:
    def __init__(self, N):
        self.N = N
        self.board = np.zeros((self.N,self.N))
        #PLAYER 1 = 1
        #PLAYER 2 = -1

    def winner(self):
        N = self.N
        win = 0
        for i in range(N-4):
            for j in range(N):
                temp = np.sum(self.board[i:i+4,j])
                if temp == 4:
                    win = 1
                elif temp == -4:
                    win = -1

        for i in range(N):
            for j in range(N-4):
                temp = np.sum(self.board[i,j:j+4])
                if temp == 4:
                    win = 1
                elif temp == -4:
                    win = -1

        for i in range(-N+1, N):
            diag = np.diagonal(self.board, i)
            if len(diag) >= 4:
                for j in range(len(diag)-3):
                    temp = np.sum(diag[j:j+4])
                    if temp == 4:
                        win = 1
                    elif temp == -4:
                        win = -1

        boardT = np.rot90(self.board)
        for i in range(-N+1, N):
            diag = np.diagonal(boardT, i)
            if len(diag) >= 4:
                for j in range(len(diag)-3):
                    temp = np.sum(diag[j:j+4])
                    if temp == 4:
                        win = 1
                    elif temp == -4:
                        win = -1
        return win

    def play(self):
        turn = 0
        board = self.board
        while self.winner() == 0:
            if turn%2 == 0:
                player = 1
            else:
                player = -1
            print(board)
            move = int(input(f"make a move bitch (player {player})")) - 1
            self.make_a_move(player, move)
            turn += 1
        print(board)
        print("WINNER!!!! ", self.winner())

    def make_a_move(self, player, move):
        board = self.board
        for i in range(7, -1, -1):
            if board[i, move] == 0:
                board[i, move] = player
                break

        

if __name__ == "__main__":
    fpr = FPR(8)
    fpr.play()