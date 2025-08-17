from PySide6.QtWidgets import QApplication
import ui

if __name__ == "__main__":
    app = QApplication([])
    window = ui.MainWindow()
    window.ui.show()
    app.exec()