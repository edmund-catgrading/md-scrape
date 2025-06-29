# Core

Phaser.Core

## width

### width: number, string

**Description:**

The width of the underlying canvas, in pixels.

> Source: [src/core/Config.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L54)

## height

### height: number, string

**Description:**

The height of the underlying canvas, in pixels.

> Source: [src/core/Config.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L59)

## zoom

### zoom: [Phaser.Scale.ZoomType](../typedef/scale.md), number

**Description:**

The zoom factor, as used by the Scale Manager.

> Source: [src/core/Config.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L64)

## parent

### parent: \*

**Description:**

A parent DOM element into which the canvas created by the renderer will be injected.

> Source: [src/core/Config.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L69)

## scaleMode

### scaleMode: [Phaser.Scale.ScaleModeType](../typedef/scale.md)

**Description:**

The scale mode as used by the Scale Manager. The default is zero, which is no scaling.

> Source: [src/core/Config.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L74)

## expandParent

### expandParent: boolean

**Description:**

Is the Scale Manager allowed to adjust the CSS height property of the parent to be 100%?

> Source: [src/core/Config.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L79)

## autoRound

### autoRound: boolean

**Description:**

Automatically round the display and style sizes of the canvas. This can help with performance in lower-powered devices.

> Source: [src/core/Config.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L84)

## autoCenter

### autoCenter: [Phaser.Scale.CenterType](../typedef/scale.md)

**Description:**

Automatically center the canvas within the parent?

> Source: [src/core/Config.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L89)

## resizeInterval

### resizeInterval: number

**Description:**

How many ms should elapse before checking if the browser size has changed?

> Source: [src/core/Config.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L94)

## fullscreenTarget

### fullscreenTarget: HTMLElement, string

**Description:**

The DOM element that will be sent into full screen mode, or its `id`. If undefined Phaser will create its own div and insert the canvas into it when entering fullscreen mode.

> Source: [src/core/Config.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L99)

## minWidth

### minWidth: number

**Description:**

The minimum width, in pixels, the canvas will scale down to. A value of zero means no minimum.

> Source: [src/core/Config.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L104)

## maxWidth

### maxWidth: number

**Description:**

The maximum width, in pixels, the canvas will scale up to. A value of zero means no maximum.

> Source: [src/core/Config.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L109)

## minHeight

### minHeight: number

**Description:**

The minimum height, in pixels, the canvas will scale down to. A value of zero means no minimum.

> Source: [src/core/Config.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L114)

## maxHeight

### maxHeight: number

**Description:**

The maximum height, in pixels, the canvas will scale up to. A value of zero means no maximum.

> Source: [src/core/Config.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L119)

## snapWidth

### snapWidth: number

**Description:**

The horizontal amount to snap the canvas by when the Scale Manager is resizing. A value of zero means no snapping.

> Source: [src/core/Config.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L124)

## snapHeight

### snapHeight: number

**Description:**

The vertical amount to snap the canvas by when the Scale Manager is resizing. A value of zero means no snapping.

> Source: [src/core/Config.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L129)

## renderType

### renderType: number

**Description:**

Force Phaser to use a specific renderer. Can be `CONST.CANVAS`, `CONST.WEBGL`, `CONST.HEADLESS` or `CONST.AUTO` (default)

> Source: [src/core/Config.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L134)

## canvas

### canvas: HTMLCanvasElement

**Description:**

Force Phaser to use your own Canvas element instead of creating one.

> Source: [src/core/Config.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L139)

## context

### context: CanvasRenderingContext2D, WebGLRenderingContext

**Description:**

Force Phaser to use your own Canvas context instead of creating one.

> Source: [src/core/Config.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L144)

## canvasStyle

### canvasStyle: string

**Description:**

Optional CSS attributes to be set on the canvas object created by the renderer.

> Source: [src/core/Config.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L149)

## customEnvironment

### customEnvironment: boolean

**Description:**

Is Phaser running under a custom (non-native web) environment? If so, set this to `true` to skip internal Feature detection. If `true` the `renderType` cannot be left as `AUTO`.

