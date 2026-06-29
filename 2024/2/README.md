# Day 2: Red-Nosed Reports

## Problem Summary

Each line in the input contains a report made of several numbers called levels.

A report is safe when:

* The levels are all increasing or all decreasing.
* Every two adjacent levels differ by at least `1` and at most `3`.
* Equal adjacent levels are not allowed.

## Part One

Count all reports that already follow the safety rules.

### Approach

For each report:

1. Compare every level with the previous level.
2. Determine whether the report is increasing or decreasing.
3. Check that the direction never changes.
4. Check that every difference is between `1` and `3`.
5. Count the report if all checks pass.

### Result

```text
411
```

## Part Two

The Problem Dampener allows one level to be removed from an unsafe report.

A report is now safe when:

* It is already safe, or
* Removing one level makes it safe.

### Approach

For each report:

1. Check whether the original report is safe.
2. If it is unsafe, remove each level one at a time.
3. Check the shortened report using the same Part One rules.
4. Count the report if any removal makes it safe.

### Result

```text
465
```

## Complexity

Let `n` be the number of levels in one report.

### Part One

* Time: `O(n)`
* Space: `O(1)`

### Part Two

* Time: `O(n²)`
* Space: `O(n)`

Part Two checks up to `n` shortened reports, and each safety check takes `O(n)` time.

## Files

```text
day-02/
├── input.txt
├── red_nosed_reports.py
└── README.md
```

## Run the Solution

```bash
python red_nosed_reports.py
```

The program reads the puzzle input from `input.txt` and prints the answers for both parts.
