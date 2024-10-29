import sys
from PyQt6 import QtWidgets
from gui import MainWindow

def main():
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()