# Phaser.Renderer

# Phaser.Renderer.Canvas

## GetBlendModes

### <static> GetBlendModes()

**Description:**

Returns an array which maps the default blend modes to supported Canvas blend modes.

If the browser doesn't support a blend mode, it will default to the normal `source-over` blend mode.

**Returns:** array - Which Canvas blend mode corresponds to which default Phaser blend mode.

> Source: [src/renderer/canvas/utils/GetBlendModes.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/utils/GetBlendModes.js#L10)  
> Since: 3.0.0

## SetTransform

### <static> SetTransform(renderer, ctx, src, camera, [parentMatrix])

**Description:**

Takes a reference to the Canvas Renderer, a Canvas Rendering Context, a Game Object, a Camera and a parent matrix

and then performs the following steps:

1. Checks the alpha of the source combined with the Camera alpha. If 0 or less it aborts.
2. Takes the Camera and Game Object matrix and multiplies them, combined with the parent matrix if given.
3. Sets the blend mode of the context to be that used by the Game Object.
4. Sets the alpha value of the context to be that used by the Game Object combined with the Camera.
5. Saves the context state.
6. Sets the final matrix values into the context via setTransform.
7. If the Game Object has a texture frame, imageSmoothingEnabled is set based on frame.source.scaleMode.
8. If the Game Object does not have a texture frame, imageSmoothingEnabled is set based on Renderer.antialias.

This function is only meant to be used internally. Most of the Canvas Renderer classes use it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](../class/renderer-canvas-canvasrenderer.md) | No | A reference to the current active Canvas renderer. |
| --- | --- | --- | --- |
| ctx | CanvasRenderingContext2D | No | The canvas context to set the transform on. |
| src | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object being rendered. Can be any type that extends the base class. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](../class/gameobjects-components-transformmatrix.md) | Yes | A parent transform matrix to apply to the Game Object before rendering. |

**Returns:** boolean - `true` if the Game Object context was set, otherwise `false`.

> Source: [src/renderer/canvas/utils/SetTransform.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/utils/SetTransform.js#L9)  
> Since: 3.12.0

# Phaser.Renderer.Snapshot

## Canvas

### <static> Canvas(sourceCanvas, config)

**Description:**

Takes a snapshot of an area from the current frame displayed by a canvas.

This is then copied to an Image object. When this loads, the results are sent

to the callback provided in the Snapshot Configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sourceCanvas | HTMLCanvasElement | No | The canvas to take a snapshot of. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md) | No | The snapshot configuration object. |

> Source: [src/renderer/snapshot/CanvasSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/CanvasSnapshot.js#L11)  
> Since: 3.0.0

## WebGL

### <static> WebGL(sourceContext, config)

**Description:**

Takes a snapshot of an area from the current frame displayed by a WebGL canvas.

This is then copied to an Image object. When this loads, the results are sent

to the callback provided in the Snapshot Configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sourceContext | WebGLRenderingContext | No | The WebGL context to take a snapshot of. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md) | No | The snapshot configuration object. |

