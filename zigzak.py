def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ['' for _ in range(numRows)]
    curr_row = 0
    going_down = False

    for char in s:
        rows[curr_row] += char
        # Change direction at top or bottom
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1

    return ''.join(rows)
