class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows

        current_row = 0
        goingdown = False

        for char in s:
            rows[current_row] += char
            if current_row == 0:
                goingdown = True
            elif current_row == numRows -1:
                goingdown = False

            if goingdown:
                current_row += 1
            else:
                current_row -= 1
        output = "".join(rows)
        return output

#Accepted Solution