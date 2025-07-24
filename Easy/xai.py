def solution(board):
    rows, cols = len(board), len(board[0])
    
    board = [list(row) for row in board]
    
    for col in range(cols):
        write_row = rows - 1
        for row in reversed(range(rows)):
            if board[row][col] == '#':
                if write_row != row:
                    board[write_row][col] = '#'
                    board[row][col] = '-'
                write_row -= 1
            elif board[row][col] == '*':
                write_row  = row - 1
                
        for r in  range(write_row + 1):
            if board[r][col] == '#':
                board[r][col] = '-'          
                    
                  
                
    to_clear = set()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '*':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == '#':
                            to_clear.add((nr, nc))
                       
                        
    for r, c in to_clear:
        board[r][c] = '-'    
        
    return[''.join(row) for row in board]
    

