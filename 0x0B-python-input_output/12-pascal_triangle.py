#!/usr/bin/python3
"""Define Pascal's triangle function"""


def pascal_triangle(n):
    """represent Pascal's triangle of size n."""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tris = triangles[-1]
        tmp = [1]
        for a in range(len(tris) - 1):
            tmp.append(tris[a] + tris[a + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
