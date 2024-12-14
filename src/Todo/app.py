from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, 
    QVBoxLayout, QHBoxLayout, QWidget, QListWidget
)
import sys


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ chính
        self.setWindowTitle("To Do App")
        self.setGeometry(100, 100, 500, 500)

        # Tạo layout chính
        main_layout = QVBoxLayout()

        # Tạo layout ngang cho input và button
        input_layout = QHBoxLayout()

        # Tạo layout dọc cho list task
        task_layout = QVBoxLayout()

        # Tạo layout ngang cho nút chức năng
        action_layout = QHBoxLayout()

        # Tạo Input cho task
        self.line_edit = QLineEdit()  # Lưu input thành thuộc tính
        self.line_edit.setPlaceholderText("Enter your task here")
        self.line_edit.setObjectName("task-input")
        input_layout.addWidget(self.line_edit)

        # Tạo Button cho Add Task
        add_button = QPushButton("Add Task")
        add_button.setObjectName("add-task-btn")
        add_button.clicked.connect(self.add_task)  # Kết nối nút Add với phương thức add_task
        input_layout.addWidget(add_button)

        # Tạo List Widget để hiển thị task
        self.task_list = QListWidget()  # Lưu List Widget thành thuộc tính
        self.task_list.setObjectName("task-list")
        task_layout.addWidget(self.task_list)

        # Tạo Button Delete Task
        delete_button = QPushButton("Delete Task")
        delete_button.setObjectName("delete-task-btn")
        delete_button.clicked.connect(self.delete_task)  # Kết nối nút Delete với phương thức delete_task
        action_layout.addWidget(delete_button)

        # Thêm layout ngang vào layout chính
        main_layout.addLayout(input_layout)
        main_layout.addLayout(task_layout)
        main_layout.addLayout(action_layout)

        # Đưa layout vào QWidget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def add_task(self):
        """Thêm một task vào danh sách"""
        task = self.line_edit.text().strip()  # Lấy text từ input và xóa khoảng trắng
        if task:  # Kiểm tra nếu task không rỗng
            index = self.task_list.count()
            self.task_list.addItem(f"{index + 1}. {task}")
            self.line_edit.clear()  # Xóa nội dung trong input sau khi thêm

    def delete_task(self):
        """Xóa task được chọn"""
        selected_item = self.task_list.currentItem()  # Lấy item được chọn
        if selected_item:  # Nếu có item được chọn
            self.task_list.takeItem(self.task_list.row(selected_item))  # Xóa item khỏi QListWidget

def load_stylesheet(file_path):
    with open(file_path, "r") as file:
        return file.read()
# Khởi chạy ứng dụng
app = QApplication(sys.argv)
# Load CSS
stylesheet = load_stylesheet("styles.css")
app.setStyleSheet(stylesheet)

window = ToDoApp()
window.show()
sys.exit(app.exec())
