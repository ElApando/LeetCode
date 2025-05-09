"""
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
"""

st_word = "PAYPALISHIRING"#"PAYPALISHIRING"#
in_row = 3
in_count = 0
in_add = 1
st_save = ""
ls_save = []
di_save = {}

ls_rows = [[] for _ in range(in_row)]

for ii in st_word:

    ls_rows[in_count].append(ii)

    if in_count == 0:
        in_add = 1
    elif in_count == in_row - 1:
        in_add = -1

    in_count = in_count + in_add


for ii  in ls_rows:
    for jj in ii:
        print(jj)

print("".join(jj for ii in ls_rows for jj in ii ))
