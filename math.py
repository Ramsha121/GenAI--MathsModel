import streamlit as st
import sympy as sp
import numpy as np
from scipy.fftpack import dct
from scipy.stats import norm

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="GenAI Math Assistant", layout="wide")

st.title("✨ GenAI Mathematical Assistant")
st.caption("Fast symbolic + numeric solver for all major math domains")

# -----------------------------
# Sidebar Menu
# -----------------------------
module = st.sidebar.selectbox(
    "Choose Math Module",
    [
        "Arithmetic",
        "Linear Algebra",
        "Trigonometry",
        "Calculus",
        "Statistics & Probability",
        "FFT",
        "Laplace Transform",
        "DCT Transform",
        "Matrices & Vectors",
        "Log & Exponential",
    ],
)

# Common symbol
x = sp.symbols("x")

# -----------------------------
# Arithmetic
# -----------------------------
if module == "Arithmetic":
    st.subheader("Basic Arithmetic Solver")
    expr = st.text_input("Enter expression", "2 + 5 * 3")

    if st.button("Calculate"):
        try:
            result = eval(expr)
            st.success(f"Answer: {result}")
        except Exception as e:
            st.error("Invalid expression")

# -----------------------------
# Linear Algebra
# -----------------------------
elif module == "Linear Algebra":
    st.subheader("Matrix Operations")
    data = st.text_area("Enter matrix (e.g., 1 2; 3 4)")

    if st.button("Compute Matrix Properties"):
        try:
            A = np.array([[float(i) for i in row.split()] for row in data.split(";")])
            st.write("Matrix:")
            st.write(A)
            st.write("Determinant:", np.linalg.det(A))
            st.write("Inverse:")
            st.write(np.linalg.inv(A))
        except:
            st.error("Invalid matrix format")

# -----------------------------
# Trigonometry
# -----------------------------
elif module == "Trigonometry":
    st.subheader("Trigonometric Calculator")
    angle = st.number_input("Enter angle in degrees", value=30.0)

    if st.button("Compute Trig Values"):
        rad = np.deg2rad(angle)
        st.write("sin:", np.sin(rad))
        st.write("cos:", np.cos(rad))
        st.write("tan:", np.tan(rad))

# -----------------------------
# Calculus
# -----------------------------
elif module == "Calculus":
    st.subheader("Derivative & Integration")
    expr = st.text_input("Enter function in x", "x**2 + sin(x)")

    if st.button("Solve Calculus"):
        try:
            derivative = sp.diff(expr, x)
            integral = sp.integrate(expr, x)
            st.write("Derivative:", derivative)
            st.write("Integral:", integral)
        except:
            st.error("Invalid function")

# -----------------------------
# Statistics & Probability
# -----------------------------
elif module == "Statistics & Probability":
    st.subheader("Stats + Normal Distribution")
    nums = st.text_input("Enter numbers separated by space", "1 2 3 4 5")
    prob_x = st.number_input("Value for Normal PDF", value=0.0)

    if st.button("Compute Statistics"):
        try:
            arr = np.array(list(map(float, nums.split())))
            st.write("Mean:", np.mean(arr))
            st.write("Std Dev:", np.std(arr))
            st.write("Normal PDF:", norm.pdf(prob_x))
        except:
            st.error("Invalid input numbers")

# -----------------------------
# FFT
# -----------------------------
elif module == "FFT":
    st.subheader("Fast Fourier Transform")
    nums = st.text_input("Enter signal values", "1 2 3 4")

    if st.button("Compute FFT"):
        try:
            arr = np.array(list(map(float, nums.split())))
            st.write("FFT Result:")
            st.write(np.fft.fft(arr))
        except:
            st.error("Invalid signal input")

# -----------------------------
# Laplace Transform
# -----------------------------
elif module == "Laplace Transform":
    st.subheader("Laplace Transform Solver")
    expr = st.text_input("Enter function in t", "exp(-t)")

    if st.button("Compute Laplace"):
        try:
            t, s = sp.symbols("t s")
            L = sp.laplace_transform(expr, t, s)
            st.write("Laplace Transform:", L)
        except:
            st.error("Invalid function")

# -----------------------------
# DCT
# -----------------------------
elif module == "DCT Transform":
    st.subheader("Discrete Cosine Transform")
    nums = st.text_input("Enter signal values", "1 2 3 4")

    if st.button("Compute DCT"):
        try:
            arr = np.array(list(map(float, nums.split())))
            st.write("DCT Result:")
            st.write(dct(arr))
        except:
            st.error("Invalid input")

# -----------------------------
# Matrices & Vectors
# -----------------------------
elif module == "Matrices & Vectors":
    st.subheader("Matrix × Vector Multiplication")

    vector = st.text_input("Enter vector", "1 2")
    matrix = st.text_area("Enter matrix", "1 2; 3 4")

    if st.button("Multiply"):
        try:
            v = np.array(list(map(float, vector.split())))
            A = np.array([[float(i) for i in row.split()] for row in matrix.split(";")])
            st.write("Result:", A.dot(v))
        except:
            st.error("Invalid matrix/vector")

# -----------------------------
# Log & Exponential
# -----------------------------
elif module == "Log & Exponential":
    st.subheader("Logarithmic & Exponential Solver")
    expr = st.text_input("Enter expression in x", "log(x) + exp(x)")

    if st.button("Solve"):
        try:
            simplified = sp.simplify(expr)
            st.write("Simplified:", simplified)

            solution = sp.solve(expr, x)
            st.write("Solution for x:", solution)
        except:
            st.warning("Expression simplified but no solvable equation form")

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit • SymPy • NumPy • SciPy")
