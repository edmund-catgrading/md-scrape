# Phaser.Display.Canvas.Smoothing

Scope:
static

> Source: [src/display/canvas/Smoothing.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L10)  
> Since: 3.0.0

# Static functions

## disable

### <static> disable(context)

**Description:**

Sets the Image Smoothing property on the given context. Set to false to disable image smoothing.

By default browsers have image smoothing enabled, which isn't always what you visually want, especially

when using pixel art in a game. Note that this sets the property on the context itself, so that any image

drawn to the context will be affected. This sets the property across all current browsers but support is

patchy on earlier browsers, especially on mobile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context on which to disable smoothing. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D, WebGLRenderingContext - The provided context.

> Source: [src/display/canvas/Smoothing.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L72)  
> Since: 3.0.0

---

## enable

### <static> enable(context)

**Description:**

Sets the Image Smoothing property on the given context. Set to false to disable image smoothing.

By default browsers have image smoothing enabled, which isn't always what you visually want, especially

when using pixel art in a game. Note that this sets the property on the context itself, so that any image

drawn to the context will be affected. This sets the property across all current browsers but support is

patchy on earlier browsers, especially on mobile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context on which to enable smoothing. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D, WebGLRenderingContext - The provided context.

> Source: [src/display/canvas/Smoothing.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L43)  
> Since: 3.0.0

---

## getPrefix

### <static> getPrefix(context)

**Description:**

Gets the Smoothing Enabled vendor prefix being used on the given context, or null if not set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The canvas context to check. |
| --- | --- | --- | --- |

**Returns:** string - The name of the property on the context which controls image smoothing (either `imageSmoothingEnabled` or a vendor-prefixed version thereof), or `null` if not supported.

> Source: [src/display/canvas/Smoothing.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L16)  
> Since: 3.0.0

---

## isEnabled

### <static> isEnabled(context)

**Description:**

Returns `true` if the given context has image smoothing enabled, otherwise returns `false`.

Returns null if no smoothing prefix is available.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if smoothing is enabled on the context, otherwise `false`. `null` if not supported.

> Source: [src/display/canvas/Smoothing.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L101)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [disable](#disable)

    - [<static> disable(context)](#static-disablecontext)
  + [enable](#enable)

    - [<static> enable(context)](#static-enablecontext)
  + [getPrefix](#getprefix)

    - [<static> getPrefix(context)](#static-getprefixcontext)
  + [isEnabled](#isenabled)

    - [<static> isEnabled(context)](#static-isenabledcontext)

Back to top

©2025[Phaser](https://docs.phaser.io)