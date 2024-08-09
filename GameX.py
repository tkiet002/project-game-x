import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,QWidget, QPushButton, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Game_X(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Game X- Thi thuc hanh")
        self.setGeometry(100,100,400,400)
        self.UIComponent();
        
    def UIComponent(self):
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget) 
        
        self.button_start = QPushButton("Bắt đầu game", self)
        self.button_end = QPushButton("Thoát game", self)
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_end)
        
        central_widget.setLayout(layout)
        
        self.button_start.clicked.connect(self.start_game)
        self.button_end.clicked.connect(self.end_game)
    def end_game(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Exit program?")
        
        label = QLabel("Bạn chuẩn bị thoát trò chơi")
        
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)
        dialog.exec_()
        self.close()
        
    def start_game(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Exit program?")
        
        label = QLabel("Trò chơi bắt đầu")
        
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)
        dialog.exec_()
def main():
    App = QApplication(sys.argv)
    window = Game_X()
    window.show()
    sys.exit(App.exec_())
    
    
if __name__ == "__main__":
    main()