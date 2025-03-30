from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Body Mass Index")
        self.setFixedSize(600, 570)
        
        # Create a central widget and set it as the central widget of the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        input_layout = QHBoxLayout()

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create a QLineEdit widget for weight input
        self.weight_input = QLineEdit(self)
        layout.addWidget(self.weight_input)
        self.weight_input.setPlaceholderText("Insert the weight in Kg: ")
        input_layout.addWidget(self.weight_input)
        
        # Create a QLineEdit widget for the height input
        self.height_input = QLineEdit(self)
        layout.addWidget(self.height_input)
        self.height_input.setPlaceholderText("Insert the height in meters: ")
        input_layout.addWidget(self.height_input)

        # Add the input layout to the main vertical layout
        layout.addLayout(input_layout)
        
        # Create a QPushButton widget for the calculate button
        button = QPushButton("Calculate")
        button.clicked.connect(self.calculate)
        layout.addWidget(button)
        
        # Create a QLabel widget for the result
        self.output_label = QLabel("Result", self)
        layout.addWidget(self.output_label)
        
    def get_input(self):
        try:
            weight = self.weight_input.text()
            height = self.height_input.text()
            return float(weight), float(height)
        except ValueError:
            return None, None
        
    def calculate(self):
        weight,height = self.get_input()
        if weight is None or height is None:
            self.output_label.setText("Invalid input. Please enter a valid input.")
        bmi = weight / (height ** 2)
        self.output_label.setText(f"Your BMI is {bmi:.2f}")

#Test for my GitHub!