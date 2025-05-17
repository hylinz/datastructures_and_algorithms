## Summary 

The goal is to pick a combination of items to put in a bag so that the total weight doesn’t go over the bag’s limit, while the total benefit (value) of the items is as high as possible. Each item has a specific weight and benefit, and you can only include each item once (either you take it or leave it).

For this assignment, you’ll use two search methods—Breadth-First Search (BFS) and Depth-First Search (DFS)—to explore different item combinations and find the one with the maximum benefit without exceeding the weight limit.


# Solution

So, here’s what my code does in a nutshell:

1. **Read Data**  
   First, it grabs the list of items and the max weight allowed from a JSON file where each item has a weight and a benefit (value).

2. **Setup**  
   I use a classic dynamic programming (DP) approach to solve the knapsack problem (yes there was googling lol).
   ```python
   dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
   ```

3. **DP Table**  
   - The `dp` table is a 2D list where each row corresponds to items considered so far, and each column corresponds to a possible weight limit from 0 up to the max weight.
   Like this:

    | Item | Weight | Benefit |
    |-------|--------|---------|
    | 1     | 1      | 10      |
    | 2     | 2      | 15      |
    | 3     | 3      | 40      |


   - For each item and each possible weight, the code decides whether it’s better to take the item or skip it:
     - If the item fits in the current weight limit, compare the benefit of taking it vs not taking it.
     - Otherwise, just keep the benefit without taking the item.

     ```python
    for i in range(1, n + 1):
    for w in range(max_weight + 1):
        if items[i - 1]['weight'] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - items[i - 1]['weight']] + items[i - 1]['benefit']
            )
        else:
            dp[i][w] = dp[i - 1][w]
     ```

4. **Backtracking**  
   After filling out the `dp` table, I start from the bottom-right corne (saw this in a youtube video) and move backwards to figure out which items contributed to the max benefit. If the benefit changed when including an item, that item is part of the solution.

    ```python
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1]['weight']
    ```

5. **Output**  
   Finally, it prints out the total weight and total benefit of the items taken, plus a list of the item IDs that were chosen.

    ----------------------------------------

    Mr Knapsack is walking out with:

    Total Weight: 419
    
    Total Benefit: 307
    
    Items Taken: [11, 10, 7, 6, 5, 3, 2, 1]

    ----------------------------------------

