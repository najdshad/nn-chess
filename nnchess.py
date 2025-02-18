import numpy as np

class Piece:
    def __init__(self, piece: np.byte):
        self.piece = piece

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

x = Piece(0x88)

print(x.name())


# def fen_to_board(fen):
#     for row in fen.split('/'):


bitboard = np.array(np.zeros((8, 8)), dtype=bool)
INIT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen = INIT_FEN

