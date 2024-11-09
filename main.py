import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog
import sympy as sp
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, 
                                                NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np

class IntegralImageWindow(QDialog):
    def __init__(self, integral_latex, result_latex):
        super().__init__()
        self.setWindowTitle('Integral Image')
        layout = QVBoxLayout()
        
        # Create a figure to display the integral with result
        latex_fig, latex_ax = plt.subplots(figsize=(6, 2))  # Adjust size as needed
        latex_expr = f"${integral_latex} = {result_latex}$"  # Combine integral and result with equal sign
        latex_ax.text(0.5, 0.5, latex_expr, fontsize=20, ha='center', va='center')
        latex_ax.axis('off')  # Hide axes for better display
        latex_ax.set_frame_on(False)  # Turn off the frame
        
        # Display the LaTeX figure on a new window
        canvas = FigureCanvas(latex_fig)
        layout.addWidget(canvas)

        self.setLayout(layout)

class IntegrationCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Advanced Integration Calculator')
        layout = QVBoxLayout()
        
        # Input section
        self.label_function = QLabel('Enter the function:')
        self.input_function = QLineEdit()
        layout.addWidget(self.label_function)
        layout.addWidget(self.input_function)
        
        self.label_variable = QLabel('Enter the variable:')
        self.input_variable = QLineEdit()
        layout.addWidget(self.label_variable)
        layout.addWidget(self.input_variable)
        
        self.label_limits = QLabel('Enter lower and upper limits (comma-separated for definite integration):')
        self.input_limits = QLineEdit()
        layout.addWidget(self.label_limits)
        layout.addWidget(self.input_limits)
        
        # Result display
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)
        
        # Calculate button
        self.button_integrate = QPushButton('Calculate Integral')
        self.button_integrate.clicked.connect(self.calculate_integral)
        layout.addWidget(self.button_integrate)
        
        # Matplotlib figure for function graph
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        # Set the layout
        self.setLayout(layout)
        
    def calculate_integral(self):
        func = self.input_function.text().replace('^', '**')  # Replace ^ with ** for Python syntax
        var = self.input_variable.text()
        limits = self.input_limits.text().strip()

        try:
            x = sp.Symbol(var)
            expr = sp.sympify(func, evaluate=False)  # Set evaluate=False to preserve complex structures

            if limits:
                limits_split = limits.split(',')
                if len(limits_split) == 2:
                    lower, upper = map(float, limits_split)
                    result = sp.integrate(expr, (x, lower, upper))
                    integral_latex = sp.latex(sp.Integral(expr, (x, lower, upper)))
                    result_latex = sp.latex(result)
                else:
                    raise ValueError("Please enter valid lower and upper limits separated by a comma.")
            else:
                result = sp.integrate(expr, x)
                integral_latex = sp.latex(sp.Integral(expr, x))
                result_latex = sp.latex(result)

            result_latex = sp.latex(result)
            self.result_area.setText(f'Integral result:\n{result}\n\nLaTeX: {result_latex}')
            
            # Display the integral and result as an image in a new window
            self.display_integral_image(integral_latex, result_latex)

            # Plot the function if limits are provided
            if limits:
                self.plot_function(expr, x, lower, upper)
            else:
                self.plot_function(expr, x)

        except ValueError as ve:
            self.result_area.setText(f'Input Error: {str(ve)}')
        except Exception as e:
            self.result_area.setText(f'Error: {str(e)}')
        
    def display_integral_image(self, integral_latex, result_latex):
        # Ensure the latex is in a valid form (removing unsupported commands)
        integral_latex = integral_latex.replace(r'\limits', '')  # Remove the \limits command if present

        # Create and show the IntegralImageWindow with the integral LaTeX and result LaTeX
        self.integral_window = IntegralImageWindow(integral_latex, result_latex)
        self.integral_window.exec_()

    def plot_function(self, expr, x, lower=None, upper=None):
        self.ax.clear()
        
        # Convert sympy expression to a lambda function with support for complex functions
        func = sp.lambdify(x, expr, 'numpy')
        
        # Plot range based on limits
        if lower is not None and upper is not None:
            x_vals = np.linspace(lower, upper, 1000)  # Adjust range based on limits
        else:
            x_vals = np.linspace(-10, 10, 1000)  # Default range if no limits

        try:
            y_vals = func(x_vals)
            self.ax.plot(x_vals, y_vals, label=f'Function: {expr}')
        except Exception as e:
            self.result_area.append(f"\nWarning: Plotting error: {str(e)}")
            return
        
        # Shading for definite integral
        if lower is not None and upper is not None:
            x_shade = np.linspace(lower, upper, 1000)
            y_shade = func(x_shade)
            self.ax.fill_between(x_shade, y_shade, color='lightgreen', alpha=0.5, label='Area under curve')
        
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.legend()
        self.ax.grid(True)
        
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntegrationCalculator()
    window.show()
    sys.exit(app.exec_())
