# You are enjoying a food festival, you have a limited stomach
# capacity, and various food items are available with
# different tastes and quantities. Each food item has an
# associated taste value and quantity. You want to maximise
# the total taste value you enjoy within your given stomach
# capacity. However, you can either take a particular food
# item or not, and you cannot take a partial portion of food
# items. Given each food item's taste value and quantity,
# determine the maximum total taste value you can obtain
# while respecting your stomach capacity.

# Solution---

# The given scenario is similar to a 0/1 Knapsack problem
# Stomach capacity => Knapsack size
# Food quantity => jewel weight
# Taste value => profit

# Approach: First, let's start by writing a recursive code
# Then we try to memoize it to form DP characteristics

# BASIC RECURSIVE APPROACH
def max_taste_val(quantity, value, cap, items):
    # base condition
    if cap == 0 or items == 0:
        return 0

    # recursive condition 1
    if quantity[items-1] > cap:
        return max_taste_val(quantity, value, cap, items-1)

    # recursive condition 2
    elif quantity[items-1] <= cap:
        return max(value[items-1] + max_taste_val(quantity, value, cap-quantity[items-1], items-1),
                   max_taste_val(quantity, value, cap, items-1))


# DP MEMOIZED APPROACH

# here, a matrix called 'dp' is used to memoize/store the results from recursive calls
# as the values of 'cap' and 'items' are the ones changing in recursive calls, we assign indices to the matrix
# based on 'cap' and 'items'

def max_taste_val_dp_init(quantity, value, cap, items):
    dp = [[-1 for __ in range(cap+1)] for _ in range(items+1)]

    return max_taste_val_dp(quantity, value, dp, cap, items)


def max_taste_val_dp(quantity, value, dp, cap, items):
    # base condition 1
    if cap == 0 or items == 0:
        return 0

    # base condition 2
    if dp[items][cap] != -1:
        return dp[items][cap]  # leverages the power of DP by returning pre-stored results

    # recursive condition 1
    if quantity[items-1] > cap:
        dp[items][cap] = max_taste_val_dp(quantity, value, dp, cap, items-1)
        return dp[items][cap]
    elif quantity[items-1] <= cap:
        dp[items][cap] = max(value[items-1] + max_taste_val_dp(quantity, value, dp, cap-quantity[items-1], items-1),
                             max_taste_val_dp(quantity, value, dp, cap, items-1))
        return dp[items][cap]


if __name__ == '__main__':
    # food_quantity = [1, 2, 4, 3]
    # taste_value = [1, 2, 3, 5]
    # stomach_cap = 9

    # food_quantity = [1, 3, 4, 5]
    # taste_value = [1, 4, 5, 7]
    # stomach_cap = 7

    food_quantity = input("Enter the quantity of food items, seperated by space: ").split()
    food_quantity = [int(i) for i in food_quantity]

    taste_value = input("Enter the taste value of food items, seperated by space: ").split()
    taste_value = [int(i) for i in taste_value]

    stomach_cap = int(input("Enter stomach capacity: "))

    if len(food_quantity) != len(taste_value):
        print("Invalid number of items, as items' quantity and value are not of same length!")
        exit(0)

    print("----------")

    print("Max total taste value obtained: ",
          max_taste_val_dp_init(food_quantity, taste_value, stomach_cap, len(food_quantity)))
