#!/usr/bin/env python
# Peri
# 2021.10.28
# Lab Exercise 5
# Invoice.py
# Using Mu 1.1.0.beta.3
# This program displays a student invoice that calculates total cost.
# Fake address generator: https://www.prepostseo.com/tool/fake-address-generator

# Create functions to define each segment of the program
def school_header():
    print("*" * 50)
    print(" " * 10 + "Aufderharfort Community College")
    print(" " * 10 + "3135 Johnston Ports")
    print(" " * 10 + "Aufderharfort, AR 41250")

def product_price_header():
    print("-" * 50)
    print(" " * 10 + "Product Name:\tProduct Price:")

def total_header():
    print("-" * 50)
    # Define the product prices
    book_prices = 52.99
    lab_fees = 25.00
    tuition = 157.93 * 3
    # Display the product names and prices
    print(" " * 10 + "Books\t" + "\t$" + str(book_prices))
    print(" " * 10 + "Lab Fees\t" + "\t$" + str(lab_fees))
    print(" " * 10 + "Tuition\t" + "\t$" + str(tuition))
    # Separate the above from the total
    print("-" * 50)
    # Display the total
    print("\t\t\t\tTotal")
    print("\t\t\t\t$" + " " + str(book_prices + lab_fees + tuition))
    print("-" * 50)

def closer():
    print(" " * 3 + "Thank you for being a Aufderharfort Student")
    print("*" * 50)

# Specify what order functions are to be called
def main():
    school_header()
    product_price_header()
    total_header()
    closer()

# Call all defined functions
if __name__ == "__main__":
    main()