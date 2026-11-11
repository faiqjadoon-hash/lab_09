# Lab 09 - Problem-Solving Practice 1

This lab is a set of **LeetCode / ICPC-style problems**. The goal isn't just a passing
test - it's practising the whole loop from *problem* to *plan* to *working code*, using
the problem-solving techniques from Unit 01 and the analysis ideas from Unit 04.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 09 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 09 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** Your own account
   - **Repository name:** `lab09-csci1030u`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.  For the TA to see your work, you will need to add them as a collaborator.


Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab09-your-username
cd lab09-your-username
```

## How to approach each problem

Before writing (or generating) any code, spend a couple of minutes on the **outline**:

1. **Restate** the problem in your own words.
2. **Try a small example by hand** - what's the answer for a tiny input, and how did
   you get it?
3. **Sketch the approach** - what steps turn the input into the output? Is there an
   obvious brute-force way, and a faster way?

Each function in `lab09.py` has an `# Outline` comment - jot your plan there first. Once
you have a plan, *then* turn it into code (you may use an AI assistant to help - see
**Using AI** below).

## Problems

Edit **`lab09.py`**. Don't rename the functions - the tests use these names.

### Part 1 - `two_sum(nums, target)`

Return the two **indices** `[i, j]` (with `i < j`) of the numbers in `nums` that add up
to `target`. Assume exactly one pair works.

```python
two_sum([2, 7, 11, 15], 9)   # returns [0, 1]   (2 + 7)
two_sum([3, 2, 4], 6)        # returns [1, 2]   (2 + 4)
```

### Part 2 - `max_profit(prices)`

`prices[i]` is a stock's price on day `i`. Return the most profit you can make by buying
on one day and selling on a **later** day. If you can't make any profit, return `0`.

```python
max_profit([7, 1, 5, 3, 6, 4])   # returns 5   (buy at 1, sell at 6)
max_profit([7, 6, 4, 3, 1])      # returns 0   (prices only fall)
```

### Part 3 - `max_subarray(nums)`

Return the largest sum of any **contiguous** (in-a-row) block of numbers in `nums`. The
list has at least one number.

```python
max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])   # returns 6   (4 + -1 + 2 + 1)
max_subarray([5, 4, -1, 7, 8])                  # returns 23  (the whole list)
```

### Part 4 - `is_balanced(s)`  *(stretch - optional)*

Return `True` if every bracket in `s` is closed correctly and in the right order. The
brackets are `(` `)` `[` `]` `{` `}`.

```python
is_balanced("()[]{}")   # returns True
is_balanced("{[]}")     # returns True
is_balanced("([)]")     # returns False   (closed in the wrong order)
```

Hint: a **list used as a stack** (`append` to push, `pop` to remove the last item) is a
natural fit here.

This part is optional - the three problems above are the core of the lab.

## Verifying Correctness

Run the pre-written tests to check your work:

```
pytest
```

Read the output closely - a failing test shows the input, what it expected, and what
your code returned. Fix, save, and run `pytest` again.

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 09 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 09 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab09-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

Starting this half of the term, you **may use an AI assistant to help you write the
code** for the lab. Build one habit first, though: **work out the problem-solving
outline yourself before you involve the AI.** For each problem, restate it, try a small
example by hand, and sketch your approach - *then* lean on the AI to help turn that plan
into Python. Let the AI do the implementing, not the thinking.

Use a free model, and be ready to **explain and modify** any code you submit - the lab
instructor may ask you to walk through it or change how it works.
