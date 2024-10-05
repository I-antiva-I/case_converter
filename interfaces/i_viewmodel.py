from abc import abstractmethod, ABCMeta

from PyQt5.QtCore import QObject


class IViewModelMeta(ABCMeta, type(QObject)):
    pass


class IViewModel(metaclass=IViewModelMeta):
    @property
    @abstractmethod
    def model(self):
        """
        Abstract getter for the model.
        """
        pass

    @model.setter
    @abstractmethod
    def model(self, value):
        """
        Abstract setter for the model.
        """
        pass

    @property
    @abstractmethod
    def shared_data(self):
        """
        Abstract getter for the shared data.
        """
        pass

