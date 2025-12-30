#  Billing System

A simple web-based billing application built with **Flask** and **CSV storage**.  
It allows users to add items to a bill, remove items, and generate printable invoices with tax calculations.

---

##  Features
- Add items to a bill with **Bill ID, Item Name, Quantity, Price**
- Remove items from an existing bill
- Print invoice with **subtotal, 18% tax, and final amount**
- Simple and lightweight – data stored in `bills.csv`
- User-friendly web interface with HTML & CSS

---

##  Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Storage:** CSV File

---

## 📂 Project Structure
📁 Billing-System  
 ┣ 📂 templates  
 ┃ ┣ index.html  
 ┃ ┣ add.html  
 ┃ ┣ remove.html  
 ┃ ┣ print.html  
 ┃ ┗ exit.html  
 ┣ 📂 static  
 ┃ ┗ styles.css  
 ┣ app.py  
 ┣ bills.csv (auto-created after first entry)  
 ┗ README.md  

---

##  How to Run
1. Clone this repository:  
   `git clone <your-repo-url>`  
   `cd Billing-System`  

2. Install dependencies:  
   `pip install flask`  

3. Run the Flask app:  
   `python app.py`  

4. Open in browser:  
   `http://127.0.0.1:5000/`  

---

##  Use Cases
- Small shops/vendors for simple billing  
- Educational project to learn Flask & CSV handling  

---

##  Sample Bill Output
**Bill ID:** 101  

| Item Name | Quantity | Price | Total |  
|-----------|----------|-------|-------|  
| Pen       | 2        | 10    | 20    |  
| Notebook  | 1        | 50    | 50    |  

**Subtotal:** 70  
**Tax (18%):** 12.6  
**Final Amount:** 82.6  

---

##  Acknowledgements
Developed as a practice project to understand **Flask routing, form handling, and CSV-based data storage**.
