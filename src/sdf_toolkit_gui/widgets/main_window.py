from PyQt6.QtWidgets import (
    QFrame,
    QGridLayout,
    QMainWindow,
    QWidget,
)

from sdf_toolkit_gui.widgets.settings_panel import SettingsPanel


class Panel(QFrame):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SDF Toolkit")
        self.setFixedSize(1024, 1024)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QGridLayout(central)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        self.left_panel = Panel()
        self.settings_panel = SettingsPanel(self.left_panel)
        layout.addWidget(self.left_panel, 0, 0, 2, 1)

        self.top_right_panel = Panel()
        layout.addWidget(self.top_right_panel, 0, 1)

        self.bottom_right_panel = Panel()
        layout.addWidget(self.bottom_right_panel, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
