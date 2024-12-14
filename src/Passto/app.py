from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, 
    QVBoxLayout, QHBoxLayout, QWidget, QListWidget,QLabel, QTableWidget,QTableWidgetItem
)
import sys


class Passto(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ chính
        self.setWindowTitle("Passto")
        self.setGeometry(100, 100, 500, 500)

        # Tạo layout chính
        main_layout = QVBoxLayout()

        input_layout = QVBoxLayout()
        table_layout = QVBoxLayout()
        
        # Platform input
        self.platform_label = QLabel("Enter platform")
        input_layout.addWidget(self.platform_label)
        
        self.platform_input = QLineEdit()
        self.platform_input.setPlaceholderText("Enter platform here...")
        self.platform_input.setObjectName("platform-input")
        input_layout.addWidget(self.platform_input)
        
        # Username input
        self.username_label = QLabel("Enter username")
        input_layout.addWidget(self.username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username here...")
        self.username_input.setObjectName("username-input")
        input_layout.addWidget(self.username_input)
        
        # Password input
        self.password_label = QLabel("Enter password")
        input_layout.addWidget(self.password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password here...")
        self.password_input.setObjectName("password-input")
        input_layout.addWidget(self.password_input)
        
        # Button
        add_button = QPushButton("Add")
        add_button.setObjectName("add-btn")
        add_button.clicked.connect(self.add)
        input_layout.addWidget(add_button)
        
        # Table
        self.table = QTableWidget()
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Platform", "Email/Username", "Password"])
        table_layout.addWidget(self.table)
    
        # Thêm layout ngang vào layout chính
        main_layout.addLayout(input_layout)
        main_layout.addLayout(table_layout)
        
        # Đưa layout vào QWidget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def add(self):
        # Lấy dữ liệu từ các input
        platform = self.platform_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        # Kiểm tra xem input có rỗng không
        if not platform or not username or not password:
            return
        
        # Thêm dữ liệu vào bảng
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(platform))
        self.table.setItem(row_position, 1, QTableWidgetItem(username))
        self.table.setItem(row_position, 2, QTableWidgetItem(password))
        
        # Xóa dữ liệu trong input
        self.platform_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        

def load_stylesheet(file_path):
    with open(file_path, "r") as file:
        return file.read()
# Khởi chạy ứng dụng
app = QApplication(sys.argv)
# Load CSS
stylesheet = load_stylesheet("styles.css")
app.setStyleSheet(stylesheet)

window = Passto()
window.show()
sys.exit(app.exec())
