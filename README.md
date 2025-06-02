# 🧾 Python Table PDF Generator

This project is a simple attempt to create a **PDF table** using Python's `fpdf` library, where **cell text wraps automatically** and the **row height adjusts based on the tallest cell**.

**📖also to memorize keigo while I'm making the pdf**

## ✅ What It Does
- Generates a PDF file with a table.
- Automatically wraps text inside cells.
- Attempts to adjust row height dynamically based on content.

## ⚠️ Current Challenge
When a cell contains long text and wraps into multiple lines, **only that specific cell grows in height**, while other cells in the same row remain unchanged. This causes **misalignment** between columns.

## 🎯 Next Objective
The next development step is to:

> **Ensure all cells in a row adjust to the height of the tallest cell**, so the table remains clean and aligned across all columns.

## 🛠️ Tech Stack
- Python
- [`fpdf`](https://pyfpdf.github.io/fpdf2/)

## 📄 Sample Output
See Sonkeigo_Kenjougo_Verbs_Fixed.pdf for the basic output and Sonkeigo_Kenjougo_Verbs_Fixed_WrapAttempt.pdf for my ongoing text wrap attempt output!
