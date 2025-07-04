import streamlit as st

def main():
    """
    This function creates a simple calculator web application using Streamlit.
    It takes two numbers and an operation from the user, performs the calculation,
    and displays the result.
    """

    st.set_page_config(page_title="Simple Calculator", layout="centered")

    st.title("🔢 Simple Calculator")
    st.markdown("---")

    # Input for the first number
    # st.number_input provides a numeric input field.
    # The 'format' parameter ensures it handles floats.
    st.header("Enter Numbers")
    num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f", key="num1")

    # Input for the second number
    num2 = st.number_input("Enter the second number:", value=0.0, format="%.2f", key="num2")

    st.markdown("---")

    # Dropdown for selecting the operation
    st.header("Select Operation")
    operation = st.selectbox(
        "Choose an operation:",
        ("Add", "Subtract", "Multiply", "Divide"),
        key="operation"
    )

    st.markdown("---")

    result = None # Initialize result to None

    # Button to perform the calculation
    if st.button("Calculate", key="calculate_button"):
        try:
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0: # Prevent division by zero
                    result = num1 / num2
                else:
                    st.error("Error: Division by zero is not allowed.")
                    result = "Undefined" # Set result to a string for error case
        except Exception as e:
            # Catch any other potential errors during calculation
            st.error(f"An error occurred during calculation: {e}")
            result = "Error"

    # Display the result
    st.header("Result")
    if result is not None:
        if isinstance(result, (int, float)):
            st.success(f"The result of {num1} {operation.lower()} {num2} is: **{result:.2f}**")
        else:
            # Display error string if result was set to "Undefined" or "Error"
            st.warning(f"Calculation could not be completed: {result}")
    else:
        st.info("Enter numbers and select an operation, then click 'Calculate'.")

# Run the Streamlit application
if __name__ == "__main__":
    main()
