from PyQt6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from sdf_toolkit_gui.widgets.path_selector import PathSelector


class CopyTab(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)


class SdfTab(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        self.sdf_settings = QWidget()
        layout.addWidget(self.sdf_settings, stretch=1)


class SettingsPanel(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = QTabWidget()
        self.copy_tab = CopyTab()
        self.sdf_tab = SdfTab()
        self.tabs.addTab(self.copy_tab, "Copy")
        self.tabs.addTab(self.sdf_tab, "SDF")
        layout.addWidget(self.tabs, stretch=1)

        self.input_path = PathSelector("Input Image:")
        self.output_path = PathSelector("Output Dir:", mode="directory")
        layout.addWidget(self.input_path)
        layout.addWidget(self.output_path)
