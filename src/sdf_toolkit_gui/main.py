import sys

from PyQt6.QtWidgets import QApplication

from sdf_toolkit_gui.fonts import FontProvider
from sdf_toolkit_gui.widgets.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    FontProvider.load()
    app.setFont(FontProvider.default())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()