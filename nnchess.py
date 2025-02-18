import numpy as np

INIT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

class Piece:
    def __init__(self, piece: np.byte, position: np.array):
        self.piece = piece
        self.position = position

    def name(self):
        type = (self.piece >> 3) & 0b111  # Extract bits 5-3
        color = (self.piece >> 5) & 1 # Extract bit 6
        name: str = ''

        match color:
            case 0b0:
                name = 'White '
            case 0b1:
                name = 'Black '

        match type:
            case 0b000:
                name += 'Pawn'
            case 0b001:
                name += 'Knight'
            case 0b010:
                name += 'Bishop'
            case 0b011:
                name += 'Rook'
            case 0b100:
                name += 'Queen'
            case 0b101:
                name += 'King'

        return name
    
    def move(self):
        pass


class Board:
    def __init__(self):
        self.fen = INIT_FEN
        self.bitboard = np.array(np.zeros((8, 8)), dtype=bool)
        self.pieces = np.array(dtype=Piece)

    def add_piece(self, piece: Piece):
        self.pieces.append(piece)

    def initialize_board(self):
        for piece in self.pieces:
            pass




if __name__ == "__main__":
    x = Piece(0x88)
    board = Board()
    print(x.name())
    print(board.fen_to_board(INIT_FEN))
    