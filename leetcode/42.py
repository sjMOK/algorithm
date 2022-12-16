def trap(height):
    water = 0
    j = 0
    max_height = max(height)

    for i in range(0, height.index(max_height)):
        if height[i] < height[j]:
            water += height[j] - height[i]
        else:
            j = i

    j = len(height) - 1
    for i in range(j, height.index(max_height), -1):
        if height[i] < height[j]:
            water += height[j] - height[i]
        else:
            j = i

    return water
