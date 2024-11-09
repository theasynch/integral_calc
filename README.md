
# 🎯 Integral Calculator

## 📜 Description

The **Integral Calculator** allows users to calculate both definite and indefinite integrals of mathematical functions. This tool accepts complex expressions involving polynomials, trigonometric functions, and more, and provides the result along with a graphical representation of the function and the area under the curve (for definite integrals). It also renders the integral expression in LaTeX format, displaying it alongside the result.

This calculator is designed for educational and computational purposes, helping users visualize mathematical integrals and understand their results with clear notations.

## 🚀 Features

- **Complex Integral Handling**: Support for polynomials, trigonometric functions, rational expressions, and more.
- **Definite & Indefinite Integrals**: Compute integrals with or without limits.
- **LaTeX Display**: Shows the integral expression in LaTeX for correct mathematical notation.
- **Graphical Visualization**: Visualize the function and the area under the curve for definite integrals.
- **Real-Time Calculation**: Instant calculation and rendering of results.

## ⚙️ Installation

To run the Integral Calculator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/integral-calculator.git
   cd integral-calculator
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

## 🖥️ Usage

1. **Input Function**: Enter the mathematical function you want to integrate (e.g., `(x+1)/(sin(x) + tan^2(x))`).
2. **Specify the Variable**: Input the variable to integrate with respect to (e.g., `x`).
3. **Set Limits (for Definite Integrals)**: If you want a definite integral, specify the lower and upper limits, separated by a comma (e.g., `0, 10`).
4. **Calculate Integral**: Click the **"Calculate Integral"** button to get the result.
5. **View Results**: The result will be displayed, along with the integral expression in LaTeX format and a graph of the function (for definite integrals).

### 🌟 Example

**Parameters**:
- **Function**: `(x+1)/(sin(x) + tan^2(x))`
- **Variable**: `x`
- **Limits**: `0, 5`

After clicking **"Calculate Integral"**, the integral result will be displayed along with a graph of the function and the area under the curve (for definite integrals).


## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and submit a pull request. Ensure that your changes are well-documented and include relevant tests.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [SymPy](https://www.sympy.org/) - For symbolic mathematics and integral calculation.
- [Matplotlib](https://matplotlib.org/) - For rendering the graphical representation of the function and area under the curve.
- [Open Source Community](https://opensource.guide/) - For guidance and support in developing open-source software.
