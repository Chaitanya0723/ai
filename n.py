def solve(n):
    def place(row, cols):
        if row == n:
            res.append(cols)
            return True
        for col in range(n):
            if col in cols or any(abs(col - c) == row - r for r, c in enumerate(cols)):
                continue
            if place(row + 1, cols + [col]):
                return True
        return False
    res = []
    place(0, [])
    for i in res[0]:  # Print only the first solution
        print('.' * i + 'Q' + '.' * (n - i - 1))

solve(4)