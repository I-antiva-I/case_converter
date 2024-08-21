from typing import Set, List
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QWidget

from components.small_word import SmallWord
from models.shared_data_model import SharedDataModel
from models.information_model import InformationModel
from interfaces.i_viewmodel import IViewModel, IViewModelMeta
from views.information_view import InformationView


class InformationViewModel(QObject, IViewModel):
    __metaclass__ = IViewModelMeta

    # Signals
    small_words_modified = pyqtSignal(set)

    def __init__(self, view: InformationView, model: InformationModel, shared_data: SharedDataModel = None):
        super().__init__()

        self.view = view
        self.model = model
        self._SHARED_DATA = shared_data

        self._word_components: List[QWidget] = []

        self.shared_data.set_small_words(self.model.small_words)
        self.add_small_words_to_view()

        # Signal connection
        self.view.button_add_new_word.clicked.connect(lambda: self._on_add_button_clicked())
        self.small_words_modified.connect(self._SHARED_DATA.set_small_words)

    # <editor-fold desc="[+] View & Model">

    @property
    def view(self) -> InformationView:
        return self._view

    @view.setter
    def view(self, value : InformationView):
        self._view = value

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

    # <editor-fold desc="[+] Model Properties">

    @pyqtProperty(type=set, notify=small_words_modified)
    def small_words(self) -> Set[str]:
        return self._model.small_words

    @small_words.setter
    def small_words(self, value) -> None:
        if self._model.small_words != value:
            self._model.small_words = value
            self.small_words_modified.emit(value)

    # </editor-fold>

    # <editor-fold desc="[+] Signal Slots">

    def _on_remove_button_clicked(self, word):
        self.model.small_words.discard(word)
        self.add_small_words_to_view()
        self.small_words_modified.emit(self.model.small_words)

    def _on_add_button_clicked(self):
        word_to_add: str = self.view.line_edit_new_word.text().strip(" ").lower()
        self._add_small_word(word_to_add)
        self.view.line_edit_new_word.clear()

    def _add_small_word(self, word):
        self.model.small_words.add(word)
        self.add_small_words_to_view()
        self.small_words_modified.emit(self.model.small_words)

    def add_small_words_to_view(self):
        for component in self._word_components:
            component.deleteLater()

        self._word_components.clear()

        for index, word in enumerate(self.model.sorted_small_words):
            component = SmallWord(word, index + 1)
            self._word_components.append(component)
            self.view.word_container.layout().addWidget(component)
            component.button_remove_clicked.connect(self._on_remove_button_clicked)
