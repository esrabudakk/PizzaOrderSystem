import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QComboBox, QLineEdit


# TODO : Küçük bir GUI örneği

class PizzaOrder(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Pizza Order System")
        self.setGeometry(100, 100, 400, 250)

        # Create pizza size label and dropdown
        self.size_label = QLabel("Select Pizza Size:", parent=self)
        self.size_label.move(20, 20)
        self.size_dropdown = QComboBox(self)
        self.size_dropdown.addItems(["Small", "Medium", "Large"])
        self.size_dropdown.move(150, 20)

        # Create toppings label and text input
        self.toppings_label = QLabel("Enter Toppings (comma separated):", parent=self)
        self.toppings_label.move(20, 60)
        self.toppings_input = QLineEdit(self)
        self.toppings_input.move(250, 60)

        # Create submit button
        self.submit_button = QPushButton("Place Order", parent=self)
        self.submit_button.move(150, 150)
        self.submit_button.clicked.connect(self.place_order)

        # Create order summary label
        self.summary_label = QLabel("", parent=self)
        self.summary_label.move(20, 200)

        # Show the window
        self.show()

    def place_order(self):
        # Get selected pizza size and toppings
        size = self.size_dropdown.currentText()
        toppings = self.toppings_input.text()

        # Calculate price based on size and number of toppings
        price = 0
        if size == "Small":
            price = 10 + 1.5 * len(toppings.split(","))
        elif size == "Medium":
            price = 12 + 1.75 * len(toppings.split(","))
        elif size == "Large":
            price = 15 + 2 * len(toppings.split(","))

        # Display order summary
        self.summary_label.setText(f"You ordered a {size} pizza with {toppings} for ${price:.2f}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    order_system = PizzaOrder()
    sys.exit(app.exec_())
