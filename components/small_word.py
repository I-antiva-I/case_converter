from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QFrame, QSizePolicy


class SmallWord(QWidget):
    """
    The `SmallWord` represents a word and its index in a styled frame, with a remove button.
    """

    # <editor-fold desc="[+] Signals">

    # Signal emitted when the remove button is clicked, passing the word as a string.
    button_remove_clicked = pyqtSignal(str)

    # </editor-fold>

    def __init__(self, word: str, index: int):
        """
        Initializes the SmallWord widget with a given word and index.

        :param word: The word assigned to the instance `SmallWord`.
        :param index: The index of the word.
        """

        super().__init__()

        self.word = word

        # Component definition
        frame = QFrame()
        frame.setLayout(QHBoxLayout())

        label_word = QLabel(word)
        label_index = QLabel(str(index))

        remove_button = QPushButton("Remove")

        # Component placement
        frame.layout().addWidget(label_index)
        frame.layout().addWidget(label_word)
        frame.layout().addWidget(remove_button)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(frame)

        # Margins, spacing and size policies
        self.layout().setContentsMargins(0, 0, 0, 0)
        frame.layout().setContentsMargins(0, 0, 0, 0)
        frame.layout().setSpacing(8)

        label_index.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        label_word.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        remove_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)

        # Style settings
        self.setProperty("class", "small-word")
        modifier_odd_even = "odd" if index % 2 == 1 else "even"
        frame.setProperty("class", "small-word__frame small-word__frame--"+modifier_odd_even)
        label_index.setProperty("class", "small-word__label small-word__label--index")
        label_word.setProperty("class", "small-word__label small-word__label--word")
        remove_button.setProperty("class", "button button--remove")
        label_index.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Signal connection
        remove_button.clicked.connect(self._on_remove_button_clicked)

    def _on_remove_button_clicked(self):
        """
        Emits the `button_remove_clicked` signal when the remove button is clicked.
        """
        self.button_remove_clicked.emit(self.word)
