from typing import Tuple, Set, Iterable, List


class CursorStyle:
    Default = 0
    Wait = 1
    CrossHair = 2
    Hand = 3
    Rotate = 4
    Magnify = 5
    ArrowCopy = 6
    CrosshairCopy = 7


class Dialogs:
    def KillSplash() -> None: ...
    def SetCustomColorDialog(handler: EventHandler) -> None: ...
    def ShowAboutDialog(forceSimpleDialog: bool) -> None: ...
    def ShowCheckListBox(title: str, message: str, items: IList, checkState: List[bool]) -> Set(bool): ...
    @overload
    def ShowColorDialog(color: Color) -> Tuple[bool, Color]: ...
    @overload
    def ShowColorDialog(color: Color4f, allowAlpha: bool) -> Tuple[bool, Color4f]: ...
    @overload
    def ShowColorDialog(color: Color, includeButtonColors: bool, dialogTitle: str) -> Tuple[bool, Color]: ...
    @overload
    def ShowColorDialog(parent: IWin32Window, color: Color4f, allowAlpha: bool) -> Tuple[bool, Color4f]: ...
    @overload
    def ShowColorDialog(parent: Object, color: Color4f, allowAlpha: bool) -> Tuple[bool, Color4f]: ...
    @overload
    def ShowColorDialog(parent: Object, color: Color4f, allowAlpha: bool, colorCallback: OnColorChangedEvent) -> Tuple[bool, Color4f]: ...
    def ShowComboListBox(title: str, message: str, items: IList) -> Object: ...
    def ShowContextMenu(items: Iterable[str], screenPoint: Point, modes: Iterable[int]) -> int: ...
    def ShowEditBox(title: str, message: str, defaultText: str, multiline: bool) -> Tuple[bool, str]: ...
    def ShowLineTypes(title: str, message: str, doc: RhinoDoc) -> Object: ...
    @overload
    def ShowListBox(title: str, message: str, items: IList) -> Object: ...
    @overload
    def ShowListBox(title: str, message: str, items: IList, selectedItem: Object) -> Object: ...
    @overload
    def ShowMessage(message: str, title: str) -> ShowMessageResult: ...
    @overload
    def ShowMessage(message: str, title: str, buttons: ShowMessageButton, icon: ShowMessageIcon) -> ShowMessageResult: ...
    @overload
    def ShowMessage(parent: Object, message: str, title: str, buttons: ShowMessageButton, icon: ShowMessageIcon, defaultButton: ShowMessageDefaultButton, options: ShowMessageOptions, mode: ShowMessageMode) -> ShowMessageResult: ...
    @overload
    def ShowMessageBox(message: str, title: str) -> DialogResult: ...
    @overload
    def ShowMessageBox(message: str, title: str, buttons: MessageBoxButtons, icon: MessageBoxIcon) -> DialogResult: ...
    def ShowMultiListBox(title: str, message: str, items: List[str], defaults: List[str]) -> Set(str): ...
    @overload
    def ShowNumberBox(title: str, message: str, number: float) -> Tuple[bool, float]: ...
    @overload
    def ShowNumberBox(title: str, message: str, number: float, minimum: float, maximum: float) -> Tuple[bool, float]: ...
    def ShowPropertyListBox(title: str, message: str, items: IList, values: List[str]) -> Set(str): ...
    def ShowSelectLayerDialog(layerIndex: int, dialogTitle: str, showNewLayerButton: bool, showSetCurrentButton: bool, initialSetCurrentState: bool) -> Tuple[bool, int, bool]: ...
    def ShowSelectLinetypeDialog(linetypeIndex: int, displayByLayer: bool) -> Tuple[bool, int]: ...
    def ShowSelectMultipleLayersDialog(defaultLayerIndices: Iterable[int], dialogTitle: str, showNewLayerButton: bool) -> Tuple[bool, Set(int)]: ...
    def ShowSemiModal(form: Form) -> DialogResult: ...
    def ShowSunDialog(sun: Sun) -> bool: ...
    def ShowTextDialog(message: str, title: str) -> None: ...


