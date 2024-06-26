from typing import override


class Parent:
    def func(self) -> None:
        pass


class Child(Parent):
    @override
    def func(self) -> None:
        pass


class Child2(Parent):
    def func(self) -> None:
        pass
