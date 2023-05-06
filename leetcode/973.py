def kClosest(points, k):
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]

print(kClosest([[1,3],[-2,2]], 1))