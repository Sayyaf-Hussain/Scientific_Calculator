
import streamlit as st
import math

# Functions for calculations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base)

# Streamlit UI
st.title("Scientific Calculator")

operation = st.selectbox("Select operation:", [
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Power",
    "Square Root",
    "Sine",
    "Cosine",
    "Tangent",
    "Logarithm"
])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number:", step=0.1)
    num2 = st.number_input("Enter second number:", step=0.1)

if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)
elif operation == "Power":
    result = power(num1, num2)
elif operation == "Square Root":
    num = st.number_input("Enter number:", step=0.1)
    result = square_root(num)
elif operation == "Sine":
    num = st.number_input("Enter angle in degrees:", step=1.0)
    result = sin(num)
elif operation == "Cosine":
    num = st.number_input("Enter angle in degrees:", step=1.0)
    result = cos(num)
elif operation == "Tangent":
    num = st.number_input("Enter angle in degrees:", step=1.0)
    result = tan(num)
elif operation == "Logarithm":
    num = st.number_input("Enter number:", step=0.1)
    base = st.number_input("Enter base (default is 10):", value=10, step=1)
    result = log(num, base)

if 'result' in locals():
    st.write(f"Result: {result}")
