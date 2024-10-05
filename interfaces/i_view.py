from abc import abstractmethod, ABCMeta

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget

from interfaces.i_viewmodel import IViewModel


class IViewMeta(ABCMeta, type(QWidget)):
    pass


class IView(metaclass=IViewMeta):
    @property
    @abstractmethod
    def viewmodel(self) -> IViewModel:
        """
        Abstract getter for the viewmodel.
        """
        pass

    @viewmodel.setter
    @abstractmethod
    def viewmodel(self, value: IViewModel):
        """
        Abstract setter for the viewmodel.
        """
        pass
