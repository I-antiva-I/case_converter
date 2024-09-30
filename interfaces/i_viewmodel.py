from abc import abstractmethod, ABCMeta


class IViewModelMeta(ABCMeta):
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

