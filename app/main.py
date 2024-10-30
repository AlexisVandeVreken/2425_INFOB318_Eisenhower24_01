import sys
from PyQt6 import QtWidgets
from gui import MainWindow

def main():
    app = QtWidgets.QApplication([])

    window = MainWindow()
    #stylesheet = load_stylesheet("app\style.qss", window.theme)
    #app.setStyleSheet(stylesheet)
    window.show()

    sys.exit(app.exec())
"""
def load_stylesheet(qss_file, theme):
    with open(qss_file, "r") as file:
        qss = file.read()

        return qss
"""
if __name__ == "__main__":
    main()