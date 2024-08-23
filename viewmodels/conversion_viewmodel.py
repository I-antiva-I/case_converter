import pyperclip
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal

from models.shared_data_model import SharedDataModel
from models.conversion_model import ConversionModel
from interfaces.i_viewmodel import IViewModel, IViewModelMeta
from views.conversion_view import ConversionView


class ConversionViewModel(QObject, IViewModel):
    __metaclass__ = IViewModelMeta

    # Signals
    text_modified = pyqtSignal(str)

    def __init__(self, view: ConversionView, model: ConversionModel, shared_data: SharedDataModel = None):
        super().__init__()

        self.view = view
        self.model = model
        self._SHARED_DATA = shared_data

        # Signal connection
        self.view.button_upper_case.clicked.connect(lambda: self._on_button_upper_case_clicked())
        self.view.button_lower_case.clicked.connect(lambda: self._on_button_lower_case_clicked())
        self.view.button_inverse_case.clicked.connect(lambda: self._on_button_inverse_case_clicked())
        self.view.button_sentence_case.clicked.connect(lambda: self._on_button_sentence_case_clicked())
        self.view.button_capitalized_case.clicked.connect(lambda: self._on_button_capitalized_case_clicked())
        self.view.button_title_case.clicked.connect(lambda: self._on_button_title_case_clicked())
        
        self.view.text_edit.textChanged.connect(self._on_text_changed)

        self.view.button_copy_text.clicked.connect(lambda: self._on_button_copy_clicked())
        self.view.button_paste_text.clicked.connect(lambda: self._on_button_paste_clicked())
        self.view.button_clear_text.clicked.connect(lambda: self._on_button_clear_clicked())

    # <editor-fold desc="[+] View & Model">

    @property
    def view(self) -> ConversionView:
        return self._view

    @view.setter
    def view(self, value : ConversionView):
        self._view = value

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

    # <editor-fold desc="[+] Signal Slots">

    def _on_button_upper_case_clicked(self):
        self._view.text_edit.setText(self.model.to_upper_case(self.model.text))

    def _on_button_lower_case_clicked(self):
        self._view.text_edit.setText(self.model.to_lower_case(self.model.text))

    def _on_button_inverse_case_clicked(self):
        self._view.text_edit.setText(self.model.to_inverse_case(self.model.text))

    def _on_button_capitalized_case_clicked(self):
        self._view.text_edit.setText(self.model.to_capitalized_case(self.model.text))

    def _on_button_title_case_clicked(self):
        self._view.text_edit.setText(self.model.to_title_case(self.model.text, self._SHARED_DATA.small_words))

    def _on_button_sentence_case_clicked(self):
        self._view.text_edit.setText(self.model.to_sentence_case(self.model.text))

    def _on_text_changed(self):
        self.text = self._view.text_edit.toPlainText()

    def _on_button_copy_clicked(self):
        pyperclip.copy(self._view.text_edit.toPlainText())

    def _on_button_paste_clicked(self):
        self._view.text_edit.setPlainText(pyperclip.paste())

    def _on_button_clear_clicked(self):
        self._view.text_edit.setPlainText("")

    # </editor-fold>
