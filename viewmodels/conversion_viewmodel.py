import pyperclip
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal

from models.shared_data_model import SharedDataModel
from models.conversion_model import ConversionModel
from interfaces.i_viewmodel import IViewModel, IViewModelMeta
from views.conversion_view import ConversionView


class ConversionViewModel(IViewModel, metaclass=IViewModelMeta):
    # Signals
    text_modified = pyqtSignal(str)
    copy_text_signal = pyqtSignal(str)
    paste_text_signal = pyqtSignal()
    clear_text_signal = pyqtSignal()

    def __init__(self, model: ConversionModel, shared_data: SharedDataModel = None):
        super().__init__()

        self.model = model
        self._SHARED_DATA = shared_data

    # <editor-fold desc="[+] Model">

    @property
    def model(self) -> ConversionModel:
        return self._model

    @model.setter
    def model(self, value : ConversionModel):
        self._model = value

    @property
    def shared_data(self) -> SharedDataModel:
        return self._SHARED_DATA

    # </editor-fold>

    # <editor-fold desc="[+] Model Properties">

    @pyqtProperty(type=str, notify=text_modified)
    def text(self) -> str:
        return self._model.text

    @text.setter
    def text(self, value) -> None:
        if self._model.text != value:
            self._model.text = value
            self.text_modified.emit(value)

    # </editor-fold>

    # <editor-fold desc="[+] Commands">

    def set_upper_case(self):
        self.text = self.model.to_upper_case(self.model.text)

    def set_lower_case(self):
        self.text = self.model.to_lower_case(self.model.text)

    def set_inverse_case(self):
        self.text = self.model.to_inverse_case(self.model.text)

    def set_capitalized_case(self):
        self.text = self.model.to_capitalized_case(self.model.text)

    def set_title_case(self):
        self.text = self.model.to_title_case(self.model.text, self._SHARED_DATA.small_words)

    def set_sentence_case(self):
        self.text = self.model.to_sentence_case(self.model.text)

    def copy_text(self):
        #pyperclip.copy(self._view.text_edit.toPlainText())
        pass

    def paste_text(self):
        #self._view.text_edit.setPlainText(pyperclip.paste())
        pass

    def paste_text(self):
        #self._view.text_edit.setPlainText("")
        pass

    # </editor-fold>
