from typing import Tuple, Set, Iterable, List


class BrepCurveList:
    def Add(self, curve: Curve) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Curve: ...
    def GetEnumerator(self) -> IEnumerator: ...


class BrepEdgeList:
    @overload
    def Add(self, curve3dIndex: int) -> BrepEdge: ...
    @overload
    def Add(self, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, edgeTolerance: float) -> BrepEdge: ...
    @overload
    def Add(self, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, edgeTolerance: float) -> BrepEdge: ...
    @overload
    def Add(self, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge: ...
    @overload
    def Add(self, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> BrepEdge: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def SplitEdgeAtParameters(self, edgeIndex: int, edgeParameters: Iterable[float]) -> int: ...
    def SplitKinkyEdge(self, edgeIndex: int, kinkToleranceRadians: float) -> bool: ...


class BrepFaceList:
    @overload
    def Add(self, surface: Surface) -> BrepFace: ...
    @overload
    def Add(self, surfaceIndex: int) -> BrepFace: ...
    def AddConeFace(self, vertex: BrepVertex, edge: BrepEdge, revEdge: bool) -> BrepFace: ...
    def AddRuledFace(self, edgeA: BrepEdge, revEdgeA: bool, edgeB: BrepEdge, revEdgeB: bool) -> BrepFace: ...
    def ExtractFace(self, faceIndex: int) -> Brep: ...
    def Flip(self, onlyReversedFaces: bool) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> BrepFace: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def RemoveAt(self, faceIndex: int) -> None: ...
    def RemoveSlits(self) -> bool: ...
    def ShrinkFaces(self) -> bool: ...
    def SplitBipolarFaces(self) -> bool: ...
    def SplitClosedFaces(self, minimumDegree: int) -> bool: ...
    def SplitFaceAtTangents(self, faceIndex: int) -> bool: ...
    def SplitFacesAtTangents(self) -> bool: ...
    def SplitKinkyFace(self, faceIndex: int, kinkTolerance: float) -> bool: ...
    @overload
    def SplitKinkyFaces(self) -> bool: ...
    @overload
    def SplitKinkyFaces(self, kinkTolerance: float) -> bool: ...
    @overload
    def SplitKinkyFaces(self, kinkTolerance: float, compact: bool) -> bool: ...
    def StandardizeFaceSurface(self, faceIndex: int) -> bool: ...
    def StandardizeFaceSurfaces(self) -> None: ...


class BrepLoopList:
    @overload
    def Add(self, loopType: BrepLoopType) -> BrepLoop: ...
    @overload
    def Add(self, loopType: BrepLoopType, face: BrepFace) -> BrepLoop: ...
    def AddOuterLoop(self, faceIndex: int) -> BrepLoop: ...
    def AddPlanarFaceLoop(self, faceIndex: int, loopType: BrepLoopType, boundaryCurves: Iterable[Curve]) -> BrepLoop: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> BrepLoop: ...
    def GetEnumerator(self) -> IEnumerator: ...


class BrepSurfaceList:
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Surface: ...
    def GetEnumerator(self) -> IEnumerator: ...


class BrepTrimList:
    @overload
    def Add(self, curve2dIndex: int) -> BrepTrim: ...
    @overload
    def Add(self, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim: ...
    @overload
    def Add(self, rev3d: bool, edge: BrepEdge, curve2dIndex: int) -> BrepTrim: ...
    @overload
    def Add(self, edge: BrepEdge, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim: ...
    def AddCurveOnFace(self, face: BrepFace, edge: BrepEdge, rev3d: bool, curve2dIndex: int) -> BrepTrim: ...
    def AddSingularTrim(self, vertex: BrepVertex, loop: BrepLoop, iso: IsoStatus, curve2dIndex: int) -> BrepTrim: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> BrepTrim: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @overload
    def MatchEnds(self) -> bool: ...
    @overload
    def MatchEnds(self, trimIndex: int) -> bool: ...
    @overload
    def MatchEnds(self, loop: BrepLoop) -> bool: ...
    @overload
    def MatchEnds(self, trim0: BrepTrim, trim1: BrepTrim) -> bool: ...


class BrepVertexList:
    @overload
    def Add(self) -> BrepVertex: ...
    @overload
    def Add(self, point: Point3d, vertexTolerance: float) -> BrepVertex: ...
    def AddPointOnFace(self, face: BrepFace, s: float, t: float) -> BrepVertex: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> BrepVertex: ...
    def GetEnumerator(self) -> IEnumerator: ...


class MeshFaceList:
    @overload
    def AddFace(self, face: MeshFace) -> int: ...
    @overload
    def AddFace(self, vertex1: int, vertex2: int, vertex3: int) -> int: ...
    @overload
    def AddFace(self, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> int: ...
    def AddFaces(self, faces: Iterable[MeshFace]) -> Set(int): ...
    def AdjacentFaces(self, faceIndex: int) -> Set(int): ...
    def Clear(self) -> None: ...
    def ConvertNonPlanarQuadsToTriangles(self, planarTolerance: float, angleToleranceRadians: float, splitMethod: int) -> int: ...
    def ConvertQuadsToTriangles(self) -> bool: ...
    def ConvertTrianglesToQuads(self, angleToleranceRadians: float, minimumDiagonalLengthRatio: float) -> bool: ...
    def CullDegenerateFaces(self) -> int: ...
    @overload
    def DeleteFaces(self, faceIndexes: Iterable[int]) -> int: ...
    @overload
    def DeleteFaces(self, faceIndexes: Iterable[int], compact: bool) -> int: ...
    def Destroy(self) -> None: ...
    def ExtractDuplicateFaces(self) -> Mesh: ...
    def ExtractFaces(self, faceIndices: Iterable[int]) -> Mesh: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> MeshFace: ...
    @property
    def QuadCount(self) -> int: ...
    @property
    def TriangleCount(self) -> int: ...
    def GetClashingFacePairs(self, maxPairCount: int) -> Set(IndexPair): ...
    def GetConnectedFaces(self, faceIndex: int, angleRadians: float, greaterThanAngle: bool) -> Set(int): ...
    def GetConnectedFacesToEdges(self, startFaceIndex: int, treatNonmanifoldLikeUnwelded: bool) -> Set(int): ...
    def GetDuplicateFaces(self) -> Set(int): ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetFace(self, index: int) -> MeshFace: ...
    def GetFaceAspectRatio(self, index: int) -> float: ...
    def GetFaceBoundingBox(self, faceIndex: int) -> BoundingBox: ...
    def GetFaceCenter(self, faceIndex: int) -> Point3d: ...
    def GetFaceVertices(self, faceIndex: int) -> Tuple[bool, Point3f, Point3f, Point3f, Point3f]: ...
    def GetTopologicalVertices(self, faceIndex: int) -> Set(int): ...
    def GetZeroAreaFaces(self) -> Tuple[bool, Set(int), Set(int)]: ...
    def HasNakedEdges(self, faceIndex: int) -> bool: ...
    def Insert(self, index: int, face: MeshFace) -> None: ...
    def IsHidden(self, faceIndex: int) -> bool: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def RemoveAt(self, index: int, compact: bool) -> None: ...
    def RemoveZeroAreaFaces(self, fixedFaceCount: int) -> Tuple[int, int]: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: MeshFace) -> None: ...
    @overload
    def SetFace(self, index: int, face: MeshFace) -> bool: ...
    @overload
    def SetFace(self, index: int, vertex1: int, vertex2: int, vertex3: int) -> bool: ...
    @overload
    def SetFace(self, index: int, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> bool: ...
    @overload
    def ToIntArray(self, asTriangles: bool) -> Set(int): ...
    @overload
    def ToIntArray(self, asTriangles: bool, replacedIndices: List) -> Tuple[Set(int), List]: ...


class MeshFaceNormalList:
    @overload
    def AddFaceNormal(self, normal: Vector3f) -> int: ...
    @overload
    def AddFaceNormal(self, normal: Vector3d) -> int: ...
    @overload
    def AddFaceNormal(self, x: float, y: float, z: float) -> int: ...
    @overload
    def AddFaceNormal(self, x: Single, y: Single, z: Single) -> int: ...
    def Clear(self) -> None: ...
    def ComputeFaceNormals(self) -> bool: ...
    def Destroy(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Vector3f: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Vector3f) -> None: ...
    @overload
    def SetFaceNormal(self, index: int, normal: Vector3d) -> bool: ...
    @overload
    def SetFaceNormal(self, index: int, normal: Vector3f) -> bool: ...
    @overload
    def SetFaceNormal(self, index: int, x: Single, y: Single, z: Single) -> bool: ...
    @overload
    def SetFaceNormal(self, index: int, x: float, y: float, z: float) -> bool: ...
    def UnitizeFaceNormals(self) -> bool: ...


class MeshNgonList:
    def AddNgon(self, ngon: MeshNgon) -> int: ...
    def AddNgons(self, ngons: Iterable[MeshNgon]) -> Set(int): ...
    @overload
    def AddPlanarNgons(self, planarTolerance: float) -> int: ...
    @overload
    def AddPlanarNgons(self, planarTolerance: float, minimumNgonVertexCount: int, minimumNgonFaceCount: int, allowHoles: bool) -> int: ...
    def Clear(self) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> MeshNgon: ...
    @property
    def UnsignedCount(self) -> UInt32: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetNgon(self, index: int) -> MeshNgon: ...
    def GetNgonBoundary(self, ngonFaceIndexList: Iterable[int]) -> Set(int): ...
    @overload
    def GetNgonBoundingBox(self, ngon: MeshNgon) -> BoundingBox: ...
    @overload
    def GetNgonBoundingBox(self, index: int) -> BoundingBox: ...
    @overload
    def GetNgonCenter(self, index: int) -> Point3d: ...
    @overload
    def GetNgonCenter(self, ngon: MeshNgon) -> Point3d: ...
    def GetNgonEdgeCount(self, index: int) -> int: ...
    def GetNgonOuterEdgeCount(self, index: int) -> int: ...
    def Insert(self, index: int, ngon: MeshNgon) -> None: ...
    @overload
    def IsValid(self, index: int) -> UInt32: ...
    @overload
    def IsValid(self, index: int, textLog: TextLog) -> UInt32: ...
    def NgonBoundaryVertexList(self, ngon: MeshNgon, bAppendStartPoint: bool) -> Set(Point3d): ...
    def NgonHasHoles(self, index: int) -> bool: ...
    def NgonIndexFromFaceIndex(self, meshFaceIndex: int) -> int: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveNgons(self, indices: Iterable[int]) -> int: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: MeshNgon) -> None: ...
    @UnsignedCount.setter
    def UnsignedCount(self, value: UInt32) -> None: ...
    def SetNgon(self, index: int, ngon: MeshNgon) -> None: ...


class MeshTextureCoordinateList:
    @overload
    def Add(self, tc: Point3d) -> int: ...
    @overload
    def Add(self, tc: Point2f) -> int: ...
    @overload
    def Add(self, s: Single, t: Single) -> int: ...
    @overload
    def Add(self, s: float, t: float) -> int: ...
    def AddRange(self, textureCoordinates: Set(Point2f)) -> bool: ...
    def Clear(self) -> None: ...
    def Destroy(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Point2f: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def NormalizeTextureCoordinates(self) -> bool: ...
    def ReverseTextureCoordinates(self, direction: int) -> bool: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Point2f) -> None: ...
    @overload
    def SetTextureCoordinate(self, index: int, tc: Point2f) -> bool: ...
    @overload
    def SetTextureCoordinate(self, index: int, tc: Point3f) -> bool: ...
    @overload
    def SetTextureCoordinate(self, index: int, s: float, t: float) -> bool: ...
    @overload
    def SetTextureCoordinate(self, index: int, s: Single, t: Single) -> bool: ...
    @overload
    def SetTextureCoordinates(self, mapping: TextureMapping) -> bool: ...
    @overload
    def SetTextureCoordinates(self, textureCoordinates: Set(Point2f)) -> bool: ...
    def ToFloatArray(self) -> Set(Single): ...
    def TransposeTextureCoordinates(self) -> bool: ...


class MeshTopologyEdgeList:
    def CollapseEdge(self, topologyEdgeIndex: int) -> bool: ...
    def EdgeLine(self, topologyEdgeIndex: int) -> Line: ...
    @property
    def Count(self) -> int: ...
    @overload
    def GetConnectedFaces(self, topologyEdgeIndex: int) -> Set(int): ...
    @overload
    def GetConnectedFaces(self, topologyEdgeIndex: int) -> Tuple[Set(int), Set(bool)]: ...
    def GetEdgeIndex(self, topologyVertex1: int, topologyVertex2: int) -> int: ...
    @overload
    def GetEdgesForFace(self, faceIndex: int) -> Set(int): ...
    @overload
    def GetEdgesForFace(self, faceIndex: int) -> Tuple[Set(int), Set(bool)]: ...
    def GetTopologyVertices(self, topologyEdgeIndex: int) -> IndexPair: ...
    def IsEdgeUnwelded(self, topologyEdgeIndex: int) -> bool: ...
    def IsHidden(self, topologyEdgeIndex: int) -> bool: ...
    def IsNgonInterior(self, topologyEdgeIndex: int) -> bool: ...
    def IsSwappableEdge(self, topologyEdgeIndex: int) -> bool: ...
    @overload
    def SplitEdge(self, topologyEdgeIndex: int, t: float) -> bool: ...
    @overload
    def SplitEdge(self, topologyEdgeIndex: int, point: Point3d) -> bool: ...
    def SwapEdge(self, topologyEdgeIndex: int) -> bool: ...


class MeshTopologyVertexList:
    def ConnectedEdge(self, topologyVertexIndex: int, edgeAtVertexIndex: int) -> int: ...
    def ConnectedEdges(self, topologyVertexIndex: int) -> Set(int): ...
    def ConnectedEdgesCount(self, topologyVertexIndex: int) -> int: ...
    def ConnectedFaces(self, topologyVertexIndex: int) -> Set(int): ...
    @overload
    def ConnectedTopologyVertices(self, topologyVertexIndex: int) -> Set(int): ...
    @overload
    def ConnectedTopologyVertices(self, topologyVertexIndex: int, sorted: bool) -> Set(int): ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Point3f: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndicesFromFace(self, faceIndex: int) -> Set(int): ...
    def IsHidden(self, topologyVertexIndex: int) -> bool: ...
    def MeshVertexIndices(self, topologyVertexIndex: int) -> Set(int): ...
    @Item.setter
    def Item(self, index: int, value: Point3f) -> None: ...
    @overload
    def SortEdges(self) -> bool: ...
    @overload
    def SortEdges(self, topologyVertexIndex: int) -> bool: ...
    def TopologyVertexIndex(self, vertexIndex: int) -> int: ...


class MeshVertexColorList:
    @overload
    def Add(self, color: Color) -> int: ...
    @overload
    def Add(self, red: int, green: int, blue: int) -> int: ...
    def AppendColors(self, colors: Set(Color)) -> bool: ...
    def Clear(self) -> None: ...
    def CreateMonotoneMesh(self, baseColor: Color) -> bool: ...
    def Destroy(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Color: ...
    @property
    def Tag(self) -> MappingTag: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Color) -> None: ...
    @Tag.setter
    def Tag(self, value: MappingTag) -> None: ...
    @overload
    def SetColor(self, face: MeshFace, color: Color) -> bool: ...
    @overload
    def SetColor(self, index: int, color: Color) -> bool: ...
    @overload
    def SetColor(self, index: int, red: int, green: int, blue: int) -> bool: ...
    def SetColors(self, colors: Set(Color)) -> bool: ...


class MeshVertexList:
    @overload
    def Add(self, vertex: Point3f) -> int: ...
    @overload
    def Add(self, vertex: Point3d) -> int: ...
    @overload
    def Add(self, x: Single, y: Single, z: Single) -> int: ...
    @overload
    def Add(self, x: float, y: float, z: float) -> int: ...
    @overload
    def AddVertices(self, vertices: Iterable[Point3f]) -> None: ...
    @overload
    def AddVertices(self, vertices: Iterable[Point3d]) -> None: ...
    @overload
    def Align(self, distance: float, whichVertices: Iterable[bool]) -> int: ...
    @overload
    def Align(meshes: Iterable[Mesh], distance: float, whichVertices: Iterable[Iterable[bool]]) -> int: ...
    def Clear(self) -> None: ...
    def CombineIdentical(self, ignoreNormals: bool, ignoreAdditional: bool) -> bool: ...
    def CullUnused(self) -> int: ...
    def Destroy(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Point3f: ...
    @property
    def UseDoublePrecisionVertices(self) -> bool: ...
    def GetConnectedVertices(self, vertexIndex: int) -> Set(int): ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetTopologicalIndenticalVertices(self, vertexIndex: int) -> Set(int): ...
    def GetVertexFaces(self, vertexIndex: int) -> Set(int): ...
    def Hide(self, vertexIndex: int) -> None: ...
    def HideAll(self) -> None: ...
    def IsHidden(self, vertexIndex: int) -> bool: ...
    def Point3dAt(self, index: int) -> Point3d: ...
    @overload
    def Remove(self, index: int, shrinkFaces: bool) -> bool: ...
    @overload
    def Remove(self, indices: Iterable[int], shrinkFaces: bool) -> bool: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Point3f) -> None: ...
    @UseDoublePrecisionVertices.setter
    def UseDoublePrecisionVertices(self, value: bool) -> None: ...
    @overload
    def SetVertex(self, index: int, vertex: Point3d) -> bool: ...
    @overload
    def SetVertex(self, index: int, vertex: Point3f) -> bool: ...
    @overload
    def SetVertex(self, index: int, x: float, y: float, z: float) -> bool: ...
    @overload
    def SetVertex(self, index: int, x: Single, y: Single, z: Single) -> bool: ...
    @overload
    def SetVertex(self, index: int, x: float, y: float, z: float, updateNormals: bool) -> bool: ...
    def Show(self, vertexIndex: int) -> None: ...
    def ShowAll(self) -> None: ...
    def ToFloatArray(self) -> Set(Single): ...
    def ToPoint3dArray(self) -> Set(Point3d): ...
    def ToPoint3fArray(self) -> Set(Point3f): ...


class MeshVertexNormalList:
    @overload
    def Add(self, normal: Vector3f) -> int: ...
    @overload
    def Add(self, normal: Vector3d) -> int: ...
    @overload
    def Add(self, x: float, y: float, z: float) -> int: ...
    @overload
    def Add(self, x: Single, y: Single, z: Single) -> int: ...
    def AddRange(self, normals: Set(Vector3f)) -> bool: ...
    def Clear(self) -> None: ...
    def ComputeNormals(self) -> bool: ...
    def Destroy(self) -> None: ...
    def Flip(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Vector3f: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Vector3f) -> None: ...
    @overload
    def SetNormal(self, index: int, normal: Vector3f) -> bool: ...
    @overload
    def SetNormal(self, index: int, normal: Vector3d) -> bool: ...
    @overload
    def SetNormal(self, index: int, x: Single, y: Single, z: Single) -> bool: ...
    @overload
    def SetNormal(self, index: int, x: float, y: float, z: float) -> bool: ...
    def SetNormals(self, normals: Set(Vector3f)) -> bool: ...
    def ToFloatArray(self) -> Set(Single): ...
    def UnitizeNormals(self) -> bool: ...


class MeshVertexStatusList:
    def Add(self, hidden: bool) -> None: ...
    def AddRange(self, values: Iterable[bool]) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, hidden: bool) -> bool: ...
    def CopyTo(self, array: Set(bool), arrayIndex: int) -> None: ...
    def Destroy(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def HiddenCount(self) -> int: ...
    @property
    def Item(self, index: int) -> bool: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: bool) -> None: ...


class NurbsCurveKnotList:
    def ClampEnd(self, end: CurveEnd) -> bool: ...
    def Contains(self, item: float) -> bool: ...
    def CopyTo(self, array: Set(float), arrayIndex: int) -> None: ...
    def CreatePeriodicKnots(self, knotSpacing: float) -> bool: ...
    def CreateUniformKnots(self, knotSpacing: float) -> bool: ...
    def EnsurePrivateCopy(self) -> None: ...
    def EpsilonEquals(self, other: NurbsCurveKnotList, epsilon: float) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsClampedEnd(self) -> bool: ...
    @property
    def IsClampedStart(self) -> bool: ...
    @property
    def Item(self, index: int) -> float: ...
    def IndexOf(self, item: float) -> int: ...
    @overload
    def InsertKnot(self, value: float) -> bool: ...
    @overload
    def InsertKnot(self, value: float, multiplicity: int) -> bool: ...
    def KnotMultiplicity(self, index: int) -> int: ...
    def RemoveKnotAt(self, t: float) -> bool: ...
    def RemoveKnots(self, index0: int, index1: int) -> bool: ...
    def RemoveMultipleKnots(self, minimumMultiplicity: int, maximumMultiplicity: int, tolerance: float) -> int: ...
    @Item.setter
    def Item(self, index: int, value: float) -> None: ...
    def SuperfluousKnot(self, start: bool) -> float: ...


class NurbsCurvePointList:
    def ChangeEndWeights(self, w0: float, w1: float) -> bool: ...
    def Contains(self, item: ControlPoint) -> bool: ...
    def ControlPolygon(self) -> Polyline: ...
    def CopyTo(self, array: Set(ControlPoint), arrayIndex: int) -> None: ...
    def EnsurePrivateCopy(self) -> None: ...
    def EpsilonEquals(self, other: NurbsCurvePointList, epsilon: float) -> bool: ...
    @property
    def ControlPolygonLength(self) -> float: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> ControlPoint: ...
    @property
    def PointSize(self) -> int: ...
    @overload
    def GetPoint(self, index: int) -> Tuple[bool, Point4d]: ...
    @overload
    def GetPoint(self, index: int) -> Tuple[bool, Point3d]: ...
    def GetWeight(self, index: int) -> float: ...
    def IndexOf(self, item: ControlPoint) -> int: ...
    def MakeNonRational(self) -> bool: ...
    def MakeRational(self) -> bool: ...
    @Item.setter
    def Item(self, index: int, value: ControlPoint) -> None: ...
    @overload
    def SetPoint(self, index: int, point: Point4d) -> bool: ...
    @overload
    def SetPoint(self, index: int, point: Point3d) -> bool: ...
    @overload
    def SetPoint(self, index: int, point: Point3d, weight: float) -> bool: ...
    @overload
    def SetPoint(self, index: int, x: float, y: float, z: float) -> bool: ...
    @overload
    def SetPoint(self, index: int, x: float, y: float, z: float, weight: float) -> bool: ...
    def SetWeight(self, index: int, weight: float) -> bool: ...
    def UVNDirectionsAt(self, index: int) -> Tuple[bool, Vector3d, Vector3d, Vector3d]: ...
    def ValidateSpacing(self, closeTolerance: float, stackTolerance: float) -> Tuple[bool, Set(int), Set(int)]: ...


class NurbsSurfaceKnotList:
    def CreatePeriodicKnots(self, knotSpacing: float) -> bool: ...
    def CreateUniformKnots(self, knotSpacing: float) -> bool: ...
    def EnsurePrivateCopy(self) -> None: ...
    def EpsilonEquals(self, other: NurbsSurfaceKnotList, epsilon: float) -> bool: ...
    @property
    def ClampedAtEnd(self) -> bool: ...
    @property
    def ClampedAtStart(self) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> float: ...
    @overload
    def InsertKnot(self, value: float) -> bool: ...
    @overload
    def InsertKnot(self, value: float, multiplicity: int) -> bool: ...
    def KnotMultiplicity(self, index: int) -> int: ...
    def RemoveKnots(self, index0: int, index1: int) -> bool: ...
    def RemoveKnotsAt(self, u: float, v: float) -> bool: ...
    def RemoveMultipleKnots(self, minimumMultiplicity: int, maximumMultiplicity: int, tolerance: float) -> int: ...
    @Item.setter
    def Item(self, index: int, value: float) -> None: ...
    def SuperfluousKnot(self, start: bool) -> float: ...


class NurbsSurfacePointList:
    def EnsurePrivateCopy(self) -> None: ...
    def EpsilonEquals(self, other: NurbsSurfacePointList, epsilon: float) -> bool: ...
    @property
    def CountU(self) -> int: ...
    @property
    def CountV(self) -> int: ...
    @property
    def PointSize(self) -> int: ...
    def GetControlPoint(self, u: int, v: int) -> ControlPoint: ...
    def GetGrevillePoint(self, u: int, v: int) -> Point2d: ...
    @overload
    def GetPoint(self, u: int, v: int) -> Tuple[bool, Point3d]: ...
    @overload
    def GetPoint(self, u: int, v: int) -> Tuple[bool, Point4d]: ...
    def GetWeight(self, u: int, v: int) -> float: ...
    def SetControlPoint(self, u: int, v: int, cp: ControlPoint) -> bool: ...
    @overload
    def SetPoint(self, u: int, v: int, point: Point3d) -> bool: ...
    @overload
    def SetPoint(self, u: int, v: int, point: Point4d) -> bool: ...
    @overload
    def SetPoint(self, u: int, v: int, point: Point3d, weight: float) -> bool: ...
    @overload
    def SetPoint(self, u: int, v: int, x: float, y: float, z: float) -> bool: ...
    @overload
    def SetPoint(self, u: int, v: int, x: float, y: float, z: float, weight: float) -> bool: ...
    def SetWeight(self, u: int, v: int, weight: float) -> bool: ...
    def UVNDirectionsAt(self, u: int, v: int) -> Tuple[bool, Vector3d, Vector3d, Vector3d]: ...
    def ValidateSpacing(self, closeTolerance: float, stackTolerance: float) -> Tuple[bool, Set(IndexPair), Set(IndexPair)]: ...


class SubDEdgeList:
    def Add(self, tag: SubDEdgeTag, v0: SubDVertex, v1: SubDVertex) -> SubDEdge: ...
    @overload
    def Find(self, id: UInt32) -> SubDEdge: ...
    @overload
    def Find(self, id: int) -> SubDEdge: ...
    @property
    def Count(self) -> int: ...
    def GetEnumerator(self) -> IEnumerator: ...


class SubDFaceList:
    @overload
    def Find(self, id: UInt32) -> SubDFace: ...
    @overload
    def Find(self, id: int) -> SubDFace: ...
    @property
    def Count(self) -> int: ...
    def GetEnumerator(self) -> IEnumerator: ...


class SubDVertexList:
    def Add(self, tag: SubDVertexTag, vertex: Point3d) -> SubDVertex: ...
    @overload
    def Find(self, id: UInt32) -> SubDVertex: ...
    @overload
    def Find(self, id: int) -> SubDVertex: ...
    @property
    def Count(self) -> int: ...
    @property
    def First(self) -> SubDVertex: ...