class DistanceDisplayMode:
    Decimal = 0
    Fractional = 1
    FeetInches = 2


class DrawingUtilities:
    @overload
    def BitmapFromIconResource(resourceName: str, assembly: Assembly) -> Bitmap: ...
    @overload
    def BitmapFromIconResource(resourceName: str, bitmapSize: Size, assembly: Assembly) -> Bitmap: ...
    @overload
    def CreateMeshPreviewImage(mesh: Mesh, color: Color, size: Size) -> Bitmap: ...
    @overload
    def CreateMeshPreviewImage(meshes: Iterable[Mesh], colors: Iterable[Color], size: Size) -> Bitmap: ...
    @overload
    def IconFromResource(resourceName: str, assembly: Assembly) -> Icon: ...
    @overload
    def IconFromResource(resourceName: str, size: Size, assembly: Assembly) -> Icon: ...
    def ImageFromResource(resourceName: str, assembly: Assembly) -> Image: ...
    def LoadBitmapWithScaleDown(iconName: str, sizeDesired: int, assembly: Assembly) -> Bitmap: ...
    def LoadIconWithScaleDown(iconName: str, sizeDesired: int, assembly: Assembly) -> Icon: ...


class FloatPanelMode:
    Show = 0
    Hide = 1
    Toggle = 2


class Fonts:
    def __init__(self): ...
    @property
    def BoldHeadingFont() -> Font: ...
    @property
    def HeadingFont() -> Font: ...
    @property
    def NormalFont() -> Font: ...
    @property
    def SmallFont() -> Font: ...
    @property
    def TitleFont() -> Font: ...
    def GetUiFont(style: Style, size: Size) -> Font: ...


class GetColorEventArgs:
    @property
    def IncludeButtonColors(self) -> bool: ...
    @property
    def InputColor(self) -> Color: ...
    @property
    def SelectedColor(self) -> Color: ...
    @property
    def Title(self) -> str: ...
    @SelectedColor.setter
    def SelectedColor(self, value: Color) -> None: ...


class IDialogService:
    def ObjectToWindowHandle(self, window: Object, useMainRhinoWindowWhenNull: bool) -> IntPtr: ...
    def ShowMultiListBox(self, title: str, message: str, items: List[str], defaults: List[str]) -> Set(str): ...
    def WrapAsIWin32Window(self, handle: IntPtr) -> Object: ...


class IHelp:
    @property
    def HelpUrl(self) -> str: ...


class ILocalizationService:
    def LocalizeCommandName(self, assembly: Assembly, languageId: int, english: str) -> str: ...
    def LocalizeDialogItem(self, assembly: Assembly, languageId: int, key: str, english: str) -> str: ...
    def LocalizeForm(self, assembly: Assembly, languageId: int, formOrUserControl: Object) -> None: ...
    def LocalizeString(self, assembly: Assembly, languageId: int, english: str, contextId: int) -> str: ...


class IPanel:
    def PanelClosing(self, documentSerialNumber: UInt32, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: UInt32, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: UInt32, reason: ShowPanelReason) -> None: ...


class IPanelsService:
    def DestroyNativeWindow(self, host: Object, nativeObject: Object, disposeOfNativeObject: bool) -> None: ...
    def SetF1Hook(self, nativeObject: Object, hook: EventHandler) -> None: ...
    def SupportedType(self, type: Type) -> Tuple[bool, str]: ...


