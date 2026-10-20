# 🛒 Python Shopping Bill Calculator

A simple shopping bill calculator built using Python. This project calculates discounts, delivery charges, and the final payable amount based on the total cart value.

## 🚀 Features

- Calculate discounts based on cart amount
- Apply a 20% discount on purchases of ₹5,000 or more
- Apply a 10% discount on purchases of ₹3,000 or more
- Provide free delivery on purchases of ₹1,000 or more
- Charge ₹50 delivery for purchases below ₹1,000
- Generate a shopping bill with a final payable amount
- Validate negative cart amounts

## 🛠️ Technologies Used

- Python 3
- Functions and nested functions
- Conditional statements
- Arithmetic operations
- User input and output

## 📋 Discount Rules

| Cart Amount | Discount | Delivery Charges |
|---|---|---|
| ₹5,000 or more | 20% | Free |
| ₹3,000–₹4,999.99 | 10% | Free |
| ₹1,000–₹2,999.99 | No discount | Free |
| Below ₹1,000 | No discount | ₹50 |

## 💻 How to Run

1. Install Python 3 on your computer.
2. Clone this repository or download the project files.
3. Open the project folder in VS Code.
4. Open the terminal and run:

```bash
python shopping_bill.py
```

5. Enter your total cart amount when prompted.

## 🧾 Example Output

```text
Enter total cart amount: Rs. 4000

------ SHOPPING BILL ------
Cart Amount: Rs. 4000.0
Discount: Rs. 400.0
Delivery Charges: Rs. 0
---------------------------
Final Bill: Rs. 3600.0
```

## 🎯 Learning Objectives

This project demonstrates the use of Python functions, nested functions, conditional logic, percentage calculations, and basic input validation.

## 🔮 Future Improvements

- Handle invalid text input
- Display currency values to two decimal places
- Add product names, quantities, and individual prices
- Generate and save receipts to a file
- Add unit tests for discount and delivery rules

## 👨‍💻 Author

**Abhishek Chaurasiya**

GitHub: [AbhiCode0](https://github.com/AbhiCode0)

---

⭐ If you find this project useful, feel free to explore the code and learn from it.

