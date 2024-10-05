from __future__ import annotations
import pyperclip
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal

from enums.case_type import CaseType
from enums.control_type import ControlType

from models.shared_data_model import SharedDataModel
from models.conversion_model import ConversionModel

from interfaces.i_viewmodel import IViewModel, IViewModelMeta


class ConversionViewModel(QObject, IViewModel, metaclass=IViewModelMeta):

    # <editor-fold desc="[+] Signals">

    # Signal for property changes
    text_updated = pyqtSignal(str)

    # Signal to notify QTextEdit
    text_modified = pyqtSignal(str)

    # </editor-fold>

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

    @pyqtProperty(type=str, notify=text_updated)
    def text(self) -> str:
        return self._model.text

    @text.setter
    def text(self, value) -> None:
        if self._model.text != value:
            self._model.text = value
            self.text_updated.emit(value)

    # </editor-fold>

    # <editor-fold desc="[+] Commands">

    def text_to_case(self, case_type: CaseType):

        if case_type is CaseType.UPPER:
            self.text = self.model.to_upper_case(self.text)

        elif case_type is CaseType.LOWER:
            self.text = self.model.to_lower_case(self.text)

        elif case_type is CaseType.INVERSE:
            self.text = self.model.to_inverse_case(self.text)

        elif case_type is CaseType.SENTENCE:
            self.text = self.model.to_sentence_case(self.text)

        elif case_type is CaseType.CAPITALIZED:
            self.text = self.model.to_capitalized_case(self.text)

        elif case_type is CaseType.TITLE:
            self.text = self.model.to_title_case(self.text, self._SHARED_DATA.small_words)

        else:
            raise ValueError("Unknown/Unsupported CaseType enum value "+str(case_type))

        self.text_modified.emit(self.text)

    def on_control_signal(self, control_type: ControlType):

        if control_type is ControlType.CLEAR:
            self.text = ""
            self.text_modified.emit(self.text)

        elif control_type is ControlType.COPY:
            pyperclip.copy(text=self.text)

        elif control_type is ControlType.PASTE:
            self.text = pyperclip.paste()
            self.text_modified.emit(self.text)

        else:
            raise ValueError("Unknown/Unsupported ControlType enum value "+str(control_type))

    # </editor-fold>
