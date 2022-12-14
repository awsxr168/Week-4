from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

assert all(len(row) == len(board[0]) for row in board), f"The board should have lines of equal length."

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    if input_board[x][y] != old or x < 0 or y < 0 or x > len(input_board[y])-1 or y > len(input_board[x])-1:
        return
    
    input_board[x][y] == new
    
    # recursion
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x, y-1)
    flood_fill(input_board, old, new, x, y+1)

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
