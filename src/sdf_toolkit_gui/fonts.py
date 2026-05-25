from PyQt6.QtGui import QFont, QFontDatabase

from sdf_toolkit_gui.resources import resource_path

_FONT_FILES = [
    "fonts/Inter-VariableFont_opsz,wght.ttf",
]


class FontProvider:
    FAMILY = "Inter"
    DEFAULT_SIZE = 12

    @staticmethod
    def load() -> None:
        for font_file in _FONT_FILES:
            font_id = QFontDatabase.addApplicationFont(str(resource_path(font_file)))

    @staticmethod
    def default() -> QFont:
        return QFont(FontProvider.FAMILY, FontProvider.DEFAULT_SIZE, weight=QFont.Weight.Normal)
