from typing import Tuple, Set, Iterable, List


class BezierF:
    @overload
    def __init__(self, p0: PointF, p1: PointF, p2: PointF, p3: PointF): ...
    @overload
    def __init__(self, x0: Single, y0: Single, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single): ...
    def Distance(self, point: PointF) -> Single: ...
    def Extremes(self) -> Tuple[Set(Single), Set(Single)]: ...
    @property
    def Bounds(self) -> RectangleF: ...
    @property
    def IsClosed(self) -> bool: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def P0(self) -> PointF: ...
    @property
    def P1(self) -> PointF: ...
    @property
    def P2(self) -> PointF: ...
    @property
    def P3(self) -> PointF: ...
    @property
    def T0(self) -> SizeF: ...
    @property
    def T3(self) -> SizeF: ...
    def PointAt(self, t: Single) -> PointF: ...
    def Project(self, point: PointF) -> Single: ...
    def Reverse(self) -> BezierF: ...
    def TangentAt(self, t: Single) -> SizeF: ...


class BezierShape:
    Unknown = 0
    Arch = 1
    SingleInflection = 2
    DoubleInflection = 3
    Cusp = 4
    Closed = 5
    LoopAtStart = 6
    LoopAtEnd = 7
    LoopOnInterior = 8


class GH_2DIndex:
    @overload
    def __init__(self, other: GH_2DIndex): ...
    @overload
    def __init__(self, new_i: int, new_j: int): ...
    def Set(self, new_i: int, new_j: int) -> None: ...
    def Shift(self, offset_i: int, offset_j: int) -> None: ...




class GH_3DIndex:
    @overload
    def __init__(self, other: GH_3DIndex): ...
    @overload
    def __init__(self, new_i: int, new_j: int, new_k: int): ...
    def Set(self, new_i: int, new_j: int, new_k: int) -> None: ...
    def Shift(self, offset_i: int, offset_j: int, offset_k: int) -> None: ...


class GH_NaturalComparer:
    def __init__(self): ...


class GH_NaturalStringComparer:
    def __init__(self): ...
    def Compare(s1: str, s2: str) -> int: ...