class IRhinoUiDialogService:
    def ShowCheckListBox(self, title: str, message: str, items: IList, checkState: List[bool]) -> Set(bool): ...
    def ShowComboListBox(self, title: str, message: str, items: IList) -> Object: ...
    def ShowEditBox(self, title: str, message: str, defaultText: str, multiline: bool) -> Tuple[bool, str]: ...
    def ShowLineTypes(self, title: str, message: str, doc: RhinoDoc) -> Object: ...
    def ShowListBox(self, title: str, message: str, items: IList, selectedItem: Object) -> Object: ...
    def ShowMultiListBox(self, items: List[str], message: str, title: str, defaults: List[str]) -> Set(str): ...
    def ShowNumberBox(self, title: str, message: str, number: float, minimum: float, maximum: float) -> Tuple[bool, float]: ...
    def ShowPopupMenu(self, arrItems: Set(str), arrModes: Set(int), screenPointX: Nullable, screenPointY: Nullable) -> int: ...


class IStackedDialogPageService:
    @overload
    def GetImageHandle(self, image: Image, canBeNull: bool) -> IntPtr: ...
    @overload
    def GetImageHandle(self, icon: Icon, canBeNull: bool) -> IntPtr: ...
    @overload
    def GetNativePageWindow(self, nativeWindowObject: Object) -> Tuple[IntPtr, Object]: ...
    @overload
    def GetNativePageWindow(self, pageObject: Object) -> Tuple[IntPtr, Object, Object]: ...
    def RedrawPageControl(self, pageControl: Object) -> None: ...
    def TryGetControlMinimumSize(self, controlObject: Object) -> Tuple[bool, SizeF]: ...


class LOC:
    def COMMANDNAME(english: str) -> str: ...
    @overload
    def CON(english: str) -> LocalizeStringPair: ...
    @overload
    def CON(english: str, assemblyFromObject: Object) -> LocalizeStringPair: ...
    @overload
    def COV(english: str) -> LocalizeStringPair: ...
    @overload
    def COV(english: str, assemblyFromObject: Object) -> LocalizeStringPair: ...
    @overload
    def STR(english: str) -> str: ...
    @overload
    def STR(english: str, assemblyOrObject: Object) -> str: ...


class Localization:
    def FormatDistanceAndTolerance(distance: float, units: UnitSystem, dimStyle: DimensionStyle, alternate: bool) -> str: ...
    def FormatNumber(x: float, units: UnitSystem, mode: DistanceDisplayMode, precision: int, appendUnitSystemName: bool) -> str: ...
    @property
    def CurrentLanguageId() -> int: ...
    @property
    def RunningAsEnglish() -> bool: ...
    @overload
    def LocalizeCommandName(english: str) -> str: ...
    @overload
    def LocalizeCommandName(english: str, assemblyOrObject: Object) -> str: ...
    @overload
    def LocalizeCommandOptionName(english: str, contextId: int) -> LocalizeStringPair: ...
    @overload
    def LocalizeCommandOptionName(english: str, assemblyOrObject: Object, contextId: int) -> LocalizeStringPair: ...
    @overload
    def LocalizeCommandOptionValue(english: str, contextId: int) -> LocalizeStringPair: ...
    @overload
    def LocalizeCommandOptionValue(english: str, assemblyOrObject: Object, contextId: int) -> LocalizeStringPair: ...
    def LocalizeDialogItem(assemblyOrObject: Object, key: str, english: str) -> str: ...
    def LocalizeForm(formOrUserControl: Object) -> None: ...
    @overload
    def LocalizeString(english: str, contextId: int) -> str: ...
    @overload
    def LocalizeString(english: str, assemblyOrObject: Object, contextId: int) -> str: ...
    def SetLanguageId(id: int) -> bool: ...
    def UnitSystemName(units: UnitSystem, capitalize: bool, singular: bool, abbreviate: bool) -> str: ...


class LocalizeStringPair:
    def __init__(self, english: str, local: str): ...
    @property
    def English(self) -> str: ...
    @property
    def Local(self) -> str: ...
    def op_Implicit(lcp: LocalizeStringPair) -> str: ...
    def ToString(self) -> str: ...


