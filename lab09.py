# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   Restate: find two positions i < j with nums[i] + nums[j] == target.
    #   Example: two_sum([3, 2, 4], 6) -> 2 + 4 = 6 at indices [1, 2].
    #   Plan: walk once keeping a dict {value: index} of seen numbers.
    #   For each x at j, the partner needed is target - x. If it's in the
    #   dict, we already have an earlier index i -> return [i, j]. Else store x.
    #   Brute force is O(n^2); this is O(n) time, O(n) space.
    seen = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], j]
        seen[x] = j
    return []  # unreachable given the guarantee, but keeps the function total


def max_profit(prices):
    # Outline:
    #   Restate: pick buy day b < sell day s to maximise prices[s] - prices[b];
    #   return 0 if no such positive pair exists.
    #   Example: [7, 1, 5, 3, 6, 4] -> buy 1, sell 6 -> 5.
    #   Plan: one pass. Track the cheapest price seen so far (best buy) and
    #   the best profit so far. For each price, profit-if-sold-today is
    #   price - min_so_far; update best. O(n) time, O(1) space.
    min_price = float('inf')
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best


def max_subarray(nums):
    # Outline:
    #   Restate: find a contiguous block with the largest possible sum
    #   (the block must be non-empty).
    #   Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 4 + -1 + 2 + 1 = 6.
    #   Plan: Kadane's algorithm. At each index, the best block ending here
    #   is either just nums[i], or the previous best-ending-here plus nums[i]
    #   (whichever is larger). Track the max of these over all positions.
    #   O(n) time, O(1) space.
    best_ending_here = best_overall = nums[0]
    for x in nums[1:]:
        best_ending_here = max(x, best_ending_here + x)
        best_overall = max(best_overall, best_ending_here)
    return best_overall


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Restate: check that (), [], {} are nested and closed in the right order.
    #   Example: "{[]}" -> True; "([)]" -> False (wrong order).
    #   Plan: use a list as a stack of opening brackets. On an opening char,
    #   push it. On a closing char, the top of the stack must be its matching
    #   opener - if the stack is empty or mismatched, return False. At the end,
    #   the stack must be empty. O(n) time, O(n) space.
    closing_to_opening = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[ch]:
                return False
    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
    print(two_sum([3, 2, 4], 6))            # [1, 2]
    print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
    print(max_profit([7, 6, 4, 3, 1]))      # 0
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([5, 4, -1, 7, 8]))                 # 23
    print(is_balanced("()[]{}"))            # True
    print(is_balanced("{[]}"))              # True
    print(is_balanced("([)]"))              # False


if __name__ == "__main__":
    main()