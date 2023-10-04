def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratios for each item
    ratios = [(item[1] / item[0], item[0], item[1]) for item in items]

    # Sort items by value-to-weight ratio in descending order
    ratios.sort(reverse=True)

    total_value = 0.0
    knapsack = []

    for ratio, weight, value in ratios:
        if capacity >= weight:
            # Add the entire item to the knapsack
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            # Add a fraction of the item to the knapsack
            fraction = capacity / weight
            knapsack.append((capacity, value * fraction))
            total_value += value * fraction
            break

    return total_value, knapsack

# Example usage:
items = [(2, 20), (3, 25), (4, 40), (5, 50)]
capacity = 10

max_value, selected_items = fractional_knapsack(items, capacity)

print("Maximum value:", max_value)
print("Selected items:")
for weight, value in selected_items:
    print("   Weight:", weight, " Value:", value)