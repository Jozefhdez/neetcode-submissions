class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        n = 9

        # Rows
        for i in range(n):
            for j in range(n):
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
        # Columns
        for j in range(n):
            for i in range(n):
                if board[i][j] in columns[j]:
                    return False
                if board[i][j] != ".":
                    columns[j].add(board[i][j])
        # Boxes
        for i in range(n):
            for j in range(n):
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in boxes[box_index]:
                    return False
                if board[i][j] != ".":
                    boxes[box_index].add(board[i][j])
        
        print(boxes)
        
        return True