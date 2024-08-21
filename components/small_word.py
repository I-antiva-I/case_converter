from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QFrame, QSizePolicy


class SmallWord(QWidget):
    # Signals
    button_remove_clicked = pyqtSignal(str)

    def __init__(self, word: str, index: int):
        super().__init__()

        self.word = word

        # Component Definition
        self.setLayout(QHBoxLayout())

        frame = QFrame()
        frame.setLayout(QHBoxLayout())

        label_word = QLabel(word)
        label_index = QLabel(str(index))

        remove_button = QPushButton("Remove")

        # Component Placement
        frame.layout().addWidget(label_index)
        frame.layout().addWidget(label_word)
        frame.layout().addWidget(remove_button)

        self.layout().addWidget(frame)

        # External Margins, Spacing and Size Policies
        self.layout().setContentsMargins(0, 0, 0, 0)
        frame.layout().setContentsMargins(0, 0, 0, 0)
        frame.layout().setSpacing(8)

        label_index.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        label_word.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        remove_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        frame.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)

        # Style Settings
        self.setProperty("class", "small-word")
        modifier_odd_even = "odd" if index % 2 == 1 else "even"
        frame.setProperty("class", "small-word__frame small-word__frame--"+modifier_odd_even)
        label_index.setProperty("class", "small-word__label small-word__label--index")
        label_word.setProperty("class", "small-word__label small-word__label--word")
        remove_button.setProperty("class", "button button--remove")
        label_index.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Signal Connection
        remove_button.clicked.connect(self._on_remove_button_clicked)

    def _on_remove_button_clicked(self):
        self.button_remove_clicked.emit(self.word)
