# SAT Resolution Algorithm in Python

This is a simple Python implementation of the **propositional logic resolution algorithm** for checking the (un)satisfiability of a formula in Conjunctive Normal Form (CNF).

## 📋 How it works

The program reads multiple clauses from the standard input in the following format:
```
<number> <number> ... <number> 0
```
- Each number represents a literal (e.g., `1` means `x1`, `-1` means `¬x1`).
- The `0` marks the end of a clause.
- An empty line marks the end of input.

### Example:
```
1 -2 0
2 3 0
-1 -3 0
```

## ▶️ Running the script

```bash
python resolution_sat.py
```

You'll be prompted to input clauses one by one.

## 📄 Output

The script will tell you whether the formula is:

- ✅ **Satisfiable** (no contradiction)
- ❌ **Unsatisfiable** (a contradiction was found via resolution)
