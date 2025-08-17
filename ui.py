import os
from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QSizePolicy
import duck


class MainWindow:
    def __init__(self):
        self.duckdb_file = "<file_path>"
        self.db = None
        self.conn = None
        self.load_main_windows()
        self.init_duckdb_table()
        self.init_shortcut()

    def init_shortcut(self):
        self.action_open = self.ui.actionOpen
        self.action_open.triggered.connect(self.open_file_dialog)

    def open_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            self.ui,
            "Choose one DuckDB file",
            "",
            "DuckDB file (*.duckdb)",
        )

        if len(files) == 1:
            self.duckdb_file = files[0]
            QMessageBox.information(
                self.ui,
                "Ok",
                f"Selected: \n{self.duckdb_file}",
            )
        elif len(files) >= 2:
            QMessageBox.warning(
                self.ui,
                "Selected too many files",
                f"Selected {len(files)} files, please select only one file!",
            )
        else:
            QMessageBox.warning(self.ui, "No file", "Should select one!")

        self.db = duck.DuckDB(self.duckdb_file)
        self.conn = self.db.connect_database()
        if self.conn:
            self.db_table_refresh()
        else:
            QMessageBox.critical(
                self.ui, "Connection Failed", "Failed to connect to DuckDB."
            )

    def load_main_windows(self):
        DIR = os.path.dirname(__file__)
        ui_path = os.path.join(DIR, "ui/qt.ui")
        loader = QUiLoader()
        self.ui = loader.load(ui_path)
        self.ui.centralwidget.setLayout(self.ui.horizontalLayout)
        self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.layout = self.ui.horizontalLayout

    def init_duckdb_table(self):
        self.duckdb_ui_table = QTableWidget()
        self.layout.addWidget(self.duckdb_ui_table)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.duckdb_ui_table.setSizePolicy(size_policy)

    def db_table_refresh(self):
        db_header, table_rows = self.db.fetch_all_tables()
        # refresh ui table
        self.duckdb_ui_table.setColumnCount(len(db_header))
        self.duckdb_ui_table.setRowCount(len(table_rows))
        self.duckdb_ui_table.setHorizontalHeaderLabels(db_header)
        ui_header = self.duckdb_ui_table.horizontalHeader()
        ui_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, row in enumerate(table_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.duckdb_ui_table.setItem(i, j, item)
        self.ui.show()
