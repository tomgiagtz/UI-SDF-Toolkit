from typing import Literal

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class PathSelector(QWidget):
    path_selected = pyqtSignal(str)

    def __init__(
        self,
        label: str,
        mode: Literal["file", "directory"] = "file",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._mode = mode
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 0, 16, 0)

        self.label = QLabel(label)
        self.label.setStyleSheet("font-weight: bold")
        self.line_edit = QLineEdit()
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self._browse)

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit, stretch=1)
        layout.addWidget(self.browse_button)

    def _browse(self) -> None:
        if self._mode == "directory":
            path = QFileDialog.getExistingDirectory(self, "Select Directory")
        else:
            path, _ = QFileDialog.getOpenFileName(
                self, "Select File", "", "Images (*.png *.tiff *.tif *.exr);;All Files (*)"
            )
        if path:
            self.line_edit.setText(path)
            self.path_selected.emit(path)