> Source: [src/renderer/snapshot/WebGLSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/WebGLSnapshot.js#L11)  
> Since: 3.0.0

# Phaser.Renderer.WebGL.Utils

## getTintFromFloats

### <static> getTintFromFloats(r, g, b, a)

**Description:**

Packs four floats on a range from 0.0 to 1.0 into a single Uint32

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| r | number | No | Red component in a range from 0.0 to 1.0 |
| --- | --- | --- | --- |
| g | number | No | Green component in a range from 0.0 to 1.0 |
| b | number | No | Blue component in a range from 0.0 to 1.0 |
| a | number | No | Alpha component in a range from 0.0 to 1.0 |

**Returns:** number - The packed RGBA values as a Uint32.

> Source: [src/renderer/webgl/Utils.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L15)  
> Since: 3.0.0

## getTintAppendFloatAlpha

### <static> getTintAppendFloatAlpha(rgb, a)

**Description:**

Packs a Uint24, representing RGB components, with a Float32, representing

the alpha component, with a range between 0.0 and 1.0 and return a Uint32

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | number | No | Uint24 representing RGB components |
| --- | --- | --- | --- |
| a | number | No | Float32 representing Alpha component |

**Returns:** number - Packed RGBA as Uint32

> Source: [src/renderer/webgl/Utils.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L38)  
> Since: 3.0.0

## getTintAppendFloatAlphaAndSwap

### <static> getTintAppendFloatAlphaAndSwap(rgb, a)

**Description:**

Packs a Uint24, representing RGB components, with a Float32, representing

the alpha component, with a range between 0.0 and 1.0 and return a

swizzled Uint32

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | number | No | Uint24 representing RGB components |
| --- | --- | --- | --- |
| a | number | No | Float32 representing Alpha component |

**Returns:** number - Packed RGBA as Uint32

> Source: [src/renderer/webgl/Utils.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L57)  
> Since: 3.0.0

## getFloatsFromUintRGB

### <static> getFloatsFromUintRGB(rgb)

**Description:**

Unpacks a Uint24 RGB into an array of floats of ranges of 0.0 and 1.0

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | number | No | RGB packed as a Uint24 |
| --- | --- | --- | --- |

**Returns:** array - Array of floats representing each component as a float

> Source: [src/renderer/webgl/Utils.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L80)  
> Since: 3.0.0

## checkShaderMax

### <static> checkShaderMax(gl, maxTextures)

**Description:**

Check to see how many texture units the GPU supports in a fragment shader

and if the value specific in the game config is allowed.

This value is hard-clamped to 16 for performance reasons on Android devices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gl | WebGLRenderingContext | No | The WebGLContext used to create the shaders. |
| --- | --- | --- | --- |
| maxTextures | number | No | The Game Config maxTextures value. |

**Returns:** number - The number of texture units that is supported by this browser and GPU.

> Source: [src/renderer/webgl/Utils.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L99)  
> Since: 3.50.0

## parseFragmentShaderMaxTextures

### <static> parseFragmentShaderMaxTextures(fragmentShaderSource, maxTextures)

**Description:**

Checks the given Fragment Shader Source for `%count%` and `%forloop%` declarations and

replaces those with GLSL code for setting `texture = texture2D(uMainSampler[i], outTexCoord)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fragmentShaderSource | string | No | The Fragment Shader source code to operate on. |
| --- | --- | --- | --- |
| maxTextures | number | No | The number of maxTextures value. |

**Returns:** string - The modified Fragment Shader source.

> Source: [src/renderer/webgl/Utils.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L131)  
> Since: 3.50.0

## setGlowQuality

### <static> setGlowQuality(shader, game, [quality], [distance])

**Description:**

Takes the Glow FX Shader source and parses out the **SIZE** and **DIST**

consts with the configuration values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| shader | string | No | The Fragment Shader source code to operate on. |
| --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No | The Phaser Game instance. |
| quality | number | Yes | The quality of the glow (defaults to 0.1) |
| distance | number | Yes | The distance of the glow (defaults to 10) |

**Returns:** string - The modified Fragment Shader source.

> Source: [src/renderer/webgl/Utils.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L174)  
> Since: 3.60.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Renderer.Canvas](#phaserrenderercanvas)

  + [GetBlendModes](#getblendmodes)

    - [<static> GetBlendModes()](#static-getblendmodes)
  + [SetTransform](#settransform)

    - [<static> SetTransform(renderer, ctx, src, camera, [parentMatrix])](#static-settransformrenderer-ctx-src-camera-parentmatrix)
* [Phaser.Renderer.Snapshot](#phaserrenderersnapshot)

  + [Canvas](#canvas)

    - [<static> Canvas(sourceCanvas, config)](#static-canvassourcecanvas-config)
  + [WebGL](#webgl)

    - [<static> WebGL(sourceContext, config)](#static-webglsourcecontext-config)
* [Phaser.Renderer.WebGL.Utils](#phaserrendererwebglutils)

  + [getTintFromFloats](#gettintfromfloats)

    - [<static> getTintFromFloats(r, g, b, a)](#static-gettintfromfloatsr-g-b-a)
  + [getTintAppendFloatAlpha](#gettintappendfloatalpha)

    - [<static> getTintAppendFloatAlpha(rgb, a)](#static-gettintappendfloatalphargb-a)
  + [getTintAppendFloatAlphaAndSwap](#gettintappendfloatalphaandswap)

    - [<static> getTintAppendFloatAlphaAndSwap(rgb, a)](#static-gettintappendfloatalphaandswaprgb-a)
  + [getFloatsFromUintRGB](#getfloatsfromuintrgb)

    - [<static> getFloatsFromUintRGB(rgb)](#static-getfloatsfromuintrgbrgb)
  + [checkShaderMax](#checkshadermax)

    - [<static> checkShaderMax(gl, maxTextures)](#static-checkshadermaxgl-maxtextures)
  + [parseFragmentShaderMaxTextures](#parsefragmentshadermaxtextures)

    - [<static> parseFragmentShaderMaxTextures(fragmentShaderSource, maxTextures)](#static-parsefragmentshadermaxtexturesfragmentshadersource-maxtextures)
  + [setGlowQuality](#setglowquality)

    - [<static> setGlowQuality(shader, game, [quality], [distance])](#static-setglowqualityshader-game-quality-distance)

Back to top

©2025[Phaser](https://docs.phaser.io)