class ModifierKey:
    #None = 0
    Control = 1
    Shift = 2


class MouseButton:
    #None = 0
    Left = 1
    Right = 2
    Middle = 4


class MouseCallback:
    @property
    def Enabled(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...


class MouseCallbackEventArgs:
    @property
    def Button(self) -> MouseButtons: ...
    @property
    def CtrlKeyDown(self) -> bool: ...
    @property
    def MouseButton(self) -> MouseButton: ...
    @property
    def ShiftKeyDown(self) -> bool: ...
    @property
    def View(self) -> RhinoView: ...
    @property
    def ViewportPoint(self) -> Point: ...


class MouseCursor:
    @property
    def Location() -> Point2d: ...
    def SetToolTip(tooltip: str) -> None: ...


class ObjectPropertiesPage:
    @overload
    def AnySelectedObject(self) -> bool: ...
    @overload
    def AnySelectedObject(self, allMustMatch: bool) -> bool: ...
    @property
    def AllObjectsMustBeSupported(self) -> bool: ...
    @property
    def EnglishPageTitle(self) -> str: ...
    @property
    def Icon(self) -> Icon: ...
    @property
    def LocalPageTitle(self) -> str: ...
    @property
    def PageControl(self) -> Object: ...
    @property
    def PageIconEmbeddedResourceString(self) -> str: ...
    @property
    def PageType(self) -> PropertyPageType: ...
    @property
    def SelectedObjects(self) -> Set(RhinoObject): ...
    @property
    def SupportedTypes(self) -> ObjectType: ...
    @property
    def SupportsSubObjects(self) -> bool: ...
    @overload
    def GetSelectedObjects(self) -> Set(T): ...
    @overload
    def GetSelectedObjects(self, filter: ObjectType) -> Set(RhinoObject): ...
    def InitializeControls(self, rhObj: RhinoObject) -> None: ...
    def ModifyPage(self, callbackAction: Action) -> None: ...
    def OnActivate(self, active: bool) -> bool: ...
    def OnCreateParent(self, hwndParent: IntPtr) -> None: ...
    def OnHelp(self) -> None: ...
    def OnSizeParent(self, width: int, height: int) -> None: ...
    def PageIcon(self, sizeInPixels: Size) -> Icon: ...
    @overload
    def RunScript(self, e: ObjectPropertiesPageEventArgs) -> Result: ...
    @overload
    def RunScript(self, doc: RhinoDoc, objectList: Set(RhinoObject)) -> Result: ...
    @overload
    def ShouldDisplay(self, e: ObjectPropertiesPageEventArgs) -> bool: ...
    @overload
    def ShouldDisplay(self, rhObj: RhinoObject) -> bool: ...
    def UpdatePage(self, e: ObjectPropertiesPageEventArgs) -> None: ...


class ObjectPropertiesPageCollection:
    def Add(self, page: ObjectPropertiesPage) -> None: ...
    @property
    def Document(self) -> RhinoDoc: ...
    @property
    def DocumentRuntimeSerailNumber(self) -> UInt32: ...


class ObjectPropertiesPageEventArgs:
    def __init__(self, page: ObjectPropertiesPage): ...
    @property
    def DocRuntimeSerialNumber(self) -> UInt32: ...
    @property
    def Document(self) -> RhinoDoc: ...
    @property
    def EventRuntimeSerialNumber(self) -> UInt32: ...
    @property
    def ObjectCount(self) -> int: ...
    @property
    def Objects(self) -> Set(RhinoObject): ...
    @property
    def ObjectTypes(self) -> UInt32: ...
    @property
    def Page(self) -> ObjectPropertiesPage: ...
    @property
    def View(self) -> RhinoView: ...
    @property
    def Viewport(self) -> RhinoViewport: ...
    @overload
    def GetObjects(self) -> Set(T): ...
    @overload
    def GetObjects(self, filter: ObjectType) -> Set(RhinoObject): ...
    @overload
    def IncludesObjectsType(self) -> bool: ...
    @overload
    def IncludesObjectsType(self, objectTypes: ObjectType) -> bool: ...
    @overload
    def IncludesObjectsType(self, allMustMatch: bool) -> bool: ...
    @overload
    def IncludesObjectsType(self, objectTypes: ObjectType, allMustMatch: bool) -> bool: ...


class OnColorChangedEvent:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, color: Color4f, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, color: Color4f) -> None: ...


