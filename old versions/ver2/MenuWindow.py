from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from DiaryApp import DiaryApp
from RetrieveWindow import RetrieveWindow

class MenuWindow(QWidget):
    def __init__(self, db, pwm):
        """
        Menu window after login.
        :param db: Database instance
        :param pwm: PasswordManager instance
        """
        super().__init__()
        self.db = db
        self.pwm = pwm

        # Window settings
        self.setWindowTitle("Diary Menu")
        self.setGeometry(700, 300, 300, 220)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title label
        title_label = QLabel("What would you like to do?")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # --- Buttons ---
        self.add_entry_btn = QPushButton("Add New Entry")
        self.add_entry_btn.clicked.connect(self.open_new_entry)
        layout.addWidget(self.add_entry_btn)

        self.retrieve_entries_btn = QPushButton("Retrieve Entries")
        self.retrieve_entries_btn.clicked.connect(self.open_retrieve_entries)
        layout.addWidget(self.retrieve_entries_btn)

        self.change_password_btn = QPushButton("Change Password")
        self.change_password_btn.clicked.connect(self.change_password)
        layout.addWidget(self.change_password_btn)

        # Placeholder for future buttons
        # self.other_feature_btn = QPushButton("Other Feature")
        # self.other_feature_btn.clicked.connect(self.other_feature)
        # layout.addWidget(self.other_feature_btn)

    # --- Button Methods ---
    def open_new_entry(self):
        """Open the diary entry window."""
        self.diary_window = DiaryApp(self.db)
        self.diary_window.show()
        self.close()

    def open_retrieve_entries(self):
        """Open the diary retrieval window."""
        self.retrieve_window = RetrieveWindow(self.db)
        self.retrieve_window.show()
        self.close()

    def change_password(self):
        """Prompt user to change the password."""
        new_password, ok = QInputDialog.getText(
            self,
            "Change Password",
            "Enter new password (leave blank for no password):"
        )
        if ok:
            self.pwm.set_password(new_password)
            QMessageBox.information(self, "Password Updated", "Password updated successfully!")
