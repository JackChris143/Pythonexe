import streamlit as st
from streamlit_ace import st_ace
import sys
import io

# Title of the Web App
st.set_page_config(page_title="Python Executor",page_icon="")
st.title("Python Code Executor")

# Sidebar with a brief description or user instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
    - Write Python code in the editor below.
    - Before running the code, click"ctrl+enter".
    - Click "Run Code" to execute your Python code.
    - The output will appear below.
    - Use standard Python modules (e.g., math, os, etc.) for execution.
    """)

# Ace editor for Python code input
code = st_ace(language='python', theme='terminal', height=400)

# Button to run the code
if st.button("Run Code"):
    # Capture output using StringIO
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    try:
        # Execute the code entered by the user
        exec(code)
    except Exception as e:
        # If there’s an error, show the error message
        st.error(f"Error: {e}")

    # Reset stdout and capture the output
    sys.stdout = old_stdout
    output = mystdout.getvalue()

    # Display the output from execution
    if output:
        st.subheader("Output:")
        st.code(output)
    else:
        st.warning("No output or code executed.")
