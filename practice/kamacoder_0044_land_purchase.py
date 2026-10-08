def min_land_difference(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    sum_row = [0] * n
    sum_col = [0] * m
    best = float("inf")
    total = 0

    for i in range(n):
        sum_row[i] = sum(grid[i])
        total += sum_row[i]

    for j in range(m):
        for i in range(n):
            sum_col[j] += grid[i][j]

    half = 0
    for i in range(n - 1):
        half += sum_row[i]
        best = min(best, abs(total - 2 * half))

    half = 0
    for j in range(m - 1):
        half += sum_col[j]
        best = min(best, abs(total - 2 * half))

    return best
