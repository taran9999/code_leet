def solution(board):
    # store sets corresponding to each row, column, and sub-box
    row_nums = {}
    col_nums = {}
    box_nums = {}

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != ".":
                # if found a number, append it to the corresponding sets
                num = int(board[row][col])
                if row not in row_nums:
                    row_nums[row] = set()
                else:
                    if num in row_nums[row]: return False
                row_nums[row].add(num)

                if col not in col_nums:
                    col_nums[col] = set()
                else:
                    if num in col_nums[col]: return False
                col_nums[col].add(num)

                # calculate the box num with integer division: col / 3 + (row / 3) * 3
                # 0, 1, 2, 3, 4, 5, 6, 7, 8: left to right, top to bottom
                box = (col // 3) + 3 * (row // 3)
                if box not in box_nums:
                    box_nums[box] = set()
                else:
                    if num in box_nums[box]: return False
                box_nums[box].add(num)

    return True
