#!/usr/bin/python3
from ThunkHelpers import *

lib("libSDL2")

# these need function pointers
#  fn("int SDL_TLSSet(SDL_TLSID, const void*, void (*)(void*))")
#  fn("void SDL_qsort(void*, size_t, size_t, int (*)(const void*, const void*))")
#  fn("SDL_AssertState (* SDL_GetAssertionHandler(void**))(const SDL_AssertData*, void*)")
#  fn("SDL_AssertState (* SDL_GetDefaultAssertionHandler())(const SDL_AssertData*, void*)")
#  fn("SDL_bool SDL_GetEventFilter(int (**)(void*, SDL_Event*), void**)")
#  fn("void SDL_GetMemoryFunctions(void* (**)(size_t), void* (**)(size_t, size_t), void* (**)(void*, size_t), void (**)(void*))")
#  fn("void SDL_LogGetOutputFunction(void (**)(void*, int, SDL_LogPriority, const char*), void**)")

# these need va_args
#  fn("int SDL_snprintf(char*, size_t, const char*, ...)")
#  fn("int SDL_sscanf(const char*, const char*, ...)")
#  fn("void SDL_Log(const char*, ...)")
#  fn("void SDL_LogCritical(int, const char*, ...)")
#  fn("void SDL_LogDebug(int, const char*, ...)")
#  fn("void SDL_LogError(int, const char*, ...)")
#  fn("void SDL_LogInfo(int, const char*, ...)")
#  fn("void SDL_LogMessage(int, SDL_LogPriority, const char*, ...)")
#  fn("void SDL_LogVerbose(int, const char*, ...)")
#  fn("void SDL_LogWarn(int, const char*, ...)")
#  fn("int SDL_SetError(const char*, ...)")

# these also need va_args
#  fn("void SDL_LogMessageV(int, SDL_LogPriority, const char*, __va_list_tag*)")
#  fn("int SDL_vsnprintf(char*, size_t, const char*, __va_list_tag*)")
#  fn("int SDL_vsscanf(const char*, const char*, __va_list_tag*)")

