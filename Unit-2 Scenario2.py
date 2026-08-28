# Number of Ways to Make Change using Dynamic Programming

class ChangeMaker:

    def calculate(self, coins, target):

        # Create DP array
        ways = [0] * (target + 1)

        # One way to make amount 0
        ways[0] = 1

        # Calculate number of ways
        for coin in coins:
            for amount in range(coin, target + 1):
                ways[amount] = ways[amount] + ways[amount - coin]

        return ways[target]


# Main Program

coins = list(map(int, input("Enter coin values (space separated): ").split()))
target = int(input("Enter target amount: "))

obj = ChangeMaker()

answer = obj.calculate(coins, target)

print("\nTotal Ways =", answer)
