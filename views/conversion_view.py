from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QGridLayout, QHBoxLayout, QTextEdit, QSizePolicy, \
    QGraphicsDropShadowEffect

from managers.scroll_bar_manager import manage_scroll_bar


class ConversionView(QWidget):
    def __init__(self):
        super().__init__()

        # [i] Buttons and TextEdit should be public, in order for viewmodel to access them

        # <editor-fold desc="[+] Case buttons">
        self.button_upper_case = QPushButton("Upper Case")
        self.button_lower_case = QPushButton("Lower Case")
        self.button_inverse_case = QPushButton("Reverse Case")
        self.button_sentence_case = QPushButton("Sentence Case")
        self.button_capitalized_case = QPushButton("Capitalized Case")
        self.button_title_case = QPushButton("Title Case")

        group_case_buttons = QGroupBox("Case Transformations")
        group_case_buttons.setLayout(QGridLayout())

        group_case_layout: QGridLayout = group_case_buttons.layout()
        # QGridLayout Parameters: widget; row; column; rowSpan; columnSpan
        group_case_layout.addWidget(self.button_upper_case, 0, 0, 1, 1)
        group_case_layout.addWidget(self.button_lower_case, 0, 1, 1, 1)
        group_case_layout.addWidget(self.button_inverse_case, 0, 2, 1, 1)
        group_case_layout.addWidget(self.button_sentence_case, 1, 0, 1, 1)
        group_case_layout.addWidget(self.button_capitalized_case, 1, 1, 1, 1)
        group_case_layout.addWidget(self.button_title_case, 1, 2, 1, 1)

        # </editor-fold>

        # <editor-fold desc="[+] Text control buttons">

        self.button_copy_text = QPushButton("Copy")
        self.button_paste_text = QPushButton("Paste")
        self.button_clear_text = QPushButton("Clear")

        group_control_buttons = QGroupBox("Controls")
        group_control_buttons.setLayout(QGridLayout())

        group_control_layout: QGridLayout = group_control_buttons.layout()
        # QGridLayout Parameters: widget; row; column; rowSpan; columnSpan
        group_control_layout.addWidget(self.button_copy_text, 0, 0, 1, 1)
        group_control_layout.addWidget(self.button_paste_text, 0, 1, 1, 1)
        group_control_layout.addWidget(self.button_clear_text, 0, 2, 1, 1)

        # </editor-fold>

        # Text Edit
        self.text_edit = QTextEdit()
        group_text = QGroupBox("Text Area")
        group_text.setLayout(QVBoxLayout())
        group_text.layout().addWidget(self.text_edit)

        # View Layout and Group Placement
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(group_case_buttons, stretch=0)
        layout.addWidget(group_control_buttons, stretch=0)
        layout.addWidget(group_text, stretch=1)

        # External Margins, Spacing and Size Policies
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        group_control_buttons.layout().setContentsMargins(0, 0, 0, 0)
        group_control_buttons.layout().setSpacing(8)
        group_case_buttons.layout().setContentsMargins(0, 0, 0, 0)
        group_case_buttons.layout().setSpacing(8)
        group_text.layout().setContentsMargins(0, 0, 0, 0)

        group_case_buttons.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        group_control_buttons.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        group_text.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        # Style Settings
        group_case_buttons.setProperty("class", "group group--case-buttons")
        group_control_buttons.setProperty("class", "group group--control-buttons")
        group_text.setProperty("class", "group group--text")

        self.button_sentence_case.setProperty("class", "button button--sentence")
        self.button_capitalized_case.setProperty("class", "button button--capitalized")
        self.button_upper_case.setProperty("class", "button button--upper")
        self.button_lower_case.setProperty("class", "button button--lower")
        self.button_inverse_case.setProperty("class", "button button--inverse")
        self.button_title_case.setProperty("class", "button button--title")

        self.button_copy_text.setProperty("class", "button button--copy")
        self.button_paste_text.setProperty("class", "button button--paste")
        self.button_clear_text.setProperty("class", "button button--clear")

        self.text_edit.setObjectName("text-edit")

        # Signal Connection
        self.text_edit.verticalScrollBar().rangeChanged.\
            connect(lambda min_v, max_v: manage_scroll_bar(self.text_edit, "text-edit", max_v))