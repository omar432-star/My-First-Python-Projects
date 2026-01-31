# 💰 Tip Calculator

A simple and interactive Python tool to help friends split a bill fairly. No more headaches or manual math at the restaurant!

## 🚀 How it works:
1. **Total Bill**: Enter the final amount on the receipt.
2. **Tip Percentage**: Choose how much you want to tip (10%, 12%, or 15%).
3. **Split Count**: Enter the number of people sharing the bill.
4. **Result**: The program calculates the exact amount each person owes, rounded to two decimal places.

## 🛠️ Features:
* Uses **Float** data types for precise currency calculation.
* Uses **F-Strings** for clean and readable output.
* Includes error handling logic for accurate splitting.

## 💻 Sample Code Snippet:
```python
# The logic behind the calculation
person_formula = float(bill * (1 + (tip / 100)) / people_split)
final_amount = round(person_formula, 2)
