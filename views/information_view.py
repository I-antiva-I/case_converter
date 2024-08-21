from typing import List

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QGridLayout, QHBoxLayout, QTextEdit, QFrame, \
    QScrollArea, QSizePolicy
from PyQt5.QtCore import Qt


from components.small_word import SmallWord
from managers.scroll_bar_manager import manage_scroll_bar


class InformationView(QWidget):

    def __init__(self):
        super().__init__()

        # <editor-fold desc="[+] Small Words">

        self.group_words = QGroupBox("Small words")
        self.group_words.setLayout(QVBoxLayout())

        # Word List
        self.frame_word_list = QFrame()
        self.frame_word_list.setLayout(QVBoxLayout())

        self.scroll_area_word_list = QScrollArea()
        self.scroll_area_word_list.setWidgetResizable(True)
        self.scroll_area_word_list.setWidget(self.frame_word_list)

        # New Word
        self.frame_new_word = QFrame()
        self.frame_new_word.setLayout(QHBoxLayout())

        self.line_edit_new_word = QLineEdit()
        self.button_add_new_word = QPushButton("Add")

        self.frame_new_word.layout().addWidget(self.line_edit_new_word)
        self.frame_new_word.layout().addWidget(self.button_add_new_word)

        self.group_words.layout().addWidget(self.scroll_area_word_list)
        self.group_words.layout().addWidget(self.frame_new_word)

        # </editor-fold>

        # <editor-fold desc="[+] Case Info Labels">

        self.group_info = QGroupBox("How case conversion works")
        self.group_info.setLayout(QVBoxLayout())

        emphasis_color: str = "dodgerblue"
        label_info_case_upper = QLabel("⭐ <b>Upper</b> - changes each letter of the text to upper case. "
                                       "Example: <b>'a sentence with words'</b> turns into <b>'A SENTENCE WITH WORDS'</b>.")

        label_info_case_lower = QLabel("⭐ <b>Lower</b> - changes each letter of the text to lower case. "
                                       "Example: <b>'A SENTENCE WITH WORDS'</b> turns into <b>'a sentence with words'</b>.")

        label_info_case_capitalize = QLabel("⭐ <b>Capitalize</b> - changes the first letter of each word "
                                            "to upper case and all other letters to lower case. "
                                            "Example: <b>'A sentence with words'</b> turns into <b>'A Sentence with Words'</b>.")

        label_info_case_title = QLabel("⭐ <b>Title</b> - if word is included in the <b>'small words'</b>, "
                                       "changes each letter of the word to lower case, otherwise applies the 'Capitalize' rule. "
                                       "List of the <b>'small words'</b> can be modified. "
                                       f"Example: <b>'A SENTENCE <span style='color: {emphasis_color};'>WITH</span> WORDS</b> "
                                       f"turns into <b>'A Sentence <span style='color: {emphasis_color};'>with</span> Words'</b>.")

        label_info_case_reverse = QLabel("⭐ <b>Reverse</b> - changes lower case to upper case and vice versa. "
                                         "Example: <b>'A Sentence With Words'</b> turns into <b>'a sENTENCE wITH wORDS'</b>.")

        label_info_case_sentence = QLabel("⭐ <b>Sentence</b> - changes the first letter of the first word "
                                          "to upper case and all other letters to lower case. "
                                          "Example: <b>'a sentence with words</b> turns into <b>'A sentence with words'</b>.")

        # Turn on Word Wrap
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

        self.group_info.layout().addWidget(self.scroll_area_info)

        # </editor-fold>

        # Group Placement
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.group_info, stretch=1)
        self.layout().addWidget(self.group_words, stretch=1)

        # External Margins, Spacing and Size Policies
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
        self.frame_word_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)

        self.frame_new_word.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_new_word.layout().setSpacing(8)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(8)

        # Style Settings
        self.scroll_area_info.setObjectName("scroll-area-info")
        self.scroll_area_info.setProperty("class", "scroll-area scroll-area--with-scroll-bar")
        self.line_edit_new_word.setObjectName("line-edit")
        self.scroll_area_word_list.setObjectName("scroll-area-word-list")
        self.group_info.setProperty("class", "group group--info")
        self.group_words.setProperty("class", "group group--words")
        self.frame_word_list.setProperty("class", "frame frame--words")
        self.frame_info.setProperty("class", "frame frame--info")
        self.button_add_new_word.setProperty("class", "button button--add")
        label_info_case_title.setProperty("class", "label label--last")

        # Signal Connection
        self.scroll_area_word_list.verticalScrollBar().\
            rangeChanged.connect(lambda min_v, max_v: manage_scroll_bar(self.scroll_area_word_list, "scroll-area", max_v))

    @property
    def word_container(self) -> QWidget:
        return self.frame_word_list