class OpenFileDialog:
    def __init__(self): ...
    @property
    def DefaultExt(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FileNames(self) -> Set(str): ...
    @property
    def Filter(self) -> str: ...
    @property
    def InitialDirectory(self) -> str: ...
    @property
    def MultiSelect(self) -> bool: ...
    @property
    def Title(self) -> str: ...
    @DefaultExt.setter
    def DefaultExt(self, value: str) -> None: ...
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @InitialDirectory.setter
    def InitialDirectory(self, value: str) -> None: ...
    @MultiSelect.setter
    def MultiSelect(self, value: bool) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    def ShowDialog(self) -> DialogResult: ...
    def ShowOpenDialog(self) -> bool: ...


class OptionPageButtons:
    #None = 0
    DefaultButton = 1
    ApplyButton = 2


class OptionsDialogPage(StackedDialogPage):
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...


class PanelEventArgs:
    def __init__(self, panelId: Guid, documentSerialNumber: UInt32): ...
    @property
    def Document(self) -> RhinoDoc: ...
    @property
    def DocumentSerialNumber(self) -> UInt32: ...
    @property
    def PanelId(self) -> Guid: ...


class PanelIds:
    @property
    def ContextHelp() -> Guid: ...
    @property
    def Display() -> Guid: ...
    @property
    def Environment() -> Guid: ...
    @property
    def GroundPlane() -> Guid: ...
    @property
    def Layers() -> Guid: ...
    @property
    def Libraries() -> Guid: ...
    @property
    def LightManager() -> Guid: ...
    @property
    def Materials() -> Guid: ...
    @property
    def Notes() -> Guid: ...
    @property
    def ObjectProperties() -> Guid: ...
    @property
    def Rendering() -> Guid: ...
    @property
    def Sun() -> Guid: ...
    @property
    def Texture() -> Guid: ...


class Panels:
    def add_Closed(value: EventHandler) -> None: ...
    def add_Show(value: EventHandler) -> None: ...
    def ChangePanelIcon(panelType: Type, icon: Icon) -> None: ...
    @overload
    def ClosePanel(panelId: Guid) -> None: ...
    @overload
    def ClosePanel(panelType: Type) -> None: ...
    @overload
    def FloatPanel(panelType: Type, mode: FloatPanelMode) -> bool: ...
    @overload
    def FloatPanel(panelTypeId: Guid, mode: FloatPanelMode) -> bool: ...
    @property
    def EtoPanelStyleName() -> str: ...
    @property
    def IconSize() -> Size: ...
    @property
    def ScaledIconSize() -> Size: ...
    def GetOpenPanelIds() -> Set(Guid): ...
    @overload
    def GetPanel() -> T: ...
    @overload
    def GetPanel(documentSerialNumber: UInt32) -> T: ...
    @overload
    def GetPanel(rhinoDoc: RhinoDoc) -> T: ...
    @overload
    def GetPanel(panelId: Guid) -> Object: ...
    @overload
    def GetPanel(panelId: Guid, documentSerialNumber: UInt32) -> Object: ...
    @overload
    def GetPanel(panelId: Guid, rhinoDoc: RhinoDoc) -> Object: ...
    @overload
    def GetPanels(documentRuntimeSerialNumber: UInt32) -> Set(T): ...
    @overload
    def GetPanels(doc: RhinoDoc) -> Set(T): ...
    @overload
    def GetPanels(panelId: Guid, documentRuntimeSerialNumber: UInt32) -> Set(Object): ...
    @overload
    def GetPanels(panelId: Guid, doc: RhinoDoc) -> Set(Object): ...
    def IsHiding(reason: ShowPanelReason) -> bool: ...
    @overload
    def IsPanelVisible(panelType: Type) -> bool: ...
    @overload
    def IsPanelVisible(panelId: Guid) -> bool: ...
    @overload
    def IsPanelVisible(panelType: Type, isSelectedTab: bool) -> bool: ...
    @overload
    def IsPanelVisible(panelId: Guid, isSelectedTab: bool) -> bool: ...
    def IsShowing(reason: ShowPanelReason) -> bool: ...
    def OnClosePanel(panelId: Guid, documentSerialNumber: UInt32) -> None: ...
    def OnShowPanel(panelId: Guid, documentSerialNumber: UInt32, show: bool) -> None: ...
    @overload
    def OpenPanel(panelId: Guid) -> None: ...
    @overload
    def OpenPanel(panelType: Type) -> None: ...
    @overload
    def OpenPanel(dockBarId: Guid, panelType: Type) -> Guid: ...
    @overload
    def OpenPanel(panelType: Type, makeSelectedPanel: bool) -> None: ...
    @overload
    def OpenPanel(dockBarId: Guid, panelId: Guid) -> Guid: ...
    @overload
    def OpenPanel(panelId: Guid, makeSelectedPanel: bool) -> None: ...
    @overload
    def OpenPanel(dockBarId: Guid, panelType: Type, makeSelectedPanel: bool) -> Guid: ...
    @overload
    def OpenPanel(dockBarId: Guid, panelId: Guid, makeSelectedPanel: bool) -> Guid: ...
    @overload
    def OpenPanelAsSibling(panelId: Guid, siblingPanelId: Guid) -> bool: ...
    @overload
    def OpenPanelAsSibling(panelId: Guid, siblingPanelId: Guid, makeSelectedPanel: bool) -> bool: ...
    @overload
    def PanelDockBar(panelType: Type) -> Guid: ...
    @overload
    def PanelDockBar(panelId: Guid) -> Guid: ...
    def PanelDockBars(panelId: Guid) -> Set(Guid): ...
    @overload
    def RegisterPanel(plugin: PlugIn, panelType: Type, caption: str, icon: Icon) -> None: ...
    @overload
    def RegisterPanel(plugIn: PlugIn, type: Type, caption: str, icon: Icon, panelType: PanelType) -> None: ...
    def remove_Closed(value: EventHandler) -> None: ...
    def remove_Show(value: EventHandler) -> None: ...


class PanelType:
    PerDoc = 0
    System = 1


class PropertyPageType:
    Material = 0
    Light = 1
    Custom = 2
    ObjectProperties = 3
    Dimension = 4
    Leader = 5
    Text = 6
    Hatch = 7
    Dot = 8
    TextureMapping = 9
    Detail = 10
    ClippingPlane = 11
    NamedView = 12
    Decal = 13
    View = 14
    PageCount = 15


class RhinoGetPlotWidthArgs:
    NoArgs = 0
    ByLayer = 1
    ByParent = 2
    HairLine = 4
    Default = 8
    #None = 32
    All = 268435455


class RhinoHelp:
    def Show(helpLink: str) -> bool: ...


class RhinoPageInterop:
    def NewPropertiesPanelPagePointer(page: ObjectPropertiesPage, rhinoDocRuntimeSn: UInt32) -> IntPtr: ...
    def StackedDialogPageFromUnmanagedPointer(pointer: IntPtr) -> StackedDialogPage: ...


class RhinoPlotWidthType:
    ByLayer = 0
    ByParent = 1
    Hairline = 2
    Default = 3
    #None = 4
    Varies = 5
    Width = 6


class RhinoPlotWidthValue:
    Default = 0
    Varies = -20
    ByParent = -15
    ByLayer = -10
    #None = -1


class RuiUpdateUi:
    @property
    def Checked(self) -> bool: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def FileId(self) -> Guid: ...
    @property
    def MenuHandle(self) -> IntPtr: ...
    @property
    def MenuId(self) -> Guid: ...
    @property
    def MenuIndex(self) -> int: ...
    @property
    def MenuItemId(self) -> Guid: ...
    @property
    def RadioChecked(self) -> bool: ...
    @property
    def Text(self) -> str: ...
    @property
    def WindowsMenuItemId(self) -> UInt32: ...
    @overload
    def RegisterMenuItem(file: Guid, menu: Guid, item: Guid, callBack: UpdateMenuItemEventHandler) -> bool: ...
    @overload
    def RegisterMenuItem(fileId: str, menuId: str, itemId: str, callBack: UpdateMenuItemEventHandler) -> bool: ...
    @Checked.setter
    def Checked(self, value: bool) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @RadioChecked.setter
    def RadioChecked(self, value: bool) -> None: ...
    @Text.setter
    def Text(self, value: str) -> None: ...


class SaveFileDialog:
    def __init__(self): ...
    @property
    def DefaultExt(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def Filter(self) -> str: ...
    @property
    def InitialDirectory(self) -> str: ...
    @property
    def Title(self) -> str: ...
    @DefaultExt.setter
    def DefaultExt(self, value: str) -> None: ...
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @InitialDirectory.setter
    def InitialDirectory(self, value: str) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    def ShowDialog(self) -> DialogResult: ...
    def ShowSaveDialog(self) -> bool: ...


class ShowMessageButton:
    OK = 0
    OKCancel = 1
    AbortRetryIgnore = 2
    YesNoCancel = 3
    YesNo = 4
    RetryCancel = 5


class ShowMessageDefaultButton:
    Button1 = 0
    Button2 = 256
    Button3 = 512


class ShowMessageIcon:
    #None = 0
    Error = 16
    Hand = 16
    Stop = 16
    Question = 32
    Exclamation = 48
    Warning = 48
    Information = 64
    Asterisk = 64


class ShowMessageMode:
    ApplicationModal = 0
    SystemModal = 4096
    TaskModal = 8192


class ShowMessageOptions:
    #None = 0
    SetForeground = 65536
    DefaultDesktopOnly = 131072
    TopMost = 262144
    RightAlign = 524288
    RtlReading = 1048576
    ServiceNotification = 2097152


class ShowMessageResult:
    #None = 0
    OK = 1
    Cancel = 2
    Abort = 3
    Retry = 4
    Ignore = 5
    Yes = 6
    No = 7


class ShowPanelEventArgs(PanelEventArgs):
    def __init__(self, panelId: Guid, documentSerialNumber: UInt32, show: bool): ...
    @property
    def Show(self) -> bool: ...


class ShowPanelReason:
    Show = 0
    Hide = 1
    HideOnDeactivate = 2
    ShowOnDeactivate = 3


class Size:
    Small = 0
    Normal = 1
    Large = 2
    Title = 3


class StackedDialogPage:
    def AddChildPage(self, pageToAdd: StackedDialogPage) -> None: ...
    @property
    def Children(self) -> List: ...
    @property
    def EnglishPageTitle(self) -> str: ...
    @property
    def Handle(self) -> IntPtr: ...
    @property
    def HasChildren(self) -> bool: ...
    @property
    def LocalPageTitle(self) -> str: ...
    @property
    def Modified(self) -> bool: ...
    @property
    def NavigationTextColor(self) -> Color: ...
    @property
    def NavigationTextIsBold(self) -> bool: ...
    @property
    def PageControl(self) -> Object: ...
    @property
    def PageImage(self) -> Image: ...
    @property
    def ShowApplyButton(self) -> bool: ...
    @property
    def ShowDefaultsButton(self) -> bool: ...
    def MakeActivePage(self) -> None: ...
    def OnActivate(self, active: bool) -> bool: ...
    def OnApply(self) -> bool: ...
    def OnCancel(self) -> None: ...
    def OnCreateParent(self, hwndParent: IntPtr) -> None: ...
    def OnDefaults(self) -> None: ...
    def OnHelp(self) -> None: ...
    def OnSizeParent(self, width: int, height: int) -> None: ...
    def RemovePage(self) -> None: ...
    @Modified.setter
    def Modified(self, value: bool) -> None: ...
    @NavigationTextColor.setter
    def NavigationTextColor(self, value: Color) -> None: ...
    @NavigationTextIsBold.setter
    def NavigationTextIsBold(self, value: bool) -> None: ...
    def SetEnglishPageTitle(self, newPageTile: str) -> None: ...


class StatusBar:
    def ClearMessagePane() -> None: ...
    @overload
    def HideProgressMeter() -> None: ...
    @overload
    def HideProgressMeter(docSerialNumber: UInt32) -> None: ...
    def SetDistancePane(distance: float) -> None: ...
    def SetMessagePane(message: str) -> None: ...
    def SetNumberPane(number: float) -> None: ...
    def SetPointPane(point: Point3d) -> None: ...
    @overload
    def ShowProgressMeter(lowerLimit: int, upperLimit: int, label: str, embedLabel: bool, showPercentComplete: bool) -> int: ...
    @overload
    def ShowProgressMeter(docSerialNumber: UInt32, lowerLimit: int, upperLimit: int, label: str, embedLabel: bool, showPercentComplete: bool) -> int: ...
    @overload
    def UpdateProgressMeter(position: int, absolute: bool) -> int: ...
    @overload
    def UpdateProgressMeter(docSerialNumber: UInt32, position: int, absolute: bool) -> int: ...


class Style:
    Regular = 0
    Bold = 1
    Italic = 2
    Underline = 4
    Strikeout = 8


class Toolbar:
    @property
    def BitmapSize() -> Size: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def TabSize() -> Size: ...
    @BitmapSize.setter
    def BitmapSize(value: Size) -> None: ...
    @TabSize.setter
    def TabSize(value: Size) -> None: ...


class ToolbarFile:
    def Close(self, prompt: bool) -> bool: ...
    @property
    def GroupCount(self) -> int: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def Path(self) -> str: ...
    @property
    def ToolbarCount(self) -> int: ...
    @overload
    def GetGroup(self, index: int) -> ToolbarGroup: ...
    @overload
    def GetGroup(self, name: str) -> ToolbarGroup: ...
    def GetToolbar(self, index: int) -> Toolbar: ...
    def Save(self) -> bool: ...
    def SaveAs(self, path: str) -> bool: ...


class ToolbarFileCollection:
    def FindByName(self, name: str, ignoreCase: bool) -> ToolbarFile: ...
    def FindByPath(self, path: str) -> ToolbarFile: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> ToolbarFile: ...
    @property
    def MruSidebarIsVisible() -> bool: ...
    @property
    def SidebarIsVisible() -> bool: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Open(self, path: str) -> ToolbarFile: ...
    @MruSidebarIsVisible.setter
    def MruSidebarIsVisible(value: bool) -> None: ...
    @SidebarIsVisible.setter
    def SidebarIsVisible(value: bool) -> None: ...


class ToolbarGroup:
    @property
    def Id(self) -> Guid: ...
    @property
    def IsDocked(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Visible(self) -> bool: ...
    @Visible.setter
    def Visible(self, value: bool) -> None: ...


class UpdateMenuItemEventHandler:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, cmdui: RuiUpdateUi, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, cmdui: RuiUpdateUi) -> None: ...


class WaitCursor:
    def __init__(self): ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def Set(self) -> None: ...
