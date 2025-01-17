import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow 

def main():
    app = QApplication(sys.argv)

    # 메인 윈도우 생성 및 표시
    main_window = MainWindow()
    main_window.show()

    # 이벤트 루프 실행
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()