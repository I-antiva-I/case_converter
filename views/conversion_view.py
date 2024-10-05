from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout, QTextEdit, QSizePolicy

from enums.control_type import ControlType
from enums.case_type import CaseType
from interfaces.i_view import IViewMeta, IView
from managers.scroll_bar_manager import manage_scroll_bar
from viewmodels.conversion_viewmodel import ConversionViewModel


class ConversionView(QWidget, IView, metaclass=IViewMeta):
    """
    The `ConversionView` class provides a user interface for text input and transformation.
    """

    # <editor-fold desc="[+] Signals">

    # Emitted when one of the case transformation buttons is clicked.
    case_button_clicked = pyqtSignal(CaseType)

    # Emitted when one of the control buttons (copy, paste, clear) is clicked.
    control_button_clicked = pyqtSignal(ControlType)

    # Emitted when the user modifies the text in the QTextEdit, updates value in viewmodel.
    text_changed = pyqtSignal(str)

    # </editor-fold>

    def __init__(self, viewmodel: ConversionViewModel):
        """
        Initializes view.
        :param viewmodel: Corresponding ConversionViewModel.
        """
        super().__init__()

        self.viewmodel = viewmodel

        # <editor-fold desc="[+] Buttons">

        self.button_upper_case = QPushButton("Upper Case")
        self.button_lower_case = QPushButton("Lower Case")
        self.button_inverse_case = QPushButton("Inverse Case")
        self.button_sentence_case = QPushButton("Sentence Case")
        self.button_capitalized_case = QPushButton("Capitalized Case")
        self.button_title_case = QPushButton("Title Case")

        self.button_copy_text = QPushButton("Copy")
        self.button_paste_text = QPushButton("Paste")
        self.button_clear_text = QPushButton("Clear")

        self.button_upper_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.UPPER))
        self.button_lower_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.LOWER))
        self.button_inverse_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.INVERSE))
        self.button_sentence_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.SENTENCE))
        self.button_capitalized_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.CAPITALIZED))
        self.button_title_case.clicked.connect(lambda: self._on_case_button_clicked(CaseType.TITLE))


        self.button_copy_text.clicked.connect(lambda: self._on_control_button_clicked(ControlType.COPY))
        self.button_paste_text.clicked.connect(lambda: self._on_control_button_clicked(ControlType.PASTE))
        self.button_clear_text.clicked.connect(lambda: self._on_control_button_clicked(ControlType.CLEAR))

        # </editor-fold>

        # <editor-fold desc="[+] Text edit">

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self._on_text_changed)
        self.text_edit.verticalScrollBar().rangeChanged.\
            connect(lambda min_v, max_v: manage_scroll_bar(self.text_edit, "text-edit", max_v))

        # </editor-fold>

        # <editor-fold desc="[+] Groups">

        group_case_buttons = QGroupBox("Case Transformations")
        group_control_buttons = QGroupBox("Controls")
        group_text = QGroupBox("Text Area")

        group_case_buttons.setLayout(QGridLayout())
        group_control_buttons.setLayout(QGridLayout())
        group_text.setLayout(QVBoxLayout())

        group_case_layout: QGridLayout = group_case_buttons.layout()
        group_control_layout: QGridLayout = group_control_buttons.layout()

        # QGridLayout Parameters: widget; row; column; rowSpan; columnSpan
        group_case_layout.addWidget(self.button_upper_case, 0, 0, 1, 1)
        group_case_layout.addWidget(self.button_lower_case, 0, 1, 1, 1)
        group_case_layout.addWidget(self.button_inverse_case, 0, 2, 1, 1)
        group_case_layout.addWidget(self.button_sentence_case, 1, 0, 1, 1)
        group_case_layout.addWidget(self.button_capitalized_case, 1, 1, 1, 1)
        group_case_layout.addWidget(self.button_title_case, 1, 2, 1, 1)

        group_control_layout.addWidget(self.button_copy_text, 0, 0, 1, 1)
        group_control_layout.addWidget(self.button_paste_text, 0, 1, 1, 1)
        group_control_layout.addWidget(self.button_clear_text, 0, 2, 1, 1)

        group_text.layout().addWidget(self.text_edit)

        # </editor-fold>

        # <editor-fold desc="[+] View layout and styles">

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(group_case_buttons, stretch=0)
        layout.addWidget(group_control_buttons, stretch=0)
        layout.addWidget(group_text, stretch=1)

        # Margins, spacing and size policies

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

        # Style settings
        group_case_buttons.setProperty("class", "group group--case-buttons")
        group_control_buttons.setProperty("class", "group group--control-buttons")
        group_text.setProperty("class", "group group--text")

        self.text_edit.setObjectName("text-edit")

        self.button_sentence_case.setProperty("class", "button button--sentence")
        self.button_capitalized_case.setProperty("class", "button button--capitalized")
        self.button_upper_case.setProperty("class", "button button--upper")
        self.button_lower_case.setProperty("class", "button button--lower")
        self.button_inverse_case.setProperty("class", "button button--inverse")
        self.button_title_case.setProperty("class", "button button--title")

        self.button_copy_text.setProperty("class", "button button--copy")
        self.button_paste_text.setProperty("class", "button button--paste")
        self.button_clear_text.setProperty("class", "button button--clear")

        # </editor-fold>

        # <editor-fold desc="[+] Signal connection">

        self.case_button_clicked.connect(self.viewmodel.text_to_case)
        self.control_button_clicked.connect(self.viewmodel.on_control_signal)
        self.viewmodel.text_modified.connect(self._on_text_modified)

        # </editor-fold>

    # <editor-fold desc="[+] Viewmodel">

    @property
    def viewmodel(self) -> ConversionViewModel:
        return self._viewmodel

    @viewmodel.setter
    def viewmodel(self, value : ConversionViewModel):
        self._viewmodel = value

    # </editor-fold>

    # <editor-fold desc="[+] Methods">

    def _on_case_button_clicked(self, case_type: CaseType) -> None:
        """
        Handles case transformation button clicks and emits the `case_button_clicked` signal.

        :param case_type: Corresponding CaseType.
        """

        self.case_button_clicked.emit(case_type)

    def _on_text_changed(self) -> None:
        """
        Updates the viewmodel's text
        """

        self.viewmodel.text = self.text_edit.toPlainText()

    def _on_text_modified(self, value: str) -> None:
        """
        Updates the QTextEdit's content
        :param value: New QTextEdit value.
        """

        self.text_edit.setText(value)

    def _on_control_button_clicked(self, control_type: ControlType) -> None:
        """
        Handles control button clicks and emits the `control_button_clicked` signal.

        :param control_type: Corresponding ControlType.
        """

        self.control_button_clicked.emit(control_type)

    # </editor-fold>