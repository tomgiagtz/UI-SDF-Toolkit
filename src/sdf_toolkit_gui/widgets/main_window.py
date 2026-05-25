from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPaintEvent, QPixmap
from PyQt6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QMainWindow,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from sdf_toolkit_gui.widgets.settings_panel import SettingsPanel


class Panel(QFrame):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)


class ImagePreview(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._pixmap: QPixmap | None = None
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

    def set_pixmap(self, pixmap: QPixmap | None) -> None:
        self._pixmap = pixmap
        self.update()

    def paintEvent(self, event: QPaintEvent | None) -> None:
        super().paintEvent(event)
        if self._pixmap is None:
            return
        painter = QPainter(self)
        scaled = self._pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        x = (self.width() - scaled.width()) // 2
        y = (self.height() - scaled.height()) // 2
        painter.drawPixmap(x, y, scaled)
        painter.end()


def _build_preview_panel(title: str) -> tuple[Panel, ImagePreview]:
    panel = Panel()
    layout = QVBoxLayout(panel)
    layout.setContentsMargins(8, 8, 8, 8)

    label = QLabel(title)
    label.setStyleSheet("font-weight: bold")
    layout.addWidget(label)

    image = ImagePreview()
    layout.addWidget(image, stretch=1)

    return panel, image


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SDF Toolkit")
        self.setFixedSize(1024, 1024)

        central = QWidget()
        self.setCentralWidget(central)

        grid = QGridLayout(central)
        grid.setContentsMargins(4, 4, 4, 4)
        grid.setSpacing(4)

        # Left panel — settings
        self.left_panel = Panel()
        left_layout = QVBoxLayout(self.left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_panel = SettingsPanel()
        left_layout.addWidget(self.settings_panel)
        grid.addWidget(self.left_panel, 0, 0, 2, 1)

        # Right panels — previews
        self.input_panel, self.input_preview = _build_preview_panel("Input (Preview)")
        grid.addWidget(self.input_panel, 0, 1)

        self.output_panel, self.output_preview = _build_preview_panel("Output (Preview)")
        grid.addWidget(self.output_panel, 1, 1)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)

        # Connections
        self.settings_panel.input_path.path_selected.connect(self._load_input_preview)

    def _load_input_preview(self, path_str: str) -> None:
        pixmap = QPixmap(path_str)
        self.input_preview.set_pixmap(pixmap if not pixmap.isNull() else None)

    def set_output_preview(self, path_str: str) -> None:
        pixmap = QPixmap(path_str)
        self.output_preview.set_pixmap(pixmap if not pixmap.isNull() else None)