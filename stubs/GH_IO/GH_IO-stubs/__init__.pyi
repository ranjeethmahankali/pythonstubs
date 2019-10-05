__all__ = ['Serialization','Types','UserInterface']
from typing import Tuple, Set, Iterable, List


class Branch:
    Unset = 0
    Developer = 1
    Trunk = 2
    ReleaseCandidate = 3
    Release = 4


class GH_ISerializable:
    def Read(self, reader: GH_IReader) -> bool: ...
    def Write(self, writer: GH_IWriter) -> bool: ...


class VersionNumber:
    @overload
    def __init__(self, version: Version): ...
    @overload
    def __init__(self, majorVersionNumber: int, minorVersionNumber: int, versionQuartetYyddd: int, versionQuartetHhmmb: int): ...
    @overload
    def __init__(self, major: int, minor: int, time: DateTime, buildBranch: Branch): ...
    @overload
    def CompareTo(self, value: VersionNumber) -> int: ...
    @overload
    def CompareTo(self, value: Object) -> int: ...
    @property
    def BuildBranch(self) -> Branch: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def Major(self) -> int: ...
    @property
    def MaxMajorVersionNumber() -> int: ...
    @property
    def MaxMinorVersionNumber() -> int: ...
    @property
    def MaxValid() -> VersionNumber: ...
    @property
    def MaxValidBuildBranch() -> Branch: ...
    @property
    def MaxValidTime() -> DateTime: ...
    @property
    def MinMajorVersionNumber() -> int: ...
    @property
    def MinMinorVersionNumber() -> int: ...
    @property
    def Minor(self) -> int: ...
    @property
    def MinValid() -> VersionNumber: ...
    @property
    def MinValidBuildBranch() -> Branch: ...
    @property
    def MinValidTime() -> DateTime: ...
    @property
    def Time(self) -> DateTime: ...
    @property
    def Unset() -> VersionNumber: ...
    @property
    def UnsetBuildBranch() -> Branch: ...
    @property
    def UnsetTime() -> DateTime: ...
    def ToString(self) -> str: ...
    def ToVersion(self) -> Version: ...
    @overload
    def TryParse(s: str) -> Tuple[bool, VersionNumber]: ...
    @overload
    def TryParse(v: Version) -> Tuple[bool, VersionNumber]: ...
