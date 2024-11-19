import abc

class CannotApplyProduction(Exception):
    pass

class Production(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get_left_side")
            and callable(subclass.get_left_side)
            and hasattr(subclass, "get_right_side")
            and callable(subclass.get_right_side)
            or NotImplemented
        )

    @abc.abstractmethod
    def get_left_side(self):
        """
        :return: A graph (type Graph) to be matched against the whole graph
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_right_side(self, left, lvl: int):
        """
        :param left: by now left side updated with values from the graph (type Graph)
        :param lvl: node level, prepend to any new nodes created, remember their label must be unique
        :return: right side with correct parameters
        """
        raise NotImplementedError