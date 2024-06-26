from typing import TypedDict, Unpack


class Args(TypedDict):
    a: str
    b: int


def func(**kwargs: Unpack[Args]) -> None:
    print(kwargs)


func(a='a', b=1)

# # **kwargs : dict[str, int]
# def func(**kwargs: int) -> None:
#     print(kwargs)
#
# func(a=1, b=2)
