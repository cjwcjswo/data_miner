from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Data Miner")
        self.setGeometry(100, 100, 800, 600)

        # 메인 위젯과 레이아웃 설정
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        tree_layout = QVBoxLayout()
        tree_view = QTreeView()
        tree_layout.addWidget(tree_view)

        tree_model = QStandardItemModel()
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)