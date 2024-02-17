from typing import List, Tuple

class ChessPiece:
    def __init__(self, color: str, position: Tuple[int, int]):
        self.color = color
        self.position = position

    def change_color(self):
        self.color = "white" if self.color == "black" else "black"

    def change_position(self, x: int, y: int):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.position = (x, y)
        else:
            print("Invalid position on the chessboard.")

    def is_valid_move(self, x: int, y: int) -> bool:
        raise NotImplementedError("Abstract method. Subclasses should implement this.")

class Pawn(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для пешки
        pass

class Knight(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для коня
        pass

class Bishop(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для офицера
        pass

class Rook(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для ладьи
        pass

class Queen(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для ферзя
        pass

class King(ChessPiece):
    def is_valid_move(self, x: int, y: int) -> bool:
        # Логика проверки хода для короля
        pass

def valid_moves_for_position(chess_pieces: List[ChessPiece], new_position: Tuple[int, int]) -> List[ChessPiece]:
    valid_pieces = []
    for piece in chess_pieces:
        if piece.is_valid_move(*new_position):
            valid_pieces.append(piece)
    return valid_pieces