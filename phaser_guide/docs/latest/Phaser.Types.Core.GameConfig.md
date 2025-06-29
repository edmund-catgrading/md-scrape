Types.Core

[![Phaser](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1729268756946%2Fc586ecd3-3d9b-4945-a751-7ebb30337dca.png%3Fw%3D500%26h%3D125%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=3840&q=75)](../../index.md)

Search

`⌘K`

Ask AI

Search

`⌘K`

Ask AI

38.1k stars

Phaser

API Documentation

Phaser Editor

Examples

Game of the Week

* [Phaser](../../index.md)
* [API Documentation](/api-documentation/api-documentation)
* [Phaser Editor](/phaser-editor/intro/welcome)
* [Examples](https://phaser.io/examples)
* [Game of the Week](https://phaser.io/news/2025/01/the-wildfires)

Collapse

Phaser API Documentation

* [Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)
* [Namespaces](/api-documentation/namespace)
* [Game Objects](/api-documentation/gameobjects)
* [Physics](/api-documentation/physics)
* [Events](/api-documentation/event)
* [Class](/api-documentation/class)
* [Functions](/api-documentation/function)
* [Constants](/api-documentation/constant)
* [Typedefs](/api-documentation/typedef)

Collapse

`⌘\`

# Types.Core

Phaser.Types.Core

## AudioConfig

### <static> AudioConfig

Config object containing various sound settings.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| disableWebAudio | boolean | Yes | false | Use HTML5 Audio instead of Web Audio. |
| --- | --- | --- | --- | --- |
| context | AudioContext | Yes |  | An existing Web Audio context. |
| noAudio | boolean | Yes | false | Disable all audio output. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/AudioConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/AudioConfig.js#L1)  
> Since: 3.0.0

---

## BannerConfig

### <static> BannerConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hidePhaser | boolean | Yes | false | Omit Phaser's name and version from the banner. |
| --- | --- | --- | --- | --- |
| text | string | Yes | "'#ffffff'" | The color of the banner text. |
| background | Array.<string> | Yes |  | The background colors of the banner. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/BannerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/BannerConfig.js#L1)  
> Since: 3.0.0

---

## BootCallback

### <static> BootCallback

**Type**: function

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/BootCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/BootCallback.js#L1)  
> Since: 3.0.0

---

## CallbacksConfig

### <static> CallbacksConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| preBoot | [Phaser.Types.Core.BootCallback](/api-documentation/typedef/types-core#bootcallback) | Yes | "Phaser.Types.Core.NOOP" | A function to run at the start of the boot sequence. |
| --- | --- | --- | --- | --- |
| postBoot | [Phaser.Types.Core.BootCallback](/api-documentation/typedef/types-core#bootcallback) | Yes | "Phaser.Types.Core.NOOP" | A function to run at the end of the boot sequence. At this point, all the game systems have started and plugins have been loaded. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/CallbacksConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/CallbacksConfig.js#L1)  
> Since: 3.0.0

---

## DOMContainerConfig

### <static> DOMContainerConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| createContainer | boolean | Yes | false | Should the game create a div element to act as a DOM Container? Only enable if you're using DOM Element objects. You must provide a parent object if you use this feature. |
| --- | --- | --- | --- | --- |
| behindCanvas | boolean | Yes | false | Should the DOM Container that is created (if `dom.createContainer` is true) be positioned behind (true) or over the top (false, the default) of the game canvas? |
| pointerEvents | string | Yes | "'none'" | The default `pointerEvents` attribute set on the DOM Container. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/DOMContainerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/DOMContainerConfig.js#L1)  
> Since: 3.12.0

---

## FPSConfig

### <static> FPSConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| min | number | Yes | 5 | The minimum acceptable rendering rate, in frames per second. |
| --- | --- | --- | --- | --- |
| target | number | Yes | 60 | The optimum rendering rate, in frames per second. This does not enforce the fps rate, it merely tells Phaser what rate is considered optimal for this game. |
| limit | number | Yes | 0 | Enforces an fps rate limit that the game step will run at, regardless of browser frequency. 0 means 'no limit'. Never set this higher than RAF can handle. |
| forceSetTimeOut | boolean | Yes | false | Use setTimeout instead of requestAnimationFrame to run the game loop. |
| deltaHistory | number | Yes | 10 | Calculate the average frame delta from this many consecutive frame intervals. |
| panicMax | number | Yes | 120 | The amount of frames the time step counts before we trust the delta values again. |
| smoothStep | boolean | Yes | true | Apply delta smoothing during the game update to help avoid spikes? |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/FPSConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/FPSConfig.js#L1)  
> Since: 3.0.0

---

## GameConfig

### <static> GameConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | string | Yes | 1024 | The width of the game, in game pixels. |
| --- | --- | --- | --- | --- |
| height | number | string | Yes | 768 | The height of the game, in game pixels. |
| zoom | number | Yes | 1 | Simple scale applied to the game canvas. 2 is double size, 0.5 is half size, etc. |
| type | number | Yes | "CONST.AUTO" | Which renderer to use. Phaser.AUTO, Phaser.CANVAS, Phaser.HEADLESS, or Phaser.WEBGL. AUTO picks WEBGL if available, otherwise CANVAS. |
| stableSort | number | boolean | Yes | -1 | `true` or `1` = Use the built-in StableSort (needed for older browsers), `false` or `0` = Rely on ES2019 Array.sort being stable (modern browsers only), or `-1` = Try and determine this automatically based on browser inspection (not guaranteed to work, errs on side of caution). |
| parent | HTMLElement | string | null | Yes |  |
| canvas | HTMLCanvasElement | Yes | null | Provide your own Canvas element for Phaser to use instead of creating one. |
| canvasStyle | string | Yes | null | CSS styles to apply to the game canvas instead of Phasers default styles. |
| customEnvironment | boolean | Yes | false | Is Phaser running under a custom (non-native web) environment? If so, set this to `true` to skip internal Feature detection. If `true` the `renderType` cannot be left as `AUTO`. |
| context | CanvasRenderingContext2D | Yes |  | Provide your own Canvas Context for Phaser to use, instead of creating one. |
| scene | [Phaser.Types.Scenes.SceneType](/api-documentation/typedef/types-scenes#scenetype) | Array.<[Phaser.Types.Scenes.SceneType](/api-documentation/typedef/types-scenes#scenetype)> | Yes | null | A scene or scenes to add to the game. If several are given, the first is started; the remainder are started only if they have `{ active: true }`. See the `sceneConfig` argument in `Phaser.Scenes.SceneManager#add`. |
| seed | Array.<string> | Yes |  | Seed for the random number generator. |
| title | string | Yes | "''" | The title of the game. Shown in the browser console. |
| url | string | Yes | "'<https://phaser.io>'" | The URL of the game. Shown in the browser console. |
| version | string | Yes | "''" | The version of the game. Shown in the browser console. |
| autoFocus | boolean | Yes | true | Automatically call window.focus() when the game boots. Usually necessary to capture input events if the game is in a separate frame. |
| input | boolean | [Phaser.Types.Core.InputConfig](/api-documentation/typedef/types-core#inputconfig) | Yes |  | Input configuration, or `false` to disable all game input. |
| disableContextMenu | boolean | Yes | false | Disable the browser's default 'contextmenu' event (usually triggered by a right-button mouse click). |
| banner | boolean | [Phaser.Types.Core.BannerConfig](/api-documentation/typedef/types-core#bannerconfig) | Yes | false | Configuration for the banner printed in the browser console when the game starts. |
| dom | [Phaser.Types.Core.DOMContainerConfig](/api-documentation/typedef/types-core#domcontainerconfig) | Yes |  | The DOM Container configuration object. |
| fps | [Phaser.Types.Core.FPSConfig](/api-documentation/typedef/types-core#fpsconfig) | Yes |  | Game loop configuration. |
| render | [Phaser.Types.Core.RenderConfig](/api-documentation/typedef/types-core#renderconfig) | Yes |  | Game renderer configuration. |
| callbacks | [Phaser.Types.Core.CallbacksConfig](/api-documentation/typedef/types-core#callbacksconfig) | Yes |  | Optional callbacks to run before or after game boot. |
| loader | [Phaser.Types.Core.LoaderConfig](/api-documentation/typedef/types-core#loaderconfig) | Yes |  | Loader configuration. |
| images | [Phaser.Types.Core.ImagesConfig](/api-documentation/typedef/types-core#imagesconfig) | Yes |  | Images configuration. |
| physics | [Phaser.Types.Core.PhysicsConfig](/api-documentation/typedef/types-core#physicsconfig) | Yes |  | Physics configuration. |
| plugins | [Phaser.Types.Core.PluginObject](/api-documentation/typedef/types-core#pluginobject) | Array.<[Phaser.Types.Core.PluginObjectItem](/api-documentation/typedef/types-core#pluginobjectitem)> | Yes |  | Plugins to install. |
| scale | [Phaser.Types.Core.ScaleConfig](/api-documentation/typedef/types-core#scaleconfig) | Yes |  | The Scale Manager configuration. |
| audio | [Phaser.Types.Core.AudioConfig](/api-documentation/typedef/types-core#audioconfig) | Yes |  | The Audio Configuration object. |
| pipeline | [Phaser.Types.Core.PipelineConfig](/api-documentation/typedef/types-core#pipelineconfig) | Yes |  | The WebGL Pipeline configuration object. Can also be part of the `RenderConfig`. |
| backgroundColor | string | number | Yes | "0x000000" | The background color of the game canvas. The default is black. |
| antialias | boolean | Yes | true | When set to `true`, WebGL uses linear interpolation to draw scaled or rotated textures, giving a smooth appearance. When set to `false`, WebGL uses nearest-neighbor interpolation, giving a crisper appearance. `false` also disables antialiasing of the game canvas itself, if the browser supports it, when the game canvas is scaled. |
| antialiasGL | boolean | Yes | true | Sets the `antialias` property when the WebGL context is created. Setting this value does not impact any subsequent textures that are created, or the canvas style attributes. |
| desynchronized | boolean | Yes | false | When set to `true` it will create a desynchronized context for both 2D and WebGL. See <https://developers.google.com/web/updates/2019/05/desynchronized> for details. |
| pixelArt | boolean | Yes | false | Sets `antialias` to false and `roundPixels` to true. This is the best setting for pixel-art games. |
| roundPixels | boolean | Yes | false | Draw texture-based Game Objects at only whole-integer positions. Game Objects without textures, like Graphics, ignore this property. |
| transparent | boolean | Yes | false | Whether the game canvas will be transparent. Boolean that indicates if the canvas contains an alpha channel. If set to false, the browser now knows that the backdrop is always opaque, which can speed up drawing of transparent content and images. |
| clearBeforeRender | boolean | Yes | true | Whether the game canvas will be cleared between each rendering frame. |
| preserveDrawingBuffer | boolean | Yes | false | If the value is true the WebGL buffers will not be cleared and will preserve their values until cleared or overwritten by the author. |
| premultipliedAlpha | boolean | Yes | true | In WebGL mode, the drawing buffer contains colors with pre-multiplied alpha. |
| failIfMajorPerformanceCaveat | boolean | Yes | false | Let the browser abort creating a WebGL context if it judges performance would be unacceptable. |
| powerPreference | string | Yes | "'default'" | "high-performance", "low-power" or "default". A hint to the browser on how much device power the game might use. |
| batchSize | number | Yes | 4096 | The default WebGL batch size. Represents the number of *quads* that can be added to a single batch. |
| maxLights | number | Yes | 10 | The maximum number of lights allowed to be visible within range of a single Camera in the LightManager. |
| maxTextures | number | Yes | -1 | When in WebGL mode, this sets the maximum number of GPU Textures to use. The default, -1, will use all available units. The WebGL1 spec says all browsers should provide a minimum of 8. |
| mipmapFilter | string | Yes | "'LINEAR'" | The mipmap magFilter to be used when creating WebGL textures. |
| autoMobilePipeline | boolean | Yes | true | Automatically enable the Mobile Pipeline if iOS or Android detected? |
| defaultPipeline | string | Yes | "'MultiPipeline'" | The WebGL Pipeline that Game Objects will use by default. Set to 'MultiPipeline' as standard. |
| expandParent | boolean | Yes | true | Is the Scale Manager allowed to adjust the CSS height property of the parent and/or document body to be 100%? |
| mode | [Phaser.Scale.ScaleModeType](/api-documentation/typedef/scale#scalemodetype) | Yes | "Phaser.Scale.ScaleModes.NONE" | The scale mode. |
| min | WidthHeight | Yes |  | The minimum width and height the canvas can be scaled down to. |
| max | WidthHeight | Yes |  | The maximum width the canvas can be scaled up to. |
| autoRound | boolean | Yes | false | Automatically round the display and style sizes of the canvas. This can help with performance in lower-powered devices. |
| autoCenter | [Phaser.Scale.CenterType](/api-documentation/typedef/scale#centertype) | Yes | "Phaser.Scale.Center.NO\_CENTER" | Automatically center the canvas within the parent? |
| resizeInterval | number | Yes | 500 | How many ms should elapse before checking if the browser size has changed? |
| fullscreenTarget | HTMLElement | string | Yes |  | The DOM element that will be sent into full screen mode, or its `id`. If undefined Phaser will create its own div and insert the canvas into it when entering fullscreen mode. |
| disablePreFX | boolean | Yes | false | Disables the automatic creation of the Pre FX Pipelines. If disabled, you cannot use the built-in Pre FX on Game Objects. |
| disablePostFX | boolean | Yes | false | Disables the automatic creation of the Post FX Pipelines. If disabled, you cannot use the built-in Post FX on Game Objects. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/GameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/GameConfig.js#L1)  
> Since: 3.0.0

---

## GamepadInputConfig

### <static> GamepadInputConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | \* | Yes | "window" | Where the Gamepad Manager listens for gamepad input events. |
| --- | --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/GamepadInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/GamepadInputConfig.js#L1)  
> Since: 3.0.0

---

## ImagesConfig

### <static> ImagesConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| default | string | undefined | null | Yes |
| --- | --- | --- | --- |
| missing | string | undefined | null | Yes |
| white | string | undefined | null | Yes |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/ImagesConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/ImagesConfig.js#L1)  
> Since: 3.0.0

---

## InputConfig

### <static> InputConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| keyboard | boolean | [Phaser.Types.Core.KeyboardInputConfig](/api-documentation/typedef/types-core#keyboardinputconfig) | Yes | true | Keyboard input configuration. `true` uses the default configuration and `false` disables keyboard input. |
| --- | --- | --- | --- | --- |
| mouse | boolean | [Phaser.Types.Core.MouseInputConfig](/api-documentation/typedef/types-core#mouseinputconfig) | Yes | true | Mouse input configuration. `true` uses the default configuration and `false` disables mouse input. |
| touch | boolean | [Phaser.Types.Core.TouchInputConfig](/api-documentation/typedef/types-core#touchinputconfig) | Yes | true | Touch input configuration. `true` uses the default configuration and `false` disables touch input. |
| gamepad | boolean | [Phaser.Types.Core.GamepadInputConfig](/api-documentation/typedef/types-core#gamepadinputconfig) | Yes | false | Gamepad input configuration. `true` enables gamepad input. |
| activePointers | number | Yes | 1 | The maximum number of touch pointers. See {@link Phaser.Input.InputManager#pointers}. |
| smoothFactor | number | Yes | 0 | The smoothing factor to apply during Pointer movement. See {@link Phaser.Input.Pointer#smoothFactor}. |
| windowEvents | boolean | Yes | true | Should Phaser listen for input events on the Window? If you disable this, events like 'POINTER\_UP\_OUTSIDE' will no longer fire. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/InputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/InputConfig.js#L1)  
> Since: 3.0.0

---

## KeyboardInputConfig

### <static> KeyboardInputConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | \* | Yes | "window" | Where the Keyboard Manager listens for keyboard input events. |
| --- | --- | --- | --- | --- |
| capture | Array.<number> | Yes |  | `preventDefault` will be called on every non-modified key which has a key code in this array. By default it is empty. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/KeyboardInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/KeyboardInputConfig.js#L1)  
> Since: 3.0.0

---

## LoaderConfig

### <static> LoaderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| baseURL | string | Yes |  | A URL used to resolve paths given to the loader. Example: '<http://labs.phaser.io/assets/>'. |
| --- | --- | --- | --- | --- |
| path | string | Yes |  | A URL path used to resolve relative paths given to the loader. Example: 'images/sprites/'. |
| maxParallelDownloads | number | Yes | 32 | The maximum number of resources the loader will start loading at once. |
| crossOrigin | string | undefined | Yes |  | 'anonymous', 'use-credentials', or `undefined`. If you're not making cross-origin requests, leave this as `undefined`. See {@link [https://developer.mozilla.org/en-US/docs/Web/HTML/CORS\_settings\_attributes}](https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_settings_attributes%7D). |
| responseType | string | Yes |  | The response type of the XHR request, e.g. `blob`, `text`, etc. |
| async | boolean | Yes | true | Should the XHR request use async or not? |
| user | string | Yes |  | Optional username for all XHR requests. |
| password | string | Yes |  | Optional password for all XHR requests. |
| timeout | number | Yes | 0 | Optional XHR timeout value, in ms. |
| localScheme | Array.<string> | Yes |  | An optional array of schemes that the Loader considers as being 'local' files. Defaults to: `[ 'file://', 'capacitor://' ]` if not specified. |
| withCredentials | boolean | Yes | false | Optional XHR withCredentials value. |
| imageLoadType | string | Yes | "'XHR'" | Optional load type for image, `XHR` is default, or `HTMLImageElement` for a lightweight way. |
| maxRetries | number | Yes | 2 | The number of times to retry the file load if it fails. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/LoaderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/LoaderConfig.js#L1)  
> Since: 3.0.0

---

## MouseInputConfig

### <static> MouseInputConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | \* | Yes | null | Where the Mouse Manager listens for mouse input events. The default is the game canvas. |
| --- | --- | --- | --- | --- |
| preventDefaultDown | boolean | Yes | true | If `true` the DOM `mousedown` event will have `preventDefault` set. |
| preventDefaultUp | boolean | Yes | true | If `true` the DOM `mouseup` event will have `preventDefault` set. |
| preventDefaultMove | boolean | Yes | true | If `true` the DOM `mousemove` event will have `preventDefault` set. |
| preventDefaultWheel | boolean | Yes | true | If `true` the DOM `wheel` event will have `preventDefault` set. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/MouseInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/MouseInputConfig.js#L1)  
> Since: 3.0.0

---

## NOOP

### <static> NOOP

This callback type is completely empty, a no-operation.

**Type**: function

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/NOOP.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/NOOP.js#L1)  
> Since: 3.0.0

---

## PhysicsConfig

### <static> PhysicsConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| default | string | Yes | The default physics system. It will be started for each scene. Phaser provides 'arcade', 'impact', and 'matter'. |
| --- | --- | --- | --- |
| arcade | [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](/api-documentation/typedef/types-physics-arcade#arcadeworldconfig) | Yes | Arcade Physics configuration. |
| matter | [Phaser.Types.Physics.Matter.MatterWorldConfig](/api-documentation/typedef/types-physics-matter#matterworldconfig) | Yes | Matter Physics configuration. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/PhysicsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/PhysicsConfig.js#L1)  
> Since: 3.0.0

---

## PipelineConfig

### <static> PipelineConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frameInc | number | Yes | 32 | Sets the `PipelineManager.frameInc` value to control the dimension increase in the Render Targets. |
| --- | --- | --- | --- | --- |

**Type**: Array.<[Phaser.Renderer.WebGL.WebGLPipeline](/api-documentation/class/renderer-webgl-webglpipeline)>, object.<string, [Phaser.Renderer.WebGL.WebGLPipeline](/api-documentation/class/renderer-webgl-webglpipeline)>

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/PipelineConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/PipelineConfig.js#L1)  
> Since: 3.50.0

---

## PluginObject

### <static> PluginObject

| name | type | optional | description |
| --- | --- | --- | --- |
| global | Array.<[Phaser.Types.Core.PluginObjectItem](/api-documentation/typedef/types-core#pluginobjectitem)> | Yes | Global plugins to install. |
| --- | --- | --- | --- |
| scene | Array.<[Phaser.Types.Core.PluginObjectItem](/api-documentation/typedef/types-core#pluginobjectitem)> | Yes | Scene plugins to install. |
| default | Array.<string> | Yes | The default set of scene plugins (names). |
| defaultMerge | Array.<string> | Yes | Plugins to *add* to the default set of scene plugins. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/PluginObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/PluginObject.js#L1)  
> Since: 3.8.0

---

## PluginObjectItem

### <static> PluginObjectItem

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Yes | A key to identify the plugin in the Plugin Manager. |
| --- | --- | --- | --- |
| plugin | \* | Yes | The plugin itself. Usually a class/constructor. |
| start | boolean | Yes | Whether the plugin should be started automatically. |
| systemKey | string | Yes | For a scene plugin, add the plugin to the scene's systems object under this key (`this.sys.KEY`, from the scene). |
| sceneKey | string | Yes | For a scene plugin, add the plugin to the scene object under this key (`this.KEY`, from the scene). |
| mapping | string | Yes | If this plugin is to be injected into the Scene Systems, this is the property key map used. |
| data | \* | Yes | Arbitrary data passed to the plugin's init() method. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/PluginObjectItem.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/PluginObjectItem.js#L1)  
> Since: 3.8.0

---

## RenderConfig

### <static> RenderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| antialias | boolean | Yes | true | When set to `true`, WebGL uses linear interpolation to draw scaled or rotated textures, giving a smooth appearance. When set to `false`, WebGL uses nearest-neighbor interpolation, giving a crisper appearance. `false` also disables antialiasing of the game canvas itself, if the browser supports it, when the game canvas is scaled. |
| --- | --- | --- | --- | --- |
| antialiasGL | boolean | Yes | true | Sets the `antialias` property when the WebGL context is created. Setting this value does not impact any subsequent textures that are created, or the canvas style attributes. |
| desynchronized | boolean | Yes | false | When set to `true` it will create a desynchronized context for both 2D and WebGL. See <https://developers.google.com/web/updates/2019/05/desynchronized> for details. |
| pixelArt | boolean | Yes | false | Sets `antialias` to false and `roundPixels` to true. This is the best setting for pixel-art games. |
| roundPixels | boolean | Yes | false | Draw texture-based Game Objects at only whole-integer positions. Game Objects without textures, like Graphics, ignore this property. |
| transparent | boolean | Yes | false | Whether the game canvas will be transparent. Boolean that indicates if the canvas contains an alpha channel. If set to false, the browser now knows that the backdrop is always opaque, which can speed up drawing of transparent content and images. |
| clearBeforeRender | boolean | Yes | true | Whether the game canvas will be cleared between each rendering frame. |
| preserveDrawingBuffer | boolean | Yes | false | If the value is true the WebGL buffers will not be cleared and will preserve their values until cleared or overwritten by the author. |
| premultipliedAlpha | boolean | Yes | true | In WebGL mode, the drawing buffer contains colors with pre-multiplied alpha. |
| failIfMajorPerformanceCaveat | boolean | Yes | false | Let the browser abort creating a WebGL context if it judges performance would be unacceptable. |
| powerPreference | string | Yes | "'default'" | "high-performance", "low-power" or "default". A hint to the browser on how much device power the game might use. |
| batchSize | number | Yes | 4096 | The default WebGL batch size. Represents the number of *quads* that can be added to a single batch. |
| maxLights | number | Yes | 10 | The maximum number of lights allowed to be visible within range of a single Camera in the LightManager. |
| maxTextures | number | Yes | -1 | When in WebGL mode, this sets the maximum number of GPU Textures to use. The default, -1, will use all available units. The WebGL1 spec says all browsers should provide a minimum of 8. |
| mipmapFilter | string | Yes | "''" | The mipmap magFilter to be used when creating WebGL textures. Don't set unless you wish to create mipmaps. Set to one of the following: 'NEAREST', 'LINEAR', 'NEAREST\_MIPMAP\_NEAREST', 'LINEAR\_MIPMAP\_NEAREST', 'NEAREST\_MIPMAP\_LINEAR' or 'LINEAR\_MIPMAP\_LINEAR'. |
| pipeline | [Phaser.Types.Core.PipelineConfig](/api-documentation/typedef/types-core#pipelineconfig) | Yes |  | The WebGL Pipeline configuration object. |
| autoMobilePipeline | boolean | Yes | true | Automatically enable the Mobile Pipeline if iOS or Android detected? |
| defaultPipeline | string | Yes | "'MultiPipeline'" | The WebGL Pipeline that Game Objects will use by default. Set to 'MultiPipeline' as standard. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/RenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/RenderConfig.js#L1)  
> Since: 3.0.0

---

## ScaleConfig

### <static> ScaleConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | string | Yes | 1024 | The base width of your game. Can be an integer or a string: '100%'. If a string it will only work if you have set a parent element that has a size. |
| --- | --- | --- | --- | --- |
| height | number | string | Yes | 768 | The base height of your game. Can be an integer or a string: '100%'. If a string it will only work if you have set a parent element that has a size. |
| zoom | [Phaser.Scale.ZoomType](/api-documentation/typedef/scale#zoomtype) | number | Yes | 1 | The zoom value of the game canvas. |
| parent | HTMLElement | string | Yes |  | The DOM element that will contain the game canvas, or its `id`. If undefined, or if the named element doesn't exist, the game canvas is inserted directly into the document body. If `null` no parent will be used and you are responsible for adding the canvas to your environment. |
| expandParent | boolean | Yes | true | Is the Scale Manager allowed to adjust the CSS height property of the parent and/or document body to be 100%? |
| mode | [Phaser.Scale.ScaleModeType](/api-documentation/typedef/scale#scalemodetype) | Yes | "Phaser.Scale.ScaleModes.NONE" | The scale mode. |
| min | WidthHeight | Yes |  | The minimum width and height the canvas can be scaled down to. |
| max | WidthHeight | Yes |  | The maximum width the canvas can be scaled up to. |
| snap | WidthHeight | Yes |  | Set the snapping values used by the Scale Manager when resizing the canvas. See `ScaleManager.setSnap` for details. |
| autoRound | boolean | Yes | false | Automatically round the display and style sizes of the canvas. This can help with performance in lower-powered devices. |
| autoCenter | [Phaser.Scale.CenterType](/api-documentation/typedef/scale#centertype) | Yes | "Phaser.Scale.Center.NO\_CENTER" | Automatically center the canvas within the parent? |
| resizeInterval | number | Yes | 500 | How many ms should elapse before checking if the browser size has changed? |
| fullscreenTarget | HTMLElement | string | Yes |  | The DOM element that will be sent into full screen mode, or its `id`. If undefined Phaser will create its own div and insert the canvas into it when entering fullscreen mode. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/ScaleConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/ScaleConfig.js#L1)  
> Since: 3.16.0

---

## TimeStepCallback

### <static> TimeStepCallback

**Type**: function

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/TimeStepCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/TimeStepCallback.js#L1)  
> Since: 3.0.0

---

## TouchInputConfig

### <static> TouchInputConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | \* | Yes | null | Where the Touch Manager listens for touch input events. The default is the game canvas. |
| --- | --- | --- | --- | --- |
| capture | boolean | Yes | true | Whether touch input events have preventDefault() called on them. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/TouchInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/TouchInputConfig.js#L1)  
> Since: 3.0.0

---

## WidthHeight

### <static> WidthHeight

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | Yes | 0 | The width. |
| --- | --- | --- | --- | --- |
| height | number | Yes | 0 | The height. |

**Type**: object

**Member of**: Phaser.Types.Core

> Source: [src/core/typedefs/WidthHeight.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/typedefs/WidthHeight.js#L1)  
> Since: 3.16.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)

On this page

* [Types.Core](#typescore)

  + [AudioConfig](#audioconfig)

    - [<static> AudioConfig](#static-audioconfig)
  + [BannerConfig](#bannerconfig)

    - [<static> BannerConfig](#static-bannerconfig)
  + [BootCallback](#bootcallback)

    - [<static> BootCallback](#static-bootcallback)
  + [CallbacksConfig](#callbacksconfig)

    - [<static> CallbacksConfig](#static-callbacksconfig)
  + [DOMContainerConfig](#domcontainerconfig)

    - [<static> DOMContainerConfig](#static-domcontainerconfig)
  + [FPSConfig](#fpsconfig)

    - [<static> FPSConfig](#static-fpsconfig)
  + [GameConfig](#gameconfig)

    - [<static> GameConfig](#static-gameconfig)
  + [GamepadInputConfig](#gamepadinputconfig)

    - [<static> GamepadInputConfig](#static-gamepadinputconfig)
  + [ImagesConfig](#imagesconfig)

    - [<static> ImagesConfig](#static-imagesconfig)
  + [InputConfig](#inputconfig)

    - [<static> InputConfig](#static-inputconfig)
  + [KeyboardInputConfig](#keyboardinputconfig)

    - [<static> KeyboardInputConfig](#static-keyboardinputconfig)
  + [LoaderConfig](#loaderconfig)

    - [<static> LoaderConfig](#static-loaderconfig)
  + [MouseInputConfig](#mouseinputconfig)

    - [<static> MouseInputConfig](#static-mouseinputconfig)
  + [NOOP](#noop)

    - [<static> NOOP](#static-noop)
  + [PhysicsConfig](#physicsconfig)

    - [<static> PhysicsConfig](#static-physicsconfig)
  + [PipelineConfig](#pipelineconfig)

    - [<static> PipelineConfig](#static-pipelineconfig)
  + [PluginObject](#pluginobject)

    - [<static> PluginObject](#static-pluginobject)
  + [PluginObjectItem](#pluginobjectitem)

    - [<static> PluginObjectItem](#static-pluginobjectitem)
  + [RenderConfig](#renderconfig)

    - [<static> RenderConfig](#static-renderconfig)
  + [ScaleConfig](#scaleconfig)

    - [<static> ScaleConfig](#static-scaleconfig)
  + [TimeStepCallback](#timestepcallback)

    - [<static> TimeStepCallback](#static-timestepcallback)
  + [TouchInputConfig](#touchinputconfig)

    - [<static> TouchInputConfig](#static-touchinputconfig)
  + [WidthHeight](#widthheight)

    - [<static> WidthHeight](#static-widthheight)

Back to top

©2025[Phaser](../../index.md)