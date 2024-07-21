import streamlit as st
import addition
import subtraction
import multiplication
import division

def calculator():
    st.title("Calculator App")
    st.header("Ali Haider")

    num1 = st.number_input("Enter the first number:")
    operator = st.selectbox("Select the operator", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter the second number:")

    if st.button("Calculate"):
        if operator == "+":
            result = addition.add(num1, num2)
        elif operator == "-":
            result = subtraction.subtract(num1, num2)
        elif operator == "*":
            result = multiplication.multiply(num1, num2)
        elif operator == "/":
            if num2 != 0:
                result = division.divide(num1, num2)
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operator. Please try again."

        st.write("Result:", result)

        response = st.button("Quit Calculator")
        if response:
            st.write("Goodbye!")

if __name__ == "__main__":
    calculator()
