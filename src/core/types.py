from typing import Dict, List, Optional, Protocol, Tuple, TypedDict


class Point(TypedDict):
    x: int
    y: int


class Size(TypedDict):
    width: int
    height: int


class Rect(TypedDict):
    x: int
    y: int
    width: int
    height: int


class Color(TypedDict):
    r: int
    g: int
    b: int
    a: int
