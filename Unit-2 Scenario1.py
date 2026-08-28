# Unique Paths Problem using Dynamic Programming

class PathFinder:

    def calculate(self, r, c):

        # Create DP table
        table = [[0 for y in range(c)] for x in range(r)]

        # First row and first column always have 1 path
        for x in range(r):
            table[x][0] = 1

        for y in range(c):
            table[0][y] = 1

        # Calculate remaining paths
        for x in range(1, r):
            for y in range(1, c):
                table[x][y] = table[x - 1][y] + table[x][y - 1]

        return table[r - 1][c - 1]


# Main Program

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

obj = PathFinder()

answer = obj.calculate(r, c)

print("Total Unique Paths =", answer)
