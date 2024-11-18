import abc


class Production(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "check")
            and callable(subclass.check)
            and hasattr(subclass, "apply")
            and callable(subclass.apply)
            or NotImplemented
        )

    @abc.abstractmethod
    def check(self, g) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def apply(self, g):
        raise NotImplementedError
