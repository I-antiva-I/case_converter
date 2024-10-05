from __future__ import annotations
from typing import Set, List

import re
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QWidget

from components.small_word import SmallWord
from models.shared_data_model import SharedDataModel
from models.information_model import InformationModel
from interfaces.i_viewmodel import IViewModel, IViewModelMeta


class InformationViewModel(QObject, IViewModel, metaclass=IViewModelMeta):

    # Signals
    small_words_updated = pyqtSignal(set)
    # Signals
    small_words_modified = pyqtSignal(set)

    def __init__(self, model: InformationModel, shared_data: SharedDataModel = None):
        super().__init__()

        self.model = model
        self._SHARED_DATA = shared_data
        self.shared_data.set_small_words(self.small_words)

        #self._word_components: List[QWidget] = []


       # self.add_small_words_to_view()

        # Signal connection
        #self.view.button_add_new_word.clicked.connect(lambda: self._on_add_button_clicked())
       # self.small_words_modified.connect(self._SHARED_DATA.set_small_words)

    # <editor-fold desc="[+] Model">

    @property
    def model(self) -> InformationModel:
        return self._model

    @model.setter
    def model(self, value : InformationModel):
        self._model = value

    @property
    def shared_data(self) -> SharedDataModel:
        return self._SHARED_DATA

    # </editor-fold>

    # <editor-fold desc="[+] Model properties">

    @pyqtProperty(type=set, notify=small_words_updated)
    def small_words(self) -> Set[str]:
        return self._model.small_words

    @small_words.setter
    def small_words(self, value) -> None:
        if self._model.small_words != value:
            self._model.small_words = value
            self.small_words_updated.emit(value)

    def sorted_small_words(self) -> List[str]:
        return self.model.sorted_small_words


    # </editor-fold>

    # <editor-fold desc="[+] Signal Slots">
    def on_word_removed(self, word):
        self.small_words.discard(word)
        self.small_words_modified.emit(self.small_words)

    def on_word_added(self, word: str):
        characters_to_remove: str = "!?.,;:"
        cleared_string: str = re.sub(fr'[{characters_to_remove}]', "", word)
        words_to_add: List[str] = cleared_string.strip(" ").lower().split(" ")

        if "" in words_to_add:
            words_to_add.remove("")

        if len(words_to_add) == 0:
            return
        elif len(words_to_add) == 1:
            self._add_single_small_word(words_to_add[0])
        else:
            self._add_multiple_small_words(words_to_add)

    def _add_single_small_word(self, word: str):
        self.model.add_single_small_word(word)
        self.small_words_modified.emit(self.small_words)

    def _add_multiple_small_words(self, words: List[str]):
        self.model.add_multiple_small_words(words)
        self.small_words_modified.emit(self.small_words)
