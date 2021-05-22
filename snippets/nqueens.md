```python
from copy import  deepcopy


def place_queen(row, col):
    lst = list(board[row])
    lst[col] = 'Q'
    board[row] = ''.join(lst)

def remove_queen(row, col):
    lst = list(board[row])
    lst[col] = '.'
    board[row] = ''.join(lst)


def solveNQueens(self, n: int) -> List[List[str]]:
    board = ['.'*n for _ in range(n)]
    solutions = []

    def search(row: int, banned_cols: set(), banned_diags: set(), banned_anti_diags: set()):
        for col in range(n):

            # feasibility check
            if col in banned_cols or (row - col in banned_diags) or (row + col in banned_anti_diags):
                continue 

            # assignment
            place_queen(row, col)
            # add constraints associated with assignment
            banned_cols.add(col) # ban column
            banned_diags.add(row - col) # ban diagonals
            banned_anti_diags.add(row + col) # ban anti-diagonal

            if row == n-1:
                solutions.append(deepcopy(board))
            else:
                search(row+1, banned_cols, banned_diags, banned_anti_diags)

            # remove assignment
            remove_queen(row, col)
            # remove constraints
            banned_cols.remove(col)
            banned_diags.discard(row - col)
            banned_anti_diags.discard(row + col)


    search(row=0, banned_cols=set(), banned_diags=set(), banned_anti_diags=set())
    return solutions
```