fn("char* SDL_GameControllerMappingForDeviceIndex(int)")
fn("char* SDL_GameControllerMappingForGUID(SDL_JoystickGUID)")
fn("char* SDL_GameControllerMappingForIndex(int)")
fn("char* SDL_GameControllerMapping(SDL_GameController*)")
fn("char* SDL_GetBasePath()")
fn("char* SDL_GetClipboardText()")
fn("char* SDL_getenv(const char*)")
fn("char* SDL_GetPrefPath(const char*, const char*)")
fn("char* SDL_iconv_string(const char*, const char*, const char*, size_t)")
fn("char* SDL_itoa(int, char*, int)")
fn("char* SDL_lltoa(Sint64, char*, int)")
fn("char* SDL_ltoa(long int, char*, int)")
fn("char* SDL_strchr(const char*, int)")
fn("char* SDL_strdup(const char*)")
fn("char* SDL_strlwr(char*)")
fn("char* SDL_strrchr(const char*, int)")
fn("char* SDL_strrev(char*)")
fn("char* SDL_strstr(const char*, const char*)")
fn("char* SDL_strupr(char*)")
fn("char* SDL_uitoa(unsigned int, char*, int)")
fn("char* SDL_ulltoa(Uint64, char*, int)")
fn("char* SDL_ultoa(long unsigned int, char*, int)")
fn("const char* SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis)")
fn("const char* SDL_GameControllerGetStringForButton(SDL_GameControllerButton)")
fn("const char* SDL_GameControllerNameForIndex(int)")
fn("const char* SDL_GameControllerName(SDL_GameController*)")
fn("const char* SDL_GetAudioDeviceName(int, int)")
fn("const char* SDL_GetAudioDriver(int)")
fn("const char* SDL_GetCurrentAudioDriver()")
fn("const char* SDL_GetCurrentVideoDriver()")
fn("const char* SDL_GetDisplayName(int)")
fn("const char* SDL_GetError()")
fn("const char* SDL_GetHint(const char*)")
fn("const char* SDL_GetKeyName(SDL_Keycode)")
fn("const char* SDL_GetPixelFormatName(Uint32)")
fn("const char* SDL_GetPlatform()")
fn("const char* SDL_GetRevision()")
fn("const char* SDL_GetScancodeName(SDL_Scancode)")
fn("const char* SDL_GetThreadName(SDL_Thread*)")
fn("const char* SDL_GetVideoDriver(int)")
fn("const char* SDL_GetWindowTitle(SDL_Window*)")
fn("const char* SDL_HapticName(int)")
fn("const char* SDL_JoystickNameForIndex(int)")
fn("const char* SDL_JoystickName(SDL_Joystick*)")
fn("const char* SDL_SensorGetDeviceName(int)")
fn("const char* SDL_SensorGetName(SDL_Sensor*)")
fn("const SDL_AssertData* SDL_GetAssertionReport()")
fn("const Uint8* SDL_GetKeyboardState(int*)")
fn("double SDL_acos(double)")
fn("double SDL_asin(double)")
fn("double SDL_atan2(double, double)")
fn("double SDL_atan(double)")
fn("double SDL_atof(const char*)")
fn("double SDL_ceil(double)")
fn("double SDL_copysign(double, double)")
fn("double SDL_cos(double)")
fn("double SDL_exp(double)")
fn("double SDL_fabs(double)")
fn("double SDL_floor(double)")
fn("double SDL_fmod(double, double)")
fn("double SDL_log10(double)")
fn("double SDL_log(double)")
fn("double SDL_pow(double, double)")
fn("double SDL_scalbn(double, int)")
fn("double SDL_sin(double)")
fn("double SDL_sqrt(double)")
fn("double SDL_strtod(const char*, char**)")
fn("double SDL_tan(double)")
fn("float SDL_acosf(float)")
fn("float SDL_asinf(float)")
fn("float SDL_atan2f(float, float)")
fn("float SDL_atanf(float)")
fn("float SDL_ceilf(float)")
fn("float SDL_copysignf(float, float)")
fn("float SDL_cosf(float)")
fn("float SDL_expf(float)")
fn("float SDL_fabsf(float)")
fn("float SDL_floorf(float)")
fn("float SDL_fmodf(float, float)")
fn("float SDL_GetWindowBrightness(SDL_Window*)")
fn("float SDL_log10f(float)")
fn("float SDL_logf(float)")
fn("float SDL_powf(float, float)")
fn("float SDL_scalbnf(float, int)")
fn("float SDL_sinf(float)")
fn("float SDL_sqrtf(float)")
fn("float SDL_tanf(float)")
fn("int SDL_abs(int)")
fn("int SDL_atoi(const char*)")
fn("int SDL_AtomicAdd(SDL_atomic_t*, int)")
fn("int SDL_AtomicGet(SDL_atomic_t*)")
fn("int SDL_AtomicSet(SDL_atomic_t*, int)")
fn("int SDL_AudioInit(const char*)")
fn("int SDL_AudioStreamAvailable(SDL_AudioStream*)")
fn("int SDL_AudioStreamFlush(SDL_AudioStream*)")
fn("int SDL_AudioStreamGet(SDL_AudioStream*, void*, int)")
fn("int SDL_AudioStreamPut(SDL_AudioStream*, const void*, int)")
fn("int SDL_BuildAudioCVT(SDL_AudioCVT*, SDL_AudioFormat, Uint8, int, SDL_AudioFormat, Uint8, int)")
fn("int SDL_CaptureMouse(SDL_bool)")
fn("int SDL_CondBroadcast(SDL_cond*)")
fn("int SDL_CondSignal(SDL_cond*)")
fn("int SDL_CondWait(SDL_cond*, SDL_mutex*)")
fn("int SDL_CondWaitTimeout(SDL_cond*, SDL_mutex*, Uint32)")
fn("int SDL_ConvertAudio(SDL_AudioCVT*)")
fn("int SDL_ConvertPixels(int, int, Uint32, const void*, int, Uint32, void*, int)")
fn("int SDL_CreateWindowAndRenderer(int, int, Uint32, SDL_Window**, SDL_Renderer**)")
fn("int SDL_Error(SDL_errorcode)")
fn("int SDL_FillRect(SDL_Surface*, const SDL_Rect*, Uint32)")
fn("int SDL_FillRects(SDL_Surface*, const SDL_Rect*, int, Uint32)")
fn("int SDL_GameControllerAddMapping(const char*)")
fn("int SDL_GameControllerAddMappingsFromRW(SDL_RWops*, int)")
fn("int SDL_GameControllerEventState(int)")
fn("int SDL_GameControllerGetPlayerIndex(SDL_GameController*)")
fn("int SDL_GameControllerNumMappings()")
fn("int SDL_GameControllerRumble(SDL_GameController*, Uint16, Uint16, Uint32)")
fn("int SDL_GetColorKey(SDL_Surface*, Uint32*)")
fn("int SDL_GetCPUCacheLineSize()")
fn("int SDL_GetCPUCount()")
fn("int SDL_GetCurrentDisplayMode(int, SDL_DisplayMode*)")
fn("int SDL_GetDesktopDisplayMode(int, SDL_DisplayMode*)")
fn("int SDL_GetDisplayBounds(int, SDL_Rect*)")
fn("int SDL_GetDisplayDPI(int, float*, float*, float*)")
fn("int SDL_GetDisplayMode(int, int, SDL_DisplayMode*)")
fn("int SDL_GetDisplayUsableBounds(int, SDL_Rect*)")
fn("int SDL_GetNumAllocations()")
fn("int SDL_GetNumAudioDevices(int)")
fn("int SDL_GetNumAudioDrivers()")
fn("int SDL_GetNumDisplayModes(int)")
fn("int SDL_GetNumRenderDrivers()")
fn("int SDL_GetNumTouchDevices()")
fn("int SDL_GetNumTouchFingers(SDL_TouchID)")
fn("int SDL_GetNumVideoDisplays()")
fn("int SDL_GetNumVideoDrivers()")
fn("int SDL_GetRenderDrawBlendMode(SDL_Renderer*, SDL_BlendMode*)")
fn("int SDL_GetRenderDrawColor(SDL_Renderer*, Uint8*, Uint8*, Uint8*, Uint8*)")
fn("int SDL_GetRenderDriverInfo(int, SDL_RendererInfo*)")
fn("int SDL_GetRendererInfo(SDL_Renderer*, SDL_RendererInfo*)")
fn("int SDL_GetRendererOutputSize(SDL_Renderer*, int*, int*)")
fn("int SDL_GetRevisionNumber()")
fn("int SDL_GetShapedWindowMode(SDL_Window*, SDL_WindowShapeMode*)")
fn("int SDL_GetSurfaceAlphaMod(SDL_Surface*, Uint8*)")
fn("int SDL_GetSurfaceBlendMode(SDL_Surface*, SDL_BlendMode*)")
fn("int SDL_GetSurfaceColorMod(SDL_Surface*, Uint8*, Uint8*, Uint8*)")
fn("int SDL_GetSystemRAM()")
fn("int SDL_GetTextureAlphaMod(SDL_Texture*, Uint8*)")
fn("int SDL_GetTextureBlendMode(SDL_Texture*, SDL_BlendMode*)")
fn("int SDL_GetTextureColorMod(SDL_Texture*, Uint8*, Uint8*, Uint8*)")
fn("int SDL_GetWindowBordersSize(SDL_Window*, int*, int*, int*, int*)")
fn("int SDL_GetWindowDisplayIndex(SDL_Window*)")
fn("int SDL_GetWindowDisplayMode(SDL_Window*, SDL_DisplayMode*)")
fn("int SDL_GetWindowGammaRamp(SDL_Window*, Uint16*, Uint16*, Uint16*)")
fn("int SDL_GetWindowOpacity(SDL_Window*, float*)")
fn("int SDL_GL_BindTexture(SDL_Texture*, float*, float*)")
fn("int SDL_GL_GetAttribute(SDL_GLattr, int*)")
fn("int SDL_GL_GetSwapInterval()")
fn("int SDL_GL_LoadLibrary(const char*)")
fn("int SDL_GL_MakeCurrent(SDL_Window*, SDL_GLContext)")
fn("int SDL_GL_SetAttribute(SDL_GLattr, int)")
fn("int SDL_GL_SetSwapInterval(int)")
fn("int SDL_GL_UnbindTexture(SDL_Texture*)")
fn("int SDL_HapticEffectSupported(SDL_Haptic*, SDL_HapticEffect*)")
fn("int SDL_HapticGetEffectStatus(SDL_Haptic*, int)")
fn("int SDL_HapticIndex(SDL_Haptic*)")
fn("int SDL_HapticNewEffect(SDL_Haptic*, SDL_HapticEffect*)")
fn("int SDL_HapticNumAxes(SDL_Haptic*)")
fn("int SDL_HapticNumEffectsPlaying(SDL_Haptic*)")
fn("int SDL_HapticNumEffects(SDL_Haptic*)")
fn("int SDL_HapticOpened(int)")
fn("int SDL_HapticPause(SDL_Haptic*)")
fn("int SDL_HapticRumbleInit(SDL_Haptic*)")
fn("int SDL_HapticRumblePlay(SDL_Haptic*, float, Uint32)")
fn("int SDL_HapticRumbleStop(SDL_Haptic*)")
fn("int SDL_HapticRumbleSupported(SDL_Haptic*)")
fn("int SDL_HapticRunEffect(SDL_Haptic*, int, Uint32)")
fn("int SDL_HapticSetAutocenter(SDL_Haptic*, int)")
fn("int SDL_HapticSetGain(SDL_Haptic*, int)")
fn("int SDL_HapticStopAll(SDL_Haptic*)")
fn("int SDL_HapticStopEffect(SDL_Haptic*, int)")
fn("int SDL_HapticUnpause(SDL_Haptic*)")
fn("int SDL_HapticUpdateEffect(SDL_Haptic*, int, SDL_HapticEffect*)")
fn("int SDL_iconv_close(SDL_iconv_t)")
fn("int SDL_InitSubSystem(Uint32)")
fn("int SDL_Init(Uint32)")
fn("int SDL_isdigit(int)")
fn("int SDL_isspace(int)")
fn("int SDL_JoystickEventState(int)")
fn("int SDL_JoystickGetBall(SDL_Joystick*, int, int*, int*)")
fn("int SDL_JoystickGetDevicePlayerIndex(int)")
fn("int SDL_JoystickGetPlayerIndex(SDL_Joystick*)")
fn("int SDL_JoystickIsHaptic(SDL_Joystick*)")
fn("int SDL_JoystickNumAxes(SDL_Joystick*)")
fn("int SDL_JoystickNumBalls(SDL_Joystick*)")
fn("int SDL_JoystickNumButtons(SDL_Joystick*)")
fn("int SDL_JoystickNumHats(SDL_Joystick*)")
fn("int SDL_JoystickRumble(SDL_Joystick*, Uint16, Uint16, Uint32)")
fn("int SDL_LinuxSetThreadPriority(Sint64, int)")
fn("int SDL_LoadDollarTemplates(SDL_TouchID, SDL_RWops*)")
fn("int SDL_LockMutex(SDL_mutex*)")
fn("int SDL_LockSurface(SDL_Surface*)")
fn("int SDL_LockTexture(SDL_Texture*, const SDL_Rect*, void**, int*)")
fn("int SDL_LowerBlitScaled(SDL_Surface*, SDL_Rect*, SDL_Surface*, SDL_Rect*)")
fn("int SDL_LowerBlit(SDL_Surface*, SDL_Rect*, SDL_Surface*, SDL_Rect*)")
fn("int SDL_memcmp(const void*, const void*, size_t)")
fn("int SDL_MouseIsHaptic()")
fn("int SDL_NumHaptics()")
fn("int SDL_NumJoysticks()")
fn("int SDL_NumSensors()")
fn("int SDL_OpenAudio(SDL_AudioSpec*, SDL_AudioSpec*)")
fn("int SDL_PeepEvents(SDL_Event*, int, SDL_eventaction, Uint32, Uint32)")
fn("int SDL_PollEvent(SDL_Event*)")
fn("int SDL_PushEvent(SDL_Event*)")
fn("int SDL_QueryTexture(SDL_Texture*, Uint32*, int*, int*, int*)")
fn("int SDL_QueueAudio(SDL_AudioDeviceID, const void*, Uint32)")
fn("int SDL_RecordGesture(SDL_TouchID)")
fn("int SDL_RenderClear(SDL_Renderer*)")
fn("int SDL_RenderCopyExF(SDL_Renderer*, SDL_Texture*, const SDL_Rect*, const SDL_FRect*, double, const SDL_FPoint*, SDL_RendererFlip)")
fn("int SDL_RenderCopyEx(SDL_Renderer*, SDL_Texture*, const SDL_Rect*, const SDL_Rect*, double, const SDL_Point*, SDL_RendererFlip)")
fn("int SDL_RenderCopyF(SDL_Renderer*, SDL_Texture*, const SDL_Rect*, const SDL_FRect*)")
fn("int SDL_RenderCopy(SDL_Renderer*, SDL_Texture*, const SDL_Rect*, const SDL_Rect*)")
fn("int SDL_RenderDrawLineF(SDL_Renderer*, float, float, float, float)")
fn("int SDL_RenderDrawLine(SDL_Renderer*, int, int, int, int)")
fn("int SDL_RenderDrawLinesF(SDL_Renderer*, const SDL_FPoint*, int)")
fn("int SDL_RenderDrawLines(SDL_Renderer*, const SDL_Point*, int)")
fn("int SDL_RenderDrawPointF(SDL_Renderer*, float, float)")
fn("int SDL_RenderDrawPoint(SDL_Renderer*, int, int)")
fn("int SDL_RenderDrawPointsF(SDL_Renderer*, const SDL_FPoint*, int)")
fn("int SDL_RenderDrawPoints(SDL_Renderer*, const SDL_Point*, int)")
fn("int SDL_RenderDrawRectF(SDL_Renderer*, const SDL_FRect*)")
fn("int SDL_RenderDrawRect(SDL_Renderer*, const SDL_Rect*)")
fn("int SDL_RenderDrawRectsF(SDL_Renderer*, const SDL_FRect*, int)")
fn("int SDL_RenderDrawRects(SDL_Renderer*, const SDL_Rect*, int)")
fn("int SDL_RenderFillRectF(SDL_Renderer*, const SDL_FRect*)")
fn("int SDL_RenderFillRect(SDL_Renderer*, const SDL_Rect*)")
fn("int SDL_RenderFillRectsF(SDL_Renderer*, const SDL_FRect*, int)")
fn("int SDL_RenderFillRects(SDL_Renderer*, const SDL_Rect*, int)")
fn("int SDL_RenderFlush(SDL_Renderer*)")
fn("int SDL_RenderReadPixels(SDL_Renderer*, const SDL_Rect*, Uint32, void*, int)")
fn("int SDL_RenderSetClipRect(SDL_Renderer*, const SDL_Rect*)")
fn("int SDL_RenderSetIntegerScale(SDL_Renderer*, SDL_bool)")
fn("int SDL_RenderSetLogicalSize(SDL_Renderer*, int, int)")
fn("int SDL_RenderSetScale(SDL_Renderer*, float, float)")
fn("int SDL_RenderSetViewport(SDL_Renderer*, const SDL_Rect*)")
fn("int SDL_RWclose(SDL_RWops*)")
fn("int SDL_SaveAllDollarTemplates(SDL_RWops*)")
fn("int SDL_SaveBMP_RW(SDL_Surface*, SDL_RWops*, int)")
fn("int SDL_SaveDollarTemplate(SDL_GestureID, SDL_RWops*)")
fn("int SDL_SemPost(SDL_sem*)")
fn("int SDL_SemTryWait(SDL_sem*)")
fn("int SDL_SemWait(SDL_sem*)")
fn("int SDL_SemWaitTimeout(SDL_sem*, Uint32)")
fn("int SDL_SensorGetData(SDL_Sensor*, float*, int)")
fn("int SDL_SensorGetDeviceNonPortableType(int)")
fn("int SDL_SensorGetNonPortableType(SDL_Sensor*)")
fn("int SDL_SetClipboardText(const char*)")
fn("int SDL_SetColorKey(SDL_Surface*, int, Uint32)")
fn("int SDL_setenv(const char*, const char*, int)")
fn("int SDL_SetMemoryFunctions(SDL_malloc_func, SDL_calloc_func, SDL_realloc_func, SDL_free_func)")
fn("int SDL_SetPaletteColors(SDL_Palette*, const SDL_Color*, int, int)")
fn("int SDL_SetPixelFormatPalette(SDL_PixelFormat*, SDL_Palette*)")
fn("int SDL_SetRelativeMouseMode(SDL_bool)")
fn("int SDL_SetRenderDrawBlendMode(SDL_Renderer*, SDL_BlendMode)")
fn("int SDL_SetRenderDrawColor(SDL_Renderer*, Uint8, Uint8, Uint8, Uint8)")
fn("int SDL_SetRenderTarget(SDL_Renderer*, SDL_Texture*)")
fn("int SDL_SetSurfaceAlphaMod(SDL_Surface*, Uint8)")
fn("int SDL_SetSurfaceBlendMode(SDL_Surface*, SDL_BlendMode)")
fn("int SDL_SetSurfaceColorMod(SDL_Surface*, Uint8, Uint8, Uint8)")
fn("int SDL_SetSurfacePalette(SDL_Surface*, SDL_Palette*)")
fn("int SDL_SetSurfaceRLE(SDL_Surface*, int)")
fn("int SDL_SetTextureAlphaMod(SDL_Texture*, Uint8)")
fn("int SDL_SetTextureBlendMode(SDL_Texture*, SDL_BlendMode)")
fn("int SDL_SetTextureColorMod(SDL_Texture*, Uint8, Uint8, Uint8)")
fn("int SDL_SetThreadPriority(SDL_ThreadPriority)")
fn("int SDL_SetWindowBrightness(SDL_Window*, float)")
fn("int SDL_SetWindowDisplayMode(SDL_Window*, const SDL_DisplayMode*)")
fn("int SDL_SetWindowFullscreen(SDL_Window*, Uint32)")
fn("int SDL_SetWindowGammaRamp(SDL_Window*, const Uint16*, const Uint16*, const Uint16*)")
fn("int SDL_SetWindowHitTest(SDL_Window*, SDL_HitTest, void*)")
fn("int SDL_SetWindowInputFocus(SDL_Window*)")
fn("int SDL_SetWindowModalFor(SDL_Window*, SDL_Window*)")
fn("int SDL_SetWindowOpacity(SDL_Window*, float)")
fn("int SDL_SetWindowShape(SDL_Window*, SDL_Surface*, SDL_WindowShapeMode*)")
fn("int SDL_ShowCursor(int)")
fn("int SDL_ShowMessageBox(const SDL_MessageBoxData*, int*)")
fn("int SDL_ShowSimpleMessageBox(Uint32, const char*, const char*, SDL_Window*)")
fn("int SDL_SoftStretch(SDL_Surface*, const SDL_Rect*, SDL_Surface*, const SDL_Rect*)")
fn("int SDL_strcasecmp(const char*, const char*)")
fn("int SDL_strcmp(const char*, const char*)")
fn("int SDL_strncasecmp(const char*, const char*, size_t)")
fn("int SDL_strncmp(const char*, const char*, size_t)")
fn("int SDL_tolower(int)")
fn("int SDL_toupper(int)")
fn("int SDL_TryLockMutex(SDL_mutex*)")
fn("int SDL_UnlockMutex(SDL_mutex*)")
fn("int SDL_UpdateTexture(SDL_Texture*, const SDL_Rect*, const void*, int)")
fn("int SDL_UpdateWindowSurfaceRects(SDL_Window*, const SDL_Rect*, int)")
fn("int SDL_UpdateWindowSurface(SDL_Window*)")
fn("int SDL_UpdateYUVTexture(SDL_Texture*, const SDL_Rect*, const Uint8*, int, const Uint8*, int, const Uint8*, int)")
fn("int SDL_UpperBlitScaled(SDL_Surface*, const SDL_Rect*, SDL_Surface*, SDL_Rect*)")
fn("int SDL_UpperBlit(SDL_Surface*, const SDL_Rect*, SDL_Surface*, SDL_Rect*)")
fn("int SDL_VideoInit(const char*)")
fn("int SDL_WaitEvent(SDL_Event*)")
fn("int SDL_WaitEventTimeout(SDL_Event*, int)")
fn("int SDL_WarpMouseGlobal(int, int)")
fn("int SDL_wcscmp(const wchar_t*, const wchar_t*)")
fn("long int SDL_strtol(const char*, char**, int)")
fn("long unsigned int SDL_strtoul(const char*, char**, int)")
fn("SDL_AssertState SDL_ReportAssertion(SDL_AssertData*, const char*, const char*, int)")
fn("SDL_AudioDeviceID SDL_OpenAudioDevice(const char*, int, const SDL_AudioSpec*, SDL_AudioSpec*, int)")
fn("SDL_AudioSpec* SDL_LoadWAV_RW(SDL_RWops*, int, SDL_AudioSpec*, Uint8**, Uint32*)")
fn("SDL_AudioStatus SDL_GetAudioDeviceStatus(SDL_AudioDeviceID)")
fn("SDL_AudioStatus SDL_GetAudioStatus()")
fn("SDL_AudioStream* SDL_NewAudioStream(SDL_AudioFormat, Uint8, int, SDL_AudioFormat, Uint8, int)")
fn("SDL_BlendMode SDL_ComposeCustomBlendMode(SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation, SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation)")
fn("SDL_bool SDL_AtomicCASPtr(void**, void*, void*)")
fn("SDL_bool SDL_AtomicCAS(SDL_atomic_t*, int, int)")
fn("SDL_bool SDL_AtomicTryLock(SDL_SpinLock*)")
fn("SDL_bool SDL_EnclosePoints(const SDL_Point*, int, const SDL_Rect*, SDL_Rect*)")
fn("SDL_bool SDL_GameControllerGetAttached(SDL_GameController*)")
fn("SDL_bool SDL_GetHintBoolean(const char*, SDL_bool)")
fn("SDL_bool SDL_GetRelativeMouseMode()")
fn("SDL_bool SDL_GetWindowGrab(SDL_Window*)")
fn("SDL_bool SDL_GL_ExtensionSupported(const char*)")
fn("SDL_bool SDL_Has3DNow()")
fn("SDL_bool SDL_HasAltiVec()")
fn("SDL_bool SDL_HasAVX()")
fn("SDL_bool SDL_HasAVX2()")
fn("SDL_bool SDL_HasAVX512F()")
fn("SDL_bool SDL_HasClipboardText()")
fn("SDL_bool SDL_HasColorKey(SDL_Surface*)")
fn("SDL_bool SDL_HasEvents(Uint32, Uint32)")
fn("SDL_bool SDL_HasEvent(Uint32)")
fn("SDL_bool SDL_HasIntersection(const SDL_Rect*, const SDL_Rect*)")
fn("SDL_bool SDL_HasMMX()")
fn("SDL_bool SDL_HasNEON()")
fn("SDL_bool SDL_HasRDTSC()")
fn("SDL_bool SDL_HasScreenKeyboardSupport()")
fn("SDL_bool SDL_HasSSE()")
fn("SDL_bool SDL_HasSSE2()")
fn("SDL_bool SDL_HasSSE3()")
fn("SDL_bool SDL_HasSSE41()")
fn("SDL_bool SDL_HasSSE42()")
fn("SDL_bool SDL_IntersectRectAndLine(const SDL_Rect*, int*, int*, int*, int*)")
fn("SDL_bool SDL_IntersectRect(const SDL_Rect*, const SDL_Rect*, SDL_Rect*)")
fn("SDL_bool SDL_IsGameController(int)")
fn("SDL_bool SDL_IsScreenKeyboardShown(SDL_Window*)")
fn("SDL_bool SDL_IsScreenSaverEnabled()")
fn("SDL_bool SDL_IsShapedWindow(const SDL_Window*)")
fn("SDL_bool SDL_IsTablet()")
fn("SDL_bool SDL_IsTextInputActive()")
fn("SDL_bool SDL_JoystickGetAttached(SDL_Joystick*)")
fn("SDL_bool SDL_JoystickGetAxisInitialState(SDL_Joystick*, int, Sint16*)")
fn("SDL_bool SDL_PixelFormatEnumToMasks(Uint32, int*, Uint32*, Uint32*, Uint32*, Uint32*)")
fn("SDL_bool SDL_RemoveTimer(SDL_TimerID)")
fn("SDL_bool SDL_RenderGetIntegerScale(SDL_Renderer*)")
fn("SDL_bool SDL_RenderIsClipEnabled(SDL_Renderer*)")
fn("SDL_bool SDL_RenderTargetSupported(SDL_Renderer*)")
fn("SDL_bool SDL_SetClipRect(SDL_Surface*, const SDL_Rect*)")
fn("SDL_bool SDL_SetHint(const char*, const char*)")
fn("SDL_bool SDL_SetHintWithPriority(const char*, const char*, SDL_HintPriority)")
fn("SDL_cond* SDL_CreateCond()")
fn("SDL_Cursor* SDL_CreateColorCursor(SDL_Surface*, int, int)")
fn("SDL_Cursor* SDL_CreateCursor(const Uint8*, const Uint8*, int, int, int, int)")
fn("SDL_Cursor* SDL_CreateSystemCursor(SDL_SystemCursor)")
fn("SDL_Cursor* SDL_GetCursor()")
fn("SDL_Cursor* SDL_GetDefaultCursor()")
fn("SDL_DisplayMode* SDL_GetClosestDisplayMode(int, const SDL_DisplayMode*, SDL_DisplayMode*)")
fn("SDL_DisplayOrientation SDL_GetDisplayOrientation(int)")
fn("SDL_Finger* SDL_GetTouchFinger(SDL_TouchID, int)")
fn("SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(const char*)")
fn("SDL_GameControllerButtonBind SDL_GameControllerGetBindForAxis(SDL_GameController*, SDL_GameControllerAxis)")
fn("SDL_GameControllerButtonBind SDL_GameControllerGetBindForButton(SDL_GameController*, SDL_GameControllerButton)")
fn("SDL_GameControllerButton SDL_GameControllerGetButtonFromString(const char*)")
fn("SDL_GameController* SDL_GameControllerFromInstanceID(SDL_JoystickID)")
fn("SDL_GameController* SDL_GameControllerOpen(int)")
fn("SDL_Haptic* SDL_HapticOpenFromJoystick(SDL_Joystick*)")
fn("SDL_Haptic* SDL_HapticOpenFromMouse()")
fn("SDL_Haptic* SDL_HapticOpen(int)")
fn("_SDL_iconv_t* SDL_iconv_open(const char*, const char*)")
fn("SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int)")
fn("SDL_JoystickGUID SDL_JoystickGetGUIDFromString(const char*)")
fn("SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick*)")
fn("SDL_JoystickID SDL_JoystickGetDeviceInstanceID(int)")
fn("SDL_JoystickID SDL_JoystickInstanceID(SDL_Joystick*)")
fn("SDL_JoystickPowerLevel SDL_JoystickCurrentPowerLevel(SDL_Joystick*)")
fn("SDL_Joystick* SDL_GameControllerGetJoystick(SDL_GameController*)")
fn("SDL_Joystick* SDL_JoystickFromInstanceID(SDL_JoystickID)")
fn("SDL_Joystick* SDL_JoystickOpen(int)")
fn("SDL_JoystickType SDL_JoystickGetDeviceType(int)")
fn("SDL_JoystickType SDL_JoystickGetType(SDL_Joystick*)")
fn("SDL_Keycode SDL_GetKeyFromName(const char*)")
fn("SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode)")
fn("SDL_Keymod SDL_GetModState()")
fn("SDL_LogPriority SDL_LogGetPriority(int)")
fn("SDL_mutex* SDL_CreateMutex()")
fn("SDL_Palette* SDL_AllocPalette(int)")
fn("SDL_PixelFormat* SDL_AllocFormat(Uint32)")
fn("SDL_PowerState SDL_GetPowerInfo(int*, int*)")
fn("SDL_Renderer* SDL_CreateRenderer(SDL_Window*, int, Uint32)")
fn("SDL_Renderer* SDL_CreateSoftwareRenderer(SDL_Surface*)")
fn("SDL_Renderer* SDL_GetRenderer(SDL_Window*)")
fn("SDL_RWops* SDL_AllocRW()")
fn("SDL_RWops* SDL_RWFromConstMem(const void*, int)")
fn("SDL_RWops* SDL_RWFromFile(const char*, const char*)")
fn("SDL_RWops* SDL_RWFromFP(FILE*, SDL_bool)")
fn("SDL_RWops* SDL_RWFromMem(void*, int)")
fn("SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode)")
fn("SDL_Scancode SDL_GetScancodeFromName(const char*)")
fn("SDL_sem* SDL_CreateSemaphore(Uint32)")
fn("SDL_SensorID SDL_SensorGetDeviceInstanceID(int)")
fn("SDL_SensorID SDL_SensorGetInstanceID(SDL_Sensor*)")
fn("SDL_Sensor* SDL_SensorFromInstanceID(SDL_SensorID)")
fn("SDL_Sensor* SDL_SensorOpen(int)")
fn("SDL_SensorType SDL_SensorGetDeviceType(int)")
fn("SDL_SensorType SDL_SensorGetType(SDL_Sensor*)")
fn("SDL_Surface* SDL_ConvertSurfaceFormat(SDL_Surface*, Uint32, Uint32)")
fn("SDL_Surface* SDL_ConvertSurface(SDL_Surface*, const SDL_PixelFormat*, Uint32)")
fn("SDL_Surface* SDL_CreateRGBSurfaceFrom(void*, int, int, int, int, Uint32, Uint32, Uint32, Uint32)")
fn("SDL_Surface* SDL_CreateRGBSurface(Uint32, int, int, int, Uint32, Uint32, Uint32, Uint32)")
fn("SDL_Surface* SDL_CreateRGBSurfaceWithFormatFrom(void*, int, int, int, int, Uint32)")
fn("SDL_Surface* SDL_CreateRGBSurfaceWithFormat(Uint32, int, int, int, Uint32)")
fn("SDL_Surface* SDL_DuplicateSurface(SDL_Surface*)")
fn("SDL_Surface* SDL_GetWindowSurface(SDL_Window*)")
fn("SDL_Surface* SDL_LoadBMP_RW(SDL_RWops*, int)")
fn("SDL_Texture* SDL_CreateTextureFromSurface(SDL_Renderer*, SDL_Surface*)")
fn("SDL_Texture* SDL_CreateTexture(SDL_Renderer*, Uint32, int, int, int)")
fn("SDL_Texture* SDL_GetRenderTarget(SDL_Renderer*)")
fn("SDL_threadID SDL_GetThreadID(SDL_Thread*)")
fn("SDL_threadID SDL_ThreadID()")
fn("SDL_Thread* SDL_CreateThread(SDL_ThreadFunction, const char*, void*)")
fn("SDL_Thread* SDL_CreateThreadWithStackSize(SDL_ThreadFunction, const char*, size_t, void*)")
fn("SDL_TimerID SDL_AddTimer(Uint32, SDL_TimerCallback, void*)")
fn("SDL_TLSID SDL_TLSCreate()")
fn("SDL_TouchDeviceType SDL_GetTouchDeviceType(SDL_TouchID)")
fn("SDL_TouchID SDL_GetTouchDevice(int)")
fn("SDL_Window* SDL_CreateShapedWindow(const char*, unsigned int, unsigned int, unsigned int, unsigned int, Uint32)")
fn("SDL_Window* SDL_CreateWindow(const char*, int, int, int, int, Uint32)")
fn("SDL_Window* SDL_CreateWindowFrom(const void*)")
fn("SDL_Window* SDL_GetGrabbedWindow()")
fn("SDL_Window* SDL_GetKeyboardFocus()")
fn("SDL_Window* SDL_GetMouseFocus()")
fn("SDL_Window* SDL_GetWindowFromID(Uint32)")
fn("SDL_Window* SDL_GL_GetCurrentWindow()")
fn("SDL_YUV_CONVERSION_MODE SDL_GetYUVConversionMode()")
fn("SDL_YUV_CONVERSION_MODE SDL_GetYUVConversionModeForResolution(int, int)")
fn("Sint16 SDL_GameControllerGetAxis(SDL_GameController*, SDL_GameControllerAxis)")
fn("Sint16 SDL_JoystickGetAxis(SDL_Joystick*, int)")
fn("Sint64 SDL_RWseek(SDL_RWops*, Sint64, int)")
fn("Sint64 SDL_RWsize(SDL_RWops*)")
fn("Sint64 SDL_RWtell(SDL_RWops*)")
fn("Sint64 SDL_strtoll(const char*, char**, int)")
fn("size_t SDL_iconv(SDL_iconv_t, const char**, size_t*, char**, size_t*)")
fn("size_t SDL_RWread(SDL_RWops*, void*, size_t, size_t)")
fn("size_t SDL_RWwrite(SDL_RWops*, const void*, size_t, size_t)")
fn("size_t SDL_SIMDGetAlignment()")
fn("size_t SDL_strlcat(char*, const char*, size_t)")
fn("size_t SDL_strlcpy(char*, const char*, size_t)")
fn("size_t SDL_strlen(const char*)")
fn("size_t SDL_utf8strlcpy(char*, const char*, size_t)")
fn("size_t SDL_utf8strlen(const char*)")
fn("size_t SDL_wcslcat(wchar_t*, const wchar_t*, size_t)")
fn("size_t SDL_wcslcpy(wchar_t*, const wchar_t*, size_t)")
fn("size_t SDL_wcslen(const wchar_t*)")
fn("size_t SDL_WriteBE16(SDL_RWops*, Uint16)")
fn("size_t SDL_WriteBE32(SDL_RWops*, Uint32)")
fn("size_t SDL_WriteBE64(SDL_RWops*, Uint64)")
fn("size_t SDL_WriteLE16(SDL_RWops*, Uint16)")
fn("size_t SDL_WriteLE32(SDL_RWops*, Uint32)")
fn("size_t SDL_WriteLE64(SDL_RWops*, Uint64)")
fn("size_t SDL_WriteU8(SDL_RWops*, Uint8)")
fn("Uint16 SDL_GameControllerGetProduct(SDL_GameController*)")
fn("Uint16 SDL_GameControllerGetProductVersion(SDL_GameController*)")
fn("Uint16 SDL_GameControllerGetVendor(SDL_GameController*)")
fn("Uint16 SDL_JoystickGetDeviceProduct(int)")
fn("Uint16 SDL_JoystickGetDeviceProductVersion(int)")
fn("Uint16 SDL_JoystickGetDeviceVendor(int)")
fn("Uint16 SDL_JoystickGetProduct(SDL_Joystick*)")
fn("Uint16 SDL_JoystickGetProductVersion(SDL_Joystick*)")
fn("Uint16 SDL_JoystickGetVendor(SDL_Joystick*)")
fn("Uint16 SDL_ReadBE16(SDL_RWops*)")
fn("Uint16 SDL_ReadLE16(SDL_RWops*)")
fn("Uint32 SDL_DequeueAudio(SDL_AudioDeviceID, void*, Uint32)")
fn("Uint32 SDL_GetGlobalMouseState(int*, int*)")
fn("Uint32 SDL_GetMouseState(int*, int*)")
fn("Uint32 SDL_GetQueuedAudioSize(SDL_AudioDeviceID)")
fn("Uint32 SDL_GetRelativeMouseState(int*, int*)")
fn("Uint32 SDL_GetTicks()")
fn("Uint32 SDL_GetWindowFlags(SDL_Window*)")
fn("Uint32 SDL_GetWindowID(SDL_Window*)")
fn("Uint32 SDL_GetWindowPixelFormat(SDL_Window*)")
fn("Uint32 SDL_MapRGBA(const SDL_PixelFormat*, Uint8, Uint8, Uint8, Uint8)")
fn("Uint32 SDL_MapRGB(const SDL_PixelFormat*, Uint8, Uint8, Uint8)")
fn("Uint32 SDL_MasksToPixelFormatEnum(int, Uint32, Uint32, Uint32, Uint32)")
fn("Uint32 SDL_ReadBE32(SDL_RWops*)")
fn("Uint32 SDL_ReadLE32(SDL_RWops*)")
fn("Uint32 SDL_RegisterEvents(int)")
fn("Uint32 SDL_SemValue(SDL_sem*)")
fn("Uint32 SDL_WasInit(Uint32)")
fn("Uint64 SDL_GetPerformanceCounter()")
fn("Uint64 SDL_GetPerformanceFrequency()")
fn("Uint64 SDL_ReadBE64(SDL_RWops*)")
fn("Uint64 SDL_ReadLE64(SDL_RWops*)")
fn("Uint64 SDL_strtoull(const char*, char**, int)")
fn("Uint8 SDL_EventState(Uint32, int)")
fn("Uint8 SDL_GameControllerGetButton(SDL_GameController*, SDL_GameControllerButton)")
fn("Uint8 SDL_JoystickGetButton(SDL_Joystick*, int)")
fn("Uint8 SDL_JoystickGetHat(SDL_Joystick*, int)")
fn("Uint8 SDL_ReadU8(SDL_RWops*)")
fn("unsigned int SDL_HapticQuery(SDL_Haptic*)")
fn("void SDL_AddEventWatch(SDL_EventFilter, void*)")
fn("void SDL_AddHintCallback(const char*, SDL_HintCallback, void*)")
fn("void* SDL_AtomicGetPtr(void**)")
fn("void SDL_AtomicLock(SDL_SpinLock*)")
fn("void* SDL_AtomicSetPtr(void**, void*)")
fn("void SDL_AtomicUnlock(SDL_SpinLock*)")
fn("void SDL_AudioQuit()")
fn("void SDL_AudioStreamClear(SDL_AudioStream*)")
fn("void SDL_CalculateGammaRamp(float, Uint16*)")
fn("void* SDL_calloc(size_t, size_t)")
fn("void SDL_ClearError()")
fn("void SDL_ClearHints()")
fn("void SDL_ClearQueuedAudio(SDL_AudioDeviceID)")
fn("void SDL_CloseAudio()")
fn("void SDL_CloseAudioDevice(SDL_AudioDeviceID)")
fn("void SDL_Delay(Uint32)")
fn("void SDL_DelEventWatch(SDL_EventFilter, void*)")
fn("void SDL_DelHintCallback(const char*, SDL_HintCallback, void*)")
fn("void SDL_DestroyCond(SDL_cond*)")
fn("void SDL_DestroyMutex(SDL_mutex*)")
fn("void SDL_DestroyRenderer(SDL_Renderer*)")
fn("void SDL_DestroySemaphore(SDL_sem*)")
fn("void SDL_DestroyTexture(SDL_Texture*)")
fn("void SDL_DestroyWindow(SDL_Window*)")
fn("void SDL_DetachThread(SDL_Thread*)")
fn("void SDL_DisableScreenSaver()")
fn("void SDL_EnableScreenSaver()")
fn("void SDL_FilterEvents(SDL_EventFilter, void*)")
fn("void SDL_FlushEvents(Uint32, Uint32)")
fn("void SDL_FlushEvent(Uint32)")
fn("void SDL_FreeAudioStream(SDL_AudioStream*)")
fn("void SDL_FreeCursor(SDL_Cursor*)")
fn("void SDL_FreeFormat(SDL_PixelFormat*)")
fn("void SDL_FreePalette(SDL_Palette*)")
fn("void SDL_FreeRW(SDL_RWops*)")
fn("void SDL_FreeSurface(SDL_Surface*)")
fn("void SDL_free(void*)")
fn("void SDL_FreeWAV(Uint8*)")
fn("void SDL_GameControllerClose(SDL_GameController*)")
fn("void SDL_GameControllerUpdate()")
fn("void SDL_GetClipRect(SDL_Surface*, SDL_Rect*)")
fn("void SDL_GetRGBA(Uint32, const SDL_PixelFormat*, Uint8*, Uint8*, Uint8*, Uint8*)")
fn("void SDL_GetRGB(Uint32, const SDL_PixelFormat*, Uint8*, Uint8*, Uint8*)")
fn("void SDL_GetVersion(SDL_version*)")
fn("void* SDL_GetWindowData(SDL_Window*, const char*)")
fn("void SDL_GetWindowMaximumSize(SDL_Window*, int*, int*)")
fn("void SDL_GetWindowMinimumSize(SDL_Window*, int*, int*)")
fn("void SDL_GetWindowPosition(SDL_Window*, int*, int*)")
fn("void SDL_GetWindowSize(SDL_Window*, int*, int*)")
fn("void* SDL_GL_CreateContext(SDL_Window*)")
fn("void SDL_GL_DeleteContext(SDL_GLContext)")
fn("void* SDL_GL_GetCurrentContext()")
fn("void SDL_GL_GetDrawableSize(SDL_Window*, int*, int*)")
#fn("void* SDL_GL_GetProcAddress(const char*)") # native impl
fn("void SDL_GL_ResetAttributes()")
fn("void SDL_GL_SwapWindow(SDL_Window*)")
fn("void SDL_GL_UnloadLibrary()")
fn("void SDL_HapticClose(SDL_Haptic*)")
fn("void SDL_HapticDestroyEffect(SDL_Haptic*, int)")
fn("void SDL_HideWindow(SDL_Window*)")
fn("void SDL_JoystickClose(SDL_Joystick*)")
fn("void SDL_JoystickGetGUIDString(SDL_JoystickGUID, char*, int)")
fn("void SDL_JoystickUpdate()")
fn("void* SDL_LoadFile(const char*, size_t*)")
fn("void* SDL_LoadFile_RW(SDL_RWops*, size_t*, int)")
fn("void* SDL_LoadFunction(void*, const char*)")
fn("void* SDL_LoadObject(const char*)")
fn("void SDL_LockAudio()")
fn("void SDL_LockAudioDevice(SDL_AudioDeviceID)")
fn("void SDL_LockJoysticks()")
fn("void SDL_LogResetPriorities()")
fn("void SDL_LogSetAllPriority(SDL_LogPriority)")
fn("void SDL_LogSetOutputFunction(SDL_LogOutputFunction, void*)")
fn("void SDL_LogSetPriority(int, SDL_LogPriority)")
fn("void* SDL_malloc(size_t)")
fn("void SDL_MaximizeWindow(SDL_Window*)")
fn("void* SDL_memcpy(void*, const void*, size_t)")
fn("void* SDL_memmove(void*, const void*, size_t)")
fn("void SDL_MemoryBarrierAcquireFunction()")
fn("void SDL_MemoryBarrierReleaseFunction()")
fn("void* SDL_memset(void*, int, size_t)")
fn("void SDL_MinimizeWindow(SDL_Window*)")
fn("void SDL_MixAudioFormat(Uint8*, const Uint8*, SDL_AudioFormat, Uint32, int)")
fn("void SDL_MixAudio(Uint8*, const Uint8*, Uint32, int)")
fn("void SDL_PauseAudioDevice(SDL_AudioDeviceID, int)")
fn("void SDL_PauseAudio(int)")
fn("void SDL_PumpEvents()")
fn("void SDL_Quit()")
fn("void SDL_QuitSubSystem(Uint32)")
fn("void SDL_RaiseWindow(SDL_Window*)")
fn("void* SDL_realloc(void*, size_t)")
fn("void SDL_RenderGetClipRect(SDL_Renderer*, SDL_Rect*)")
fn("void SDL_RenderGetLogicalSize(SDL_Renderer*, int*, int*)")
fn("void* SDL_RenderGetMetalCommandEncoder(SDL_Renderer*)")
fn("void* SDL_RenderGetMetalLayer(SDL_Renderer*)")
fn("void SDL_RenderGetScale(SDL_Renderer*, float*, float*)")
fn("void SDL_RenderGetViewport(SDL_Renderer*, SDL_Rect*)")
fn("void SDL_RenderPresent(SDL_Renderer*)")
fn("void SDL_ResetAssertionReport()")
fn("void SDL_RestoreWindow(SDL_Window*)")
fn("void SDL_SensorClose(SDL_Sensor*)")
fn("void SDL_SensorUpdate()")
fn("void SDL_SetAssertionHandler(SDL_AssertionHandler, void*)")
fn("void SDL_SetCursor(SDL_Cursor*)")
fn("void SDL_SetEventFilter(SDL_EventFilter, void*)")
fn("void SDL_SetMainReady()")
fn("void SDL_SetModState(SDL_Keymod)")
fn("void SDL_SetTextInputRect(SDL_Rect*)")
fn("void SDL_SetWindowBordered(SDL_Window*, SDL_bool)")
fn("void* SDL_SetWindowData(SDL_Window*, const char*, void*)")
fn("void SDL_SetWindowGrab(SDL_Window*, SDL_bool)")
fn("void SDL_SetWindowIcon(SDL_Window*, SDL_Surface*)")
fn("void SDL_SetWindowMaximumSize(SDL_Window*, int, int)")
fn("void SDL_SetWindowMinimumSize(SDL_Window*, int, int)")
fn("void SDL_SetWindowPosition(SDL_Window*, int, int)")
fn("void SDL_SetWindowResizable(SDL_Window*, SDL_bool)")
fn("void SDL_SetWindowSize(SDL_Window*, int, int)")
fn("void SDL_SetWindowTitle(SDL_Window*, const char*)")
fn("void SDL_SetYUVConversionMode(SDL_YUV_CONVERSION_MODE)")
fn("void SDL_ShowWindow(SDL_Window*)")
fn("void* SDL_SIMDAlloc(size_t)")
fn("void SDL_SIMDFree(void*)")
fn("void SDL_StartTextInput()")
fn("void SDL_StopTextInput()")
fn("void* SDL_TLSGet(SDL_TLSID)")
fn("void SDL_UnionRect(const SDL_Rect*, const SDL_Rect*, SDL_Rect*)")
fn("void SDL_UnloadObject(void*)")
fn("void SDL_UnlockAudio()")
fn("void SDL_UnlockAudioDevice(SDL_AudioDeviceID)")
fn("void SDL_UnlockJoysticks()")
fn("void SDL_UnlockSurface(SDL_Surface*)")
fn("void SDL_UnlockTexture(SDL_Texture*)")
fn("void SDL_VideoQuit()")
fn("void SDL_WaitThread(SDL_Thread*, int*)")
fn("void SDL_WarpMouseInWindow(SDL_Window*, int, int)")
fn("wchar_t* SDL_wcsdup(const wchar_t*)")
fn("SDL_bool SDL_GetWindowWMInfo(SDL_Window*, SDL_SysWMinfo*)");


Generate()