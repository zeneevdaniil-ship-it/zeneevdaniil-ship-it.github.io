import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)


SITE_COLORS = {
    "primary": "#b8a99a",
    "primary_dark": "#a89580",
    "secondary": "#d9c7b8",
    "accent": "#8a7865",
    "dark": "#e8e2db",
    "darker": "#d9d1c7",
    "light": "#ffffff",
    "gray": "#a8998a",
    "text_dark": "#5a4d41",
    "text_light": "#7a6d5f",
    "bg_light": "#f5f0e8",
    "bg_medium": "#e8e2db",
    "bg_dark": "#d9d1c7",
}


INTEREST_TO_CAREERS = {
    "IT и программирование": [
        ("Разработчик ПО", "Проектирование и создание приложений, участие в разработке продуктов."),
        ("Тестировщик", "Проверка качества ПО, поиск и документирование ошибок."),
        ("Аналитик данных", "Сбор, анализ и визуализация данных для принятия решений."),
    ],
    "Дизайн и творчество": [
        ("UX/UI дизайнер", "Проектирование интерфейсов, улучшение пользовательского опыта."),
        ("Графический дизайнер", "Создание визуальных материалов, брендинг, иллюстрации."),
    ],
    "Инженерия и техника": [
        ("Инженер", "Проектирование систем и механизмов, решение технических задач."),
        ("Инженер-робототехник", "Создание и обслуживаниe роботизированных систем."),
    ],
    "Бизнес и экономика": [
        ("Продуктовый менеджер", "Определение стратегии продукта, работа с командой и метриками."),
        ("Маркетолог", "Исследование рынка, продвижение продуктов и брендов."),
    ],
    "Медицина и биология": [
        ("Медицинский лаборант", "Проведение анализов, работа с оборудованием и данными."),
        ("Биотехнолог", "Разработка биотехнологических решений и продуктов."),
    ],
}


class CareerGuidanceWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AI Карьерный Навигатор")
        self.resize(420, 360)
        self._apply_palette()
        self._build_ui()

    def _apply_palette(self) -> None:
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(SITE_COLORS["bg_light"]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(SITE_COLORS["text_dark"]))
        palette.setColor(QPalette.ColorRole.Base, QColor(SITE_COLORS["light"]))
        palette.setColor(QPalette.ColorRole.Button, QColor(SITE_COLORS["accent"]))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(SITE_COLORS["light"]))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(SITE_COLORS["primary"]))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(SITE_COLORS["light"]))
        self.setPalette(palette)

    def _build_ui(self) -> None:
        root = QVBoxLayout()
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)

        title = QLabel("Подбор направлений по интересам")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.DemiBold))
        title.setStyleSheet(
            f"color: {SITE_COLORS['text_dark']};"
        )
        root.addWidget(title)

        subtitle = QLabel(
            "Выберите область интересов — мы предложим возможные профессии и подсказки."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet(f"color: {SITE_COLORS['text_light']};")
        root.addWidget(subtitle)

        row = QHBoxLayout()
        interest_label = QLabel("Интересы")
        interest_label.setStyleSheet(f"color: {SITE_COLORS['text_dark']};")
        row.addWidget(interest_label)

        self.interest_combo = QComboBox()
        self.interest_combo.addItems(list(INTEREST_TO_CAREERS.keys()))
        self.interest_combo.setStyleSheet(
            """
            QComboBox {
                padding: 6px 8px;
                border-radius: 8px;
                border: 1px solid #d9d1c7;
                background: #ffffff;
            }
            QComboBox::drop-down { border: 0; }
            """
        )
        row.addWidget(self.interest_combo, 1)
        root.addLayout(row)

        self.result = QTextEdit()
        self.result.setReadOnly(True)
        self.result.setMinimumHeight(160)
        self.result.setStyleSheet(
            f"background: {SITE_COLORS['light']};"
            f"border: 1px solid {SITE_COLORS['darker']};"
            f"border-radius: 10px;"
            f"padding: 10px;"
            f"color: {SITE_COLORS['text_dark']};"
        )
        root.addWidget(self.result)

        controls = QHBoxLayout()
        btn_suggest = QPushButton("Подобрать профессии")
        btn_suggest.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_suggest.setStyleSheet(
            f"background: {SITE_COLORS['accent']};"
            f"color: {SITE_COLORS['light']};"
            f"border: none;"
            f"padding: 10px 14px;"
            f"border-radius: 10px;"
        )
        btn_suggest.clicked.connect(self._on_suggest)

        btn_clear = QPushButton("Очистить")
        btn_clear.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_clear.setStyleSheet(
            f"background: {SITE_COLORS['primary']};"
            f"color: {SITE_COLORS['light']};"
            f"border: none;"
            f"padding: 10px 14px;"
            f"border-radius: 10px;"
        )
        btn_clear.clicked.connect(lambda: self.result.clear())

        controls.addWidget(btn_suggest)
        controls.addWidget(btn_clear)
        root.addLayout(controls)

        note = QLabel(
            "Подсказка: результаты — ориентир, пробуйте задачи и проекты в выбранной сфере."
        )
        note.setStyleSheet(f"color: {SITE_COLORS['gray']};")
        root.addWidget(note)

        self.setLayout(root)

    def _on_suggest(self) -> None:
        interest = self.interest_combo.currentText()
        careers = INTEREST_TO_CAREERS.get(interest, [])
        if not careers:
            self.result.setPlainText("Пока нет рекомендаций. Попробуйте выбрать другую область.")
            return
        lines = [f"Интерес: {interest}\n"]
        for title, desc in careers:
            lines.append(f"• {title}\n  {desc}\n")
        self.result.setPlainText("\n".join(lines))


def main() -> None:
    app = QApplication(sys.argv)
    window = CareerGuidanceWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


