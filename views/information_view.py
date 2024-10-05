from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QHBoxLayout, QFrame, \
    QScrollArea, QSizePolicy
from PyQt5.QtCore import Qt

from components.small_word import SmallWord
from interfaces.i_view import IView, IViewMeta
from managers.scroll_bar_manager import manage_scroll_bar
from viewmodels.information_viewmodel import InformationViewModel


class InformationView(QWidget, IView, metaclass=IViewMeta):
    """
    The `ConversionView` class provides a user interface for managing small words and viewing information on text
    case transformations.
    """
    # <editor-fold desc="[+] Signals">

    # Emitted when a new word is added to the list of small words.
    word_added = pyqtSignal(str)

    # Emitted when a word is removed from the list of small words.
    word_removed = pyqtSignal(str)

    # </editor-fold>

    def __init__(self, viewmodel: InformationViewModel):
        """
        Initializes view.
        :param viewmodel: Corresponding InformationViewModel.
        """
        super().__init__()

        self.viewmodel = viewmodel

        # <editor-fold desc="[+] Small words">

        # Word list
        self.frame_word_list = QFrame()
        self.frame_word_list.setLayout(QVBoxLayout())
        self.frame_word_list.layout().setAlignment(Qt.AlignTop)

        self.scroll_area_word_list = QScrollArea()
        self.scroll_area_word_list.setWidgetResizable(True)
        self.scroll_area_word_list.setWidget(self.frame_word_list)

        # New word
        self.frame_new_word = QFrame()
        self.frame_new_word.setLayout(QHBoxLayout())

        self.line_edit_new_word = QLineEdit()
        self.button_add_new_word = QPushButton("Add")
        self.button_add_new_word.clicked.connect(self._on_add_button_clicked)

        self.frame_new_word.layout().addWidget(self.line_edit_new_word)
        self.frame_new_word.layout().addWidget(self.button_add_new_word)

        # </editor-fold>

        # <editor-fold desc="[+] Case info labels">

        emphasis_color: str = "deepskyblue"

        label_info_case_upper = QLabel("⭐ <b>Upper</b> - changes each letter of the text to upper case. "
                                       "Example: <b>'a sentence with words'</b> turns into <b>'A SENTENCE WITH WORDS'</b>.")

        label_info_case_lower = QLabel("⭐ <b>Lower</b> - changes each letter of the text to lower case. "
                                       "Example: <b>'A SENTENCE WITH WORDS'</b> turns into <b>'a sentence with words'</b>.")

        label_info_case_capitalize = QLabel("⭐ <b>Capitalize</b> - changes the first letter of each word "
                                            "to upper case and all other letters to lower case. "
                                            "Example: <b>'A sentence with words'</b> turns into <b>'A Sentence with Words'</b>.")

        label_info_case_title = QLabel("⭐ <b>Title</b> - if word is included in the <b>'small words'</b>, "
                                       "changes each letter of the word to lower case, otherwise applies "
                                       "the 'Capitalize' rule. "
                                       "List of the <b>'small words'</b> can be modified. "
                                       f"Example: <b>'A SENTENCE "
                                       f"<span style='color: {emphasis_color};'>WITH</span> WORDS</b> "
                                       f"turns into <b>'A Sentence <span "
                                       f"style='color: {emphasis_color};'>with</span> Words'</b>.")

        label_info_case_reverse = QLabel("⭐ <b>Reverse</b> - changes lower case to upper case and vice versa. "
                                         "Example: <b>'A Sentence With Words'</b> turns into <b>'a sENTENCE wITH wORDS'</b>.")

        label_info_case_sentence = QLabel("⭐ <b>Sentence</b> - changes the first letter of the first word "
                                          "to upper case and all other letters to lower case. "
                                          "Example: <b>'a sentence with words</b> turns into <b>'A sentence with words'</b>.")

        # Turn on word wrap
        label_info_case_upper.setWordWrap(True)
        label_info_case_lower.setWordWrap(True)
        label_info_case_title.setWordWrap(True)
        label_info_case_capitalize.setWordWrap(True)
        label_info_case_reverse.setWordWrap(True)
        label_info_case_sentence.setWordWrap(True)

        self.frame_info = QFrame()
        self.frame_info.setLayout(QVBoxLayout())

        self.frame_info.layout().addWidget(label_info_case_upper)
        self.frame_info.layout().addWidget(label_info_case_lower)
        self.frame_info.layout().addWidget(label_info_case_reverse)
        self.frame_info.layout().addWidget(label_info_case_sentence)
        self.frame_info.layout().addWidget(label_info_case_capitalize)
        self.frame_info.layout().addWidget(label_info_case_title)

        self.scroll_area_info = QScrollArea()
        self.scroll_area_info.setWidgetResizable(True)
        self.scroll_area_info.setWidget(self.frame_info)

        # </editor-fold>

        # <editor-fold desc="[+] Groups">

        self.group_words = QGroupBox("Small words")
        self.group_words.setLayout(QVBoxLayout())
        self.group_words.layout().addWidget(self.scroll_area_word_list)
        self.group_words.layout().addWidget(self.frame_new_word)

        self.group_info = QGroupBox("How case conversion works")
        self.group_info.setLayout(QVBoxLayout())
        self.group_info.layout().addWidget(self.scroll_area_info)

        # </editor-fold>

        # <editor-fold desc="[+] View layout and styles">

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.group_info, stretch=1)
        self.layout().addWidget(self.group_words, stretch=1)

        # Margins, spacing and size policies

        self.group_info.layout().setContentsMargins(0, 0, 0, 0)
        self.group_info.layout().setSpacing(8)
        self.group_info.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)

        self.frame_info.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_info.layout().setSpacing(0)

        self.group_words.layout().setContentsMargins(0, 0, 0, 0)
        self.group_words.layout().setSpacing(8)
        self.group_words.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)

        self.frame_word_list.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_word_list.layout().setSpacing(8)
        self.frame_word_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.frame_new_word.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_new_word.layout().setSpacing(8)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(8)

        # Style Settings

        self.scroll_area_info.setObjectName("scroll-area-info")
        self.scroll_area_info.setProperty("class", "scroll-area scroll-area--with-scroll-bar")

        self.scroll_area_word_list.setObjectName("scroll-area-word-list")

        self.line_edit_new_word.setObjectName("line-edit")

        self.group_info.setProperty("class", "group group--info")
        self.group_words.setProperty("class", "group group--words")

        self.frame_word_list.setProperty("class", "frame frame--words")
        self.frame_info.setProperty("class", "frame frame--info")

        self.button_add_new_word.setProperty("class", "button button--add")

        label_info_case_title.setProperty("class", "label label--last")

        # </editor-fold>

        # <editor-fold desc="[+] Signal Connection">

        self.scroll_area_word_list.verticalScrollBar().\
            rangeChanged.connect(lambda min_v, max_v: manage_scroll_bar(self.scroll_area_word_list, "scroll-area", max_v))

        self.viewmodel.small_words_modified.connect(self.display_words)

        self.word_added.connect(self.viewmodel.on_word_added)
        self.word_removed.connect(self.viewmodel.on_word_removed)

        # </editor-fold>

        self.word_components = []

        self.display_words()

    # <editor-fold desc="[+] Viewmodel">

    @property
    def viewmodel(self) -> InformationViewModel:
        return self._viewmodel

    @viewmodel.setter
    def viewmodel(self, value : InformationViewModel):
        self._viewmodel = value

    # </editor-fold>

    # <editor-fold desc="[+] Methods">

    def _on_add_button_clicked(self) -> None:
        """
        Handles the "Add" button click event.
        """
        word: str = self.line_edit_new_word.text()
        self.word_added.emit(word)

    def _on_remove_button_clicked(self, word: str) -> None:
        """
        Handles the "Remove" button click event.
        """
        self.word_removed.emit(word)

    def display_words(self) -> None:
        """
        Clears the current word list and refills it with the small words from the viewmodel.
        """
        for word in self.word_components:
            word.deleteLater()
            pass

        self.word_components.clear()

        for index, word in enumerate(self.viewmodel.sorted_small_words()):
            component = SmallWord(word, index + 1)
            self.word_components.append(component)
            self.frame_word_list.layout().addWidget(component)

            component.button_remove_clicked.connect(self._on_remove_button_clicked)

    # </editor-fold>
