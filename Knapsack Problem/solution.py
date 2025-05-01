import json
import sys

def read_json():
    with open('input/data.json', 'r') as data:
        return json.load(data)

def knapsack_dp(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if items[i - 1]['weight'] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items[i - 1]['weight']] + items[i - 1]['benefit']
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1]['weight']

    return dp[n][max_weight], selected_items

def main(data):
    if not data['maximum_weight'] or len(data['items']) < 1:
        return

    max_weight = data['maximum_weight']
    items = data['items']
    benefit, selected_items = knapsack_dp(items, max_weight)
    total_weight = sum(item['weight'] for item in selected_items)

    print("\n" + "-" * 40 + "\n")
    print("Mr Knapsack is walking out with:")
    print(f"Total Weight: {total_weight}")
    print(f"Total Benefit: {benefit}")
    print("Items Taken:", [item['id'] for item in selected_items])
    print("\n" + "-" * 40)

if __name__ == "__main__":
    data = read_json()
    if not data:
        sys.exit(0)
    main(data)
