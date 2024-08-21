from abc import abstractmethod, ABCMeta

from PyQt5.QtCore import QObject


class IViewModelMeta(ABCMeta, type(QObject)):
    pass


class IViewModel:
    __metaclass__ = IViewModelMeta

    @property
    @abstractmethod
    def view(self):
        pass

    @view.setter
    @abstractmethod
    def view(self, value):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @model.setter
    @abstractmethod
    def model(self, value):
        pass

    # [i] Should be read only
    @property
    @abstractmethod
    def shared_data(self):
        pass

