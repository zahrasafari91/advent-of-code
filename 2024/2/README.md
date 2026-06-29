# Day 2: Red-Nosed Reports

## Problem Summary

Each line contains a report made of several numbers.

A report is safe when:

* All numbers are consistently increasing or decreasing.
* Every two adjacent numbers differ by at least 1 and at most 3.
* Equal adjacent values are not allowed.

The goal is to count the number of safe reports.

## Approach

For each report:

1. Compare every number with the previous number.
2. Determine whether the report is increasing or decreasing.
3. Confirm that the direction does not change.
4. Confirm that every difference is between 1 and 3.
5. Count the report if all checks pass.

The solution stops checking a report as soon as it finds an invalid pair.

## Complexity

* Time: `O(n)` for each report
* Space: `O(1)`

## Run the Solution

```bash
python red_nosed_reports.py
```

The program reads the input from:

```text
input.txt
```

## Result

```text
411
```
