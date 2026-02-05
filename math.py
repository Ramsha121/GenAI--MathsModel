import streamlit as st
import sympy as sp
import numpy as np
from scipy.fftpack import dct
from scipy.stats import norm

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="GenAI Math Assistant", page_icon="🧠", layout="wide")

# -----------------------------
# Custom CSS for Beautiful UI
# -----------------------------
st.markdown(
    """
    <style>
        .main {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 8px;
        }
        .stButton>button {
            border-radius: 12px;
            background-color: #ff4b2b;
            color: white;
            font-weight: bold;
            height: 3em;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #ff416c;
            color: white;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("✨ GenAI Mathematical Assistant")
st.caption("⚡ Ultra‑fast symbolic + numeric solver across all math domains")

# -----------------------------
# Sidebar Menu
# -----------------------------
with st.sidebar:
    st.header("📚 Select Module")
    module = st.selectbox(
        "Choose Math Area",
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

    st.markdown("---")
    st.info("Built with ❤️ using Streamlit, SymPy, NumPy & SciPy")

# Common symbol
x = sp.symbols("x")

# Layout columns for centered UI
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    # -----------------------------
    # Arithmetic
    # -----------------------------
    if module == "Arithmetic":
        st.subheader("🧮 Basic Arithmetic Solver")
        expr = st.text_input("Enter expression", "2 + 5 * 3")

        if st.button("🚀 Calculate"):
            try:
                result = eval(expr)
                st.success(f"Answer: {result}")
            except Exception:
                st.error("Invalid expression")

    # -----------------------------
    # Linear Algebra
    # -----------------------------
    elif module == "Linear Algebra":
        st.subheader("📐 Matrix Operations")
        data = st.text_area("Enter matrix (e.g., 1 2; 3 4)")

        if st.button("🚀 Compute Matrix Properties"):
            try:
                A = np.array([[float(i) for i in row.split()] for row in data.split(";")])
                st.write("Matrix:")
                st.write(A)
                st.write("Determinant:", np.linalg.det(A))
                st.write("Inverse:")
                st.write(np.linalg.inv(A))
            except Exception:
                st.error("Invalid matrix format")

    # -----------------------------
    # Trigonometry
    # -----------------------------
    elif module == "Trigonometry":
        st.subheader("📏 Trigonometric Calculator")
        angle = st.number_input("Enter angle in degrees", value=30.0)

        if st.button("🚀 Compute Trig Values"):
            rad = np.deg2rad(angle)
            st.write("sin:", np.sin(rad))
            st.write("cos:", np.cos(rad))
            st.write("tan:", np.tan(rad))

    # -----------------------------
    # Calculus
    # -----------------------------
    elif module == "Calculus":
        st.subheader("∂ Derivative & Integration")
        expr = st.text_input("Enter function in x", "x**2 + sin(x)")

        if st.button("🚀 Solve Calculus"):
            try:
                derivative = sp.diff(expr, x)
                integral = sp.integrate(expr, x)
                st.write("Derivative:", derivative)
                st.write("Integral:", integral)
            except Exception:
                st.error("Invalid function")

    # -----------------------------
    # Statistics & Probability
    # -----------------------------
    elif module == "Statistics & Probability":
        st.subheader("📊 Statistics + Normal Distribution")
        nums = st.text_input("Enter numbers separated by space", "1 2 3 4 5")
        prob_x = st.number_input("Value for Normal PDF", value=0.0)

        if st.button("🚀 Compute Statistics"):
            try:
                arr = np.array(list(map(float, nums.split())))
                st.write("Mean:", np.mean(arr))
                st.write("Std Dev:", np.std(arr))
                st.write("Normal PDF:", norm.pdf(prob_x))
            except Exception:
                st.error("Invalid input numbers")

    # -----------------------------
    # FFT
    # -----------------------------
    elif module == "FFT":
        st.subheader("🌊 Fast Fourier Transform")
        nums = st.text_input("Enter signal values", "1 2 3 4")

        if st.button("🚀 Compute FFT"):
            try:
                arr = np.array(list(map(float, nums.split())))
                st.write("FFT Result:")
                st.write(np.fft.fft(arr))
            except Exception:
                st.error("Invalid signal input")

    # -----------------------------
    # Laplace Transform
    # -----------------------------
    elif module == "Laplace Transform":
        st.subheader("🔁 Laplace Transform Solver")
        expr = st.text_input("Enter function in t", "exp(-t)")

        if st.button("🚀 Compute Laplace"):
            try:
                t, s = sp.symbols("t s")
                L = sp.laplace_transform(expr, t, s)
                st.write("Laplace Transform:", L)
            except Exception:
                st.error("Invalid function")

    # -----------------------------
    # DCT
    # -----------------------------
    elif module == "DCT Transform":
        st.subheader("🎵 Discrete Cosine Transform")
        nums = st.text_input("Enter signal values", "1 2 3 4")

        if st.button("🚀 Compute DCT"):
            try:
                arr = np.array(list(map(float, nums.split())))
                st.write("DCT Result:")
                st.write(dct(arr))
            except Exception:
                st.error("Invalid input")

    # -----------------------------
    # Matrices & Vectors
    # -----------------------------
    elif module == "Matrices & Vectors":
        st.subheader("🧩 Matrix × Vector Multiplication")

        vector = st.text_input("Enter vector", "1 2")
        matrix = st.text_area("Enter matrix", "1 2; 3 4")

        if st.button("🚀 Multiply"):
            try:
                v = np.array(list(map(float, vector.split())))
                A = np.array([[float(i) for i in row.split()] for row in matrix.split(";")])
                st.write("Result:", A.dot(v))
            except Exception:
                st.error("Invalid matrix/vector")

    # -----------------------------
    # Log & Exponential
    # -----------------------------
    elif module == "Log & Exponential":
        st.subheader("📈 Logarithmic & Exponential Solver")
        expr = st.text_input("Enter expression in x", "log(x) + exp(x)")

        if st.button("🚀 Solve"):
            try:
                simplified = sp.simplify(expr)
                st.write("Simplified:", simplified)

                solution = sp.solve(expr, x)
                st.write("Solution for x:", solution)
            except Exception:
                st.warning("Expression simplified but no solvable equation form")
