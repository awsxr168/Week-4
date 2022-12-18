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

    if input_board[x][y] == "#" or x < 0 or y < 0 or x > len(input_board[0])-1 or y > len(input_board)-1:
        return
    
    input_board[x][y] == new

    # recursive calls for adjacent locations in four directions

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

# Your code has an index out of bound error. 
# It comes from line 30 where you have the line below as the coditions: x > len(input_board[y])-1 or y > len(input_board[x])-1 
# Because your test case has y = 22, which greater than the len(input_board), it will return out of bound, as there does not exist an index for input_board. 
# In addition, you are actually comparing the y-axis for the line: y > len(input_board[x])-1 
# A way you can do to run correct is: x > len(input_board[0])-1 or y > len(input_board)-1. 
# Furthermore, string is immutable in Python, meaning you can not change it by index, you will have to replace the whole string with a new one. 
# This why if you run your code, it does not run properly.