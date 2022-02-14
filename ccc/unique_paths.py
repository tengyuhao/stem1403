"""
Unique Paths
"""


def getPaths(m, n):
    """
    :param m: rows
    :param n: cols
    :return: final result
    """
    f = [[0 for x in range(n)] for y in range(m)]
    print(f)
    # f[0][0]. f[0][1], f[0][2], ..., f[0][n-1]
    # f[1][0]. f[1][1], f[1][2], ..., f[1][n-1]
    # ...
    # f[m-1][0]. f[1][1], f[1][2], ..., f[m-1][n-1]
    # f[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                f[i][j] = 1
            else:
                f[i][j] = f[i-1][j] + f[i][j-1]

    return f[m-1][n-1]


# test
m = 4
n = 8
print(getPaths(m, n))
