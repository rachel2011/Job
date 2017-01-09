"""
1. enumerate- Iterate over indices and items of a list
alist = ['a1', 'a2', 'a3']
for i, a in enumerate(alist):
    print i, a
Result:
0 a1
1 a2
2 a3

2. zip- Iterate over two lists in parallel
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b
Result:[(a1,b1),(a2,b2),(a3,b3)]

zip(*zip(alist, blist))=>[(a1,a2,a3),(b1,b2,b3)]
"""


# We perform a swap on each layer, moving the top edge to the right edge,
# the right to the bottom, and so on. start from outmost layer O(n^2)
def rotate(matrix):
    n = len(matrix) # number of row
    for i in range(n/2 + 1):
        for j in range(i, n-i-1):
            top = matrix[i][j] # save the top layer
            matrix[i][j] = matrix[n-j-1][i] # move the left to the top
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1] #move the bottom to the left
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = top
    return matrix




# Test
matrix = []
print rotate(matrix)

matrix = [[]]
print rotate(matrix)


matrix = [[1,2],[3,4]]
print rotate(matrix)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print rotate(matrix)






