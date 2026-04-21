# 🌐 Shiny Web App (Python) – Loan & Economic Insights Dashboard

This project is an interactive **web application built using Shiny for Python**, showcasing financial analysis tools and economic insights through a multi-tab dashboard.

---

## 🧠 What is Shiny (Python)?

**Shiny (Python)** is a framework for building interactive web applications directly in Python.

It is based on **reactive programming**, where:
- User inputs (e.g., sliders, buttons)  
- Automatically trigger updates in outputs (e.g., plots, tables, text)

---

## 🚀 Features

The app is divided into **three interactive tabs**:

---

### 📊 Tab A: Loan Calculator
An interactive financial simulation tool that allows users to:

- Input:
  - Interest rate  
  - Loan amount  
  - Loan tenure  
  - Investment assumptions  

- Output:
  - 📈 Dynamic plots  
  - 📋 Repayment tables  
  - 🧾 Calculated results  

Uses reactive programming to instantly update results when inputs change.

---

### ⚠️ Tab B: Economic Insights
- Displays draggable information panels  
- Highlights key economic risks  
- Includes visual elements (image-based content)  

---

### 💻 Tab C: Interactive Code Editor
- Embeds a live Python editor via Trinket  
- Allows users to experiment with Python code directly inside the app  

---

## 🧩 Project Structure

```bash id="shiny-structure"
shiny-web-app/
├── app.py                              # Main Shiny app
├── calculator.py                       # Loan calculation logic
├── Session 10 Group Work Slides Roger.jpg  # Supporting image
