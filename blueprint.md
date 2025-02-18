# Board Representation

bitboard for each piece
INIT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

# Piece bit allocation

7: occupied flag -> 1 = exists, 0 = empty
6: color -> 0 = white, 1 = black
5-3 : piece type -> 000 = Pawn, 001 = Knight, 010 = Bishop, 011 = Rook, 100 = Queen, 101 = King
2-0 : flags -> Can be used for en passant, castling rights, promotions