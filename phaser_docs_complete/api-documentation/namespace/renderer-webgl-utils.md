# Phaser.Renderer.WebGL.Utils

Scope:
static

> Source: [src/renderer/webgl/Utils.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/Utils.js#L9)  
> Since: 3.0.0

# Static functions

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

---

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

---

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

---

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

---

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

---

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

---

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

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [checkShaderMax](#checkshadermax)

    - [<static> checkShaderMax(gl, maxTextures)](#static-checkshadermaxgl-maxtextures)
  + [getFloatsFromUintRGB](#getfloatsfromuintrgb)

    - [<static> getFloatsFromUintRGB(rgb)](#static-getfloatsfromuintrgbrgb)
  + [getTintAppendFloatAlpha](#gettintappendfloatalpha)

    - [<static> getTintAppendFloatAlpha(rgb, a)](#static-gettintappendfloatalphargb-a)
  + [getTintAppendFloatAlphaAndSwap](#gettintappendfloatalphaandswap)

    - [<static> getTintAppendFloatAlphaAndSwap(rgb, a)](#static-gettintappendfloatalphaandswaprgb-a)
  + [getTintFromFloats](#gettintfromfloats)

    - [<static> getTintFromFloats(r, g, b, a)](#static-gettintfromfloatsr-g-b-a)
  + [parseFragmentShaderMaxTextures](#parsefragmentshadermaxtextures)

    - [<static> parseFragmentShaderMaxTextures(fragmentShaderSource, maxTextures)](#static-parsefragmentshadermaxtexturesfragmentshadersource-maxtextures)
  + [setGlowQuality](#setglowquality)

    - [<static> setGlowQuality(shader, game, [quality], [distance])](#static-setglowqualityshader-game-quality-distance)

Back to top

©2025[Phaser](https://docs.phaser.io)