> Source: [src/core/Config.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L154)

## sceneConfig

### sceneConfig: object

**Description:**

The default Scene configuration object.

> Source: [src/core/Config.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L159)

## seed

### seed: Array.<string>

**Description:**

A seed which the Random Data Generator will use. If not given, a dynamic seed based on the time is used.

> Source: [src/core/Config.js#L164](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L164)

## gameTitle

### gameTitle: string

**Description:**

The title of the game.

> Source: [src/core/Config.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L171)

## gameURL

### gameURL: string

**Description:**

The URL of the game.

> Source: [src/core/Config.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L176)

## gameVersion

### gameVersion: string

**Description:**

The version of the game.

> Source: [src/core/Config.js#L181](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L181)

## autoFocus

### autoFocus: boolean

**Description:**

If `true` the window will automatically be given focus immediately and on any future mousedown event.

> Source: [src/core/Config.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L186)

## stableSort

### stableSort: number, boolean

**Description:**

`false` or `0` = Use the built-in StableSort (needed for older browsers), `true` or `1` = Rely on ES2019 Array.sort being stable (modern browsers only), or `-1` = Try and determine this automatically based on browser inspection (not guaranteed to work, errs on side of caution).

> Source: [src/core/Config.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L191)

## domCreateContainer

### domCreateContainer: boolean

**Description:**

Should the game create a div element to act as a DOM Container? Only enable if you're using DOM Element objects. You must provide a parent object if you use this feature.

> Source: [src/core/Config.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L205)

## domPointerEvents

### domPointerEvents: string

**Description:**

The default `pointerEvents` attribute set on the DOM Container.

> Source: [src/core/Config.js#L210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L210)

## inputKeyboard

### inputKeyboard: boolean

**Description:**

Enable the Keyboard Plugin. This can be disabled in games that don't need keyboard input.

> Source: [src/core/Config.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L217)

## inputKeyboardEventTarget

### inputKeyboardEventTarget: \*

**Description:**

The DOM Target to listen for keyboard events on. Defaults to `window` if not specified.

> Source: [src/core/Config.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L222)

## inputKeyboardCapture

### inputKeyboardCapture: Array.<number>

**Description:**

`preventDefault` will be called on every non-modified key which has a key code in this array. By default, it is empty.

> Source: [src/core/Config.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L227)

## inputMouse

### inputMouse: boolean, object

**Description:**

Enable the Mouse Plugin. This can be disabled in games that don't need mouse input.

> Source: [src/core/Config.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L232)

## inputMouseEventTarget

### inputMouseEventTarget: \*

**Description:**

The DOM Target to listen for mouse events on. Defaults to the game canvas if not specified.

> Source: [src/core/Config.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L237)

## inputMousePreventDefaultDown

### inputMousePreventDefaultDown: boolean

**Description:**

Should `mousedown` DOM events have `preventDefault` called on them?

> Source: [src/core/Config.js#L242](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L242)

## inputMousePreventDefaultUp

### inputMousePreventDefaultUp: boolean

**Description:**

Should `mouseup` DOM events have `preventDefault` called on them?

> Source: [src/core/Config.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L247)

## inputMousePreventDefaultMove

### inputMousePreventDefaultMove: boolean

**Description:**

Should `mousemove` DOM events have `preventDefault` called on them?

> Source: [src/core/Config.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L252)

## inputMousePreventDefaultWheel

### inputMousePreventDefaultWheel: boolean

**Description:**

Should `wheel` DOM events have `preventDefault` called on them?

> Source: [src/core/Config.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L257)

## inputTouch

### inputTouch: boolean

**Description:**

Enable the Touch Plugin. This can be disabled in games that don't need touch input.

> Source: [src/core/Config.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L262)

## inputTouchEventTarget

### inputTouchEventTarget: \*

**Description:**

The DOM Target to listen for touch events on. Defaults to the game canvas if not specified.

> Source: [src/core/Config.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L267)

## inputTouchCapture

### inputTouchCapture: boolean

**Description:**

Should touch events be captured? I.e. have prevent default called on them.

> Source: [src/core/Config.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L272)

## inputActivePointers

### inputActivePointers: number

**Description:**

The number of Pointer objects created by default. In a mouse-only, or non-multi touch game, you can leave this as 1.

> Source: [src/core/Config.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L277)

## inputSmoothFactor

### inputSmoothFactor: number

**Description:**

The smoothing factor to apply during Pointer movement. See [Phaser.Input.Pointer#smoothFactor](../class/input-pointer.md).

> Source: [src/core/Config.js#L282](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L282)

## inputWindowEvents

### inputWindowEvents: boolean

**Description:**

Should Phaser listen for input events on the Window? If you disable this, events like 'POINTER\_UP\_OUTSIDE' will no longer fire.

> Source: [src/core/Config.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L287)

## inputGamepad

### inputGamepad: boolean

**Description:**

Enable the Gamepad Plugin. This can be disabled in games that don't need gamepad input.

> Source: [src/core/Config.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L292)

## inputGamepadEventTarget

### inputGamepadEventTarget: \*

**Description:**

The DOM Target to listen for gamepad events on. Defaults to `window` if not specified.

> Source: [src/core/Config.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L297)

## disableContextMenu

### disableContextMenu: boolean

**Description:**

Set to `true` to disable the right-click context menu.

> Source: [src/core/Config.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L302)

## audio

### audio: [Phaser.Types.Core.AudioConfig](../typedef/types-core.md)

**Description:**

The Audio Configuration object.

> Source: [src/core/Config.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L307)

## hideBanner

### hideBanner: boolean

**Description:**

Don't write the banner line to the console.log. See `Phaser.Types.Core.BannerConfig` for details of this object.

> Source: [src/core/Config.js#L314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L314)

## hidePhaser

### hidePhaser: boolean

**Description:**

Omit Phaser's name and version from the banner.

> Source: [src/core/Config.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L319)

## bannerTextColor

### bannerTextColor: string

**Description:**

The color of the banner text.

> Source: [src/core/Config.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L324)

## bannerBackgroundColor

### bannerBackgroundColor: Array.<string>

**Description:**

The background colors of the banner.

> Source: [src/core/Config.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L329)

## fps

### fps: [Phaser.Types.Core.FPSConfig](../typedef/types-core.md)

**Description:**

The Frame Rate Configuration object, as parsed by the Timestep class.

> Source: [src/core/Config.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L339)

## disablePreFX

### disablePreFX: boolean

**Description:**

Disables the automatic creation of the Pre FX Pipelines. If disabled, you cannot use the built-in Pre FX on Game Objects.

> Source: [src/core/Config.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L344)

## disablePostFX

### disablePostFX: boolean

**Description:**

Disables the automatic creation of the Post FX Pipelines. If disabled, you cannot use the built-in Post FX on Game Objects.

> Source: [src/core/Config.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L349)

## pipeline

### pipeline: [Phaser.Types.Core.PipelineConfig](../typedef/types-core.md)

**Description:**

An object mapping WebGL names to WebGLPipeline classes. These should be class constructors, not instances.

> Source: [src/core/Config.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L358)

## autoMobilePipeline

### autoMobilePipeline: boolean

**Description:**

Automatically enable the Mobile Pipeline if iOS or Android detected?

> Source: [src/core/Config.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L363)

## defaultPipeline

### defaultPipeline: string

**Description:**

The WebGL Pipeline that Game Objects will use by default. Set to 'MultiPipeline' as standard. See also 'autoMobilePipeline'.

> Source: [src/core/Config.js#L368](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L368)

## antialias

### antialias: boolean

**Description:**

When set to `true`, WebGL uses linear interpolation to draw scaled or rotated textures, giving a smooth appearance. When set to `false`, WebGL uses nearest-neighbor interpolation, giving a crisper appearance. `false` also disables antialiasing of the game canvas itself, if the browser supports it, when the game canvas is scaled.

> Source: [src/core/Config.js#L373](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L373)

## antialiasGL

### antialiasGL: boolean

**Description:**

Sets the `antialias` property when the WebGL context is created. Setting this value does not impact any subsequent textures that are created, or the canvas style attributes.

> Source: [src/core/Config.js#L378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L378)

## mipmapFilter

### mipmapFilter: string

**Description:**

Sets the mipmap magFilter to be used when creating WebGL textures. Don't set unless you wish to create mipmaps. Set to one of the following: 'NEAREST', 'LINEAR', 'NEAREST\_MIPMAP\_NEAREST', 'LINEAR\_MIPMAP\_NEAREST', 'NEAREST\_MIPMAP\_LINEAR' or 'LINEAR\_MIPMAP\_LINEAR'.

> Source: [src/core/Config.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L383)

## desynchronized

### desynchronized: boolean

**Description:**

When set to `true` it will create a desynchronized context for both 2D and WebGL. See <https://developers.google.com/web/updates/2019/05/desynchronized> for details.

> Source: [src/core/Config.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L388)

## roundPixels

### roundPixels: boolean

**Description:**

Draw texture-based Game Objects at only whole-integer positions. Game Objects without textures, like Graphics, ignore this property.

> Source: [src/core/Config.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L393)

## pixelArt

### pixelArt: boolean

**Description:**

Prevent pixel art from becoming blurred when scaled. It will remain crisp (tells the WebGL renderer to automatically create textures using a linear filter mode).

> Source: [src/core/Config.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L398)

## transparent

### transparent: boolean

**Description:**

Whether the game canvas will have a transparent background.

> Source: [src/core/Config.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L410)

## clearBeforeRender

### clearBeforeRender: boolean

**Description:**

Whether the game canvas will be cleared between each rendering frame. You can disable this if you have a full-screen background image or game object.

> Source: [src/core/Config.js#L415](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L415)

## preserveDrawingBuffer

### preserveDrawingBuffer: boolean

**Description:**

If the value is true the WebGL buffers will not be cleared and will preserve their values until cleared or overwritten by the author.

> Source: [src/core/Config.js#L420](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L420)

## premultipliedAlpha

### premultipliedAlpha: boolean

**Description:**

In WebGL mode, sets the drawing buffer to contain colors with pre-multiplied alpha.

> Source: [src/core/Config.js#L425](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L425)

## failIfMajorPerformanceCaveat

### failIfMajorPerformanceCaveat: boolean

**Description:**

Let the browser abort creating a WebGL context if it judges performance would be unacceptable.

> Source: [src/core/Config.js#L430](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L430)

## powerPreference

### powerPreference: string

**Description:**

"high-performance", "low-power" or "default". A hint to the browser on how much device power the game might use.

> Source: [src/core/Config.js#L435](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L435)

## batchSize

### batchSize: number

**Description:**

The default WebGL Batch size. Represents the number of *quads* that can be added to a single batch.

> Source: [src/core/Config.js#L440](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L440)

## maxTextures

### maxTextures: number

**Description:**

When in WebGL mode, this sets the maximum number of GPU Textures to use. The default, -1, will use all available units. The WebGL1 spec says all browsers should provide a minimum of 8.

> Source: [src/core/Config.js#L445](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L445)

## maxLights

### maxLights: number

**Description:**

The maximum number of lights allowed to be visible within range of a single Camera in the LightManager.

> Source: [src/core/Config.js#L450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L450)

## backgroundColor

### backgroundColor: [Phaser.Display.Color](../namespace/display-color.md)

**Description:**

The background color of the game canvas. The default is black. This value is ignored if `transparent` is set to `true`.

> Source: [src/core/Config.js#L457](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L457)

## preBoot

### preBoot: [Phaser.Types.Core.BootCallback](../typedef/types-core.md)

**Description:**

Called before Phaser boots. Useful for initializing anything not related to Phaser that Phaser may require while booting.

> Source: [src/core/Config.js#L468](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L468)

## postBoot

### postBoot: [Phaser.Types.Core.BootCallback](../typedef/types-core.md)

**Description:**

A function to run at the end of the boot sequence. At this point, all the game systems have started and plugins have been loaded.

> Source: [src/core/Config.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L473)

## physics

### physics: [Phaser.Types.Core.PhysicsConfig](../typedef/types-core.md)

**Description:**

The Physics Configuration object.

> Source: [src/core/Config.js#L478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L478)

## defaultPhysicsSystem

### defaultPhysicsSystem: boolean, string

**Description:**

The default physics system. It will be started for each scene. Either 'arcade', 'impact' or 'matter'.

> Source: [src/core/Config.js#L483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L483)

## loaderBaseURL

### loaderBaseURL: string

**Description:**

A URL used to resolve paths given to the loader. Example: '<http://labs.phaser.io/assets/>'.

> Source: [src/core/Config.js#L488](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L488)

## loaderPath

### loaderPath: string

**Description:**

A URL path used to resolve relative paths given to the loader. Example: 'images/sprites/'.

> Source: [src/core/Config.js#L493](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L493)

## loaderMaxParallelDownloads

### loaderMaxParallelDownloads: number

**Description:**

Maximum parallel downloads allowed for resources (Default to 32).

> Source: [src/core/Config.js#L498](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L498)

## loaderCrossOrigin

### loaderCrossOrigin: string, undefined

**Description:**

'anonymous', 'use-credentials', or `undefined`. If you're not making cross-origin requests, leave this as `undefined`. See {@link <https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_settings_attributes>}.

> Source: [src/core/Config.js#L503](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L503)

## loaderResponseType

### loaderResponseType: string

**Description:**

The response type of the XHR request, e.g. `blob`, `text`, etc.

> Source: [src/core/Config.js#L508](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L508)

## loaderAsync

### loaderAsync: boolean

**Description:**

Should the XHR request use async or not?

> Source: [src/core/Config.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L513)

## loaderUser

### loaderUser: string

**Description:**

Optional username for all XHR requests.

> Source: [src/core/Config.js#L518](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L518)

## loaderPassword

### loaderPassword: string

**Description:**

Optional password for all XHR requests.

> Source: [src/core/Config.js#L523](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L523)

## loaderTimeout

### loaderTimeout: number

**Description:**

Optional XHR timeout value, in ms.

> Source: [src/core/Config.js#L528](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L528)

## loaderMaxRetries

### loaderMaxRetries: number

**Description:**

The number of times to retry a file load if it fails.

> Source: [src/core/Config.js#L533](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L533)

## loaderWithCredentials

### loaderWithCredentials: boolean

**Description:**

Optional XHR withCredentials value.

> Source: [src/core/Config.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L538)

## loaderImageLoadType

### loaderImageLoadType: string

**Description:**

Optional load type for image, `XHR` is default, or `HTMLImageElement` for a lightweight way.

> Source: [src/core/Config.js#L543](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L543)

## loaderLocalScheme

### loaderLocalScheme: Array.<string>

**Description:**

An array of schemes that the Loader considers as being 'local' files. Defaults to: `[ 'file://', 'capacitor://' ]`.

> Source: [src/core/Config.js#L551](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L551)

## glowFXQuality

### glowFXQuality: number

**Description:**

The quality of the Glow FX (defaults to 0.1)

> Source: [src/core/Config.js#L556](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L556)

## glowFXDistance

### glowFXDistance: number

**Description:**

The distance of the Glow FX (defaults to 10)

> Source: [src/core/Config.js#L561](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L561)

## installGlobalPlugins

### installGlobalPlugins: any

**Description:**

An array of global plugins to be installed.

> Source: [src/core/Config.js#L584](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L584)

## installScenePlugins

### installScenePlugins: any

**Description:**

An array of Scene level plugins to be installed.

> Source: [src/core/Config.js#L589](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L589)

## defaultPlugins

### defaultPlugins: any

**Description:**

The plugins installed into every Scene (in addition to CoreScene and Global).

> Source: [src/core/Config.js#L620](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L620)

## defaultImage

### defaultImage: string

**Description:**

A base64 encoded PNG that will be used as the default blank texture.

> Source: [src/core/Config.js#L628](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L628)

## missingImage

### missingImage: string

**Description:**

A base64 encoded PNG that will be used as the default texture when a texture is assigned that is missing or not loaded.

> Source: [src/core/Config.js#L633](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L633)

## whiteImage

### whiteImage: string

**Description:**

A base64 encoded PNG that will be used as the default texture when a texture is assigned that is white or not loaded.

> Source: [src/core/Config.js#L638](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Config.js#L638)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Core](#core)

  + [width](#width)

    - [width: number, string](#width-number-string)
  + [height](#height)

    - [height: number, string](#height-number-string)
  + [zoom](#zoom)

    - [zoom: Phaser.Scale.ZoomType, number](#zoom-phaserscalezoomtype-number)
  + [parent](#parent)

    - [parent: \*](#parent-)
  + [scaleMode](#scalemode)

    - [scaleMode: Phaser.Scale.ScaleModeType](#scalemode-phaserscalescalemodetype)
  + [expandParent](#expandparent)

    - [expandParent: boolean](#expandparent-boolean)
  + [autoRound](#autoround)

    - [autoRound: boolean](#autoround-boolean)
  + [autoCenter](#autocenter)

    - [autoCenter: Phaser.Scale.CenterType](#autocenter-phaserscalecentertype)
  + [resizeInterval](#resizeinterval)

    - [resizeInterval: number](#resizeinterval-number)
  + [fullscreenTarget](#fullscreentarget)

    - [fullscreenTarget: HTMLElement, string](#fullscreentarget-htmlelement-string)
  + [minWidth](#minwidth)

    - [minWidth: number](#minwidth-number)
  + [maxWidth](#maxwidth)

    - [maxWidth: number](#maxwidth-number)
  + [minHeight](#minheight)

    - [minHeight: number](#minheight-number)
  + [maxHeight](#maxheight)

    - [maxHeight: number](#maxheight-number)
  + [snapWidth](#snapwidth)

    - [snapWidth: number](#snapwidth-number)
  + [snapHeight](#snapheight)

    - [snapHeight: number](#snapheight-number)
  + [renderType](#rendertype)

    - [renderType: number](#rendertype-number)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [context](#context)

    - [context: CanvasRenderingContext2D, WebGLRenderingContext](#context-canvasrenderingcontext2d-webglrenderingcontext)
  + [canvasStyle](#canvasstyle)

    - [canvasStyle: string](#canvasstyle-string)
  + [customEnvironment](#customenvironment)

    - [customEnvironment: boolean](#customenvironment-boolean)
  + [sceneConfig](#sceneconfig)

    - [sceneConfig: object](#sceneconfig-object)
  + [seed](#seed)

    - [seed: Array.<string>](#seed-arraystring)
  + [gameTitle](#gametitle)

    - [gameTitle: string](#gametitle-string)
  + [gameURL](#gameurl)

    - [gameURL: string](#gameurl-string)
  + [gameVersion](#gameversion)

    - [gameVersion: string](#gameversion-string)
  + [autoFocus](#autofocus)

    - [autoFocus: boolean](#autofocus-boolean)
  + [stableSort](#stablesort)

    - [stableSort: number, boolean](#stablesort-number-boolean)
  + [domCreateContainer](#domcreatecontainer)

    - [domCreateContainer: boolean](#domcreatecontainer-boolean)
  + [domPointerEvents](#dompointerevents)

    - [domPointerEvents: string](#dompointerevents-string)
  + [inputKeyboard](#inputkeyboard)

    - [inputKeyboard: boolean](#inputkeyboard-boolean)
  + [inputKeyboardEventTarget](#inputkeyboardeventtarget)

    - [inputKeyboardEventTarget: \*](#inputkeyboardeventtarget-)
  + [inputKeyboardCapture](#inputkeyboardcapture)

    - [inputKeyboardCapture: Array.<number>](#inputkeyboardcapture-arraynumber)
  + [inputMouse](#inputmouse)

    - [inputMouse: boolean, object](#inputmouse-boolean-object)
  + [inputMouseEventTarget](#inputmouseeventtarget)

    - [inputMouseEventTarget: \*](#inputmouseeventtarget-)
  + [inputMousePreventDefaultDown](#inputmousepreventdefaultdown)

    - [inputMousePreventDefaultDown: boolean](#inputmousepreventdefaultdown-boolean)
  + [inputMousePreventDefaultUp](#inputmousepreventdefaultup)

    - [inputMousePreventDefaultUp: boolean](#inputmousepreventdefaultup-boolean)
  + [inputMousePreventDefaultMove](#inputmousepreventdefaultmove)

    - [inputMousePreventDefaultMove: boolean](#inputmousepreventdefaultmove-boolean)
  + [inputMousePreventDefaultWheel](#inputmousepreventdefaultwheel)

    - [inputMousePreventDefaultWheel: boolean](#inputmousepreventdefaultwheel-boolean)
  + [inputTouch](#inputtouch)

    - [inputTouch: boolean](#inputtouch-boolean)
  + [inputTouchEventTarget](#inputtoucheventtarget)

    - [inputTouchEventTarget: \*](#inputtoucheventtarget-)
  + [inputTouchCapture](#inputtouchcapture)

    - [inputTouchCapture: boolean](#inputtouchcapture-boolean)
  + [inputActivePointers](#inputactivepointers)

    - [inputActivePointers: number](#inputactivepointers-number)
  + [inputSmoothFactor](#inputsmoothfactor)

    - [inputSmoothFactor: number](#inputsmoothfactor-number)
  + [inputWindowEvents](#inputwindowevents)

    - [inputWindowEvents: boolean](#inputwindowevents-boolean)
  + [inputGamepad](#inputgamepad)

    - [inputGamepad: boolean](#inputgamepad-boolean)
  + [inputGamepadEventTarget](#inputgamepadeventtarget)

    - [inputGamepadEventTarget: \*](#inputgamepadeventtarget-)
  + [disableContextMenu](#disablecontextmenu)

    - [disableContextMenu: boolean](#disablecontextmenu-boolean)
  + [audio](#audio)

    - [audio: Phaser.Types.Core.AudioConfig](#audio-phasertypescoreaudioconfig)
  + [hideBanner](#hidebanner)

    - [hideBanner: boolean](#hidebanner-boolean)
  + [hidePhaser](#hidephaser)

    - [hidePhaser: boolean](#hidephaser-boolean)
  + [bannerTextColor](#bannertextcolor)

    - [bannerTextColor: string](#bannertextcolor-string)
  + [bannerBackgroundColor](#bannerbackgroundcolor)

    - [bannerBackgroundColor: Array.<string>](#bannerbackgroundcolor-arraystring)
  + [fps](#fps)

    - [fps: Phaser.Types.Core.FPSConfig](#fps-phasertypescorefpsconfig)
  + [disablePreFX](#disableprefx)

    - [disablePreFX: boolean](#disableprefx-boolean)
  + [disablePostFX](#disablepostfx)

    - [disablePostFX: boolean](#disablepostfx-boolean)
  + [pipeline](#pipeline)

    - [pipeline: Phaser.Types.Core.PipelineConfig](#pipeline-phasertypescorepipelineconfig)
  + [autoMobilePipeline](#automobilepipeline)

    - [autoMobilePipeline: boolean](#automobilepipeline-boolean)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: string](#defaultpipeline-string)
  + [antialias](#antialias)

    - [antialias: boolean](#antialias-boolean)
  + [antialiasGL](#antialiasgl)

    - [antialiasGL: boolean](#antialiasgl-boolean)
  + [mipmapFilter](#mipmapfilter)

    - [mipmapFilter: string](#mipmapfilter-string)
  + [desynchronized](#desynchronized)

    - [desynchronized: boolean](#desynchronized-boolean)
  + [roundPixels](#roundpixels)

    - [roundPixels: boolean](#roundpixels-boolean)
  + [pixelArt](#pixelart)

    - [pixelArt: boolean](#pixelart-boolean)
  + [transparent](#transparent)

    - [transparent: boolean](#transparent-boolean)
  + [clearBeforeRender](#clearbeforerender)

    - [clearBeforeRender: boolean](#clearbeforerender-boolean)
  + [preserveDrawingBuffer](#preservedrawingbuffer)

    - [preserveDrawingBuffer: boolean](#preservedrawingbuffer-boolean)
  + [premultipliedAlpha](#premultipliedalpha)

    - [premultipliedAlpha: boolean](#premultipliedalpha-boolean)
  + [failIfMajorPerformanceCaveat](#failifmajorperformancecaveat)

    - [failIfMajorPerformanceCaveat: boolean](#failifmajorperformancecaveat-boolean)
  + [powerPreference](#powerpreference)

    - [powerPreference: string](#powerpreference-string)
  + [batchSize](#batchsize)

    - [batchSize: number](#batchsize-number)
  + [maxTextures](#maxtextures)

    - [maxTextures: number](#maxtextures-number)
  + [maxLights](#maxlights)

    - [maxLights: number](#maxlights-number)
  + [backgroundColor](#backgroundcolor)

    - [backgroundColor: Phaser.Display.Color](#backgroundcolor-phaserdisplaycolor)
  + [preBoot](#preboot)

    - [preBoot: Phaser.Types.Core.BootCallback](#preboot-phasertypescorebootcallback)
  + [postBoot](#postboot)

    - [postBoot: Phaser.Types.Core.BootCallback](#postboot-phasertypescorebootcallback)
  + [physics](#physics)

    - [physics: Phaser.Types.Core.PhysicsConfig](#physics-phasertypescorephysicsconfig)
  + [defaultPhysicsSystem](#defaultphysicssystem)

    - [defaultPhysicsSystem: boolean, string](#defaultphysicssystem-boolean-string)
  + [loaderBaseURL](#loaderbaseurl)

    - [loaderBaseURL: string](#loaderbaseurl-string)
  + [loaderPath](#loaderpath)

    - [loaderPath: string](#loaderpath-string)
  + [loaderMaxParallelDownloads](#loadermaxparalleldownloads)

    - [loaderMaxParallelDownloads: number](#loadermaxparalleldownloads-number)
  + [loaderCrossOrigin](#loadercrossorigin)

    - [loaderCrossOrigin: string, undefined](#loadercrossorigin-string-undefined)
  + [loaderResponseType](#loaderresponsetype)

    - [loaderResponseType: string](#loaderresponsetype-string)
  + [loaderAsync](#loaderasync)

    - [loaderAsync: boolean](#loaderasync-boolean)
  + [loaderUser](#loaderuser)

    - [loaderUser: string](#loaderuser-string)
  + [loaderPassword](#loaderpassword)

    - [loaderPassword: string](#loaderpassword-string)
  + [loaderTimeout](#loadertimeout)

    - [loaderTimeout: number](#loadertimeout-number)
  + [loaderMaxRetries](#loadermaxretries)

    - [loaderMaxRetries: number](#loadermaxretries-number)
  + [loaderWithCredentials](#loaderwithcredentials)

    - [loaderWithCredentials: boolean](#loaderwithcredentials-boolean)
  + [loaderImageLoadType](#loaderimageloadtype)

    - [loaderImageLoadType: string](#loaderimageloadtype-string)
  + [loaderLocalScheme](#loaderlocalscheme)

    - [loaderLocalScheme: Array.<string>](#loaderlocalscheme-arraystring)
  + [glowFXQuality](#glowfxquality)

    - [glowFXQuality: number](#glowfxquality-number)
  + [glowFXDistance](#glowfxdistance)

    - [glowFXDistance: number](#glowfxdistance-number)
  + [installGlobalPlugins](#installglobalplugins)

    - [installGlobalPlugins: any](#installglobalplugins-any)
  + [installScenePlugins](#installsceneplugins)

    - [installScenePlugins: any](#installsceneplugins-any)
  + [defaultPlugins](#defaultplugins)

    - [defaultPlugins: any](#defaultplugins-any)
  + [defaultImage](#defaultimage)

    - [defaultImage: string](#defaultimage-string)
  + [missingImage](#missingimage)

    - [missingImage: string](#missingimage-string)
  + [whiteImage](#whiteimage)

    - [whiteImage: string](#whiteimage-string)

Back to top

©2025[Phaser](https://docs.phaser.io)