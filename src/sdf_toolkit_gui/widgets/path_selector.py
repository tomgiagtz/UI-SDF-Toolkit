from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class PathSelector(QWidget):
    def __init__(self, label: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 0, 16, 0)

        self.label = QLabel(label)
        self.line_edit = QLineEdit()
        self.browse_button = QPushButton("Browse...")

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit, stretch=1)
        layout.addWidget(self.browse_button)
