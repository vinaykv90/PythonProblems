'''
Zigzag Conversion - LC 6 - Medium - Array

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        numCols = math.ceil(n / (2 * numRows - 2)) * (numRows - 1)

        result = [[" "] * numCols for _ in range(numRows)]

        curRow, curCol = 0, 0
        index = 0

        while index < n:
            while curRow < numRows and index < n:
                result[curRow][curCol] = s[index]
                curRow += 1
                index += 1
            
            curRow -= 2
            curCol += 1

            while curRow > 0 and curCol < numCols and index < n:
                result[curRow][curCol] = s[index]
                curRow -= 1
                curCol += 1
                index += 1
            
        final = ''    
        for i in result:
            final += ''.join(i)
        
        return final.replace(' ', '')        
        return result
